---
title: Linux用户和权限管理看了你就会用啦
date: 2020-10-12 12:09:51
permalink: /pages/0de5ba/
categories:
  - 技术
  - linux
tags:
  - 
---
# 前言

> 只有光头才能变强

回顾前面：

*   [看完这篇Linux基本的操作就会了](http://mp.weixin.qq.com/s?__biz=MzI4Njg5MDA5NA==&mid=2247484231&idx=1&sn=4cf217a4d692a7aba804e5d96186b15b&chksm=ebd74246dca0cb5024de2f1d9f9e2ecb631e49752713c25bbe44f44856e919df5a973049c189#rd)

没想到上一篇能在知乎获得千赞呀，Linux也快期末考试了，也有半个月没有写文章了。这篇主要将Linux下的**用户和权限**知识点再整理一下。

那么接下来就开始吧，如果文章有错误的地方请大家多多包涵，不吝在评论区指正哦~

# 一、Linux下的用户

Linux是一个**多用户的系统**，我们可以多个用户同时登陆Linux~

*   账户**实质**上就是一个**用户在系统上的标识**。

Linux中的账户包括

*   **用户账户**
    *   **普通用户账户**：在系统上的任务是进行普通工作
    *   **超级用户账户**（或管理员账户）：在系统上的任务是对普通用户和整个系统进行管理。
*   **组账户**(组是用户的集合)
    *   标准组：标准组可以容纳多个用户
    *   私有组：私有组中只有用户自己

当一个用户同**属于多个组**时，将这些组分为

*   **主组**（初始组）：用户登录系统时的组。
*   **附加组**：登录后可切换的其他组

上面也说了，账户的实质上就是用户在系统上的标识，这些标识是用**文件保存**起来的：

*   用户名和 UID 被保存在`/etc/passwd`文件中，文件权限 `(-rw-r--r--)`
*   组和GID 被保存在 `/etc/group`文件中，文件权限`(-r--------)`
*   用户口令(密码)被保存在 `/etc/shadow`文件中 ，文件权限`(-rw-r--r-- )`
*   组口令被保存在 `/etc/gshadow`文件中 ，文件权限 `(-r--------)`

也就是说：**我们创建的用户，这个用户的信息由不同的文件来保存着**。

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecf025da0aec?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecf31772af4b?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd1986a7b85?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd19c5e4e0c?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

有了上面的知识点，下面我来简述一下创建用户的时候会发生什么：

*   用户名和 UID 被保存在 `/etc/passwd` 这个文件中，用户的口令通常用`shadow passwords`保护
*   当用户登录时，他们**被分配了一个主目录和一个运行的程序**（通常是 shell）
*   若没有指定他所属于的组，RHEL/CentOS就建立一个和**该用户同名的私有组**，且用户被分配到这个私有组中

再来回顾一下：账户的实质上就是用户在系统上的标识，这些标识是用**文件保存**起来的。也就是说：我们是可以**直接编辑修改系统账户文件来维护账户**。

*   但是**不建议这样做**，如果明确要这样做的话，最好使用命令检测一下你编辑的语法是否有问题：
    *   `pwck`：验证用户账号文件，认证信息的完整性。该命令检测文件`“/etc/passwd”`和`“/etc/shadow”` 的每行中字段的格式和值是否正确
    *   `grpck`：验证组账号文件，认证信息的完整性。该命令检测文件`“/etc/group”`和`“/etc/gshadow”`的每行中字段的格式和值是否正确。

既然不建议我们直接编辑文件的方式来管理用户，那么Linux是肯定**有现成的命令**给我们使用的：

## 1.1管理Linux用户的命令

**用户管理**：

*   `useradd`
*   `usermod`
*   `userdel`

**组管理**：

*   `groupadd`
*   `groupmod`
*   `groupdel`

**批量管理用户**：

*   成批添加/更新一组账户：`newusers`
*   成批更新用户的口令：`chpasswd`

**组成员管理**：

*   向标准组中添加用户
    *   `gpasswd -a <用户账号名> <组账号名>`
    *   `usermod -G <组账号名> <用户账号名>`
*   从标准组中删除用户
    *   `gpasswd -d <用户账号名> <组账号名>`

**口令维护**(禁用、恢复和删除用户口令)：

*   **设置用户口令**：
    *   `passwd [<用户账号名>]`
*   禁用用户账户口令
    *   `passwd -l <用户账号名>`
*   查看用户账户口令状态
    *   `passwd -S <用户账号名>`
*   恢复用户账户口令
    *   `passwd -u <用户账号名>`
*   清除用户账户口令
    *   `passwd -d <用户账号名>`

**口令时效设置**：

*   修改 `/etc/login.defs` 的相关配置参数

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd19c616464?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

设置**已存在用户的口令时效**：

*   `chage`命令

**用户切换命令**：

*   `su`
    *   直接切换为超级用户
*   `sudo`
    *   直接使用 sudo 命令前缀执行系统管理命令。执行系统管理命令时无需知道超级用户的口令，使用普通用户自己的口令即可

更多资料查询：

*   [www.cnblogs.com/slgkaifa/p/…](https://www.cnblogs.com/slgkaifa/p/6852884.html)\-\-linux权限之su和sudo的差别

**用户相关的命令**：

*   `id`：显示用户当前的uid、gid和用户所属的组列表
*   `groups`：显示指定用户所属的组列表
*   `whoami`：显示当前用户的名称
*   `w/who`：显示登录用户及相关信息
*   `newgrp`：用于转换用户的当前组到指定的组账号，用户必须属于该组才可以正确执行该命令

## 1.2Linux用户的练习题

> 用cat命令，观察如下文件：/etc/passwd , /etc/shadow, /etc/group,/etc/gshadow；显示useradd命令添加用户参数的默认值

![](https://user-gold-cdn.xitu.io/2018/6/11/163eece7c6712492?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecf025f36fab?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd1f336da6b?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd22de58362?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

> 建立linux账户jkXX（XX为学生学号末两位），要求用户组为users，并设置密码；观察/etc/passwd和/etc/shadow文件的变化；退出root账户，用jkXX账户登录，在其主目录下建立一个myfirst文件，并用长格式列出myfirst文件

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd21b5fd3f6?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd2340b7942?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eece7c6ad10de?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecf026259010?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

> 用root账户登录；添加组jsj；设置用户jkXX为jsj组用户，观察/etc/passwd、/etc/group和/etc/gshadow文件变化

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd821acf4ce?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eece85e8bf7b7?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd8255fd565?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd8510d9c08?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

> 添加一个新用户airXX（XX为学生学号末两位），观察新用户airXX的用户id和组id；然后删除该用户，注意不要在命令中加选项，观察用户文件和组文件的变化；观察airXX用户的目录是否存在；

![](https://user-gold-cdn.xitu.io/2018/6/11/163eece886c90da7?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd882d6f51d?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecfb91b729cc?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecf026f4d658?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecef3982a1d0?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecef3b98a001?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

> shadow文件中密码为\*号和！！代表什么？

答：`*`代表账户禁用；`！！`代表密码锁定。

> airXX用户组id是多少？这个组是什么类型的组？这样做有什么好处？

答：air08用户组id是501，这个组属于私有组。每个未指定组的用户会建立一个同名的组，这样的组称为私有组，只有一个用户，既有利于防止信息泄露，也也有利于防止不合理的授权。总之，有利于安全管理。

> 默认情况下删除用户，但却保留了用户的主目录，这样做有什么好处？

答：保留用户目录，防止将用户目录下有价值的资料误删除。

> 用cat命令，观察文件/etc/passwd；仿照passwd文件的格式，用vi编辑一个新的文件，文件名为userXX（XX为学生学号末两位），文件包括3条记录，用户名分别为jkXX（XX为学生学号末两位），peter，jason，他们的用户id大于1000，组id大于1000，要求peter和jason同组；用命令newusers根据文件userXX的内容批量生成用户；观察/etc/passwd文件的变化。

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="594" height="94"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="314" height="18"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="415" height="52"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="378" height="25"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="445" height="75"></svg>)

> 用cat命令，观察文件/etc/shadow；用vi编辑一个新文件，文件名为mimaXX（XX为学生学号末两位），文件包括3条记录，每条记录用户名与上一步骤要求相同，密码自行设置，用户名和密码用冒号：隔开；用命令chpasswd根据文件mimaXX的内容批量生成密码；观察文件/etc/shadow变化；用命令chpasswd \-m再次批量生成密码，观察文件/etc/shadow变化；

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="329" height="18"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="137" height="63"></svg>)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd42457805d?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eeceae8eebd5f?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

> 退出root账户，用jkXX账户登录。退出jkXX账户，返回root账户，观察/etc/shadow文件;用passwd命令锁定用户jkXX，观察/etc/shadow文件变化；然后退出root账户，用jkXX账户登录，是否成功？

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecf15e157162?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecf317baf879?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eeceaecc9de64?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eeceaed0e06dc?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd8f2974eb6?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

> 用chage命令查看peter账户的时间设置；重新设置peter账户的时间，要求两天内不能更改口令，且口令最长的存活期为 90 天，并在口令过期前 5 天通知用户，口令超期7天密码失效；用chage命令再次查看peter账户的时间设置

![](https://user-gold-cdn.xitu.io/2018/6/11/163eeceaed486bac?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd900929cd7?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

> 用root账户登录；用su切换到jason账户；用cd进入用户主目录；创建一个新文件abc，用长格式列出abc文件；观察文件的用户和组的属性

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="267" height="66"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="406" height="79"></svg>)

> 锁定账户后，shadow文件发生了什么变化？

答：锁定账户的密码之前会锁定标志！！

> 用su切换用户后，建立的新文件文件属于哪个用户？

答：新文件属于切换之后的用户。

> 两次执行chpasswd命令，结果是否相同？加密算法md5和sha512哪个更安全？

答：两次执行chpasswd命令结果不同，默认情况采用sha512加密算法；\-m选项时，采用md5加密算法；sha512更安全，因为加密信息长度更长，破解计算量大。

> 建立三个普通用户账户，要求如下：用户名分别为jkXX（XX为学生学号末两位），peter，jason，其中jkXX和jason为相同普通组成员；观察/etc/passwd文件的变化。为jkXX账户添加root组；

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="606" height="261"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="378" height="20"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="347" height="192"></svg>)

> 分别练习id，groups，whoami，who命令，显示当前账户的信息；用su命令切换到jkXX账户，分别练习id，groups，whoami，who命令，显示当前账户的信息。用newgrp切换jkXX账户的组，分别练习id，groups，whoami，who命令，显示当前账户的信息

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="682" height="160"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="680" height="162"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="466" height="180"></svg>)

