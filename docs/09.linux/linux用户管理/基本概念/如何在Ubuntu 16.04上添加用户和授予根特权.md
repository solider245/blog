---
title: 04上添加用户和授予根特权
date: 2020-10-12 12:09:51
permalink: /pages/7ec927/
categories:
  - linux用户管理
  - 基本概念
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 08:24:49
 * @LastEditTime: 2020-07-17 08:24:49
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\基本概念\如何在Ubuntu 16.04上添加用户和授予根特权.md
 * @日行一善，每日一码
--> 
Ubuntu 16.04 LTS使您能够为计划访问服务器的任何人添加用户。 创建用户是一项基本设置，但对于服务器安全性而言是重要且至关重要的设置。 在本教程中，我们将创建一个用户并向您信任的用户授予管理访问权限（称为root）。

[![](https://mluh4on6k7db.i.optimole.com/h1xpWcI-ao12eDyH/w:653/h:367/q:90/https://www.liquidweb.com/kb/wp-content/uploads/2020/04/add.user_.grant_.privs_.042920.jpg)

![](https://mluh4on6k7db.i.optimole.com/h1xpWcI-ao12eDyH/w:1280/h:720/q:90/https://www.liquidweb.com/kb/wp-content/uploads/2020/04/add.user_.grant_.privs_.042920.jpg)

](https://www.youtube.com/embed/qm-HqF1qHMg?rel=)

## 飞行前检查

1.  我们将需要打开一个终端并以root用户身份登录。
2.  我们将在Linux Ubuntu 16.04 LTS服务器上以该root用户身份工作

## 创建具有根特权的用户

**步骤1：添加用户**

为您的新用户创建一个用户名，在我的示例中，我的新用户是Tom：

```
adduser tom
```

然后，系统将提示您输入该用户的密码。 我们建议使用强密码，因为恶意漫游器被编程为猜测简单密码。 如果您需要安全密码，此第三方 [密码生成器](https://www.lastpass.com/password-generator) 可以帮助您创建一个。

**输出** ：

```
~# adduser tom
 Adding user `tom' ...
 Adding new group `tom' (1002) ...
 Adding new user `tom' (1002) with group `tom' ...
 Creating home directory `/home/tom' ...
 Copying files from `/etc/skel' ...
 Enter new UNIX password:
 Retype new UNIX password:
 passwd: password updated successfully
```

注意

用户名应小写，并避免使用特殊字符。 如果您收到以下错误，请更改用户名。 ``~# adduser Tom
adduser: Please enter a username matching the regular expression configured via the NAME_REGEX[_SYSTEM] configuration variable.  Use the `--force-badname' option to relax this check or reconfigure NAME_REGEX.``

接下来，将出现一个文本提示，要求我们输入有关您的新用户的信息。 输入此信息是主观的，不是必需的。 如果需要，可以通过在每个字段中按Enter来跳过此信息。 我们建议根据需要添加尽可能多的信息以跟踪使用情况。

```
Enter the new value or press ENTER for the default
 Full Name []:
 Room Number []:
 Work Phone []:
 Home Phone []:
 Other []:
```

最后，系统将要求您检查信息的准确性。 输入 **Y** 继续下一步。

```
Is the information correct? [Y/n]
```

### **步骤2：授予根权限**

为用户分配root用户访问权限是为了授予该用户在我们系统上的最高特权，因此请注意。 一旦添加了用户Tom，他就可以对整个系统进行更改，因此仅允许需要此权限的用户访问此文件至关重要。 此后，Tom将能够使用通常为root用户保留的sudo选项执行命令。

```
usermod -aG sudo tom
```

### **步骤3：验证新用户**

以root用户身份，您可以使用su –命令切换到新用户，然后进行测试以查看您的新用户是否具有root用户特权。

```
su - tom
```

如果已正确授予用户root权限，则以下命令将在列表中显示tom。

```
grep '^sudo' /etc/group
```

输出：

```
sudo:x:27:tom
```

而已！ 我们添加了一个用户，然后在Ubuntu 16.04 LTS服务器上授予该用户root特权。