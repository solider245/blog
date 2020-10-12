---
title: 操作系统-多用户如何理解（Linux）
date: 2020-10-12 12:09:51
permalink: /pages/629516/
categories:
  - linux用户管理
  - 基本概念
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 17:22:05
 * @LastEditTime: 2020-07-17 17:22:05
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\基本概念\操作系统-多用户如何理解（Linux）.md
 * @日行一善，每日一码
--> 
　　单用户、多用户、单任务、多任务，这么多种操作系统容易让人迷糊。其实这种初看你会觉得理解了一点，但其实你仔细研究会发现，多用户到底讲的是什么鬼？

　　多任务比较简单，就是应用程序都要放置到内存上去给CPU调度执行的，你正在使用的浏览器、QQ、音乐播放器，都放置在内存中（不一定此刻就在执行），你同一时刻即在浏览网页、玩QQ、听歌，这就是多任务。

　　由于Linux继承了Unix的特性，天生支持用户模式，不太好对比，我们来看看Windows操作系统。

　　个人计算机操作系统早期一般都是单用户操作系统，其主要特点是在某一时间为单个用户服务。早期的DOS操作系统是单用户单任务操作系统，Windows XP则是单用户多任务操作系统。现在常用的Windows操作系统都是多用户、多任务的操作系统，使用最广泛的win7，win10都是多用户，多任务操作系统。

　　我们平时使用的时候没看到什么多用户啊，都是我一个人在使用啊，难道说我坐在电脑前敲键盘，这里还有别的用户可以坐在电脑边跟我一起敲键盘？

　　注意我们看到的是多用户的操作系统，而不是多用户的电脑，一般电脑叫什么？是不是叫个人计算机，是不是你一个人在使用，所以这里的多用户指的是操作系统的层的多用户，也就是不仅你输入密码登陆的那个账号可以使用系统资源（内存、磁盘、cpu），还有由你登陆的用户创建的新用户可以使用。 多个用户能够同时访问和使用同一台计算机，其中的一个用户具有管理所有这些用户账户和整个计算机的资源的权限，在Windows上，这个具有管理其他用户和计算机资源的用户一般叫administrator。

　　那么比如像Windows xp这种单用户系统，只能有一个用户在同一时间使用，比如使用远程桌面，多用户可以同时登录，单用户则会把其他用户挤掉。这里的远程桌面就是一个软件，客户端，可以对你的电脑进行操作。

　　再举一个例子，用win7的管理员登录进去后，切换为账户guest执行关机命令，系统提示其他用户正在登录，可以说明win7是多用户多任务的操作系统。

　　今天的主题是Linux，在Linux中是如何管理多用户的呢？

　　一、用户与组的概念

　　1．理解linux多用户，多任务的特性

　　Linux是一个真实的、完整的多用户多任务操作系统，多用户多任务就是可以在系统上建立多个用户，而多个用户可以在同一时间内登录同一个系统执行各自不同的任务，而互不影响，例如某台linux服务器上有4个用户，分别是root、www、ftp和mysql，在同一时间内，root用户可能在查看系统日志，管理维护系统，www用户可能在修改自己的网页程序，ftp用户可能在上传软件到服务器，mysql用户可能在执行自己的SQL查询，每个用户互不干扰，有条不紊的进行着自己的工作，而每个用户之间不能越权访问，比如www用户不能执行mysql用户的SQL查询操作，ftp用户也不能修改www用户的网页程序，因此可知，不同用户具有不同的权限，每个用户是在权限允许的范围内完成不同的任务，linux正是通过这种权限的划分与管理，实现了多用户多任务的运行机制。

　　2．linux下用户的角色分类

　　在linux下用户是根据角色定义的，具体分为三种角色：

　　 超级用户：拥有对系统的最高管理权限，默认是root用户。
　　 普通用户：只能对自己目录下的文件进行访问和修改，具有登录系统的权限，例如上面提到的www用户、ftp用户等。
　　 虚拟用户：也叫“伪”用户，这类用户最大的特点是不能登录系统，它们的存在主要是方便系统管理，满足相应的系统进程对文件属主的要求。例如系统默认的bin、adm、nobody用户等，一般运行的web服务，默认就是使用的nobody用户，但是nobody用户是不能登录系统的。

　　3．用户和组的概念

　　我们知道，Linux是一个多用户多任务的分时操作系统，如果要使用系统资源，就必须向系统管理员申请一个账户，然后通过这个账户进入系统。这个账户和用户是一个概念，通过建立不同属性的用户，一方面，可以合理的利用和控制系统资源，另一方面也可以帮助用户组织文件，提供对用户文件的安全性保护。

　　每个用户都用一个唯一的用户名和用户口令，在登录系统时，只有正确输入了用户名和密码，才能进入系统和自己的主目录。

