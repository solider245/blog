---
title: 管理用户和组，文件权限和属性以及对帐户启用sudo访问–第8部分
date: 2020-10-12 12:09:51
permalink: /pages/686cb3/
categories:
  - linux用户管理
  - 基本概念
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 08:01:18
 * @LastEditTime: 2020-07-17 08:01:19
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\基本概念\管理用户和组，文件权限和属性以及对帐户启用sudo访问–第8部分.md
 * @日行一善，每日一码
--> 
去年八月，Linux基金会启动了 **LFCS** 认证（ **Linux Foundation Certified Sysadmin** ），这是一个全新的计划，其目的是允许世界各地的个人参加考试，以获取对Linux系统的基础到中间操作支持的认证。支持正在运行的系统和服务，以及整体监视和分析，以及智能决策，从而能够决定何时将问题上报给更高级别的支持团队。

[![Linux用户和组管理](https://www.tecmint.com/wp-content/uploads/2014/10/lfcs-Part-8.png)

![Linux Users and Groups Management](https://www.tecmint.com/wp-content/uploads/2014/10/lfcs-Part-8.png)

](https://www.tecmint.com/wp-content/uploads/2014/10/lfcs-Part-8.png)

Linux Foundation认证的Sysadmin –第8部分

请快速浏览以下视频，该视频描述了Linux Foundation Certification Program的简介。

本文是一个10篇教程的长篇系列文章的第8部分，在本节中，我们将指导您如何管理LFCS认证考试所需的Linux系统中的用户和组权限。

由于Linux是多用户操作系统（因为它允许不同计算机或终端上的多个用户访问一个系统），因此您将需要知道如何执行有效的用户管理：如何添加，编辑，暂停或删除用户帐户，并向他们授予执行其分配任务所需的权限。

### 添加用户帐户

要添加新的用户帐户，您可以以超级用户身份运行以下两个命令之一。

\# adduser \[new\_account\]
# useradd \[new\_account\]

将新的用户帐户添加到系统后，将执行以下操作。

**1.** 创建他/她的主目录（ 默认为 **/ home / username** ）。

**2.** 以下隐藏文件被复制到用户的主目录中，并将用于为其用户会话提供环境变量。

.bash\_logout
.bash\_profile
.bashrc

**3.** 在/ var / spool / mail / **username中** 为用户创建一个邮件假脱机 。

**4.** 创建一个组，并为其赋予与新用户帐户相同的名称。

##### 了解/ etc / passwd

完整的帐户信息存储在 **/ etc / passwd** 文件中。 该文件包含每个系统用户帐户的记录，并具有以下格式（字段由冒号分隔）。

\[username\]:\[x\]:\[UID\]:\[GID\]:\[Comment\]:\[Home directory\]:\[Default shell\]

1.  字段 **\[用户名\]** 和 **\[注释\]** 不言自明。
2.  第二个字段中 的 **x** 表示该帐户受阴影密码（在 **/ etc / shadow中** ）保护，需要以 **\[username\]** 身份登录 。
3.  的 **\[UID\]** 和 **\[GID\]** 字段是表示所述用户标识和所述主组识别到整数 **\[用户名\]** 所属分别。
4.  在 **\[主目录\]** 指示的绝对路径 **\[用户名\]** 的主目录，
5.  在 **\[默认的shell\]** 是将提供给该用户时，他或她登录系统的外壳。

##### 了解/ etc / group

组信息存储在 **/ etc / group** 文件中。 每条记录具有以下格式。

\[Group name\]:\[Group password\]:\[GID\]:\[Group members\]

1.  **\[Group name\]** 是组的名称。
2.  一个 **X** 在 **\[组密码\]** 表示未使用组密码。
3.  **\[GID\]** ：与/ etc / passwd中的相同。
4.  **\[组成员\]** ： **\[组名\]** 成员的用户逗号分隔列表 。

[![在Linux中添加用户帐户](https://www.tecmint.com/wp-content/uploads/2014/10/add-user-accounts.png)

![Add User Accounts in Linux](https://www.tecmint.com/wp-content/uploads/2014/10/add-user-accounts.png)

](https://www.tecmint.com/wp-content/uploads/2014/10/add-user-accounts.png)

添加用户帐户

添加帐户后，您可以使用 **usermod** 命令 编辑以下信息（仅**列出** 几个字段） ，其基本语法usermod如下。

\# usermod \[options\] \[username\]

###### 设置帐户的到期日期

使用 **–expiredate** 标志，后跟日期， 格式 为 **YYYY\-MM\-DD** 。

\# usermod \-\-expiredate 2014\-10\-30 tecmint

###### 将用户添加到补充组

使用组合 **\-ag** ，或 **\-append** **\-基** 的选择，其次是一个逗号分隔的组列表。

\# usermod \-\-append \-\-groups root,users tecmint

###### 更改用户主目录的默认位置

使用 **\-d** 或 **–home** 选项，后跟新主目录的绝对路径。

\# usermod \-\-home /tmp tecmint

###### 更改用户默认使用的外壳

使用 **–shell** ，然后 使用 新shell的路径。

\# usermod \-\-shell /bin/sh tecmint

###### 显示用户所属的组

\# groups tecmint
# id tecmint

现在，让我们一次性执行上述所有命令。

\# usermod \-\-expiredate 2014\-10\-30 \-\-append \-\-groups root,users \-\-home /tmp \-\-shell /bin/sh tecmint

[![usermod命令示例](https://www.tecmint.com/wp-content/uploads/2014/10/usermod-command-examples-620x161.png)

![usermod Command Examples](https://www.tecmint.com/wp-content/uploads/2014/10/usermod-command-examples-620x161.png)

](https://www.tecmint.com/wp-content/uploads/2014/10/usermod-command-examples.png)

usermod命令示例

在上面的示例中，我们将 **tecmint** 用户帐户 的有效期限设置为 **2014年10月30日** 。 我们还将帐户添加到 **root** 和users组。 最后，我们将 `sh` 其 设置 为默认外壳，并将主目录的位置更改为 **/ tmp** ：

**另请阅读** ：

1.  [Linux中的15个useradd命令示例](https://www.tecmint.com/add-users-in-linux/)
2.  [Linux中的15个usermod命令示例](https://www.tecmint.com/usermod-command-examples/)

对于现有帐户，我们还可以执行以下操作。

###### 通过锁定密码来禁用帐户

使用 **\-L** （大写L）或 **\-lock** 选项可锁定用户密码。

\# usermod \-\-lock tecmint

###### 解锁用户密码

使用 **–u** 或 **–unlock** 选项可解锁先前被阻止的用户密码。

\# usermod \-\-unlock tecmint

[![在Linux中锁定用户](https://www.tecmint.com/wp-content/uploads/2014/10/lock-user-in-linux-620x224.png)

![Lock User in Linux](https://www.tecmint.com/wp-content/uploads/2014/10/lock-user-in-linux-620x224.png)

](https://www.tecmint.com/wp-content/uploads/2014/10/lock-user-in-linux.png)

锁定用户帐号

###### 创建一个新组以对需要由多个用户访问的文件进行读写访问

运行以下一系列命令以实现目标。

\# groupadd common\_group # Add a new group
# chown :common\_group common.txt # Change the group owner of common.txt to common\_group
# usermod \-aG common\_group user1 # Add user1 to common\_group
# usermod \-aG common\_group user2 # Add user2 to common\_group
# usermod \-aG common\_group user3 # Add user3 to common\_group

###### 删除群组

您可以使用以下命令删除组。

\# groupdel \[group\_name\]

如果存在由 **group\_name** 拥有的文件 ，则不会删除它们，但是组所有者将设置为 已删除组 的 **GID** 。

### Linux文件权限

除了我们在“ [存档工具和设置文件属性\-](https://www.tecmint.com/compress-files-and-finding-files-in-linux/) 本系列”的 [第3部分中](https://www.tecmint.com/compress-files-and-finding-files-in-linux/) 讨论的基本读取，写入和执行权限外 ，还有其他一些使用较少（但并非不重要）的权限设置，有时也称为“ **特殊权限** ”。

像前面讨论的基本权限一样，它们是使用八进制文件或通过指示权限类型的字母（符号）来设置的。

###### 删除用户帐号

您可以使用 带有**–remove** 选项 的 **userdel** 命令 删除帐户（以及帐户的主目录（如果归用户所有）以及驻留在其中的所有文件以及邮件假脱机） 。

\# userdel \-\-remove \[username\]

#### 集团管理

每次将新用户帐户添加到系统时，都会使用用户名作为其唯一成员来创建一个具有相同名称的组。 以后可以将其他用户添加到组中。 组的目的之一是通过对文件和其他系统资源设置正确的权限来实现对这些资源的简单访问控制。

例如，假设您具有以下用户。

1.  user1（主要组：user1）
2.  user2（主要组：user2）
3.  user3（主要组：user3）

每个人都必须 **阅读** 并 **写入** 到一个名为访问 **common.txt** 位于某处您的本地系统上，也可能在该网络共享 **user1的** 创造。 您可能会想做类似的事情，

\# chmod 660 common.txt
OR
# chmod u=rw,g=rw,o= common.txt \[notice the space between the last equal sign and the file name\]

然而，这将只提供 **读取** 和 **写入** 到文件的所有者和那些谁是该文件（组所有者的成员的用户访问 **USER1** 在这种情况下）。 再次，您可能会想将 **user2** 和 **user3** 添加 到组 **user1中** ，但这也将使他们能够访问用户 **user1** 和组 **user1** 拥有的其余文件 。

这是团体派上用场的地方，这是在这种情况下应该采取的措施。

##### 了解Setuid

将 **setuid** 权限应用于可执行文件时，运行该程序的用户将继承该程序所有者的有效特权。 由于此方法可以合理地引起安全问题，因此必须将具有setuid许可权的文件数保持为最少。 当系统用户需要访问root拥有的文件时，您可能会找到设置了此权限的程序。

总结起来，不仅用户可以执行二进制文件，而且还可以利用root用户的特权来执行该文件。 例如，让我们检查 **/ bin / passwd** 的权限 。 该二进制文件用于更改帐户的密码，并修改 **/ etc / shadow** 文件。 超级用户可以更改任何人的密码，但所有其他用户只能更改自己的密码。

[![passwd命令示例](https://www.tecmint.com/wp-content/uploads/2014/10/passwd-command.png)

![passwd Command Examples](https://www.tecmint.com/wp-content/uploads/2014/10/passwd-command.png)

](https://www.tecmint.com/wp-content/uploads/2014/10/passwd-command.png)

passwd命令示例

因此，任何用户都应具有运行 **/ bin / passwd的** 权限 ，但只有root才能指定帐户。 其他用户只能更改其相应的密码。

[![在Linux中更改用户密码](https://www.tecmint.com/wp-content/uploads/2014/10/change-user-password.png)

![Change User Password in Linux](https://www.tecmint.com/wp-content/uploads/2014/10/change-user-password.png)

](https://www.tecmint.com/wp-content/uploads/2014/10/change-user-password.png)

修改用户密码

##### 了解Setgid

将 **setgid** 位置1 后，实际用户 的有效 **GID** 变为组所有者 的有效**GID** 。 因此，任何用户都可以在授予该文件的组所有者的特权下访问该文件。 另外，在目录上设置setgid位时，新创建的文件将继承与该目录相同的组，并且新创建的子目录也将继承父目录的setgid位。 每当某个特定组的成员需要访问目录中的所有文件时，无论文件所有者的主要组如何，您都将很可能使用此方法。

\# chmod g+s \[filename\]

要将 **setgid** 设置为 八进制形式，请在数字 **2之前** 添加当前（或所需的）基本权限。

\# chmod 2755 \[directory\]

###### 在目录中设置SETGID

[![在Linux中添加Setgid](https://www.tecmint.com/wp-content/uploads/2014/10/add-setgid-to-directory-620x190.png)

![Add Setgid in Linux](https://www.tecmint.com/wp-content/uploads/2014/10/add-setgid-to-directory-620x190.png)

](https://www.tecmint.com/wp-content/uploads/2014/10/add-setgid-to-directory.png)

将Setgid添加到目录

##### 了解粘性位

当 在文件上设置 “ **sticky bit** ”时，Linux只会忽略它，而对于目录，它具有防止用户删除甚至重命名其包含的文件的作用，除非用户拥有该目录，该文件或是root用户。

\# chmod o+t \[directory\]

要将 **粘性位** 设置为 八进制形式，请在数字 **1之前** 添加当前（或所需的）基本权限。

\# chmod 1755 \[directory\]

没有粘性位，任何能够写入目录的人都可以删除或重命名文件。 因此，通常在 可写的 目录（例如 **/ tmp）** 上找到粘性位 。

[![在Linux中添加Stickybit](https://www.tecmint.com/wp-content/uploads/2014/10/add-sticky-bit-to-directory.png)

![Add Stickybit in Linux](https://www.tecmint.com/wp-content/uploads/2014/10/add-sticky-bit-to-directory.png)

](https://www.tecmint.com/wp-content/uploads/2014/10/add-sticky-bit-to-directory.png)

将Stickybit添加到目录

### 特殊的Linux文件属性

还有其他属性可以进一步限制文件上允许的操作。 例如，防止文件被重命名，移动，删除甚至修改。 它们是使用 [chattr命令](https://www.tecmint.com/chattr-command-examples/) 设置的 ，可以使用 **lsattr** 工具 进行查看 ，如下所示。

\# chattr +i file1
# chattr +a file2

执行完这两个命令后， **file1** 将是不可变的（这意味着它不能被移动，重命名，修改或删除），而 **file2** 将进入仅追加模式（只能在追加模式下打开以进行写入）。

[![保护文件免遭删除](https://www.tecmint.com/wp-content/uploads/2014/10/chattr-command.png)

![Protect File from Deletion](https://www.tecmint.com/wp-content/uploads/2014/10/chattr-command.png)

](https://www.tecmint.com/wp-content/uploads/2014/10/chattr-command.png)

Chattr命令保护文件

### 访问根帐户并使用sudo

用户获取根帐户访问权限的方法之一是通过键入。

$ su

然后输入root的密码。

如果身份验证成功，您将以 **root用户** 身份登录， 当前工作目录与以前相同。 如果要改为放置在根目录的主目录中，请运行。

$ su \-

然后输入root的密码。

[![在Linux上启用sudo访问](https://www.tecmint.com/wp-content/uploads/2014/10/Enable-Sudo-Access.png)

![Enable sudo Access on Linux](https://www.tecmint.com/wp-content/uploads/2014/10/Enable-Sudo-Access.png)

](https://www.tecmint.com/wp-content/uploads/2014/10/Enable-Sudo-Access.png)

在用户上启用Sudo访问

上述过程要求普通用户知道root的密码，这会带来严重的安全风险。 因此，sysadmin可以配置 **sudo** 命令，以允许普通用户以非常受控制且受限制的方式以其他用户（通常是超级用户）的身份执行命令。 因此，可以对用户设置限制，以使用户能够运行一个或多个特定的特权命令，而不能运行其他命令。

**另请参阅** ： [su和sudo用户之间的区别](https://www.tecmint.com/su-vs-sudo-and-how-to-configure-sudo-in-linux/)

要使用 **sudo进行** 身份验证 ，用户将使用他/她自己的密码。 输入命令后，将提示我们输入密码（不是超级用户的密码），并且如果身份验证成功（并且如果已授予用户运行命令的权限），则会执行指定的命令。

要授予对sudo的访问权限，系统管理员必须编辑 **/ etc / sudoers** 文件。 建议使用 **visudo** 命令 编辑此文件， 而不是直接使用文本编辑器打开它。

\# visudo

这将 使用**vim** 打开 **/ etc / sudoers** 文件 （您可以按照 本系列的 [第2部分“安装和使用vim作为编辑器”中](https://www.tecmint.com/vi-editor-usage/) 给出的说明 进行编辑）。[](https://www.tecmint.com/vi-editor-usage/)

这些是最相关的行。

Defaults    secure\_path="/usr/sbin:/usr/bin:/sbin"
root        ALL=(ALL) ALL
tecmint     ALL=/bin/yum update
gacanepa    ALL=NOPASSWD:/bin/updatedb
%admin      ALL=(ALL) ALL

让我们仔细看看它们。

Defaults    secure\_path="/usr/sbin:/usr/bin:/sbin:/usr/local/bin"

此行使您可以指定将用于 **sudo** 的目录 ，并用于防止使用特定于用户的目录，这可能会损害系统。

下几行用于指定权限。

root        ALL=(ALL) ALL

1.  第一个 **ALL** 关键字指示此规则适用于所有主机。
2.  第二个 **ALL** 表示第一列中的用户可以使用任何用户的特权运行命令。
3.  第三个 **ALL** 表示可以运行任何命令。

tecmint     ALL=/bin/yum update

如果在 **\=** 号 后未指定任何用户 ，则sudo假定为root用户。 在这种情况下，用户 **tecmint** 将能够以 root 用户**身份** 运行 **yum update** 。

gacanepa    ALL=NOPASSWD:/bin/updatedb

该 **NOPASSWD** 指令允许用户gacanepa到运行 **/斌/ updatedb的** 无需输入他的密码。

%admin      ALL=(ALL) ALL

在 **％** 迹象表明，这条线适用于被称为“组 **管理** ”。 该行其余部分的含义与普通用户相同。 这意味着“ **admin** ” 组的成员 可以在所有主机上以任何用户身份运行所有命令。

要查看sudo授予您哪些特权，请使用“ **\-l** ”选项将其列出。

[![Sudo访问规则](https://www.tecmint.com/wp-content/uploads/2014/10/sudo-access-rules-620x305.png)

![Sudo Access Rules](https://www.tecmint.com/wp-content/uploads/2014/10/sudo-access-rules-620x305.png)

](https://www.tecmint.com/wp-content/uploads/2014/10/sudo-access-rules.png)

Sudo访问规则

### PAM（可插入身份验证模块）

**可插拔身份验证模块** （PAM）提供了使用模块在每个应用程序和/或每个服务的基础上设置特定身份验证方案的灵活性。 在所有现代Linux发行版中都存在的该工具克服了Linux早期开发人员经常遇到的问题，当时每个需要身份验证的程序都必须专门编译以了解如何获取必要的信息。

例如，对于PAM，您的密码是存储在 **/ etc / shadow** 还是网络内部的单独服务器上 都没有关系 。

例如，当登录程序需要对用户进行身份验证时，PAM动态提供包含正确身份验证方案功能的库。 因此，更改登录应用程序（或使用PAM的任何其他程序）的身份验证方案很容易，因为它仅涉及编辑配置文件（最有可能是，以该应用程序命名的文件，位于内部 `/etc/pam.d` ，而不太可能位于中 `/etc/pam.conf` ）。

里面的文件 `/etc/pam.d` 指示哪些应用程序在本地使用PAM。 另外，我们可以通过检查某个应用程序是否 已链接到 PAM库（ **libpam** ） 来判断某个应用程序是否使用PAM ：

\# ldd $(which login) | grep libpam # login uses PAM
# ldd $(which top) | grep libpam # top does not use PAM

[![检查Linux PAM库](https://www.tecmint.com/wp-content/uploads/2014/10/Check-Linux-PAM-Library.png)

![Check Linux PAM Library](https://www.tecmint.com/wp-content/uploads/2014/10/Check-Linux-PAM-Library.png)

](https://www.tecmint.com/wp-content/uploads/2014/10/Check-Linux-PAM-Library.png)

检查Linux PAM库

在上图中，我们可以看到 **libpam** 已与登录应用程序链接。 这是有道理的，因为此应用程序涉及系统用户身份验证的操作，而top不涉及。

让我们检查一下 **passwd** 的PAM配置文件 \-是的，众所周知的实用程序，用于更改用户的密码。 它位于 **/etc/pam.d/passwd** ：

\# cat /etc/passwd

[![Linux密码的PAM配置文件](https://www.tecmint.com/wp-content/uploads/2014/10/PAM-Configuration-File-for-Linux-Password.png)

![PAM Configuration File for Linux Password](https://www.tecmint.com/wp-content/uploads/2014/10/PAM-Configuration-File-for-Linux-Password.png)

](https://www.tecmint.com/wp-content/uploads/2014/10/PAM-Configuration-File-for-Linux-Password.png)

Linux密码的PAM配置文件

第一列表示 `type` 要与 `module-path` （第三列） 一起使用的身份验证的身份 。 当在类型之前出现连字符时，如果无法加载模块（因为无法在系统中找到该模块），则PAM不会将其记录到系统日志中。

以下身份验证类型可用：

1.  `account` ：此模块类型检查用户或服务是否提供了有效的凭据进行身份验证。
2.  `auth` ：此模块类型可验证用户是他/她声称的身份，并授予所需的任何特权。
3.  `password` ：此模块类型允许用户或服务更新其密码。
4.  `session` ：此模块类型指示验证成功之前和/或之后应该执行的操作。

第二列（称为 `control` ）指出了与此模块的身份验证失败时应该发生的情况：

1.  `requisite` ：如果通过此模块的身份验证失败，则将立即拒绝整体身份验证。
2.  `required` 与必填项相似，尽管在拒绝身份验证之前将调用此服务列出的所有其他模块。
3.  `sufficient` ：如果通过此模块的身份验证失败，即使先前标记为必需的失败，PAM仍将授予身份验证。
4.  `optional` ：如果通过此模块的身份验证失败或成功，则除非此服务是为此类型定义的唯一模块，否则不会发生任何事情。
5.  `include` 表示应从另一个文件读取给定类型的行。
6.  `substack` 与include类似，但身份验证失败或成功不会导致整个模块退出，而只会导致子堆栈退出。

第四列（如果存在）显示要传递给模块的参数。

**/etc/pam.d/passwd中的** 前三行 （如上所示）加载 **system\-auth** 模块，以检查用户是否提供了有效的凭证（帐户）。 如果是这样，则允许他/她通过授予使用passwd（ **auth** ）的 权限来更改身份验证令牌（密码 ）。

例如，如果您追加

remember=2

到下一行

password    sufficient    pam\_unix.so sha512 shadow nullok try\_first\_pass use\_authtok

在 **/etc/pam.d/system\-auth中** ：

password    sufficient    pam\_unix.so sha512 shadow nullok try\_first\_pass use\_authtok remember=2

每个用户的最后两个哈希密码保存在 **/ etc / security / opasswd中，** 因此它们无法重复使用：

[![Linux密码字段](https://www.tecmint.com/wp-content/uploads/2014/10/Linux-Password-Fields.png)

![Linux Password Fields](https://www.tecmint.com/wp-content/uploads/2014/10/Linux-Password-Fields.png)

](https://www.tecmint.com/wp-content/uploads/2014/10/Linux-Password-Fields.png)

Linux密码字段

### 摘要

有效的用户和文件管理技能是任何系统管理员必备的工具。 在本文中，我们介绍了基础知识，希望您可以将其用作基础上的良好起点。 请随时在下面留下您的评论或问题，我们会尽快答复。