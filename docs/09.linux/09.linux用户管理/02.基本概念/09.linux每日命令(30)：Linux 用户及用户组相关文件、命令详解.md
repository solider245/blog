---
title: linux每日命令(30)：Linux 用户及用户组相关文件、命令详解
date: 2020-10-12 12:09:51
permalink: /pages/849de0/
categories:
  - linux用户管理
  - 基本概念
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 08:07:00
 * @LastEditTime: 2020-07-17 08:07:00
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\基本概念\linux每日命令(30)：Linux 用户及用户组相关文件、命令详解.md
 * @日行一善，每日一码
--> 
**阅读目录(Content)**

*   [一. 用户、用户组概念及其文件结构详解](#_label0)
*   [二. 常用的用户、用户组shell命令](#_label1)

*   [用户相关命令](#_lab2_1_0)

*   [useradd](#_label3_1_0_0)
*   [userdel](#_label3_1_0_1)
*   [usermod](#_label3_1_0_2)
*   [passwd](#_label3_1_0_3)

*   [用户组相关命令](#_lab2_1_1)

*   [groupadd](#_label3_1_1_0)
*   [groupdel](#_label3_1_1_1)
*   [groupmod](#_label3_1_1_2)

*   [三. 综合示例](#_label2)

*   [1.建立两个用户组group1和group2，以及三个用户dennis、daniel、abigale，并且将前2个用户分配在group1用户组下，后一个分配在group2用户组下，并给dennis设置密码](#_lab2_2_0)
*   [2.改变abigale的用户组由group2变为group1](#_lab2_2_1)

[回到顶部(go to top)](#_labelTop)

# 一. 用户、用户组概念及其文件结构详解

Linux用户只有两个等级：root及非root。Linux中还有一部分用户，如：apache、mysql、nobody、ftp等，这些也都是非root用户，即普通用户。Linux的权限实际是上不同用户所能访问的文件的不同产生的假象。而这些假象的造成，还要涉及到另外一个概念：用户组

*   一个用户至少要属于一个用户组
*   一个用户可以属于多个用户组

用户组存在的原因主要还是方便分配权限。而用户本身和权限的差别不是很大，各个用户之间主要的不同是：

*   是否拥有密码
*   home目录（普通用户可以有一个以自己用户名命名的home目录，存放的地址是/home/username，root用户的home目录是：/root）
*   shell

像nobody这样用来执行Nginx的工作进程的用户，一般不分配密码和shell，甚至连home目录都没有。

为什么不分配密码？如果设置了密码，程序无法自动使用。由于不会有人使用这个用户登录系统，所以就没有必要分配shell。（备注：其实严格上说是有分配shell，只是分配的shell是/sbin/nologin这个特殊的shell，没有任何其他功能，主要功能是防止你登陆。）

所有用户都可以通过查看/etc/passwd查看。以下为我的系统中的用户信息：

```
[hc@localhost ~]$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
systemd-network:x:192:192:systemd Network Management:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
polkitd:x:999:998:User for polkitd:/:/sbin/nologin
libstoragemgmt:x:998:995:daemon account for libstoragemgmt:/var/run/lsm:/sbin/nologin
rpc:x:32:32:Rpcbind Daemon:/var/lib/rpcbind:/sbin/nologin
colord:x:997:994:User for colord:/var/lib/colord:/sbin/nologin
gluster:x:996:993:GlusterFS daemons:/var/run/gluster:/sbin/nologin
saslauth:x:995:76:Saslauthd user:/run/saslauthd:/sbin/nologin
abrt:x:173:173::/etc/abrt:/sbin/nologin
setroubleshoot:x:994:991::/var/lib/setroubleshoot:/sbin/nologin
rtkit:x:172:172:RealtimeKit:/proc:/sbin/nologin
pulse:x:171:171:PulseAudio System Daemon:/var/run/pulse:/sbin/nologin
rpcuser:x:29:29:RPC Service User:/var/lib/nfs:/sbin/nologin
nfsnobody:x:65534:65534:Anonymous NFS User:/var/lib/nfs:/sbin/nologin
unbound:x:993:988:Unbound DNS resolver:/etc/unbound:/sbin/nologin
chrony:x:992:987::/var/lib/chrony:/sbin/nologin
qemu:x:107:107:qemu user:/:/sbin/nologin
radvd:x:75:75:radvd user:/:/sbin/nologin
tss:x:59:59:Account used by the trousers package to sandbox the tcsd daemon:/dev/null:/sbin/nologin
usbmuxd:x:113:113:usbmuxd user:/:/sbin/nologin
geoclue:x:991:985:User for geoclue:/var/lib/geoclue:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
sssd:x:990:984:User for sssd:/:/sbin/nologin
gdm:x:42:42::/var/lib/gdm:/sbin/nologin
gnome-initial-setup:x:989:983::/run/gnome-initial-setup/:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
avahi:x:70:70:Avahi mDNS/DNS-SD Stack:/var/run/avahi-daemon:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
tcpdump:x:72:72::/:/sbin/nologin
hc:x:1000:1000:hc:/home/hc:/bin/bash
nginx:x:988:982:nginx user:/var/cache/nginx:/sbin/nologin
redis:x:987:981:Redis Database Server:/var/lib/redis:/sbin/nologin
uwsgi:x:986:980:uWSGI daemon user:/run/uwsgi:/sbin/nologin
mysql:x:27:27:MariaDB Server:/var/lib/mysql:/sbin/nologin
mongod:x:985:979:mongod:/var/lib/mongo:/bin/false

```

文件的每一行代表着一个用户，每一行由冒号"："分割成7个字段，其结构如下：

```
用户名：密码：UID：GID：用户全名：home目录：shell

```

UID：

*   UID 0 root用户
*   UID 1~999 是占坑用户，即一些无法登录的用户（以前是系统是1~499，最近刚改）
*   UID 1000 以上是正常的可登录用户

GID：前面说了一个用户可以属于多个用户组，但这里只有一个，表示的是专职用户组，即一个用户只有一个专职用户组，其属于其他用户组的关联关系存储在/etc/group 文件中。

其中比较特殊的是密码字段，统一由x代替了，看/etc/passwd就知道一开始Linux是将密码存在这个文件里的，由于考虑到/etc/passwd可以被所有人查看，所以将统一存储到/etc/shadow文件（只有root权限可以访问）中，具体数据如下：

```
[hc@localhost ~]$ cat /etc/shadow
cat: /etc/shadow: Permission denied
[hc@localhost ~]$ sudo cat /etc/shadow
[sudo] password for hc:
root:$6$yknGgCVbJAppRylr$SY.X4RUN.6dIG8fT9ofTu03/lcUzcfn4pNNeUWwkakZlH4oNF45h8eDYNxsJhz3Gm6/5ovsdJzdJMCZkKDQzs0::0:99999:7:::
bin:*:17632:0:99999:7:::
daemon:*:17632:0:99999:7:::
adm:*:17632:0:99999:7:::
lp:*:17632:0:99999:7:::
sync:*:17632:0:99999:7:::
shutdown:*:17632:0:99999:7:::
halt:*:17632:0:99999:7:::
mail:*:17632:0:99999:7:::
operator:*:17632:0:99999:7:::
games:*:17632:0:99999:7:::
ftp:*:17632:0:99999:7:::
nobody:*:17632:0:99999:7:::
systemd-network:!!:17861::::::
dbus:!!:17861::::::
polkitd:!!:17861::::::
libstoragemgmt:!!:17861::::::
rpc:!!:17861:0:99999:7:::
colord:!!:17861::::::
gluster:!!:17861::::::
saslauth:!!:17861::::::
abrt:!!:17861::::::
setroubleshoot:!!:17861::::::
rtkit:!!:17861::::::
pulse:!!:17861::::::
rpcuser:!!:17861::::::
nfsnobody:!!:17861::::::
unbound:!!:17861::::::
chrony:!!:17861::::::
qemu:!!:17861::::::
radvd:!!:17861::::::
tss:!!:17861::::::
usbmuxd:!!:17861::::::
geoclue:!!:17861::::::
ntp:!!:17861::::::
sssd:!!:17861::::::
gdm:!!:17861::::::
gnome-initial-setup:!!:17861::::::
sshd:!!:17861::::::
avahi:!!:17861::::::
postfix:!!:17861::::::
tcpdump:!!:17861::::::
hc:$6$h7GHf6NOXJgamNHh$gwsxvkU88Puv5Nt5bn14Wj7UsU0DclLoXMi/99sr36lqn4osb6oKRF/AdCszGAjsYeUl6PX66u/SSJ5MhYsMT0::0:99999:7:::
nginx:!!:17861::::::
redis:!!:17861::::::
uwsgi:!!:17861::::::
mysql:!!:17861::::::
mongod:!!:17862::::::

```

其结构如下：

用：分割，从左往右依次为

*   账户名：账户名与/etc/passwd里面的账户名是一一对应的关系。
*   密码：这里可以看到3类，分别是奇奇怪怪的字符串、\*和！！其中，奇奇怪怪的字符串就是加密过的密码文件。\*代表帐号被锁定(即)，!!表示这个密码已经过期了。奇奇怪怪的字符串是以$6$开头的，表明是用SHA\-512加密的，$1$ 表明是用MD5加密的、$2$ 是用Blowfish加密的、$5$是用 SHA\-256加密的。
*   修改日期：这个是表明上一次修改密码的日期与1970\-1\-1相距的天数密码不可改的天数：假如这个数字是8，则8天内不可改密码，如果是0，则随时可以改。
*   密码需要修改的期限：如果是99999则永远不用改。如果是其其他数字比如12345，那么必须在距离1970\-1\-1的12345天内修改密码，否则密码失效。
*   修改期限前N天发出警告：比如你在第五条规定今年6月20号规定密码必须被修改，系统会从距离6\-20号的N天前向对应的用户发出警告。
*   密码过期的宽限：假设这个数字被设定为M，那么帐号过期的M天内修改密码是可以修改的，改了之后账户可以继续使用。
*   帐号失效日期：假设这个日期为X，与第三条一样，X表示的日期依然是1970\-1\-1相距的天数，过了X之后，帐号失效。
*   保留：被保留项，暂时还没有被用上。

再来看看/etc/group文件：

```
[hc@localhost ~]$ cat /etc/group
root:x:0:
bin:x:1:
daemon:x:2:
sys:x:3:
adm:x:4:
tty:x:5:
disk:x:6:
lp:x:7:
mem:x:8:
kmem:x:9:
wheel:x:10:
cdrom:x:11:
mail:x:12:postfix
man:x:15:
dialout:x:18:
floppy:x:19:
games:x:20:
tape:x:33:
video:x:39:
ftp:x:50:
lock:x:54:
audio:x:63:
nobody:x:99:
users:x:100:
utmp:x:22:
utempter:x:35:
input:x:999:
systemd-journal:x:190:
systemd-network:x:192:
dbus:x:81:
polkitd:x:998:
printadmin:x:997:
cgred:x:996:
libstoragemgmt:x:995:
rpc:x:32:
colord:x:994:
dip:x:40:
gluster:x:993:
ssh_keys:x:992:
saslauth:x:76:
abrt:x:173:
setroubleshoot:x:991:
rtkit:x:172:
pulse-access:x:990:
pulse-rt:x:989:
pulse:x:171:
rpcuser:x:29:
nfsnobody:x:65534:
unbound:x:988:
chrony:x:987:
kvm:x:36:qemu
qemu:x:107:
radvd:x:75:
tss:x:59:
libvirt:x:986:
usbmuxd:x:113:
geoclue:x:985:
ntp:x:38:
sssd:x:984:
gdm:x:42:
gnome-initial-setup:x:983:
sshd:x:74:
avahi:x:70:
slocate:x:21:
postdrop:x:90:
postfix:x:89:
tcpdump:x:72:
stapusr:x:156:
stapsys:x:157:
stapdev:x:158:
hc:x:1000:hc
nginx:x:982:
redis:x:981:
uwsgi:x:980:
mysql:x:27:
mongod:x:979:

```

其结构如下：

```
组名：用户组密码：GID：用户组内的用户名

```

正常的使用中很少会用到用户组密码，其存储在/etc/gshadow中。

用户组文件比较特特殊的是“”用户组内的用户名”，其实就是这个组下的用户列表，每个用户之间用逗号“,”分割；本字段可以为空；如果字段为空表示用户组为GID的用户名

普通用户的权限非常的低，就连在系统里安装软件的权限都没有，很多时候可以临时给普通用户以特权，就是sudo（在命令前添加sudo）。比如：

```
sudo cat /etc/shadow

```

完成后需要您输入root的密码，这样 就可以假借root身份了，centos默认普通用户是没有sudo权限的，这与主要以桌面版为主的Ubuntu和Fedora不同，如需给予用户root特权，就需要更改/etc/sudoers文件，修改内容。

比如我为了给hc用户增加sudo特权，就用root权限，修改/etc/sudoers文件，在root下面加入了hc用户

修改前

```
## Allow root to run any commands anywhere
root    ALL=(ALL)     ALL

```

修改后效果如下

```
## Allow root to run any commands anywhere
root	ALL=(ALL) 	ALL
hc      ALL=(ALL)       ALL

```

如果要给某个用户组添加sudo特权则为：（与给用户不同的是多了一个%）

```
## Allows people in group wheel to run all commands
%wheel ALL=(ALL) ALL

```

另外一种方式是添加不需要输入root密码即有root权限的用户，添加方法如下：

```
%wheel	ALL=(ALL)	NOPASSWD: ALL

```

另外还可以设定到底有哪些执行权限，具体的规则如下：（具体可看[sudoers配置文件详解](http://ncforest.blog.163.com/blog/static/295626642007551417331/)）

```
授权用户 主机=[(切换到哪些用户或用户组)] [是否需要密码验证] 命令1,[(切换到哪些用户或用户组)] [是否需要密码验证] [命令2],[(切换到哪些用户或用户组)] [是否需要密码验证] [命令3]......

```

另外默认情况下第一次使用sudo时，需要输入root密码，如果5分钟内再次执行sudo则无需再输入密码，超过5分钟则要重新输入。这个时间也是可以进行配置的，在sudoers中添加如下内容即可：

```
Defaults:用户名 timestamp_timeout=20

```

其中单位是分钟，如果设为0，则表示每次都要输入密码。

讲解了这么多，接下来学习下常用的shell命令

[回到顶部(go to top)](#_labelTop)

# 二. 常用的用户、用户组shell命令

## 用户相关命令

### useradd

功能：

用来创建用户

语法 ：

```
useradd 选项 用户名

```

选项：

| 选项 | 描述 |
| --- | --- |
| \-d 目录 | 指定用户主目录，如果此目录不存在，则同时使用\-m选项，可以创建主目录，也是用户登入时的启始目录 |
| \-g 用户组 | 指定用户所属的群组 |
| \-G 用户组 | 指定用户所属的附加群组 |
| \-u 用户号 | 指定用户id |
| \-e | 指定帐号的有效期限 |
| \-f | 指定在密码过期后多少天即关闭该帐号 |
| \-m | 自动建立用户的登入目录 |
| \-M | 不要自动建立用户的登入目录 |
| \-n | 取消建立以用户名称为名的群组 |
| \-r | 建立系统帐号 |
| \-s Shell文件 | 指定用户登入后所使用的shell |

示例1：

```
useradd –d /home/sam -m sam

```

添加了一个用户sam，并且他的主目录为/home/sam，没有主目录的时候自动创建。（/home为默认的用户主目录所在的父目录）

示例2：

```
sudo useradd username -m -s /sbin/nologin -d /home/username -g groupname

```

其中：

\-s /sbin/nologin 设置不能登陆
\-d 设置用户主目录
\-g 用户组
\-m 创建用户目录

示例3：

```
useradd -s /bin/sh -g group –G adm,root gem

```

添加一个用户gem，使用的Shell是/bin/sh，主用户组为group，附加组为adm，root。

### userdel

功能：

用来删除用户

语法：

```
userdel 选项 用户名

```

\-r 把用户的主目录一起删除。

### usermod

功能：

用来修改用户

语法：

```
usermod 选项 用户名

```

示例：

```
usermod -s /bin/ksh -d /home/z –g developer sam

```

将sam用户的Shell改为/bin/ksh，主目录改为/home/z，用户组为developer。

### passwd

功能：

用来修改用户口令

语法：

```
passwd 选项 用户名

```

选项：

| 选项 | 描述 |
| --- | --- |
| \-l | 锁定口令，即禁用账号。 |
| \-u | 口令解锁。 |
| \-d | 使账号无口令。 |
| \-f | 强迫用户下次登录时修改口令。 |

示例1： 修改用户密码

```
$ passwd

Old password:******
New password:*******
Re-enter new password:*******

```

假设当前用户是sam，则上面的命令修改该用户自己的口令。

如果是超级用户，可以用下列形式指定任何用户的口令：

```
# passwd sam

New password:*******
Re-enter new password:*******

```

示例2：

```
# passwd -d sam

```

说明：

将用户sam的口令删除，这样用户sam下一次登录时，系统就不再询问口令。

示例3：

```
# passwd -l sam

```

说明：

锁定sam用户，使其不能登录。

## 用户组相关命令

### groupadd

功能：

创建用户组

语法：

```
groupadd 选项 用户组

```

参数：

| 选项 | 描述 |
| --- | --- |
| \-g | 指定新用户组的组标识号（GID）。 |
| \-o | 一般与\-g选项同时使用，表示新用户组的GID可以与系统已有用户组的GID相同。 |

示例1:

```
groupadd group1

```

说明：
此命令向系统中增加了一个新组group1，新组的组标识号是在当前已有的最大组标识号的基础上加1。

示例2：

```
groupadd -g 101 group2

```

说明：
此命令向系统中增加了一个新组group2，同时指定新组的组标识号是101。

### groupdel

功能：

用于删除群组。需要从系统上删除群组时，可用groupdel(group delete)指令来完成这项工作。倘若该群组中仍包括某些用户，则必须先删除这些用户后，方能删除群组。

语法：

```
groupdel [群组名称]

```

示例：

```
groupdel group2

```

### groupmod

功能：

用于更改一个组在系统上的定义

语法：

```
groupmod [-g <群组识别码> <-o>][-n <新群组名称>][群组名称]

```

选项：

| 选项 | 描述 |
| --- | --- |
| \-g | \-\-gid GID 修改组的GID号 |
| \-n | \-\-new\-name NEW\_GROUP 更改组的组名 |
| \-o | 与\-g配置使用，可以设定不唯一的组ID值 |
| \-h | \-\-help 获得groupmod命令的使用帮助信息 |

例子：

假设已存在组testbed,gid为4000

示例：

```
groupmod -n testbed-new testbed

```

将testbed组名更改为testnbed\-new

```
groupmod -g 5000 testbed-new

```

将testbed\-new组的组ID更改为5

[回到顶部(go to top)](#_labelTop)

# 三. 综合示例

## 1.建立两个用户组group1和group2，以及三个用户dennis、daniel、abigale，并且将前2个用户分配在group1用户组下，后一个分配在group2用户组下，并给dennis设置密码

输出：

```
[root@localhost ~]# groupadd group1
[root@localhost ~]# groupadd group2
[root@localhost ~]# useradd -g group1 dennis
[root@localhost ~]# useradd -g group1 daniel
[root@localhost ~]# useradd -g group2 abigale
[root@localhost ~]# passwd dennis
Changing password for user dennis.
New password:
BAD PASSWORD: The password fails the dictionary check - it is too simplistic/systematic
Retype new password:
passwd: all authentication tokens updated successfully.
[root@localhost ~]# tail -3  /etc/passwd
dennis:x:1000:1000::/home/dennis:/bin/bash
daniel:x:1001:1000::/home/daniel:/bin/bash
abigale:x:1002:1001::/home/abigale:/bin/bash
[root@localhost ~]# tail -3  /etc/group
docker:x:995:root
group1:x:1000:
group2:x:1001:
[root@localhost ~]# cd /home/
[root@localhost home]# ll
total 0
drwx------. 2 abigale group2  62 Nov 29 00:36 abigale
drwx------. 2 daniel  group1  62 Nov 29 00:36 daniel
drwx------. 2 dennis  group1  62 Nov 29 00:36 dennis

```

## 2.改变abigale的用户组由group2变为group1

输出：

```
[root@localhost home]# usermod -g group1 abigale
[root@localhost home]# ll
total 0
drwx------. 2 abigale group1  62 Nov 29 00:36 abigale
drwx------. 2 daniel  group1  62 Nov 29 00:36 daniel
drwx------. 2 dennis  group1  62 Nov 29 00:36 dennis
[root@localhost home]# tail -3  /etc/passwd
dennis:x:1000:1000::/home/dennis:/bin/bash
daniel:x:1001:1000::/home/daniel:/bin/bash
abigale:x:1002:1000::/home/abigale:/bin/bash

```

参考文章：
[https://www.cnblogs.com/duhuo/p/5892513.html](https://www.cnblogs.com/duhuo/p/5892513.html)
[https://blog.csdn.net/chanrayli/article/details/78998941](https://blog.csdn.net/chanrayli/article/details/78998941)

分类: [linux](https://www.cnblogs.com/huchong/category/1203138.html)