　　用户组是具有相同特征用户的逻辑集合，有时我们需要让多个用户具有相同的权限，比如查看、修改某一个文件的权限，一种方法是分别对多个用户进行文件访问授权，如果有10个用户的话，就需要授权10次，显然这种方法不太合理；另一种方法是建立一个组，让这个组具有查看、修改此文件的权限，然后将所有需要访问此文件的用户放入这个组中，那么所有用户就具有了和组一样的权限。这就是用户组，将用户分组是Linux 系统中对用户进行管理及控制访问权限的一种手段，通过定义用户组，在很大程度上简化了管理工作。

　　4．用户和组的关系：

　　这里的用户和组的关系有点像数据库里面的关系：

　　用户和用户组的对应关系有：一对一、一对多、多对一和多对多；下图展示了这种关系：

　　 一对一：即一个用户可以存在一个组中，也可以是组中的唯一成员。
　　 一对多：即一个用户可以存在多个用户组中。那么此用户具有多个组的共同权限。
　　 多对一：多个用户可以存在一个组中，这些用户具有和组相同的权限。
　　 多对多：多个用户可以存在多个组中。其实就是上面三个对应关系的扩展。

　　二、用户配置文件概述

　　1．用户和组相关的配置文件

　　（1）/etc/passwd文件

　　系统用户配置文件，是用户管理中最重要的一个文件。这个文件记录了Linux系统中每个用户的一些基本属性，并且对所有用户可读。/etc/passwd中每一行记录对应一个用户，每行记录又被冒号分割，其格式和具体含义如下：

　　用户名:口令:用户标识号:组标识号:注释性描述:主目录:默认shell

　　下面是/etc/passwd文件的部分输出：

　　\[root@localhost ~\]# more /etc/passwd
　　　　root:x:0:0:root:/root:/bin/bash
　　　　bin:x:1:1:bin:/bin:/sbin/nologin
　　　　daemon:x:2:2:daemon:/sbin:/sbin/nologin
　　　　adm:x:3:4:adm:/var/adm:/sbin/nologin
　　　　lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin

　　下面是每个字段的详细含义：

　　 用户名：是代表用户账号的字符串。
　　 口令：存放着加密后的用户口令，虽然这个字段存放的只是用户口令的加密串，不是明文，但是由于/etc/passwd文件对所有用户都可读，所以这仍是一个安全隐患。因此，现在许多Linux 版本都使用了shadow技术，把真正加密后的用户口令存放到/etc/shadow文件中，而在/etc/passwd文件的口令字段中只存放一个特殊的字符，例如用“x”或者“\*”来表示。

　　 用户标识号：就是用户的UID，每个用户都有一个UID，并且是唯一的，通常UID号的取值范围是0～65535，0是超级用户root的标识号，1～99由系统保留，作为管理账号，普通用户的标识号从100开始。而在Linux系统中，普通用户UID默认从500开始。UID是linux下确认用户权限的标志，用户的角色和权限都是通过UID来实现的，因此多个用户公用一个UID是非常危险的，会造成系统权限和管理的混乱，例如将普通用户的UID设置为0后，这个普通用户就具有了root用户的权限，这是极度危险的操作。因此要尽量保持用户UID的唯一性。

　　 组标识号：就是组的GID，与用户的UID类似，这个字段记录了用户所属的用户组。它对应着/etc/group文件中的一条记录。
　　 注释性描述：字段是对用户的描述信息，比如用户的住址、电话、姓名等等。
　　 主目录：也就是用户登录到系统之后默认所处的目录，也可以叫做用户的主目录、家目录、根目录等等。
　　 默认shell：就是用户登录系统后默认使用的命令解释器，shell是用户和linux内核之间的接口，用户所作的任何操作，都是通过shell传递给系统内核的。linux下常用的shell有sh、bash、csh等，管理员可以根据用户的习惯，为每个用户设置不同的shell。

　　（2）/etc/shadow文件

　　用户影子文件，由于/etc/passwd文件是所有用户都可读的，这样就导致了用户的密码容易出现泄露，因此，linux将用户的密码信从/etc/passwd中分离出来，单独的放到了一个文件中，这个文件就是/etc/shadow，该文件只有root用户拥有读权限，从而保证了用户密码的安全性。

　　下面介绍下/etc/shadow文件内容的格式：

　　用户名:加密口令:最后一次修改时间:最小时间间隔:最大时间间隔:警告时间:不活动时间:失效时间:保留字段

例如：

　　下面是/etc/shadow文件的部分输出：

　　\[root@localhost ~\]# more /etc/shadow
　　　　root:$1$Uvip.QJI$GteCsLrSSfpnMs.VCOvbs/:14169:0:99999:7:::
　　　　bin:\*:13934:0:99999:7:::
　　　　daemon:\*:13934:0:99999:7:::
　　　　adm:\*:13934:0:99999:7:::

　　下面是每个字段的详细含义：

