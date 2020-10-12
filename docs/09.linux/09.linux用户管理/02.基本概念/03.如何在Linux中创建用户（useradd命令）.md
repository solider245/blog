---
title: 如何在Linux中创建用户（useradd命令）
date: 2020-10-12 12:09:51
permalink: /pages/c33200/
categories:
  - linux用户管理
  - 基本概念
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 08:50:08
 * @LastEditTime: 2020-07-17 08:50:09
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\基本概念\如何在Linux中创建用户（useradd命令）.md
 * @日行一善，每日一码
--> 
Linux是一个多用户系统，这意味着多个人可以同时与同一个系统进行交互。 作为系统管理员，您有责任通过创建和 [删除用户](https://linuxize.com/post/how-to-delete-users-in-linux-using-the-userdel-command/) 并将其分配给不同的 [组](https://linuxize.com/post/how-to-add-user-to-group-in-linux/) 来管理系统的用户和 [组](https://linuxize.com/post/how-to-add-user-to-group-in-linux/) 。

在本文中，我们将讨论如何使用 `useradd` 命令 创建新的用户帐户 。

## `useradd` 命令 [＃](#useradd-command)

该 `useradd` 命令 的常规语法 如下：

```sh
useradd [OPTIONS] USERNAME

```

复制

只有root或具有 [sudo](https://linuxize.com/post/sudo-command-in-linux/) 特权的 用户 才能使用该 `useradd` 命令创建新的用户帐户。

调用时， `useradd` 根据命令行上指定的选项和 `/etc/default/useradd` 文件中 设置的默认值创建一个新的用户帐户 。

此文件中定义的变量因分布而异，这导致 `useradd` 命令在不同的系统上产生不同的结果。

`useradd` 还读取 [`/etc/login.defs`](http://man7.org/linux/man-pages/man5/login.defs.5.html) 文件 的内容 。 此文件包含影子密码套件的配置，例如密码过期策略，创建系统用户和常规用户时使用的用户ID范围等。

## 如何在Linux中创建新用户 [＃](#how-to-create-a-new-user-in-linux)

要创建新的用户帐户，请先调用 `useradd` 命令，然后再键入用户名。

例如，创建一个名为 `username` 您 的新用户， 您将运行：

```
sudo useradd username
```

不带任何选项执行时， `useradd` 使用 `/etc/default/useradd` 文件中 指定的默认设置创建一个新的用户帐户 。

该命令增加了一个入口 `/etc/passwd` ， 和 文件。 [`/etc/shadow,`](https://linuxize.com/post/etc-shadow-file/) `/etc/group` `/etc/gshadow`

为了能够以新创建的用户身份登录，您需要设置用户密码。 为此，请运行 [`passwd`](https://linuxize.com/post/how-to-change-user-password-in-linux/) 命令，然后输入用户名：

```
sudo passwd username
```

系统将提示您输入并确认密码。 确保使用强密码。

```output
Changing password for user username.
New password:
Retype new password:
passwd: all authentication tokens updated successfully.

```

## 如何添加新用户和创建主目录 [＃](#how-to-add-a-new-user-and-create-home-directory)

在大多数Linux发行版中，当使用创建新的用户帐户时 `useradd` ，不会创建用户的主目录。

使用 `-m` （ `--create-home` ）选项将用户主目录创建为 `/home/username` ：

```
sudo useradd -m username
```

上面的命令创建新用户的主目录，并将文件从 `/etc/skel` 目录 复制 到用户的主目录。 如果您 在 目录中 [列出文件](https://linuxize.com/post/how-to-list-files-in-linux-using-the-ls-command/) `/home/username` ，则会看到初始化文件：

```
ls -la /home/username/
```

```output
drwxr-xr-x 2 username username 4096 Dec 11 11:23 .
drwxr-xr-x 4 root     root     4096 Dec 11 11:23 ..
-rw-r--r-- 1 username username  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 username username 3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 username username  807 Apr  4  2018 .profile

```

在主目录中，用户可以编写，编辑和删除文件和目录。

## 创建具有特定主目录的用户 [＃](#creating-a-user-with-specific-home-directory)

默认情况下，在中 `useradd` 创建用户的主目录 `/home` 。 如果要在其他位置创建用户的主目录，请使用 `d` （ `--home` ）选项。

这是显示如何创建 `username` 主目录 名为的新用户的示例 `/opt/username` ：

```
sudo useradd -m -d /opt/username username
```

## 创建具有特定用户ID的用户 [＃](#creating-a-user-with-specific-user-id)

在Linux和类似Unix的操作系统中，用户由唯一的UID和用户名标识。

用户标识符（UID）是Linux系统分配给每个用户的唯一正整数。 UID和其他访问控制策略用于确定用户可以对系统资源执行的操作的类型。

默认情况下，创建新用户时，系统会从 `login.defs` 文件中 指定的用户ID范围中分配下一个可用的UID 。

`useradd` 使用 `-u` （ `--uid` ）选项 调用 以创建具有特定UID的用户。 例如，要创建一个名为 `username` UID的 新用户 ， `1500` 请输入：

```
sudo useradd -u 1500 username
```

您可以使用以下 [`id`](https://linuxize.com/post/id-command-in-linux/) 命令 来验证用户的UID ：

```
id -u username
```

```output
1500

```

## 创建具有特定组ID的用户 [＃](#creating-a-user-with-specific-group-id)

Linux组是组织单位，用于组织和管理Linux中的用户帐户。 组的主要目的是为一组可以在组内用户之间共享的给定资源定义一组特权，例如读取，写入或执行权限。

创建新用户时，该 `useradd` 命令 的默认行为 是创建一个名称与用户名相同且GID与UID相同的组。

在 `-g` （ `--gid` ）选项允许您创建一个特定的初始登录组的用户。 您可以指定组名或GID号。 组名或GID必须已经存在。

以下示例显示如何创建一个名为的新用户并将 `username` 登录组设置为 `users` type：

```
sudo useradd -g users username
```

要验证用户的GID，请使用以下 `id` 命令：

```
id -gn username
```

```output
users

```

## 创建一个用户并分配多个组 [＃](#creating-a-user-and-assign-multiple-groups)

Linux操作系统中有两种类型的组：主要组和次要（或补充）组。 每个用户可以完全属于一个主要组，零个或多个次要组。

您可以使用 `-G` （ `--groups` ）选项 指定用户将成为成员的补充组列表 。

以下命令创建一个新用户 `username` ， 该用户名为 Primary Group `users` 和Secondary Group `wheel` 和 `docker` 。

```
sudo useradd -g users -G wheel,developers username
```

您可以通过输入来检查用户组

```
id username
```

```output
uid=1002(username) gid=100(users) groups=100(users),10(wheel),993(docker)

```

## 创建具有特定登录Shell的用户 [＃](#creating-a-user-with-specific-login-shell)

默认情况下，新用户的登录shell设置为 `/etc/default/useradd` 文件中 指定的登录shell 。 在某些发行版中，默认外壳设置为， `/bin/sh` 而在其他 发行版中，默认外壳 设置为 `/bin/bash` 。

在 `-s` （ `--shell` ）选项允许你指定新用户的登录shell。

例如，创建一个名为新用户 `username` 以 `/usr/bin/zsh` 作为登录shell类型：

```
sudo useradd -s /usr/bin/zsh username
```

检查 [`/etc/passwd`](https://linuxize.com/post/etc-passwd-file/) 文件中 的用户条目 以验证用户的登录shell：

```
grep username /etc/passwd
```

```output
username:x :1001:1001::/home/username:/usr/bin/zsh

```

## 创建具有自定义注释的用户 [＃](#creating-a-user-with-custom-comment)

在 `-c` （ `--comment` ）选项允许你添加一个简短的说明为新用户。 通常，将用户的全名或联系信息添加为注释。

在以下示例中，我们将创建一个新用户 `username` ， 该用户以 文本字符串 `Test User Account` 作为注释：

```
sudo useradd -c "Test User Account" username
```

注释保存在 `/etc/passwd` 文件中：

```
grep username /etc/passwd
```

```output
username:x :1001:1001:Test User Account:/home/username:/bin/sh

```

评论字段也称为 `GECOS` 。

## 创建具有到期日期的用户 [＃](#creating-a-user-with-an-expiry-date)

要定义新用户帐户的到期时间，请使用 `-e` （ `--expiredate` ）选项。 这对于创建临时帐户很有用。

日期必须使用 `YYYY-MM-DD` 格式 指定 。

例如，要创建一个名称为 `username` 2019年1月22日 的新用户帐户 ，您将运行：

```
sudo useradd -e 2019-01-22 username
```

使用以下 `chage` 命令来验证用户帐户的到期日期：

```
sudo chage -l username
```

输出将如下所示：

```output
Last password change					: Dec 11, 2018
Password expires					: never
Password inactive					: never
Account expires						: Jan 22, 2019
Minimum number of days between password change		: 0
Maximum number of days between password change		: 99999
Number of days of warning before password expires	: 7

```

## 创建系统用户 [＃](#creating-a-system-user)

系统与常规（普通）用户之间没有真正的技术差异。 通常，系统用户是在安装操作系统和新软件包时创建的。

使用 `-r` （ `--system` ）选项创建系统用户帐户。 例如，要创建一个名为的新系统用户， `username` 请运行：

```
sudo useradd -r username
```

系统用户的创建没有有效期。 它们的UID是从 `login.defs` 文件中 指定的系统用户ID的范围中选择的，该范围 不同于普通用户的范围。

## 更改默认的useradd值 [＃](#changing-the-default-useradd-values)

可以使用 `-D` ， `--defaults` 选项或通过手动编辑 `/etc/default/useradd` 文件中 的值 来查看和更改默认的useradd选项 。

要查看当前的默认选项，请输入：

```
useradd -D
```

输出将如下所示：

```output
GROUP=100
HOME=/home
INACTIVE=-1
EXPIRE=
SHELL=/bin/sh
SKEL=/etc/skel
CREATE_MAIL_SPOOL=no

```

假设您要将默认的登录shell从更改 `/bin/sh` 为 `/bin/bash` 。 为此，请指定新的外壳，如下所示：

```
sudo useradd -D -s /bin/bash
```

您可以通过运行以下命令来验证是否更改了默认外壳程序值：

```
sudo useradd -D | grep -i shell
```

```output
SHELL=/bin/bash

```

## 结论 [＃](#conclusion)

我们已经向您展示了如何使用 `useradd` 命令 创建新的用户帐户 。 相同的说明适用于任何Linux发行版，包括Ubuntu，CentOS，RHEL，Debian，Fedora和Arch Linux。

`useradd` 是一个低级实用程序，Debian和Ubuntu用户可以改用更友好的 [adduser](https://linuxize.com/post/how-to-add-and-delete-users-on-ubuntu-18-04/) 命令。

如有任何疑问，请随时发表评论。