# 二、权限管理

Linux是多用户的操作系统，允许多个用户同时在系统上登录和工作。 为了**确保**系统和用户的**安全**，Linux自然就有自己一套的权限管理机制了！

相信用过Linux的同学在检索文件夹文件的时候常常用到`ls -l`的命令，会出来一大串的数据。这些数据你能读懂了吗？

例如：

```

	drwxr-xr-x   3  osmond   osmond    4096  05-16 13:32   nobp

复制代码
```

其实很简单：

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="1040" height="270"></svg>)

其实我们看权限就是看`drwxr-xr-x`这么一串东西，看起来很复杂，但不是的，一下就可以理解了。我们来分解一下：

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="895" height="269"></svg>)

这9个字符**每3个一组**，组成 3 套 权限控制

*   第一套控制文件**所有者**的访问权限
*   第二套控制所有者**所在用户组**的其他成员的访问权限
*   第三套控制**系统其他用户**的访问权限

**rwx**分别代表的意思：

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="976" height="478"></svg>)

看到这里来，如果前面的你看懂了，那`drwxr-xr-x`这么一串东西我觉得你很容易就能理解了：

*   d是文件夹，后面还有9个字母，每3个分成一组，`-`号表示没有。那么这个文件夹的权限就是：
    *   **对当前用户是可读可写可执行，对同组的用户是可读可执行，对其他的用户是可读可执行**

