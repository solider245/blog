---
title: Linux下的用户和文件权限管理
date: 2020-10-12 12:09:51
permalink: /pages/3b4987/
categories:
  - linux用户管理
  - 基本概念
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 19:22:58
 * @LastEditTime: 2020-07-17 20:20:52
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\基本概念\Linux下的用户和文件权限管理.md
 * @日行一善，每日一码
--> 
**一、管理用户账号和组帐号**

**1.****用户帐号和组帐号概述**

**1.1****用户帐号**

![20200717193740_8d7ab311adafdd077f89ae7983037212.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200717193740_8d7ab311adafdd077f89ae7983037212.png)



**1.2****组帐号**

基本组(私有组)：一个用户帐号至少属于一个组，权限最大

附加组（公共组）：一个用户同时还包含在其他组中，这些组就属于附加组

**1.3UID****和GID号**

UID（User IDentity，用户标识号）

GID（Group IDentify，组标识号）

root用户账号：0

程序用户帐号：1~999(7.0以前版本1~499)

普通用户账号：1000~60000（7.0以前版本500~60000）

**2.****用户账号管理**

**2.1****用户帐号文件**

与用户帐号相关的配置文件主要有两个，分别是/etc/passwd和/etc/shadow

（1）passwd文件中的配置行格式

保存用户名称、宿主目录、登录Shell等基本信息

![](https://img-blog.csdn.net/20180817141507806?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

用“：”进行分隔，每一段有每一段的含义，总共有七个字段，每个字段含义分别如下所述：

第一字段：用户帐号

第二字段：密码占位符

第三字段：用户帐号ID

第四字段：组帐号ID

第五字段：用户说明

第六字段：宿主目录

第七字段：登录 Shell

（2）shadow文件中的配置行格式

保存用户的密码、账号有效期等信息

![](https://img-blog.csdn.net/20180817141507839?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

文件的每一行内容包含九个用冒号“:”分隔的配置字段，每个字段的含义如下所述：

第一字段：用户帐号的名称

第二字段：加密的密码字串信息

第三字段：上次修改密码的时间

第四字段：密码的最短有效天数，默认值为0，表示不进行限制

第五字段：密码的最长有效天数，默认值为99999，表示不进行限制

第六字段：提前多少天警告用户口令将过期，默认值为7

第七字段：在密码过期之后多少天禁用此用户

第八字段：帐号失效时间，默认值为空

第九字段：保留字段（未使用）

**2.2****添加、修改、删除用户帐号**

（1）useradd命令：添加用户账号

![20200717193814_44e3f443ee935df0d73dd73a301c70be.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200717193814_44e3f443ee935df0d73dd73a301c70be.png)

![](https://img-blog.csdn.net/20180817141508232?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

（2）passwd命令：设置/更改用户口令

![20200717193920_17a4503e03f5450cb15a98ce4c19e7bf.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200717193920_17a4503e03f5450cb15a98ce4c19e7bf.png)

![](https://img-blog.csdn.net/20180817141507882?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

不指定用户名时，修改当前账号的密码

![](https://img-blog.csdn.net/20180817141508171?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![](https://img-blog.csdn.net/20180817141508349?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

（3）usermod命令：修改用户账号的属性

![20200717193948_3f516b2f63aac438ecec31cda6b74f1f.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200717193948_3f516b2f63aac438ecec31cda6b74f1f.png)

![](https://img-blog.csdn.net/20180817141508114?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![](https://img-blog.csdn.net/20180817141508210?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

（4）userdel命令：删除用户账号

![20200717201932_5fc1ea94719a6545e40c28ecfd1a7c13.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200717201932_5fc1ea94719a6545e40c28ecfd1a7c13.png)


**3.****组帐号管理**

**3.1****组帐号文件**

与组账号相关的配置文件也有两个，分别是/etc/group(保存组帐号基本信息)和/etc/gshadow(保存组帐号的密码信息)

![](https://img-blog.csdn.net/20180817141508445?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

**3.2****添加、管理、删除组帐号**

（1）groupadd命令：添加组帐号

![](https://img-blog.csdn.net/20180817141508789?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

（2）gpasswd命令：添加、设置、删除组帐号

\-a:添加

\-d:删除

\-M：同时添加多个帐号

![](https://img-blog.csdn.net/20180817141508854?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

（3）groupdel命令：删除组帐号

![](https://img-blog.csdn.net/20180817141508615?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

4.查询帐号信息

4.1 groups命令：查询用户帐号所属的组

![](https://img-blog.csdn.net/20180817141508758?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

4.2 id:查询用户帐号的身份标识

![](https://img-blog.csdn.net/20180817141508796?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

4.3 finger命令：查询用户帐号的登录属性

如果没有该命令的话，可以先安装，如下：

![](https://img-blog.csdn.net/20180817141508973?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

安装完成后，可以使用finger命令了，如下：

![](https://img-blog.csdn.net/2018081714150922?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

4.4 w命令：查询当前主机的用户登录情况

![](https://img-blog.csdn.net/20180817141509115?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

**二、管理目录和文件的属性**

**1.****查看目录和文件的属性**

![](https://img-blog.csdn.net/20180817141509697?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

尽管在 Linux 系统中一切都是文件，但是每个文件的类型不尽相同，因此 Linux 系统使用了不同的字符来加以区分，常见的字符如下所示。

*   \-：普通文件。
*   d：目录文件。
*   l：链接文件。
*   b：块设备文件。
*   c：字符设备文件。
*   p：管道文件。

文件的读、写、执行权限可以简写为 rwx，亦可分别用数字 4、2、1 来表示，文件所有者，所属组及其他用户权限之间无关联，如下表所示。

![20200717202034_6b7a4215066a16bccda0434994f41766.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200717202034_6b7a4215066a16bccda0434994f41766.png)

**2.****设置目录和文件权限（使用chmod命令）**
```
chmod   \[ugoa\]  \[+\-=\]  \[rwx\]  文件或目录...

或chmod nnn 文件或目录...

u、g、o、a 分别表示属主、属组、其他用户、所有用

+、\-、= 分别表示增加、去除、设置权限

nnn:3位八进制数
```
![](https://img-blog.csdn.net/20180817141510122?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

结合“\-R”可进行递归修改，如下

![](https://img-blog.csdn.net/20180817141509625?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

**3.****设置目录和文件的归属（使用chown命令）**

chown  属主   文件或目录

chown  :属组  文件或目录

chown  属主:属组  文件或目录

![](https://img-blog.csdn.net/20180817141509390?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjM0MjQ1Ng==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

\-R：递归修改指定目录下所有文件、子目录的归属