　　 用户名：与/etc/passwd文件中的用户名有相同的含义。
　　 加密口令：存放的是加密后的用户口令字串，如果此字段是“\*”、“!”、“x”等字符，则对应的用户不能登录系统。
　　 最后一次修改时间：表示从某个时间起，到用户最近一次修改口令的间隔天数。可以通过passwd 来修改用户的密码，然后查看/etc/shadow中此字段的变化。
　　 最小时间间隔：表示两次修改密码之间的最小时间间隔。
　　 最大时间间隔：表示两次修改密码之间的最大时间间隔，这个设置能增强管理员管理用户的时效性。
　　 警告时间：表示从系统开始警告用户到密码正式失效之间的天数。
　　 不活动时间：此字段表示用户口令作废多少天后，系统会禁用此用户，也就是说系统不再让此用户登录，也不会提示用户过期，是完全禁用。
　　 失效时间：表示该用户的帐号生存期，超过这个设定时间，帐号失效，用户就无法登录系统了。如果这个字段的值为空，帐号永久可用。
　　 保留字段：linux的保留字段，目前为空，以备linux日后发展之用。

　　（3）/etc/group文件
　　用户组配置文件，用户组的所有信息都存放在此文件中。
　　下面介绍下/etc/group文件内容的格式：
　　组名:口令:组标识号:组内用户列表
例如：

　　下面是/etc/group的部分输出：

　　\[root@localhost ~\]# more /etc/group
　　　　root:x:0:root
　　　　bin:x:1:root,bin,daemon
　　　　daemon:x:2:root,bin,daemon

　　下面是/etc/group每个字段的含义：

　　 组名：是用户组的名称，由字母或数字构成。与/etc/passwd中的用户名一样，组名不能重复。
　　 口令：存放的是用户组加密后的口令字串，密码默认设置在/etc/gshadow文件中，而在这里用“x”代替，linux系统下默认的用户组都没有口令，可以通过gpasswd来给用户组添加密码。
　　 组标识号：就是GID，与/etc/passwd中的组标识号对应。
　　 组内用户列表： 显示属于这个组的所有用户，多个用户之间用逗号分隔。

　　2．/etc/login.defs文件

　　用来定义创建一个用户时的默认设置，比如指定用户的UID和GID的范围，用户的过期时间、是否需要创建用户主目录等等。

　　下面是rhel5下的/etc/login.defs文件，简单介绍如下：
　　　　MAIL\_DIR        /var/spool/mail
　　当创建用户时，同时在目录/var/spool/mail中创建一个用户mail文件
　　　　PASS\_MAX\_DAYS   99999
　　#指定密码保持有效的最大天数
　　　　PASS\_MIN\_DAYS   0
　　表示自从上次密码修改以来多少天后用户才被允许修改口令
　　　　PASS\_MIN\_LEN    5
　　指定密码的最小长度
　　　　PASS\_WARN\_AGE   7
　　表示在口令到期前多少天系统开始通知用户口令即将到期
　　　　UID\_MIN                   500
　　指定最小UID为500 ，也就是说添加用户时，用户的UID 从500开始
　　　　UID\_MAX                 60000
　　指定最大UID为60000
　　　　GID\_MIN                   500
　　指定最小GID为500，也就是添加组时，组的GID从500开始。
　　　　GID\_MAX                 60000
　　指定最大GID为60000
　　　　CREATE\_HOME     yes
　　此项是指定是否创建用户主目录，yes为创建，no为不创建。

　　3．/etc/default/useradd文件

　　当我们通过useradd命令不加任何参数创建一个用户后，用户默认的主目录一般位于/home下，默认使用的shell是/bin/bash，这是为什么呢，看看/etc/default/useradd这个文件的内容就完全明白了。

　　\[root@localhost ~\]# more /etc/default/useradd
　　　　# useradd defaults file
　　　　GROUP=100
　　　　HOME=/home  #此项表示将新建用户的主目录放在/home目录下
　　　　INACTIVE=\-1 #此项表示是否启用帐号过期禁用，\-1表示不启用
　　　　EXPIRE=     #此项表示帐号过期日期，不设置表示不启用
　　　　SHELL=/bin/bash  #此项指定了新建用户的默认shell类型
　　　　SKEL=/etc/skel  #此项用来指定用户主目录默认文件的来源，也就是说新建用户主目录下的文件都是从这个目录下复制而来的
　　　　CREATE\_MAIL\_SPOOL=no

　　/etc/default/useradd文件定义了新建用户的一些默认属性，比如用户的主目录、使用的shell等等，通过更改此文件，可以改变创建新用户的默认属性值。

　　改变此文件有两种方法，一种是通过文本编辑器方式更改，另一种是通过useradd命令来更改。这里介绍一下第二种方法：

　　Useradd命令加“\-D”参数后，就可以修改配置文件/etc/default/useradd，使用的一般格式为：
　　　　useradd \-D \[\-g group\] \[\-b base\] \[\-s shell\] \[\-f inactive\] \[\-e expire \]
　　每个选项详细含义如下：