是不是很简单？？`r-read,w-write,x-execute`，很好理解的。

对于这些rwx命令为了方便还可以换成八进制的数据来表示，我相信大家看完下面的demo也知道其实就这么一回事了：

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="970" height="574"></svg>)

**权限的优先顺序**：

*   如果UID匹配，就应用用户属主（user）权限
*   否则，如果GID匹配，就应用组（group）权限
*   如果都不匹配，就应用其它用户（other）权限
*   **超级用户root具有一切权限**，无需特殊说明

## 2.1管理Linux权限的常用命令

*   `chmod`
    *   改变文件或目录的权限
*   `chown`
    *   改变文件或目录的属主（所有者）
*   `chgrp`
    *   改变文件或目录所属的组
*   `umask`
    *   设置文件的缺省生成掩码

例子：

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecedea7f99d1?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd4f219ef23?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

## 2.2权限扩展知识

上面提到了umask属性，它用来做这样的东西的：默认生成掩码告诉系统当创建一个文件或目录时**不应该赋予其哪些权限**。

*   默认的umask的值是022，我们看一下下面的例子应该就能懂了：

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="972" height="485"></svg>)

除了上面所说的权限之外，Linux还提供了**三种特殊的权限**：

*   SUID：使用命令的**所属用户的权限来运行**，而不是命令执行者的权限
*   SGID：使用命令的**组权限来运行**。
*   Sticky\-bit：目录中的文件**只能被文件的所属用户和root用户删除**。

