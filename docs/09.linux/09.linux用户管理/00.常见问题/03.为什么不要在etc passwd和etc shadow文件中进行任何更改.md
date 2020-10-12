---
title: 为什么不要在etc passwd和etc shadow文件中进行任何更改
date: 2020-10-12 12:09:51
permalink: /pages/af99e9/
categories:
  - linux用户管理
  - 常见问题
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 08:31:01
 * @LastEditTime: 2020-07-17 08:31:51
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\常见问题\为什么不要在etc passwd和etc shadow文件中进行任何更改.md
 * @日行一善，每日一码
--> 
不要在/ etc / passwd和/ etc / shadow文件中进行任何更改，因为在进行更改之后，您需要重新引导计算机/服务器以使更改生效。 这样一来，您就可以将自己锁定在计算机之外，无论您尝试使用哪个用户或为哪个用户进行更改。
可以尝试：
1）adduser
2）passwd
参照/ etc / passwd文件
user1：x：1502：1502 :: / home / user1：/ bin / bash
user2：x：1503：1503 :: /检查创建用户的位置home / user2：/ bin / bash
user3：x：1504：1504 :: / home / user3：/ bin / bash
3）并根据您的要求提供特权
chmod \-R 600 / home / user1
chmod \-R 700 / home / user2
chmod \-R 777 / home / user3
chmod \-R 500 / home / user4

«为此，需要编辑文件/ etc / passwd并将UID和GID更改为0»
这是一个坏主意，因为在重新启动linux系统后，您将不会在Windows的登录菜单中看到具有UID 0和GID 0的用户。 linux。在这种情况下，您可以仅通过命令行登录linux。要从linux的登录菜单到达那里，请按按钮组合键Ctrl + Alt + F1。