　　 \-g default\_group
　　表示新建用户的起始组名或者GID，组名必须为已经存在的用户组名称，GID也必须是已经存在的用户组GID。与/etc/default/useradd文件中“GROUP”行对应。
　　 \-b default\_home
　　指定新建用户主目录的上级目录，也就是所有新建用户都会在此目录下创建自己的主目录。与/etc/default/useradd文件中HOME行对应。
　　 \-s default\_shell
　　指定新建用户默认使用的shell，与/etc/default/useradd文件中“SHELL”行对应。
　　 \-f default\_inactive
　　指定用户帐号过期多长时间后就永久停用，与/etc/default/useradd文件中“INACTIVE”行对应。
　　 \-e default\_expire\_date

　　指定用户帐号的过期时间。与/etc/default/useradd文件中“EXPIRE”行对应。

例子：

　　useradd –D不加任何参数时，显示/etc/default/useradd文件的当前设置

　　\[root@localhost ~\]# useradd \-D
　　　　GROUP=100
　　　　HOME=/home
　　　　INACTIVE=\-1
　　　　EXPIRE=
　　　　SHELL=/bin/bash
　　　　SKEL=/etc/skel

　　如果要修改添加用户时的默认shell为/bin/csh，可以这么操作：

　　\[root@localhost ~\]# useradd \-D \-s /bin/csh
　　\[root@localhost ~\]# useradd \-D
　　　　GROUP=100
　　　　HOME=/home
　　　　INACTIVE=\-1
　　　　EXPIRE=
　　　　SHELL=/bin/csh
　　　　SKEL=/etc/skel

　　4．/etc/skel目录

　　在创建一个新用户后，会在新用户的主目录下看到类似.bash\_profile, .bashrc, .bash\_logout等文件，这些文件是怎么来的呢，如果我想让新建立的用户在主目录下默认拥有自己指定的配置文件，该如何设置呢？
　　/etc/skel目录就是解决这个问题的，/etc/skel目录定义了新建用户在主目录下默认的配置文件，更改/etc/skel目录下的内容就可以改变新建用户默认主目录的配置文件信息。

　　**用户管理工具  **

　　一.添加、切换、删除用户组命令groupadd/newgrp/groupdel
　　1．groupadd命令
　　用来新建一个用户组。语法格式为：
　　　　groupadd \[\-g \-o\] gid  group
　　各个选项具体含义如下：
　　　　\-g：指定新建用户组的GID号，该GID号必须唯一，不能和其它用户组的GID号重复。
　　　　\-o：一般与\-g选项同时使用，表示新用户组的GID可以与系统已有用户组的GID相同。
例如：
　　创建一个linuxfans的用户组和一个fanslinux用户组，GID分别为1020和1030
　　\[root@localhost ~\]# groupadd \-g 1020 linuxfans
　　\[root@localhost ~\]# groupadd \-g 1030 fanslinux
　　\[root@localhost ~\]# more /etc/group|grep  linuxfans
　　　　linuxfans:x:1020:
　　\[root@localhost ~\]# more /etc/group|grep  fanslinux
　　　　fanslinux:x:1030:
　　2．newgrp命令
　　如果一个用户同时属于多个用户组，那么用户可以在用户组之间切换，以便具有其他用户组的权限，newgrp主要用于在多个用户组之间进行切换，语法格式为：
　　　　newgrp <用户组>
 例子：

　　下面通过实例讲述newgrp的用法：
　　首先建立了3个用户组group1、group2和group3.
　　\[root@localhost ~\]# groupadd group1
　　\[root@localhost ~\]# groupadd group2
　　\[root@localhost ~\]# groupadd group3
　　下面创建了一个用户user1，同时指定user1的主用户组为group1，附加用户组为group2和group3
　　\[root@localhost ~\]# useradd \-g group1 \-G group2,group3 user1
　　\[root@localhost ~\]# more /etc/group|grep user1
　　　　group2:x:501:user1
　　　　group3:x:502:user1
　　下面是对用户user1设置密码
　　\[root@localhost ~\]# passwd user1
　　　　Changing password for user user1.
　　　　New UNIX password:
　　　　Retype new UNIX password:
　　　　passwd: all authentication tokens updated successfully.
　　下面是切换到user1用户下，通过newgrp切换用户组进行的一系列操作，从中可以看出newgrp的作用。
　　\[root@localhost ~\]# su \- user1
　　\[user1@localhost ~\]$ whoami
　　　　user1
　　\[user1@localhost ~\]$ mkdir user1\_doc
　　\[user1@localhost ~\]$ newgrp group2
　　\[user1@localhost ~\]$ mkdir user2\_doc
　　\[user1@localhost ~\]$ newgrp group3
　　\[user1@localhost ~\]$ mkdir user3\_doc
　　\[user1@localhost ~\]$ ll
　　　　total 12
　　　　drwxr\-xr\-x  2 user1 group1 4096 Oct 24 01:18 user1\_doc
　　　　drwxr\-xr\-x  2 user1 group2 4096 Oct 24 01:18 user2\_doc
　　　　drwxr\-xr\-x  2 user1 group3 4096 Oct 24 01:19 user3\_doc
　　\[user1@localhost ~\]$
　　3．groupdel命令
　　表示删除用户组，语法格式为：
　　　　groupdel \[群组名称\]
　　当需要从系统上删除用户组时，可用groupdel指令来完成这项工作。如果该用户组中仍包括某些用户，则必须先删除这些用户后，然后才能删除用户组。
例如：

