---
title: 如何使用useradd命令在Linux中创建用户
date: 2020-10-12 12:09:51
permalink: /pages/ee7ec1/
categories:
  - linux用户管理
  - 基本概念
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 08:19:00
 * @LastEditTime: 2020-07-17 08:19:00
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\基本概念\如何使用useradd命令在Linux中创建用户.md
 * @日行一善，每日一码
--> 
Linux是一个多用户系统，这意味着不止一个人可以同时在同一系统进行交互。作为系统管理员，您有责任通过创建和删除用户来管理系统的[用户和组](https://www.myfreax.com/how-linux-adds-users-to-a-group/)，并将其分配给不同的组。

在Linux中，您可以使用useradd命令创建用户帐户并将用户分配到不同的组。useradd是一个非常实用的命令，Debian和Ubuntu用户可以使用更友好的adduser命令。

本教程介绍了useradd命令及其选项。

## **前提条件**

为了能够使用useradd命令创建新用户，您需要以root用户或具有sudo访问权限的用户身份登录。

*   [在linux创建sudo用户](https://www.myfreax.com/linux-sudo-command/)
*   [在CentOS上创建sudo用户](https://www.myfreax.com/create-a-sudo-user-on-centos/)

## **useradd命令**

在讨论如何使用useradd命令之前，让我们先回顾一下基本语法。

useradd命令表达式采用以下形式：

```sh
useradd [OPTIONS] USERNAME
```

Copy

调用useradd命令时，将会使用命令行中指定的选项以及`/etc/default/useradd`文件中指定的默认值创建新用户帐户。

此文件中定义的变量会根据Linux不同的发行版可能会有差别。如果在没有任何选项的情况下使用useradd命令，则可能会在不同的Linux发行版上生成不同的结果。

useradd命令还读取[`/etc/login.defs`](http://man7.org/linux/man-pages/man5/login.defs.5.html)文件的内容。此文件包含影子密码套件的配置，例如密码过期策略，创建系统和常规用户时使用的用户ID范围等。

## **如何在Linux中创建新用户**

使用`useradd`创建名为`username`的新用户帐户，您将运行的命令：

```shell
useradd username
```

Copy

在没有任何选项的情况下使用最简单的形式时，useradd将使用`/etc/default/useradd`文件中指定的默认设置创建一个新的用户帐户。

该命令在`/etc/passwd`，`/etc/shadow,` `/etc/group`和`/etc/gshadow`文件加入刚创建用户配置信息。

如想要能够以新创建的用户身份登录，您需要设置用户密码。为此，请运行`passwd`命令后跟用户名：

```shell
passwd username
```

Copy

系统将提示您输入并确认密码。确保使用强密码。

```output
Changing password for user username.
New password:
Retype new password:
passwd: all authentication tokens updated successfully.
```

Copy

## **如何添加新用户和创建主目录**

在大多数Linux发行版中，使用`useradd`命令创建新用户帐户时，不会创建用户主目录。

使用`-m`（`--create-home`）选项创建用户主目录`/home/username`：

```shell
useradd -m username
```

Copy

上面的命令创建新用户的主目录，并将文件从`/etc/skel`目录复制到用户的主目录。如果您列出文件的`/home/username`目录，你会看到初始化文件：

```shell
ls -la /home/username/
```

Copy

```output
drwxr-xr-x 2 username username 4096 Dec 11 11:23 .
drwxr-xr-x 4 root     root     4096 Dec 11 11:23 ..
-rw-r--r-- 1 username username  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 username username 3771 Apr  4  2018 .bashrc
-rw-r--r-- 1 username username  807 Apr  4  2018 .profile
```

Copy

在主目录中，用户可以编写，编辑和删除文件和目录。

## **使用特定主目录创建用户**

如果要在其他位置创建用户的主目录，默认是 `/home` 目录，使用`d`（`--home`）选项改变这个默认值。

例如，要创建一个以`username`主目录命名的新用户，`/opt/username`您需要运行以下命令：

```shell
useradd -m -d /opt/username username
```

Copy

## **创建具有特定用户ID的用户**

在类Unix操作系统中，用户由唯一的UID和用户名标识。

用户标识符（UID）是Linux系统为每个用户分配的唯一正整数。UID以及其他访问控制策略用于确定用户可以对系统资源执行的操作类型。

默认情况下，在创建新用户时，系统会从`login.defs`文件中指定的用户ID范围中分配下一个可用的UID 。

使用`-u`（`--uid`）选项创建具有特定UID的用户。例如，要创建一个名为`username`UID为`1500`的新用户，请输入：

```shell
useradd -u 1500 username
```

Copy

您可以使用以下`id`命令验证用户的UID ：

```shell
id -u username
```

Copy

```output
1500
```

Copy

## **创建具有特定组ID的用户**

Linux组是组织单位，用于在Linux中组织和管理用户帐户。组的主要目的是定义一组权限，例如读取，写入或执行可以在组内用户之间共享的给定资源的权限。

创建新用户时，`useradd`命令的默认行为是创建一个与用户名同名的组，以及与UID相同的GID。

使用`-g`（`--gid`）选项创建具有特定初始登录组的用户。您可以指定组名称或GID号码。组名称或GID必须已存在。

例如，要创建一个名为的新用户并将`username`登录组设置为`users`键入：

```shell
useradd -g users username
```

Copy

要验证用户的GID，请使用以下`id`命令：

```shell
id -gn username
```

Copy

```output
users
```

Copy

## **创建用户并分配多个组**

Linux操作系统中有两种类型的组主要组和辅助组或补充组。每个用户可以属于一个主要组和零个或多个次要组。

在`-G`（`--groups`）选项允许你指定的补充组，其用户将成为其成员的名单。

下面的命令将创建一个名为一个新用户`username`与主组`users`和辅助组`wheel`和`docker`。

```shell
sudo useradd -g users -G wheel,developers username
```

Copy

您可以通过键入来检查用户组

```shell
id username
```

Copy

```output
uid=1002(username) gid=100(users) groups=100(users),10(wheel),993(docker)
```

Copy

## **创建用户时指定登录Shell**

默认情况下，新用户的登录shell设置为`/etc/default/useradd`文件中指定的登录shell 。在某些Linux发行版（如Ubuntu 18.04）中，默认shell设置为`/bin/sh`而在其他版本中则设置为`/bin/bash`。

`-s`（`--shell`）选项允许你指定新用户的登录shell。

例如，要创建一个名为`username`  登录shell是 `/usr/bin/zsh`  的新用户：

```shell
useradd -s /usr/bin/zsh username
```

Copy

检查`/etc/passwd`文件中的用户条目以验证用户的登录shell：

```shell
grep username /etc/passwd
```

Copy

```output
username:x :1001:1001::/home/username:/usr/bin/zsh
```

Copy

## **使用自定义注释创建用户**

在`-c`（`--comment`）选项允许你为新用户添加一个简短的说明。通常，用户的全名或联系信息将添加为注释。

在以下示例中，我们将创建一个用户 `username`的新用户并使用`Test User Account`作为注释：

```shell
useradd -c "Test User Account" username
```

Copy

注释保存在`/etc/passwd`文件中：

```shell
grep username /etc/passwd
```

Copy

```output
username:x :1001:1001:Test User Account:/home/username:/bin/sh
```

Copy

注释字段也称为GECOS。

## **创建具有到期日期的用户**

在`-e`（`--expiredate`）选项允许你定义一个时间，新的用户帐户将到期。此选项对于创建临时帐户很有用。必须使用`YYYY-MM-DD`格式指定日期。

例如，创建一个名为 `username`到期时间设置为2019年10月22日的新用户帐户，您将运行：

```shell
useradd -e 2019-10-22 username
```

Copy

您可以使用`chage`命令验证用户帐户的到期日期：

```shell
sudo chage -l username
```

Copy

输出看起来像这样：

```output
Last password change					: Dec 11, 2018
Password expires					: never
Password inactive					: never
Account expires						: Jan 22, 2019
Minimum number of days between password change		: 0
Maximum number of days between password change		: 99999
Number of days of warning before password expires	: 7
```

Copy

## **创建系统用户**

系统与常规（普通）用户之间没有真正的技术差异。通常，在安装操作系统和新软件包时会创建系统用户。

在某些情况下，您可能需要创建一些将由某些应用程序使用的系统用户。

使用`-r`（`--system`）选项创建系统用户帐户。例如，创建一个名为`username`的新系统用户，您将运行：

```shell
useradd -r username
```

Copy

系统用户创建时没有到期日期。它们的UID是从`login.defs`文件中指定的系统用户ID范围中选择的，该范围不同于普通用户使用的范围。

## **更改默认的useradd值**

可以使用`-D`，`--defaults`选项或手动编辑`/etc/default/useradd`文件中的值来查看和更改默认的useradd选项。

要查看当前的默认选项类型：

```console-bash
useradd -D
```

Copy

输出看起来像这样：

```output
GROUP=100
HOME=/home
INACTIVE=-1
EXPIRE=
SHELL=/bin/sh
SKEL=/etc/skel
CREATE_MAIL_SPOOL=no
```

Copy

假设您要将默认登录shell更改`/bin/sh`为`/bin/bash`。为此，请指定新shell，如下所示：

```shell
useradd -D -s /bin/bash
```

Copy

您可以通过运行以下命令来验证是否更改了默认登录shell值：

```shell
sudo useradd -D | grep -i shell
```

Copy

```output
SHELL=/bin/bash
```

Copy

在本教程中，您学习了如何使用useradd命令添加新用户帐户。相同的命令适用于任何Linux发行版，包括Ubuntu，CentOS，RHEL，Debian，Fedora和Arch Linux。如果您有任何疑问，请随时发表评论。如果你喜欢我们的内容可以选择在下方二维码中捐赠我们，或者点击广告予以支持，感谢你的支持

如果你喜欢我们的内容可以选择在下方二维码中捐赠我们，或者点击广告予以支持，感谢你的支持