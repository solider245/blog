---
title: Linux 用户、用户组和权限
date: 2020-10-12 12:09:51
permalink: /pages/23adff/
categories:
  - linux用户管理
  - 基本概念
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 08:07:42
 * @LastEditTime: 2020-07-17 08:07:51
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\基本概念\Linux 用户、用户组和权限.md
 * @日行一善，每日一码
--> 
## 用户类型

除 root 用户以外，Linux 账号（用户）一般分为两类，**系统账号**和**一般账号**。

系统账号主要用于运行特定的 daemon 程序，比如我们添加专门的 Linux 用户 www 和 mysql 来运行 Nginx 和 MySQL，这是为了便于控制程序的权限（即运行此程序的账号的权限），若程序被侵入，防止攻击者可以任意执行系统中的其他行为。系统账号一般会将其登录 shell 设为 `/sbin/nologin`，即不可通过 shell 登录，一般的使用系统账号运行程序的方式为通过 sudo 以系统账号的身份启动程序。

一般账号为给 Linux 系统使用者分配的账号，默认情况下，添加用户时会为该用户创建**家目录**和 **mail spool**（`/var/mail/username`），而系统账号不会。**一般账号 uid >= 1000，系统账号 uid < 1000**。

## 添加用户

默认情况下（不指定 options）创建用户的同时会创建一个与账号同名的用户组，并将该用户组指定为账号的 **primary group**（这里称其为主用户组）。一个用户可以属于多个用户组，其中 primary 组只能指定一个，为用户的默认所在组，也就是该用户创建文件后，文件的 group 属性值。除 primary 组以外的其他组都为 **supplementary groups**（这里称其为附加用户组）。

命令：

```
$ useradd [options] LOGIN_NAME
```

常用的 options 有：

*   `-r` 创建系统账号，不会创建家目录
*   `-s` 指定登录 shell，默认为 `/bin/bash`，可以指定为 `/sbin/nologin`
*   `-g` 为用户指定其主用户组，不指定则创建一个与用户同名的组作为其主用户组。
*   `-G` 为用户指定附加用户组，可以有多个

如果通过 `usermod` 命令为用户添加附加用户组可以加上 `-a` 参数：

```
$ usermod -a -G GROUP_NAME LOGIN_NAME
```

## 用户和用户组相关的系统文件

Linux（这里更确切得说应该为 GNU/Linux 吧，单纯的 Linux 往往是指 Linux 内核，本文为了方便，简称 Linux 发行版或 GNU/Linux 为 Linux，大家自行纠正）的用户数据库以文件的形式存于 `/etc/` 下，所以有时候我们对用户的添加/修改/删除等操作，也可以不通过命令，而是直接操作文件，不过最好还是不要这样做，以免出现格式不正确问题。

*   `/etc/passwd` 用户账号信息
*   `/etc/shadow` 用户密码信息
*   `/etc/group` 用户组信息
*   `/etc/sudoers` 指定可执行 sudo 命令的用户
*   ...

```
[root@centos ~]# ll /etc/passwd /etc/shadow /etc/group /etc/sudoers
-rw-r--r--. 1 root root 464  Jan 19 12:57 /etc/group
-rw-r--r--. 1 root root 882  Jan 19 12:57 /etc/passwd
----------. 1 root root 812  Jan 19 12:57 /etc/shadow
-r--r-----. 1 root root 4328 Jan 19 12:57 /etc/sudoers
```

查看相关文件权限可见，除 root 用户外其他用户是无法操作用户账号数据的，若普通用户可以随意删改用户账号，则会出现很多问题，这显然是不允许的。

## 用户登录后的 Shell

```
[root@centos ~]# grep xvrzhao /etc/passwd
xvrzhao:x:1000:1000::/home/xvrzhao:/bin/bash
```

文件 `/etc/passwd` 中每一行为一个账号信息，不同的属性以 `:` 隔开，最后一个属性为登录 Shell，默认为 `/bin/bash`。你可以直接修改 `/etc/passwd` 文件进行修改，也可以通过 `useradd` 或 `usermod` 命令在添加用户的时候指定（`-s` 参数）或修改用户登录 Shell。

系统会为每个登录用户分配一个 Shell 环境作为用户与操作系统交互的途径，常见的 Shell 环境有 sh、 bash、 zsh 等。

