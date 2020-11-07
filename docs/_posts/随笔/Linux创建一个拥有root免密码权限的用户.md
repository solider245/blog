---
title: "Linux创建一个拥有root权限的用户"
date: 2020-07-18T23:42:47Z
lastmod: 2020-07-18T23:42:47Z
draft: true
keywords: [linux]
description: "useradd与adduser的用法"
tags: [linux 用户管理]
categories: [linux]
author: "中箭的吴起"

# You can also close(false) or open(true) something for this content.
# P.S. comment can only be closed
comment: false
toc: false
autoCollapseToc: false
postMetaInFooter: false
hiddenFromHomePage: false
# You can also define another contentCopyright. e.g. contentCopyright: "This is another copyright."
contentCopyright: false
reward: false
mathjax: false
mathjaxEnableSingleDollar: false
mathjaxEnableAutoNumber: false

# You unlisted posts you might want not want the header or footer to show
hideHeaderAndFooter: false

# You can enable or disable out-of-date content warning for individual post.
# Comment this out to use the global config.
#enableOutdatedInfoWarning: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

<!--more-->

# adduser创建方法

## 创建用户以及设置密码

```shell
sudo su #切换到root用户
adduser boss # 创建一个叫boss的普通用户
```
![20200719080750_d7b9e2dd7762e3911b2b585684ccfb93.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200719080750_d7b9e2dd7762e3911b2b585684ccfb93.png)
系统会提示你输入该用户的密码，你输入即可。其他的可以默认就行。

## 将用户设置为sudo用户组
```shell
usermod -aG sudo boss # G表示Group表示用户的组别，a表示all，不加的话，就会失去其他组别的权限，一般默认都是加的
```
## 测试root权限
```shell
su boss
sudo ls # 根目录下，不加sudo就无法查看，表示成功
```
![20200719081441_e73de1f310d0928730137a64e734562c.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200719081441_e73de1f310d0928730137a64e734562c.png)
如上，表示成功。

## 设置免密码
输入sudo的时候，我们经常要输入密码，但是在安全性要求不高的服务器，我们可以设置sudo的时候直接执行而不需要密码，这样就更加的方便。

### 单用户设置免密码
有时候我们只需要单独给一个用户设置免密码，请用以下方式。

```shell
sudo su
vim /etc/sudoers # 切换到配置文件
boss    ALL=(ALL) NOPASSWD:ALL  # 在sudo下添加这行
```
>提示：如果VIM提示只读文件无法保存，请先输入:!然后回车，然后再输入:wq!即可。
![20200719082608_ec568c4bcc3ccaeeccc379be3ab30914.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200719082608_ec568c4bcc3ccaeeccc379be3ab30914.png)

如上所示修改即可。

![20200719082537_21e67141ac8f3e52a35d71725b60fee8.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200719082537_21e67141ac8f3e52a35d71725b60fee8.png)
回到外面就表示可以了。

### 组别修改
有时候我们用户比较多，这个时候我们可以让整个组别都拥有这个权限，那么我们只要修改这个组别即可。
![20200719082856_1a9f3b6decc935ff186e2dcaf3393bec.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200719082856_1a9f3b6decc935ff186e2dcaf3393bec.png)
如上图所示，我们在sudo用户组里将其修改为免密码，同时删掉刚才我们增加的那行。
我们知道我们刚才设置过boss属于sudo用户组，现在再测试一下。

![20200719082954_37634574f84ff77660712974ddf81f69.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200719082954_37634574f84ff77660712974ddf81f69.png)
如上，成功！

当然，大家可以按照刚才的方法再增加一个用户，然后指定他的用户组即可。

# useradd方法
前面说了adduser的方法，实际上Linux里只有一种添加用户的方法，就是useradd.adduser你可以理解为是做了一个脚本来帮助大家更加友好的添加用户。

## useradd基本用法
```shell
useradd -参数 <用户名> # 例如useradd -m boy 创建一个boy用户
```
很多情况下useradd默认不创建工作目录，所以我们一般都自带一个-m，这样方便一些。

