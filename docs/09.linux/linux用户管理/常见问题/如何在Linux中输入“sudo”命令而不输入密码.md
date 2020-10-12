---
title: 如何在Linux中输入“sudo”命令而不输入密码
date: 2020-10-12 12:09:51
permalink: /pages/60a4d2/
categories:
  - linux用户管理
  - 常见问题
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 18:11:51
 * @LastEditTime: 2020-07-17 18:12:01
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\常见问题\如何在Linux中输入“sudo”命令而不输入密码.md
 * @日行一善，每日一码
--> 
在本文中，我们将解释如何配置一个sudo命令运行，而不是每次在Linux终端中输入密码。

分类: [Linux命令](https://www.howtoing.com/category/linux-commands) [操作系统](https://www.howtoing.com/category/operating-system)

* 2017\-01\-25 00:00:00*

如果你在通常单独使用的机器上运行Linux，说在笔记本电脑上，每次调用**sudo**时输入密码都会变得非常无聊。 因此，在本指南中，我们将描述[如何配置sudo命令](https://www.howtoing.com/sudoers-configurations-for-setting-sudo-in-linux/)运行而不输入密码。 此设置在 **/etc/sudoers**文件中完成，它驱动sudoers为[sudo命令](https://www.howtoing.com/su-vs-sudo-and-how-to-configure-sudo-in-linux/)使用默认安全策略插件;在用户权限指定部分。 **要点** ：在**sudeors**文件中，默认情况下启用的authenticate参数用于验证目的。 如果设置，用户必须通过密码（或其他身份验证方法）对自己进行身份验证，然后才能使用**sudo**运行命令。 但是，可以使用 **NOPASSWD** （当用户调用**sudo**命令时不需要密码）标记来覆盖此默认值。 配置用户权限的语法如下：

user\_list host\_list\=effective\_user\_list tag\_list command\_list

哪里：

1.  `user_list` \- 用户列表或已设置的用户别名。
2.  `host_list` \- 用户可以在其上运行sudo的主机或主机别名列表。
3.  `effective_user_list` \- 他们必须作为别名运行或作为别名运行的用户列表。
4.  `tag_list` \- 标签列表，如NOPASSWD。
5.  `command_list` \- 要由用户使用sudo运行的命令或命令别名列表。

要允许用户（ `aaronkilik`的示例中的`aaronkilik` ）使用**sudo**而不使用密码运行所有命令，请打开**sudoers**文件：

$ sudo visudo

并添加以下行：

aaronkilik ALL\=(ALL) NOPASSWD: ALL

对于组的情况，请在组名前使用 `%`字符，如下所示; 这意味着`sys`组的所有成员将使用sudo而不使用密码运行所有命令。

%sys ALL\=(ALL) NOPASSWD: ALL

要允许用户使用sudo而不使用密码运行给定的命令（ `/bin/kill` ），请添加以下行：

aaronkilik ALL\=(ALL) NOPASSWD:  /bin/kill

下面的行将使 `sys`组的成员运行命令： **/ bin / kill** ， **/ bin / rm**使用**sudo**而不使用密码：

%sys ALL\=(ALL) NOPASSWD:  /bin/kill,  /bin/rm

[![运行sudo without Password](https://www.howtoing.com/wp-content/uploads/2017/01/Run-sudo-Without-Password.png)](https://www.howtoing.com/wp-content/uploads/2017/01/Run-sudo-Without-Password.png)

运行sudo without Password

有关更多**sudo**配置和其他使用选项，请阅读我们的文章，描述更多的示例：

1.  [10有用的Sudoers配置在Linux中设置'sudo'](https://www.howtoing.com/sudoers-configurations-for-setting-sudo-in-linux/)
2.  [让Sudo输入您输入不正确的密码时](https://www.howtoing.com/sudo-insult-when-enter-wrong-password/)
3.  [如何保持'sudo'密码超时会话在Linux](https://www.howtoing.com/set-sudo-password-timeout-session-longer-linux/)

在本文中，我们描述了如何配置sudo命令运行而不输入密码。不要忘记向我们提供您对本指南或其他有用的软件配置的想法，供Linux系统管理员在评论中使用。