　　删除linuxfans这个用户组
　　\[root@localhost ~\]# groupdel  linuxfans
　　二. 添加、修改和删除用户命令useradd/usermod/userdel
　　1．useradd建立用户的过程
　　useradd不加任何参数创建用户时，系统首先读取添加用户配置文件/etc/login.defs和/etc/default/useradd，根据这两个配置文件中定义的规则添加用户，然后会向/etc/passwd和/etc/group文件添加用户和用户组记录，同时/etc/passwd和/etc/group对应的加密文件也会自动生成记录，接着系统会自动在/etc/default/useradd文件设定的目录下建立用户主目录，最后复制/etc/skel目录中的所有文件到新用户的主目录中，这样一个新的用户就建立完成了。
　　2．useradd的使用语法
　　useradd语法的一般格式为：
　　　　useradd  \[\-u uid \[\-o\]\] \[\-g group\] \[\-G group,...\]
               　　　　 \[\-d home\] \[\-s shell\] \[\-c comment\]
               　　　 \[\-f inactive\] \[\-e expire \] name
　　各个选项具体含义如下：
　　 \-u uid：即用户标识号，此标识号必须唯一。
　　 \-g group：指定新建用户登录时所属的默认组，或者叫主组。此群组必须已经存在。
　　 \-G group：指定新建用户的附加组，此群组必须已经存在。附加组是相对与主组而言的，当一个用户同时是多个组中的成员时，登录时的默认组成为主组，而其它组称为附加组。
　　 \-d home：指定新建用户的默认主目录，如果不指定，系统会在/etc/default/useradd文件指定的目录下创建用户主目录。
　　 \-s shell：指定新建用户使用的默认shell，如果不指定，系统以/etc/default/useradd文件中定义的shell作为新建用户的默认shell。
　　 \-c comment：对新建用户的说明信息。
　　 \-f inactive：指定帐号过期多长时间后永久停用。当值为0时帐号则立刻被停权。而当值为\-1时则关闭此功能，预设值为\-1
　　 \-e expire：指定用户的帐号过期时间，日期的指定格式为MM/DD/YY。
　　 name：指定需要创建的用户名。
　　3．usermod的使用语法
　　usermod用来修改用户的账户属性信息，使用语法如下：
　　　　usermod  \[\-u uid \[\-o\]\] \[\-g group\] \[\-G group,...\]
                \[\-d 主目录 \[\-m\]\] \[\-s shell\] \[\-c 注释\] \[\-l 新名称\]
                \[\-f 失效日期\] \[\-e 过期日期\]\[\-L|\-U\] Name
