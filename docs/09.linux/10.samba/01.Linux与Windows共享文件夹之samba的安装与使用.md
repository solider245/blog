---
title: Linux与Windows共享文件夹之samba的安装与使用
date: 2020-10-12 12:09:51
permalink: /pages/d6740d/
categories:
  - linux
  - samba
tags:
  - 
---
**1.写在前面**

当你在Windows上安装了一台Linux的虚拟机，你想访问Linux中的文件夹，将虚拟机中的文件复制到Windows主机上，你会怎么做呢？如果这台Linux主机不是虚拟机，而是一台远程主机呢？

有没有一种方法，打开Linux虚拟机中的文件夹就像在本地一样，输入路径就可以？你可能会想到FTP，本文介绍一个更简单的方法——samba。

接下来详细介绍如何在Linux上安装samba。

**2.安装方法**

**2.1 安装samba**

sudo apt\-get install samba

**2.2 创建共享目录**

// 创建的目录即之后能够在Windows主机上直接访问的目录。 // 例如：在用户gzd的主目录下新建share文件夹为共享目录 mkdir /home/gzd/smbshare // 由于Windows下的文件夹需可读可写可执行，需更改权限为777 sudo chmod 777 /home/gzd/smbshare

**2.3 修改samba配置文件**

// 修改 /etc/samba/smb.conf sudo vim /etc/samba/smb.conf // 在smb.conf文件最后加上以下内容

\[share\]

path = /home/gzd/smbshare

public = yes

writable = yes

valid users = gzd

create mask = 0644

force create mode = 0644

directory mask = 0755

force directory mode = 0755

available = yes

![Linux与Windows共享文件夹之samba的安装与使用](http://p1.pstatp.com/large/pgc-image/d44d289907bd4aea9aef33c144f5338b)

**关于smb.conf的几点解释：**

(1) \[share\]表示共享文件夹的别名，之后将直接使用这个别名

(2) force create mode 与 force directory mode的设置是因为Windows下与Linux下文件和文件夹的默认权限不同造成的，Windows下新建的文件是可执行的，必须强制设定其文件权限。

(3) valid users 设置为你当前的Linux用户名，例如我的是gzd，因为第一次打开共享文件夹时，需要验证权限。

**2.4 设置登录密码**

// 新建/etc/samba/smbpasswd文件 sudo touch /etc/samba/smbpasswd // 根据2.3设置的valid users，设置用户密码 // gzdaijie 替换为你在2.3中设置的用户名 sudo smbpasswd \-a gzd //输入两次密码后，会提示 Added user gzd. 表示设置成功 // 若用户名非当前登录系统的用户名，可能会提示Failed

**2.5 启动samba服务器**

sudo /etc/init.d/samba restart

**2.6 测试是否共享成功**

sudo apt\-get install smbclient smbclient \-L //localhost/share //还记得吗？share为2.3中设置的共享文件夹的别名 //如果共享成功，将要求输入之前设置的密码

**3.在windows上测试**

**3.1 打开windows文件管理器，输入\\\\ip地址或主机名\\share**

*   Linux的ip地址可通过ifconfig查看
*   选择记住凭据，下次输入地址后无需登录
*   第一次打开可能需要几秒时间，耐心一点
*

![Linux与Windows共享文件夹之samba的安装与使用](http://p9.pstatp.com/large/pgc-image/d2d0de0c1bb54c02b060843ccb39d491)

**3.2 尽情享受samba带来的便利吧**

*   在windows下创建文件，到Linux下看看吧！
*   在Linux的共享目录下创建文件，在windows下看看吧！