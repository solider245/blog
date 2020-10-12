---
title: linux useradd(adduser)命令参数及用法详解-linux创建新用户命令
date: 2020-10-12 12:09:51
permalink: /pages/633b3d/
categories:
  - linux用户管理
  - 基本概念
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 08:19:28
 * @LastEditTime: 2020-07-17 08:19:39
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\基本概念\linux useradd(adduser)命令参数及用法详解-linux创建新用户命令.md
 * @日行一善，每日一码
--> 
 名称：**ad[du](http://www.linuxso.com/command/du.html)ser **

**    1.作用 （linuxso注:[dd](http://www.linuxso.com/command/usera<a href=).html' target='\_blank'>useradd和adduser相同,但是addgroup是不存在的[命令](http://www.linuxso.com/command/),所以建议使用useradd，当然你的习惯才是最重要的.）**

　　useradd命令用来建立用户帐号和创建用户的起始目录，使用权限是超级用户。

**　　2.格式**

　　useradd \[\-d home\] \[\-s shell\] \[\-c comment\] \[\-m \[\-k template\]\] \[\-f inactive\] \[\-e [ex](http://www.linuxso.com/command/ex.html )pire \] \[\-p [passwd](http://www.linuxso.com/command/passwd.html )\] \[\-r\] name

**　　3.主要参数**

　　新帐号建立当不加\-D参数,useradd指令使用命令列来指定新帐号的设定值and使用系统上的预设值.新使用者帐号将产生一些系统档案，使用者目录建立，拷备起始档案等，这些均可以利用命令列选项指定。此版本为R[ed](http://www.linuxso.com/command/ed.html )HatLinux提供，可帮每个新加入的使用者建立个别的group,毋须添加\-n选项。useradd可使用的选项为\-ccomment新帐号password档的说明栏。\-dhome\_dir新帐号每次登入时所使用的home\_dir。预设值为default\_home内login名称，并当成登入时目录名称。

\-e expire\_[date](http://www.linuxso.com/command/date.html)　帐号终止日期。日期的指定格式为MM/DD/YY。

　　\-f inactive\_days　帐号过期几日后永久停权。当值为0时帐号则立刻被停权。而当值为\-1时则关闭此功能，预设值为\-1

\-g initial\_group　group名称或以数字来做为使用者登入起始群组(group)。群组名须为现有存在的名称。群组数字也须为现有存在的群组。预设的群组数字为1。

　　\-G group,\[...\]　定义此使用者为此一堆groups的成员。每个群组使用", "区格开来，不可以夹杂空白字元。群组名同\-g选项的限制。定义值为使用者的起始群组。

\-m　使用者目录如不存在则自动建立。如使用\-k选项skeleton\_dir内的档案将复制至使用者目录下。然而在/etc/skel目录下的档案也会复制过去取代。任何在skeleton\_diror/etc/skel的目录也相同会在使用者目录下一一建立。The\-k同\-m不建立目录以及不复制任何档案为预设值。

　　\-M　不建立使用者目录，即使/etc/login.defs系统档设定要建立使用者目录。

\-n　预设值使用者群组与使用者名称会相同。此选项将取消此预设值。

　　\-r　此参数是用来建立系统帐号。系统帐号的UID会比定义在系统档上/etc/login.defs.的UID\_MIN来的小。注意useradd此用法所建立的帐号不会建立使用者目录，也不会在乎纪录在/etc/login.defs.的定义值。如果你想要有使用者目录须额外指定\-m参数来建立系统帐号。这是REDHAT额外增设的选项。

\-s shell　使用者登入后使用的shell名称。预设为不填写，这样系统会帮你指定预设的登入shell。

　　\-u u[id](http://www.linuxso.com/command/id.html )　使用者的ID值。必须为唯一的ID值，除非用\-o选项。数字不可为负值。预设为最小不得小于999而逐次增加。0~999传统上是保留给系统帐号使用。改变预设值当\-D选项出现时，useradd秀出现在的预设值，或是藉由命令列的方式更新预设值。可用选项为∶

\-b default\_home　定义使用者所属目录的前一个目录。使用者名称会附加在default\_home后面用来建立新使用者的目录。当然使用\-d后则此选项无效。

　　\-e default\_expire\_date　使用者帐号停止日期。

\-f default\_inactive　帐号过期几日后停权。

　　\-g default\_group　新帐号起始群组名或ID。群组名须为现有存在的名称。群组ID也须为现有存在的群组。

\-s default\_shell　使用者登入后使用的shell名称。往后新加入的帐号都将使用此shell.如不指定任何参数，useradd显示目前预设的值。注记系统管理者有义务在/etc/skel目录下放置使用者定义档。

**　　4.说明  资料整理 www.linuxso.com**

useradd可用来建立用户账号，它和adduser命令是相同的。账号建好之后，再用passwd设定账号的密码。使用useradd命令所建立的账号，实际上是保存在/etc/passwd文本文件中。

**　　5.应用实例**

建立一个新用户账户，并设置ID：

　　#useradd caojh \-u 544

需要说明的是，设定ID值时尽量要大于500，以免冲突。因为Linux安装后会建立一些特殊用户，一般0到499之间的值留给bin、mail这样的系统账号。

资料整理 www.linuxso.com

\[root@linux ~\]# useradd \[\-u UID\] \[\-g initial\_group\] \[\-G other\_group\]
\> \-\[Mm\] \[\-c 说明栏\] \[\-d home\] \[\-s shell\] username
参数：
\-u ：后面接的是 UID ，是一组数字。直接指定一个特定的 UID 给这个帐号；
\-g ：后面接的那个群组名称就是我们上面提到的 initial group 啦～
该 group ID (GID) 会被放置到 /etc/passwd 的第四个栏位内。
\-G ：后面接的群组名称则是这个帐号还可以支援的群组。
这个参数会修改 /etc/group 内的相关资料喔！
\-M ：强制！不要建立使用者家目录
\-m ：强制！要建立使用者家目录！
\-c ：这个就是 /etc/passwd 的第五栏的说明内容啦～可以随便我们设定的啦～
\-d ：指定某个目录成为家目录，而不要使用预设值；
\-r ：建立一个系统的帐号，这个帐号的 UID 会有限制 (/etc/login.defs)
\-s ：后面接一个 shell ，预设是 /bin/bash 的啦～
范例：

范例一：完全参考预设值建立一个使用者，名称为 vbird1
\[root@linux ~\]# useradd vbird1


\[root@linux ~\]# [ls](http://www.linuxso.com/command/ls.html) \-l /home
drwxr\-xr\-x 3 vbird1 vbird1 4096 Aug 30 17:33 vbird1
\[root@linux ~\]# [grep](http://www.linuxso.com/command/grep.html)vbird1 /etc/passwd /etc/shadow /etc/group
/etc/passwd:vbird1:x:502:502::/home/vbird1:/bin/bash
/etc/shadow:vbird1:!!:13025:0:99999:7:::
/etc/group:vbird1:x:502:
\# 做这个范例只是想要让您了解，其实系统已经规范好了一些新增使用者时的参数了！
\# 因此，当我们使用 useradd 时，系统会主动的去修改 /etc/passwd 与 /etc/shadow，
\# 而这两个档案内的相关栏位参考值，则会以一些设定档的内容来规范喔！
\# 同时也要注意到，使用 useradd 新增使用者时，这个使用者的 /etc/shadow
\# 密码栏会是不可登入的 (以 !! 为开头)，因此还需要使用 passwd
\# 来给予 vbird1 密码后，才算新增完毕！

范例二：我知道我的系统当中有个群组名称为 users ，且 UID 700 并不存在，
请用这两个参数给予 vbird2 建立一个帐号！
\[root@linux ~\]# useradd \-u 700 \-g users vbird2
\[root@linux ~\]# ls \-l /home
drwxr\-xr\-x 3 vbird2 users 4096 Aug 30 17:43 vbird2
\[root@linux ~\]# grep vbird2 /etc/passwd /etc/shadow /etc/group
/etc/passwd:vbird2:x:700:100::/home/vbird2:/bin/bash
/etc/shadow:vbird2:!!:13025:0:99999:7:::
\# 看一下，UID 与 initial group 确实改变成我们需要的了！

范例三：建立一个系统帐号，名称为 vbird3
\[root@linux ~\]# usradd \-r vbird3
\[root@linux ~\]# grep vbird3 /etc/passwd /etc/shadow /etc/group
/etc/passwd:vbird3:x:101:102::/home/vbird3:/bin/bash
/etc/shadow:vbird3:!!:13025::::::
/etc/group:vbird3:x:102:
\# 很重要喔！您会发现， UID 竟然是 101 ，而 GID 怎麼会是 102，
\# 并且与 /etc/group 有对应的关系喔！有没有加 \-r 差很多！