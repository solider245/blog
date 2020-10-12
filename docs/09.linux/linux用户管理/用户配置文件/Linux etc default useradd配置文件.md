---
title: Linux etc default useradd配置文件
date: 2020-10-12 12:09:51
permalink: /pages/121978/
categories:
  - linux用户管理
  - 用户配置文件
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 09:01:33
 * @LastEditTime: 2020-07-17 09:06:40
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\用户配置文件\Linux etc default useradd配置文件.md
 * @日行一善，每日一码
--> 
/etc/default/useradd文件是在使用useradd添加用户时的一个需要调用的一个默认的配置文件，可以使用“useradd \-D参数“，这样的命令格式来修改文件里面的内容。

\[root@w ~\]# cat /etc/default/useradd

\# useradd defaults file
|GROUP=100|依赖于/etc/login.defs的USERGRUUPS_ENAB参数，如果为no，则在此处控制|

HOME=/home                        注：把用户的家目录建在/home中。

INACTIVE=\-1                       注：是否启用帐号过期停权，\-1表示不启用。

EXPIRE=                           注：帐号终止日期，不设置表示不启用。

SHELL=/bin/bash                   注：新用户默认所有的shell类型。

SKEL=/etc/skel                    注：配置新用户家目录的默认文件存放路径。

CREATE\_MAIL\_SPOOL=yes             注：创建mail文件

| **useradd命令参数** | **注释说明** |
| \-c comment | #新帐号password档的说明栏（用户的说明信息）。 |
| **\-d home\_dir** | #新帐号每次登入时所使用的home\_dir。预设值为default\_home内login名称，并当成登入时目录名称。（以指定的路径为家目录） |
| \-e expire\_date | #\*帐号终止日期。日期的指定格式为MM/DD/YY。 |
| \-f inactive\_days | #帐号过期几日后记久停权。当值为0时帐号则立刻被停权。而当值为\-1时则关闭此功能，预设值为\-1。 |
| **\-g initial\_group** | #\*group名称或以数字来做为用户登入起始用户组（group）。用户组名称须为系统现有存在的名称。用户组数字也须为现有存在的用户组。预设的用户组数字为1。（指明用户所属基本组，可为组名，也可为GID） |
| **\-G group,\[...\]** | #\*定义此用户为多个不同groups的成员。（为用户指明附加组，组必须事先存在）每个用户组使用","逗号分隔。用户组名称\-g选项的限制。默认值为用户的起始用户组。 |
| \-m | #用户目录如不存在则自动建立。如使用\-k选项，skeleton\_dir内的档案将复制至用户目录下。然后在/etc/skel目录下的档案也会复制过去取代。任何在skeleton\_diror /etc/skel的目录也相同会在用户目录下一一建立。The\-k同\-m不建立目录以及不复制任何档案为预设值。 |
| \-M | #\*不建立用户家目录，优先于/etc/login.defs文件的设定。 |
| \-n | #默认情况用户的用户组与用户的名称会相同。如果命令加了\-n参数，就不会生成和用户同名的用户组了。 |
| \-r | #此参数是用来建立系统帐号。系统帐号的UID会比定义在系统档上/etc/login.defs.的UID——MIN来的小。注意useradd此用法所建立的帐号不会建立用户家目录，也不会在乎记录在/etc/login.defs.的定义值。如果你想要有用户家目录额外指定\-m参数来建立系统帐号。这是Red Hat额外增设的选项。 |
| **\-s shell** | #\*用户登入后使用shell名称。默认值为不填写，这样系统会帮你指定预设的登入shell（根据/etc/default/useradd预设的值）。指明用户的默认shell程序，可用列表在/etc/shells文件中 |
| **\-u uid** | #\*用户的ID值。这个值必须是唯一的，除非用\-o选项。数字不可为负值。（定义在/etc/login.defs） |

命令示例：

添加一个用户old，并指定属于sa组，要求组ID为801，uid为808，并且不建立家目录及禁止其登录。

```bash
[root@cat ~]# groupadd sa -g 801
#创建用户组sa指定gid 801，这个是groupadd命令的用法
[root@cat ~]# tail -1 /etc/group
sa:x:801:
[root@cat ~]# useradd -u 808 -g sa -M -s /sbin/nologin old
#创建用户old属于指定组sa，指定uid 808，用户名old
[root@cat ~]# tail -1 /etc/passwd
old:x:808:801::/home/old:/sbin/nologin
[root@cat ~]# id old
uid=808(old) gid=801(sa) groups=801(sa)
```

新增用户并设置终止日期

```bash
[root@cat ~]# useradd -e "2016/06/01" m1
[root@cat ~]# chage -l m1
Last password change                                    : May 26, 2016
Password expires                                        : never
Password inactive                                       : never
Account expires                                         : Jun 01, 2016
Minimum number of days between password change          : 0
Maximum number of days between password change          : 99999
Number of days of warning before password expires       : 7
[root@cat ~]#
```

学习自：老男孩