它们是这样表示的：

*   SUID和SGID用s表示；Sticky\-bit用t表示
*   SUID是占用属主的x位置来表示
*   SGID是占用组的x位置来表示
*   sticky\-bit是占用其他人的x位置来表示

例如：`drwxrwxrwt 5 root root 4096 06-18 01:01 /tmp`它就拥有sticky\-bit权限。`-rwsr-xr-x 1 root root 23420 2010-08-11 /usr/bin/passwd`它就拥有SUID权限

SUID，SGID，sticky\-bit同样也有数字的表示法：

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="954" height="383"></svg>)

使用的例子：

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="830" height="518"></svg>)

---

Linux内核中有大量安全特征。EXT2/3/4**文件系统的扩展属性**（Extended Attributes）可以在某种程度上保护系统的安全

**常见的扩展属性：**

*   A（Atime）：告诉系统不要修改对这个文件的最后访问时间。
    *   **使用A属性可以提高一定的性能**。
*   S（Sync）：一旦应用程序对这个文件执行了写操作，使系统立刻把修改的结果写到磁盘。
    *   **使用S属性能够最大限度的保障文件的完整性**。
*   a（Append Only）：系统只允许在这个文件之后追加数据，不允许任何进程覆盖或者截断这个文件。如果目录具有这个属性，系统将 只允许在这个目录下建立和修改文件，而不允许删除任何文件。
*   i（Immutable）：系统不允许对这个文件进行任何的修改。如果目录具有这个属性，那么任何的进程只能修改目录之下的文件，不允许建立和删除文件。
    *   **a属性和i属性对于提高文件系统的安全性和保障文件系统的完整性有很大的好处**。

**常用命令**：

*   显示扩展属性：`lsattr [-adR] [文件|目录]`
*   修改扩展属性：`chattr [-R] [[-+=][属性]] <文件|目录>`

## 2.3权限管理练习题

> 用root账户登录，创建一个文件aaaXX（XX为学生学号末两位），用长格式查看文件权限；用chmod命令，文字设定法，给aaaXX文件同组增加写属性，观察结果；用chmod命令，数字设定法，给aaaXX文件设置权限为766，观察结果；

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="414" height="159"></svg>)

> 切换到peter账户，查看当前umask是多少，观察结果；创建一个目录foldXX（XX为学生学号末两位），查看其权限；创建一个新文件bbb，查看其权限；改变unmask为066，创建一个新文件ccc，查看其权限

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="463" height="162"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="464" height="132"></svg>)