　　各个选项具体含义如下：
　　 \-u uid：指定用户新的UID值，此值必须为唯一的ID值，除非用\-o选项。
　　 \-g group：修改用户所属的组名为新的用户组名，此用户组名必须已经存在。
　　 \-G group：修改用户所属的附加组。
　　 \-d 主目录：修改用户登录时的主目录。
　　 \-s shell：修改用户登录系统后默认使用的shell
　　 \-c 注释：修改用户的注释信息。
　　 \-l 新名称：修改用户帐号为新的名称。
　　 \-f 失效日：帐号过期多少天后永久禁用。
　　 \-e 过期日：增加或修改用户账户的过期时间。
　　 \-L：锁定用户密码，使密码无效。
　　 \-U：解除密码锁定。
　　 Name：要修改属性的系统用户。
　　4．userdel的使用语法
　　Userdel用来删除一个用户，若指定“\-r”参数不但删除用户，同时删除用户的主目录以及目录下的所有文件。语法格式为：
　　　　userdel \[\-r\]\[用户帐号\]
　　5．应用举例
　　1）添加一个用户mylinux，指定所属的主用户组为fanslinux，附加用户组为linuxfans，同时指定用户的默认主目录为/opt/mylinux
　　\[root@localhost ~\]# useradd \-g fanslinux \-G linuxfans \-d /opt/mylinux mylinux
　　\[root@localhost ~\]# more /etc/passwd|grep mylinux
　　　　mylinux:x:523:1030::/opt/mylinux:/bin/bash
　　\[root@localhost ~\]# more /etc/group|grep mylinux
　　　　linuxfans:x:1020:mylinux
　　 2）添加一个用户test\_user，指定UID为686，默认的shell为/bin/csh，让其归属为用户组linuxfans和fanslinux，同时添加对此用户的描述，
　　\[root@localhost ~\]# useradd  \-u 686 \-s /bin/csh  \-G linuxfans,fanslinux  \-c "This is test user" test\_user
　　\[root@localhost ~\]# more /etc/passwd|grep test\_user
　　　　test\_user:x:686:686:This is test user:/home/test\_user:/bin/csh
　　\[root@localhost ~\]# more /etc/group|grep test\_user
　　　　fanslinux:x:1030:test\_user
　　　　linuxfans:x:1020:mylinux,test\_user
　　test\_user:x:686:
　　 3）修改用户test\_user的主用户组为新建的组test\_group1，同时修改test\_user的附加组为linuxfans和root，最后修改test\_user的默认登录shell为/bin/bash
　　\[root@localhost ~\]# groupadd test\_group1  #添加一个新的用户组
　　\[root@localhost ~\]# more /etc/group|grep test\_group1 #显示新增用户组的信息
　　　　test\_group1:x:1031:
　　\[root@localhost ~\]# usermod \-g test\_group1 \-G linuxfans,root \-s /bin/bash test\_user
　　\[root@localhost ~\]# more /etc/passwd|grep test\_user   #从输出可知，用户的属性已经更改
　　　　test\_user:x:686:1031:This is test user:/home/test\_user:/bin/bash
　　\[root@localhost ~\]# more /etc/group|grep test\_user   #从输出可知，用户组的属性也同步更改
　　　　root:x:0:root,test\_user
　　　　linuxfans:x:1020:mylinux,test\_user
　　test\_user:x:686:
　　4）如何锁定、解除用户密码
　　下面首先对test\_user和mylinux用户设置密码
　　\[root@localhost ~\]# passwd  test\_user
　　　　Changing password for user test\_user.
　　　　New UNIX password:
　　　　Retype new UNIX password:
　　　　passwd: all authentication tokens updated successfully.
　　\[root@localhost ~\]# passwd  mylinux
　　　　Changing password for user mylinux.
　　　　New UNIX password:
　　　　Retype new UNIX password:
　　　　passwd: all authentication tokens updated successfully.
　　下面的操作是通过su命令切换到mylinux用户下，然后在mylinux下再次切换到test\_user用户下，这里的切换用户是为了说明一个问题：从超级用户root切换到普通用户下，是不需要输入普通用户密码的，系统也不会去验证密码。但普通用户之间切换是需要密码验证的。
　　\[root@localhost ~\]# su – mylinux  #通过su命令切换到mylinux用户下
　　\[mylinux@localhost ~\]$ whoami      #用whoami命令查看当前用户
　　　　mylinux
　　\[mylinux@localhost ~\]$ su \- test\_user  #这里是从mylinux用户下切换到test\_user用户下，需要输入密码
　　　　Password:
　　\[mylinux@localhost ~\]$ whoami          #成功切换到test\_user用户下
　　test\_user
　　接下来，在root用户下执行usermod锁定test\_user的密码，测试test\_user是否还能登录，从下面可以看出，密码锁定后，出现登录失败。
　　\[root@localhost ~\]# usermod \-L test\_user  #锁定test\_user用户的密码
　　\[root@localhost ~\]# su \- mylinux
　　\[mylinux@localhost ~\]$ whoami
　　　　mylinux
　　\[mylinux@localhost ~\]$ su \- test\_user  #这里输入的密码是正确的，但是提示密码错误，因为密码被锁定了
　　　　Password:
　　　　su: incorrect password
　　\[mylinux@localhost ~\]$ whoami
　　　　mylinux
　　最后对test\_user解除密码锁定，登录正常。
　　\[root@localhost ~\]# usermod \-U test\_user  #解除密码锁定
　　\[root@localhost ~\]# su – mylinux
　　\[mylinux@localhost ~\]$ whoami
　　　　mylinux
　　\[mylinux@localhost ~\]$ su \- test\_user
　　　　Password:
　　\[test\_user@localhost ~\]$ whoami  #密码锁定解除后，test\_user用户可以登录系统
　　　　test\_user

**　　文件与权限的设定**

　　所谓的文件权限，是指对文件的访问权限，包括对文件的读、写、删除、执行等，在linux下，每个用户都具有不同的权限，普通用户只能在自己的主目录下进行写操作，而在主目录之外，普通用户只能进行查找、读取操作，如何处理好文件权限和用户之间的关系，是本节讲述的重点。
　　一、查看文件的权限属性
　　使用ls命令就可以查看文件的以及目录的权限信息，不带任何参数的ls命令只显示文件名称，通过“ls –al”可以显示文件或者目录的权限信息，看下面的输出：
　　\[root@localhost oracle\]# ls \-al
　　　　total 92
　　　　drwxr\-xr\-x   3 oracle oinstall  4096 Oct 30  2006 admin
　　　　drwxr\-xr\-x   2 oracle oinstall  4096 Oct 23 18:22 bin
　　　　\-rwxr\-xr\-x   1 root   root      3939 Mar 20  2008 .createtablespace.pl
　　　　drwxr\-xr\-x   3 oracle oinstall  4096 Oct 30  2006 flash\_recovery\_area
　　　　drwxr\-xr\-x   2 oracle oinstall  4096 Jun 25 15:18 install
　　　　drwx\-\-\-\-\-\-   2 oracle oinstall 16384 Jun 25 01:10 lost+found
　　　　drwxr\-xr\-\-   3 oracle oinstall  4096 Oct 30  2008 oradata
　　　　drwxr\-xr\-x   6 oracle oinstall  4096 Oct 30  2006 oraInventory
　　　　drwxr\-xr\-x   3 oracle dba       4096 Oct 28  2006 product
 　　为了能更详细的介绍上面输出中每个属性的含义，下图列出了oradata文档每列代表的含义：
