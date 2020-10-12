---
title: chown 更改用户目录为root
date: 2020-10-12 12:09:51
permalink: /pages/425a3e/
categories:
  - 常用命令
  - chown命令
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 17:57:16
 * @LastEditTime: 2020-07-17 18:06:33
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\常用命令\chown命令\chown 更改用户目录为root.md
 * @日行一善，每日一码
--> 
```shell
chown -R root:root /home/$user 
```
通常：如果您不完全知道命令的用途，请不要执行来自网络的命令。

**特别是由根！** 。

该命令 `chown root:root /home/mynewuser` 是：

> **CH** anging了 **自己** ership给 **用户：组** 的 **/家/ mynewuser** 。
> 
   >>下面这个是英文原文     
   >>   changing the ownership to user:group of /home/mynewuser.
     
    
但是， [链接页面](https://www.digitalocean.com/community/questions/ubuntu-16-04-creating-new-user-and-adding-ssh-keys?answer=36900) 的第一条评论 会添加 `-R` （继续阅读）。

假设用户 `kevind` （使用您提供的特定名称）已经 `kevind` 创建了 一个主组 （也可以创建，如果需要的话），恢复效果的命令是：

```
chown kevind:kevind /home/kevind
```

必须以root身份执行/由root执行，以将root的所有权还原给用户 `kevind` 。

为了确保 `kevind` 根目录下没有root拥有的某些文件 ，更广泛的更改是 （出于安全原因）：

```
chown -R kevind:kevind /home/kevind
```

将 **\[R** 给定的顶部目录下的所有目录和子目录里面ecurse。 这是一个安全的命令，没有真正的理由让用户在其主目录中拥有root拥有的文件（或目录）。