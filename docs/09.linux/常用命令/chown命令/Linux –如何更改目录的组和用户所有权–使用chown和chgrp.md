---
title: Linux –如何更改目录的组和用户所有权–使用chown和chgrp
date: 2020-10-12 12:09:51
permalink: /pages/16b9cc/
categories:
  - 常用命令
  - chown命令
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 17:59:26
 * @LastEditTime: 2020-07-17 17:59:36
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\常用命令\chown命令\Linux –如何更改目录的组和用户所有权–使用chown和chgrp.md
 * @日行一善，每日一码
--> 
在本文中，让我们学习如何使用 *chgrp* 和 *chown* 命令更改目录的组和用户所有权

在Linux服务器上，默认情况下，文件或目录的组所有者是创建文件目录的用户的主要组。 在大多数情况下，主要组和用户可能使用相同的名称

假设我们需要将目录 */ home / chris / mars* 的组和用户所有权更改 为root用户，以下是我们需要执行的步骤

**步骤1：** 切换为root用户

#switch to the root user
su \- root

*注意：* 为了更改文件或目录的组所有者，必须是文件的用户所有者，并且必须是我们要更改其所有权的组的成员，否则必须是root用户。 另外，请记住，只有root用户才能更改文件或目录的用户所有权。

**步骤2：** 使用chgrp更改组所有者，使用chown更改用户所有者

#Using chgrp to change the group owner
chgrp root /home/chris/mars
#Using chown to change the user owner
chown root /home/chris/mars

或
**步骤3：** 使用chown同时更改组所有者和用户所有者

#using chown to change both group and user owner at the same time
chown root:root /home/chris/mars

这是给您的一个额外提示：更改文件上的组和用户所有权的过程与在目录上执行命令的过程相同，这使我们的工作变得容易！