> 切换到jkXX账户；创建一个文件myfile，观察其属性；用chgrp改变文件myfile组属性为root；试着去改变文件myfile主属性为root，可以吗？切换到root账户，改变文件myfile主属性为root，观察结果

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecf405a91be5?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecf406113e96?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd9a78169ec?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

> 数字设定766代表文件权限是什么？

答：766代表文件权限为`rwx-rw-rw-`

> 为什么用jkXX账户改变文件myfile的属主失败？

答：因为chown只有root账户才可以使用

> Umask为022和066对新创建的文件属性影响一样吗？为什么？

答：影响当然不一样，umask定义的是默认不应该获得的权限，066比022转换成为二进制数后，多了两个限制比特位。

> 以root账户登录，复制/usr/bin/dir文件到用户主目录，用长格式列出，设置文件的suid和sguid为1,用长格式列出；切换帐号为jkXX，运行复制过来的文件dir（注意运行当前路径下的文件要带上路径，例如./dir）；

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd9a7b5bd48?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecd9b4259aa2?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

> 切换到jkXX账户，进入/tmp目录，建立文件夹myfold，设置文件夹myfold权限为777，并且sgid和sticky\-bit为1，用长格式列出，观察myfold的属性；进入myfold，创建新文件aaa，设置属性为任何人可读可写，用长格式列出；切换到jason账户，进入/tmp/myfold目录，删除aaa文件，是否可以删除？

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="384" height="64"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="466" height="98"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="455" height="99"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="338" height="32"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="415" height="63"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="438" height="148"></svg>)

> root账户，进入用户主目录；创建一个文件bbb文件，查看文件的扩展属性；给文件bbb添加扩展属性i，然后试着删除该文件，是否成功，怎样才能删除；创建一个ccc文件，给文件ccc添加扩展属性a，用长格式列表/bin目录并重定向输出到ccc文件，观察ccc文件长度的变化，用长格式列表/etc目录，并重定向输出到ccc文件，是否成功

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="387" height="93"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="438" height="114"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="451" height="127"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="447" height="225"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="421" height="95"></svg>)

> 切换到jkXX账户，在/tmp目录下创建一个目录myshare，用getfacl查看myshare目录文件访问控制表；设置myshare文件夹对于jason用户权限为rwx，查看文件访问控制表的变化；切换到jason账户，进入myshare文件创建文件yyy，是否成功；切换到peter账户，进入myshare文件创建文件zzz，是否成功，为什么？

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="320" height="35"></svg>)

![](data:image/svg+xml;utf8,<?xml version="1.0"?><svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="453" height="114"></svg>)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eece9fcd6f2cb?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eece9fe758a0b?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecebc4700cd1?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

> myfold目录下，为什么jason账户不能删除一个任何人都可读可写的文件？

答：因为文件所在的文件夹myfold被它的所属者jk08设置了stickybit位，该文件夹下面的所有文件，只有文件所属者，以及root用户才能删除。

> 为什么peter账户在在myshare文件夹里面不能创建文件？

答：因为myshare文件夹，属于jk08用户，只有jk08对该目录具备rwx权限。此外，采用facl的方式，给jason用户开放了该目录的rwx访问权限；peter既不是文件夹的拥有者，也没有在facl中开放rwx权限；依据权限设置情况，peter只有该文件夹的rx权限。因此，不能创建文件。

> 添加扩展属性a后，用重定向将输出内容给ccc文件，可能会失败，怎样才能输出成功？

答：应该采用追加方式的重定向>>，可以在文件末尾添加内容，这样才符合文件扩展属性a的安全规定。

# 三、总结

本文主要是总结了Linux下操作用户和权限的知识~~~这两个知识点在Linux下也是很重要的，是学习Linux的基础~

**继续完善上一次的思维导图**：

![](https://user-gold-cdn.xitu.io/2018/6/11/163eecebc5a03892?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

如果文章有错的地方欢迎指正，大家互相交流。习惯在微信看技术文章，想要获取更多的Java资源的同学，可以关注微信公众号:Java3y

**文章的目录导航**：

*   [zhongfucheng.bitcron.com/post/shou\-j…](https://zhongfucheng.bitcron.com/post/shou-ji/wen-zhang-dao-hang)