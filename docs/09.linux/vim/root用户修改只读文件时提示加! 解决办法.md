---
title: root用户修改只读文件时提示加! 解决办法
date: 2020-10-12 12:09:51
permalink: /pages/48829a/
categories:
  - linux
  - vim
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 17:31:42
 * @LastEditTime: 2020-07-17 17:32:02
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\vim\root用户修改只读文件时提示加! 解决办法.md
 * @日行一善，每日一码
--> 
如题，今天在修改/etc/sudoers文件时，提示只读，需要加!，但是我是root用户呀，不是可以直接改吗？

多次修改用户也解决不了这个问题，只能加了

按照写入退出应该是 wq，但是加！后要编程 wq!
![20200717173203_6605496a553f317b14b736eff6a607f7.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200717173203_6605496a553f317b14b736eff6a607f7.png)