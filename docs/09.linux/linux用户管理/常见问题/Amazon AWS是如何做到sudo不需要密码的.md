---
title: Amazon AWS是如何做到sudo不需要密码的
date: 2020-10-12 12:09:51
permalink: /pages/3db406/
categories:
  - linux用户管理
  - 常见问题
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-18 17:08:46
 * @LastEditTime: 2020-07-18 17:08:47
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\常见问题\Amazon AWS是如何做到sudo不需要密码的.md
 * @日行一善，每日一码
--> 
我使用过很多服务商，其中就包括aws。在很多服务商那里，主机需要密码，而aws不需要，aws是证书登录。然而其他服务商登陆上以后sudo是需要密码的，而aws不需要，这点让我很惊奇。经过一系列的探究，根据将aws与其他的服务商进行对比，我发现了这里有区别。
在/etc/sudoers里有这样一行
#includedir /etc/sudoers.d
这一行引用了/etc/sudoers.d下（基本上）所有的文件（详情请参考/etc/sudoers.d/README）
然后amazon安装程序在创建了/etc/sudoers.d/90-cloud-init-users这样一个文件，内容如下
# Created by cloud-init v. 0.7.5 on Sat, 14 May 2016 12:31:57 +0000

# User rules for ubuntu
ubuntu ALL=(ALL) NOPASSWD:ALL
看来结果显而易见了，/etc/sudoers是那些sudo不需要密码的用户的文件，因为安全性，ubuntu不建议直接修改/etc/sudoers文件，而是包含/etc/sudoers.d目录下文件，通过在这个目录下创建权限文件，实现了不需要密码sudo
另外，这是90-cloud-init-users的文件信息：-r--r-----   1 root root   123 May 14  2016 90-cloud-init-users