　　![](https://img2018.cnblogs.com/blog/1554553/201812/1554553-20181228103700059-1119258535.png)

　　下面通过具体的实例讲述每列代表的含义。
　　1．第一列显示文档类型与执行权限，有十个字符组成，分为4个部分，下面将文档oradata权限分解，如下图所示：

　　![](https://img2018.cnblogs.com/blog/1554553/201812/1554553-20181228103716882-531806489.png)

　　接着对每个部分解释如下：
　　 文档类型部分：
　　当为“d”时，表示目录；当为“l”时表示软链接；当为“\-”时表示文件；当为“c”时表示串行端口字符设备文件；当为“b”时表示可供存储的块设备文件。由此可知，oradata是一个目录。
　　在接下来的三个部分中，三个字符为一组，每个字符的含义为：“r”表示只读，即read；“w”表示可写，即write；“x”表示可执行，即execute；“\-”表示无此权限，即为空。
　　 User部分：
　　第二部分是对文档所有者（user）权限的设定，“rwx”表示用户对oradata目录有读、写和执行的所有权限。
　　 Group部分：
　　第三部分是对文档所属用户组（group）权限的设定，“r\-x”表示用户组对oradata目录有读和执行的权限，但是没有写的权限。
　　 Others部分：
　　第四部分是对文档拥有者之外的其它用户权限的设定，“r\-\-”表示其它用户或用户组对oradata目录只有读的权限。
　　文档的操作权限是可以指定和更改的，通过chmod命令即可更改文件或者目录的权限，这个将在下节讲述。
　　2．第二列显示的是文档的连结数，这个连结数就是硬链接的概念，即多少个文件指向同一个索引节点,举例如下：
　　\[root@localhost ~\]#ls \-al
　　　　\-rw\-r\-\-r\-\-   1 root root 60151 Oct 25 01:01 install.log
　　\[root@localhost ~\]#ln install.log  install.log1
　　\[root@localhost ~\]#ls –al  install.log
　　　　\-rw\-r\-\-r\-\-   2 root root 60151 Oct 25 01:01 install.log
　　\[root@localhost ~\]#ln install.log  install.log2
　　\[root@localhost ~\]#ls –al  install.log
　　　　\-rw\-r\-\-r\-\-   3 root root 60151 Oct 25 01:01 install.log
　　从上面可以看出，install.log文件原始的连结数是1，然后做了两个硬链接操作，install.log文件的连接数变为3，这就是连接数的含义。
　　3．第三列显示了文档所属的用户和用户组，也就是文档是属于哪个用户以及哪个用户组所有，例如上面的oradata目录，所属的用户为oracle，所属的组为oinstall组。文件所属的用户和组是可以更改的，通过chown命令就可以修改文档的用户属性。
　　4．第四列显示的是文档的大小，默认显示的是以bytes为单位，但是也可以通过命令的参数修改显示的单位，例如可以通过“ls \-sh”组合人性化的显示文档的大小。对于目录，通常只显示文件系统默认block的大小。
　　5．第五列显示文档最后一次的修改日期，通常以月、日、时、分的方式显示，如果文档修改时间距离现在已经很远了，会使用月、日、年的方式显示。
　　6．第六列显示的是文档名称，linux下以“.”开头的文件是隐藏文件，同理以“.”开头的目录是隐藏目录，隐藏文档只有通过ls命令的“\-a”选项才能显示。
　　例如上面的.createtablespace.pl文件就是一个隐藏文件。
　　二、利用chown改变属主和属组
　　chown就是change owner的意思，主要作用就是改变文件或者目录的所有者，而所有者包含用户和用户组，其实chown就是对文件所属的用户和用户组进行的一系列设置。
　　chown使用的一般语法为：
　　\[root@localhost ~\]#chown \[\-R\] 用户名称 文件或目录
　　\[root@localhost ~\]#chown \[\-R\] 用户名称:用户组组名称 文件或目录
　　参数说明：
　　\-R : 进行递归式的权限更改，也就是将目录下的所有文件、子目录都更新成为指定的用户组权限。常常用于变更某一目录的情况。
　　注意，在执行操作前，确保指定的用户以及用户组在系统中是存在的。
例子1：

　　修改隐藏文件“.createtablespace.pl”的所属用户为oracle，所属的用户组为oinstall，操作如下：
　　\[root@localhost ~\]#chown oracle:oinstall .createtablespace.pl
　　\[root@localhost ~\]#ls \-al  .createtablespace.pl
　　　　\-rwxr\-xr\-x   1 oracle   oinstall      3939 Mar 20  2008 createtablespace.pl
　　注意，这里要确保oracle用户和oinstall组已经存在。
例子2：

　　修改oradata目录以及目录下的所有文件的所属用户为root，用户组为dba组，
　　 \[root@localhost ~\]#chown \-R root:dba oradata
　　　　drwxr\-xr\-\-   3 root dba   4096 Oct 30  2006 oradata
　　三、利用chmod改变访问权限
　　chmod用于改变文件或目录的访问权限。该命令有两种用法。一种是包含字母和操作符表达式的字符设定法；另一种是包含数字的数字设定法。
　　1. 字符设定法
　　使用语法为：
　　　　chmod \[who\] \[+ | \- | =\] \[mode\] 文件名
　　命令中各选项的含义如下：
　　 who表示操作对象，可以是下面字母中的任何一个或者它们的组合。
　　 u 表示“用户（user）”，即文件或目录的所有者。
　　 g 表示“用户组（group）”，即文件或目录所属的用户组。
　　 o 表示“其他（others）用户”。
　　 a 表示“所有（all）用户”。它是系统默认值。
　　 操作符号含义如下：
　　 “+”表示添加某个权限。
　　 “\-”表示取消某个权限。
　　 “=”表示赋予给定的权限，同时取消文档以前的所有权限。
　　 mode表示可以执行的权限，可以是“r“（只读）、“w”（可写）和“x”（可执行），以及它们的组合。
　　 文件名可以是以空格分开的文件列表，支持通配符。
　　2．举例
 　　修改install.log文件，使其所有者具有所有权限，用户组和其它用户具有只读权限：
　　\[root@localhost ~\]# ls \-al install.log
　　　　\-rw\-\-\-\-\-\-  1 root root 60151 Oct 17 16:11 install.log
　　\[root@localhost ~\]# chmod u=rwx,g+r,o+r install.log
　　\[root@localhost ~\]# ls \-al install.log
　　　　\-rwxr\-\-r\-\-  1 root root 60151 Oct 17 16:11 install.log
 　　修改/etc/fstab文件的权限，使其所有者具有读写权限，用户组和其它用户没有任何权限：
　　\[root@localhost ~\]# ll /etc/fstab
　　　　\-rwxr\-\-r\-\-  1 root root 1150 Oct 23 09:30 /etc/fstab
　　\[root@localhost ~\]# chmod u\-x,g\-r,o\-r /etc/fstab
　　\[root@localhost ~\]# ll /etc/fstab
　　　　\-rw\-\-\-\-\-\-\-  1 root root 1150 Oct 23 09:30 /etc/fstab
　　3．数字设定法
　　首先了解一下用数字表示属性的含义，0表示没有任何权限，1表示有可执行权限，与上面字符表示法中的“x”有相同的含义。2表示有可写权限，与“w”对应，4表示有可读权限，对应与“r“。
　　如果想让文件的属主拥有读和写的权限，可以通过4（可读）+2（可写）=6（可读可写）的方式来实现，那么用数字6就表示拥有读写权限。
　　使用语法：
　　　　chmod \[属主权限的数字组合\] \[用户组权限的数字组合\] \[其它用户权限的数字组合\] 文件名
　　下图展示了数字设定法的实现原理：

 ![](https://img2018.cnblogs.com/blog/1554553/201812/1554553-20181228103502861-1344487992.png)

　**　上图数字设定法含义剖析**
　　从图中可以清晰的看出，“755”组合的代表含义，第一个“7”显示了文件所有者的权限，是通过4（r）+2（w）+1（x）=7（rwx）而得到的。第二个“5”显示了文件所属组的权限，是通过4（r）+0（\-）+1（x）=5（rx）而得到的，同理最后一个“5”也有类似的含义。
举例：
　　某个文件mysqltuner.pl的默认权限为600，即“\-rw\-\-\-\-\-\-\-”，表示只有此文件的所有者（User）拥有读写权限，其它用户（Others）和组（Group）没有对此文件访问的任何权限。
　　首先修改此文件的权限为644，即“\-rw\-r\-\-r\-\-”，表示此文件的所有者（User）拥有读写权限，而其它用户（Others）和组（Group）仅仅拥有读的权限，操作如下：
　　\[linux1@localhost ~\]$ ls \-al mysqltuner.pl
　　　　\-rw\-\-\-\-\-\-\- 1 linux1 linux1 38063 Oct 26 07:49 mysqltuner.pl
　　\[linux1@localhost ~\]$ chmod 644  mysqltuner.pl
　　\[linux1@localhost ~\]$ ls \-al mysqltuner.pl
　　　　\-rw\-r\-\-r\-\- 1 linux1 linux1 38063 Oct 26 07:49 mysqltuner.pl
　　然后接着修改mysqltuner.pl文件的权限为755，即“\-rwxr\-xr\-x”，表示此文件的所有者（User）拥有读写执行权限，而其它用户（Others）和组（Group）拥有对此文件的读和执行权限。
　　\[linux1@localhost ~\]$ chmod 755  mysqltuner.pl
　　\[linux1@localhost ~\]$ ls \-al mysqltuner.pl
　　　　\-rwxr\-xr\-x 1 linux1 linux1 38063 Oct 26 07:49 mysqltuner.pl