## useradd的配置文件/etc/default/useradd
要查询useradd一般情况下会创建哪些东西，我们可以查看useradd的默认配置文件。
输入：
```shell
useradd -D
```
系统就会显示useradd的配置文件信息。
![20200719085157_31ae8b128ad43949ea2222645679c6ae.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200719085157_31ae8b128ad43949ea2222645679c6ae.png)
一般情况下，我们可以直接使用vim来编辑。
```shell
vim /etc/default/useradd
```
![20200719085445_b84981d91d15a2a77b2ba205c7b6a8e8.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200719085445_b84981d91d15a2a77b2ba205c7b6a8e8.png)
大多数情况下，我们不怎么需要去更改他的配置文件，大家知道有这么一回事，以后去修改即可。

## useradd创建用户
```shell
useradd -m boy
```
## 修改密码
```shell
passwd boy
```
## useradd 创建一个拥有管理权限的用户组

之前我们增加了一个可以不使用密码就使用sudo的用户组sudo。

现在，我们来创建一个类似的用户。

```shell
useradd -m -g sudo coder # 创建一个名叫coder,用户组为sudo，并且拥有同名工作目录的管理员用户
```
![20200719093236_0bec4e0d88c95976ac56c6c23d4e8c9d.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200719093236_0bec4e0d88c95976ac56c6c23d4e8c9d.png)
如上图所示，你甚至在sudo的时候可以直接不用密码。

当然，我们平时用zsh比较多，为了方便，我们这里可以直接指定他的sh为zsh。
## 创建一个默认sh为zsh的管理员用户组
```shell
useradd -m -g sudo -s /bin/zsh zsher
```
如果这样看起来比较复杂的话，可以用换行来使得命令更加清晰明了。
```shell
useradd -m \
  -g sudo \
  -s /bin/zsh \
  zsher
```  
![20200719093747_7b2e72a21e38c4f06f16e53057dbc865.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200719093747_7b2e72a21e38c4f06f16e53057dbc865.png)
如上所示。基本上就创建成功了。

# 直接将用户添加进管理组

前面我们设置了一个sudo组并且无密码，然后我们创建了一个boy作为一个普通用户，我们可以使用gpasswd命令来直接将boy用户提交到sudo用户组。
```shell
gpasswd -a boy sudo
```
这样的话，boy就可以直接成为管理组用户，使用起来十分方便。
gpasswd的主要用法如下：
```shell
用法：gpasswd [选项] 组

选项：
  -a, --add USER                向组 GROUP 中添加用户 USER
  -d, --delete USER             从组 GROUP 中添加或删除用户
  -h, --help                    显示此帮助信息并退出
  -Q, --root CHROOT_DIR         要 chroot 进的目录
  -r, --remove-password         移除组 GROUP 的密码
  -R, --restrict                向其成员限制访问组 GROUP
  -M, --members USER,...        设置组 GROUP 的成员列表
  -A, --administrators ADMIN,...
                                设置组的管理员列表
除非使用 -A 或 -M 选项，不能结合使用这些选项。
```



# 查看所有用户
创建的用户多了，我们就需要来查看下当前用户。
```shell
cat /etc/passwd
```
但是上面这个命令查看的太多了，你可以使用下面这个命令，只查阅活跃用户，这样会更加的清晰明了。
```shell
cat /etc/passwd|grep -v nologin|grep -v halt|grep -v shutdown|awk -F":" '{ print $1"|"$3"|"$4 }'|more
```
# userdel删除用户

有时候用户太多，我们需要删除一些用户.
```shell
userdel -r boy # 删除boy用户以及他的工作目录
```
![20200719095916_fcbf1a67ea69a31eeb6454250e4ef0d1.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200719095916_fcbf1a67ea69a31eeb6454250e4ef0d1.png)
基本上Linux用户管理的大多数用法就都在这里了。