当用户登录之后，系统会为当前 Shell 环境（可以理解为会话）设定一些环境变量，方式为：先读取 `/etc/profile` 设定，再读取 `~/.bash_profile` 设定。前者为全局设定，作用于每个用户，后者为个人设定，只作用于个人（具体请参考 [鸟哥的Linux私房菜相关章节](http://linux.vbird.org/linuxbasic/0320bash.php#settingsbashrc)）。

![login shell 的设定档读取流程](https://segmentfault.com/img/bVbGIk3 "login shell 的设定档读取流程")

## 设定用户密码

在添加用户之后，是无法通过新用户登录的，因为没有为其设定登录密码。

```
passwd [OPTION...] <accountName>
```

root 用户可以通过命令 `passwd` 设定自己的密码，也可以通过命令 `passwd accountName` 来设定其他账号的密码。而其他账号只能设定自己的密码。

## 用户组管理

你可能需要提前添加一个用户组，然后在将其他用户加入到该组中，也可能会删除一个组。可以直接修改 `/etc/group` 文件进行，也可以通过命令进行。

*   groupadd 添加
*   groupdel 删除
*   ...

具体使用方法见 `man`。

## `sudo` \- 使用其他用户的身份执行命令

之前误以为 `sudo` 是借用 root 身份来执行命令，其实它不仅可以借 root，还可以借任何其他用户的身份，前提是 root 用户为你开启了相关权限，这个权限文件为 `/etc/sudoers`，不过通常我们不直接操作文件，而是通过 `visudo` 命令。

`su` 命令是切换用户，需要输入切换到的用户的密码。而通过 `sudo` 以其他用户执行命令是输入自己的密码，而不是其他用户的密码。`su` 无法切换到没有 Shell 的用户，但是 `sudo` 可以以无 Shell 用户身份执行命令。

```
$ sudo cmd # 不指定用户则以 root 身份运行 cmd
$ sudo -u somebody cmd # 以 somebody 身份运行 cmd
```

```
[xvrzhao@centos ~]$ visudo

# ...

## Allow root to run any commands anywhere
root ALL=(ALL)  ALL

## Allows people in group wheel to run all commands
%wheel ALL=(ALL)  ALL

## Same thing without a password
# %wheel ALL=(ALL)  NOPASSWD: ALL

# ...
```

等号 `=` 左边指定可以从哪些主机上执行 `sudo`，右边指定可以以哪些用户身份执行命令，再接一个空格，后面指定可以通过 `sudo` 执行哪些命令（命令必须为绝对路径）。

上面输出的为默认配置，可以看到：

*   root 用户可以以任何用户运行任何命令
*   wheel 组的用户也可以以任何用户运行任何命令
*   若命令前加 `NOPASSWD:` 则在执行 `sudo` 时，连自己的密码都不需要输入
*   在默认配置里，除 root 外其他用户都不可以使用 `sudo`，root 需要给其他用户开放 `sudo` 权限，指定他可以以哪些身份运行哪些命令，或直接将用户加入 `wheel` 组中（`usermod -a -G wheel USER`）。

## 删除用户

```
userdel [options] USERNAME
```

若要彻底删除一个用户，先执行 `find / -user USERNAME` 搜索到所有属于该用户的文件，将其文件删除之后，再执行 `userdel -r USERNAME`，`-r` 参数表示删除该用户的同时也删除其家目录和其 mail spool。

## 文件与文件夹权限

```
[xvrzhao@centos ~]$ ll
total 0
drwxrwxr-x. 2 xvrzhao xvrzhao 6 Jan 19 14:50 my_dir
-rw-rw-r--. 1 xvrzhao xvrzhao 0 Jan 19 14:50 my_file
```

我们知道，文件的权限属性分为 `u` / `g` / `o` 和 `r` / `w` / `x`。对于文件和文件夹来说他们的 `r` / `w` / `x` 分别具有不同的含义：

*   文件

    *   `r` 文件内容可以被读取
    *   `w` 文件内容可以被修改
    *   `x` 文件可以被执行
*   文件夹

    *   `r` 可以查看此文件夹下的文件名列表
    *   `w` 可以对此文件夹下的文件进行**创建**、**删除**、**重命名**和**移动**
    *   `x` 可以将此文件夹作为工作目录，即可以 `cd` 到这个文件夹中

## 参考资料

*   [鸟哥私房菜 \- Linux 帐号管理与 ACL 权限设定](http://linux.vbird.org/linux_basic/0410accountmanager.php)
*   [鸟哥私房菜 \- Linux 的档案权限与目录配置](http://linux.vbird.org/linux_basic/0210filepermission.php)
*   [Linux 中文件 / 文件夹的权限](https://blog.csdn.net/daguanjia11/article/details/78005620)

阅读 512更新于 5月3日