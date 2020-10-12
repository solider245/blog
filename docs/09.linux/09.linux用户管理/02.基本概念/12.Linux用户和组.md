---
title: Linux用户和组
date: 2020-10-12 12:09:51
permalink: /pages/088ebc/
categories:
  - linux用户管理
  - 基本概念
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 08:03:08
 * @LastEditTime: 2020-07-17 08:03:08
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\基本概念\Linux用户和组.md
 * @日行一善，每日一码
--> 
**在GitHub上贡献**

[报告问题](https://github.com/linode/docs/issues/new?title=Linux%20Users%20and%20Groups%20Proposed%20Changes&body=Link%3A https%3A%2F%2Flinode.com%2fdocs%2ftools-reference%2flinux-users-and-groups%2f%0A%23%23%20Issue%0A%0A%23%23%20Suggested%20Fix%0A&labels=inaccurate guide) | [查看文件](https://github.com/linode/docs/blob/master/docs/tools-reference/linux-users-and-groups/index.md) | [编辑档案](https://github.com/linode/docs/edit/develop/docs/tools-reference/linux-users-and-groups/index.md)

如果您不熟悉Linux / Unix，那么权限的概念可能会令人困惑。 本指南将向您解释什么是权限，它们如何工作以及如何管理它们。 将提供许多示例来说明如何设置和更改用户和组的权限。

![Linux用户和组](https://www.linode.com/docs/tools-reference/linux-users-and-groups/linux_users_and_groups.png "Linux用户和组")

## 什么是用户和组权限？ [固定链接](#what-are-user-and-group-permissions "固定链接")

Linux / Unix操作系统能够以类似于其他操作系统的方式执行多任务。 但是，Linux与其他操作系统的主要区别在于它具有多个用户的能力。 Linux旨在允许多个用户同时访问系统。 为了使这种多用户设计正常工作，需要一种保护用户彼此之间的方法。 这是权限进入的地方。

### 读取，写入和执行权限 [固定链接](#read-write-execute-permissions "固定链接")

权限是对文件或目录执行操作的“权利”。 基本权限是读，写和执行。

*   读取\-可读权限允许查看文件的内容。 目录的读取权限允许您列出目录的内容。
*   写\-对文件的写许可权允许您修改该文件的内容。 对于目录，具有写许可权，您可以编辑目录的内容（例如，添加/删除文件）。
*   执行\-对于文件，可执行权限允许您运行文件并执行程序或脚本。 对于目录，执行权限允许您更改到其他目录，并将其设为当前工作目录。 用户通常具有默认组，但它们可能属于几个其他组。

### 查看文件权限 [固定链接](#viewing-file-permissions "固定链接")

要查看文件或目录的权限，请发出命令 `ls -l <directory/file>` 。 切记将 **<>中** 的信息替换为 实际的文件或目录名称。 以下是 `ls` 命令的 示例输出 ：

```
-rw-r--r-- 1 root root 1031 Nov 18 09:22 /etc/passwd

```

前十个字符显示访问权限。 第一个破折号（\-）表示文件的类型（目录表示d，特殊文件表示s，普通文件表示\-）。 接下来的三个字符（ **rw\-** ）定义所有者对文件的许可。 在此示例中，文件所有者仅具有读取和写入权限。 接下来的三个字符（ **r–** ）是文件所有者与同一组的成员的权限（在此示例中为只读）。 最后三个字符（ **r–** ）显示所有其他用户的权限，在此示例中为只读。

## 与用户，组和目录一起使用 [固定链接](#working-with-users-groups-and-directories "固定链接")

以下各节将介绍创建，删除和修改用户帐户所需的命令。 将讨论组以及用于创建和删除目录的命令。 将为您提供处理用户，组和目录所需的命令和说明。

### 创建和删除用户帐户 [固定链接](#creating-and-deleting-user-accounts "固定链接")

要创建新的标准用户，请使用 `useradd` 命令。 语法如下：

```
useradd <name>

```

useradd命令使用各种变量，下表中显示了其中的一些变量：

| 选项 | 描述 | 例 |
| :-- | :-- | :-- |
| `-d <home_dir>` | home\_dir将用作用户登录目录的值 | `useradd <name> -d /home/<user's home>` |
| `-e <date>` | 帐户到期的日期 | `useradd <name>** -e <YYYY-MM-DD>` |
| `-f <inactive>` | 帐户过期前的天数 | `useradd <name> -f <0 or -1>` |
| `-s <shell>` | 设置默认的外壳类型 | `useradd <name> -s /bin/<shell>` |

您将需要使用以下 `passwd` 命令 为新用户设置密码 。 注意，您将需要root特权才能更改用户密码。 语法如下：

```
passwd <username>

```

用户将可以使用 `passwd` 带有语法 的 命令 随时更改其密码 。 下面是一个示例：

```
$ passwd
Changing password for lmartin.
(current) UNIX password:
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully

```

还有另一种创建用户帐户的方法，对于初次管理员而言可能更容易。 但是，您可能需要安装新的软件包。 Debian / Ubuntu的安装命令如下：

```
apt-get install adduser

```

adduser命令自动创建主目录并设置默认组，shell等。要使用该 `adduser` 命令 创建新的标准用户， 语法如下：

```
adduser <name>

```

输入命令后，您将收到一系列提示； 这些信息大部分是可选的。 但是，您至少应包括用户名（在此示例中，用户名是cjones），当然还包括密码。

```
root@localhost:~# adduser cjones
  Adding user `cjones' ...
  Adding new group `cjones' (1001) ...
  Adding new user `cjones' (1001) with group `cjones' ...
  Creating home directory `/home/cjones' ...
  Copying files from `/etc/skel' ...
  Enter new UNIX password:
  Retype new UNIX password:
  passwd: password updated successfully
  Changing the user information for cjones
  Enter the new value, or press ENTER for the default
      Full Name []: Chuck Jones
      Room Number []: 213
      Work Phone []: 856-555-1212
      Home Phone []:
      Other []:
  Is the information correct? [Y/n] Y

```

重要的是要注意，应该始终非常重视安全性。 因此，强烈建议为每个帐户使用唯一的密码。 切勿将密码共享或提供给其他用户。

要删除用户帐户，请输入以下命令：

```
userdel <name>

```

发出上面的命令只会删除用户的帐户。 他们的文件和主目录不会被删除。

要删除用户，其主文件夹及其文件，请使用以下命令：

```
userdel -r <name>

```

### 了解须藤 [固定链接](#understanding-sudo "固定链接")

Root是超级用户，并且具有在系统上执行任何操作的能力。 因此，为了具有附加的安全层，通常使用sudo用户代替root。 虽然sudo确实是为了执行任务（在大多数情况下，该 `root` 用户或超级用户） 是为了向另一用户授予对另一用户帐户的有限访问权限，但 sudo最好被解释为一种允许用户和组访问其命令的工具。通常将无法使用。 Sudo使用户无需直接以root用户身份登录即可拥有管理特权。 sudo命令的示例如下：

```
sudo apt-get install <package>

```

在使用sudo之前，如果它不是发行版的一部分，则可能需要先安装它。 Debian的命令如下：

```
apt-get install sudo

```

对于CentOS，命令如下：

```
yum install sudo

```

为了向用户提供sudo功能，需要将他们添加到启用sudo的组中，或者需要使用一组权限将其用户名添加到sudoers文件中。 该文件是敏感的，对于访问和安全控制很重要，不应直接使用文本编辑器进行编辑。 如果对sudoers文件的编辑不正确，可能会导致无法访问系统或其他意外的权限更改。

> **注意**
>
> 有关将用户添加到默认启用sudo的组的说明，请参阅我们的“ [如何保护服务器”](#add-a-limited-user-account) 指南

该 `visudo` 命令应用于编辑sudoers文件。 在命令行中，以root用户身份登录到系统并输入命令 `visudo` 。

以下 `sudoers` 摘录允许列出的用户在命令前加上 `sudo` ， 以执行所需的任何命令 ，从而使用户可以完全控制系统。

> **警告**
>
> `sudoers` 如果用户不受信任，则 绝对不应将其添加到 具有完全权限 的 文件或组中。 您可以选择限制用户的操作， `sudo` 以增加安全性。 有关受限用法语法的一些示例， 请参阅 [使用Sudo将命令列入白名单](#whitelisting-commands-with-sudo) 。

|

```bash
1
2
3
4
5

```

 |

```bash
# User privilege specification
root    ALL=(ALL:ALL) ALL
cjones  ALL=(ALL:ALL) ALL
kbrown  ALL=(ALL:ALL) ALL
lmartin ALL=(ALL:ALL) ALL
```

 |

在为用户帐户授予sudo特权后，请保存sudoers文件并以root用户身份注销。 现在以用户身份登录，并以sudo访问身份以用户身份测试特权。 当新用户需要sudo访问时，您现在可以使用以下命令以自己的登录名编辑sudoers文件：

```
sudo visudo

```

### 使用Sudo将命令列入白名单 [固定链接](#whitelisting-commands-with-sudo "固定链接")

在许多情况下，虽然您希望用户具有提升的sudo权限，但您也将希望遵循最小特权原则，并仅向sudo用户授予他们所需命令的访问权限。 在以下示例中，已对sudoers文件进行了编辑，以将sudo的使用限制为一些明确定义的命令：

|

```bash
1
2
3
4
5
6

```

 |

```bash
    # User privilege specification
    root    ALL=(ALL:ALL) ALL
    sudousername   ALL=(ALL:ALL) ALL
    username ALL=/usr/bin/top, /usr/bin/apt-get
    # Allow members of group sudo to execute the less, ls, and apt commands
    %sudo ALL=/usr/bin/less, /usr/bin/ls, /usr/bin/apt
```

 |

尽管root和 `sudousername` users仍然具有完全的超级用户权限，但 作为sudo用户 ，该用户 `username` 仅限于 `top` 和 `apt-get` 命令。 此外，加入到所有用户 `sudo` 组分别仅限于 `less` ， `ls` 和 `apt` 与须藤权限命令。 如果要向用户 `username` sudo访问该 `sudo` 组中 列入白名单的其他3个命令，则 只需将它们添加到该 `sudo` 组中，他们仍将保留自己的唯一权限，从而使他们对sudo的访问权限总计为5个命令。 可以根据需要为任意数量的用户和组重复此过程。

> **注意**
>
> 使用上述语法将单个命令列入白名单时，重要的是使用命令的绝对路径。 该 `which` 命令可用于找到此绝对路径：
>
> ```
> which command-name
>
> ```

### 与小组合作 [固定链接](#working-with-groups "固定链接")

Linux使用组来组织用户。 组主要是为了安全起见而组织帐户集合。 通过 `/etc/group` 文件 管理组成员资格的控制，该 文件显示了组及其成员的列表。 每个用户都有一个默认或主要组。 用户登录时，将为其主要组设置组成员身份。 这意味着，当用户启动程序或创建文件时，该文件和正在运行的程序都将与该用户的当前组成员身份相关联。 用户可以访问其他组中的其他文件，只要它们也是该组的成员并且已设置访问权限即可。 要运行程序或在其他组中创建文件，用户必须运行 `newgrp` 命令以切换其当前组。 newgrp命令的示例如下：

```
$ newgrp <marketing>

```

如果输入上述命令的用户是 文件中 **营销** 组 的成员 `/etc/group` ，则当前组成员身份将更改。 重要的是要注意，现在创建的所有文件都将与 **市场营销** 组而不是用户的主要组相关联。

### 创建和删除目录 [固定链接](#creating-and-removing-directories "固定链接")

要创建目录，请使用以下命令：

```
mkdir <directory name>

```

要创建目录并同时设置权限，请使用以下选项和语法：

```
mkdir -m a=rwx <directory name>

```

该 **\-m** 选项是短期的模式， **A = RWX** 意味着所有用户都具有读，写，并在该目录执行权限。 要查看mkdir命令的所有选项的完整列表，请 `man mkdir` 在命令提示符 下输入 。

要删除文件，请使用以下命令：

```
rm <file>

```

删除目录：

```
rm -r <directory name>

```

重要的是要注意，如果删除目录，其中的所有文件也将被删除。

### 更改目录和文件权限 [固定链接](#changing-directory-and-file-permissions "固定链接")

要查看文件许可权和文件和目录所有权，请使用 `ls -al` 命令。 该 `a` 选项用于显示隐藏文件或所有文件，该 `l` 选项用于长列表。 输出将类似于以下内容：

```
drwxr-xr-x 2 user user 4096 Jan  9 10:11 documents
-rw-r--r-- 1 user user  675 Jan  7 12:05 .profile
drwxr-xr-x 4 user user 4096 Jan  7 14:55 public

```

第一列包含十个字母和破折号，显示文件或目录的权限。 第二列（带有单个数字）指示目录中包含的文件或目录的数量。 接下来的列指示所有者，其后是组名，大小，日期和上次访问时间，最后是文件名。 例如，使用上面输出的第一行，详细信息如下：

```
`drwxr-xr-x` are the permissions
`2` is the number of files or directories
`user` is the owner
`user` is the group
`4096` is the size
`Jan  9 10:11` is the date/time of last access
`documents` is the directory

```

> **注意**
>
> 由于目录本身是文件，因此任何目录都将始终 `4096` 以其大小 显示 。 这不反映目录内容的大小。

### Chmod命令 [固定链接](#chmod-command "固定链接")

该命令 `chmod` 是更改模式的缩写。 Chmod用于更改文件和目录的权限。 该命令 `chmod` 可以与字母或数字（也称为八进制）一起使用以设置权限。 chmod使用的字母在下表中：

| 信 | 允许 |
| :-- | :-- |
| \[R | 读 |
| w | 写 |
| X | 执行 |
| X | 执行（仅当文件是目录时） |
| s | 在执行时设置用户或组ID |
| Ť | 将程序文本保存在交换设备上 |
| ü | 文件拥有者的当前权限 |
| G | 该文件对同一组用户的当前权限 |
| Ø | 文件对该组中其他人的当前权限 |

重要的是要记住，文件列表第一列的第一个字符表示它是目录还是文件。 其他九个字符是文件/目录的权限。 前三个字符用于用户，后三个字符用于组，后三个字符用于其他字符。 示例 **drwxrw\-r–** 分解如下：

> **d** 是目录
>
> **rwx** 用户具有读取，写入和执行权限
>
> **rw\-** 该组具有读取和写入权限
>
> **r –** 所有其他人都具有只读权限

请注意，破折号（\-）表示已删除权限。 因此，在“所有其他”组中，r转换为仅读取权限，因此删除了写入和执行权限。

相反，加号（+）等同于授予权限： `chmod u+r,g+x <filename>`

上面的示例翻译如下：

```
u is for user
r is for read
g is for group
x is for execute

```

换句话说，向用户授予了读取权限，并且向组授予了该文件的执行权限。 请注意，当为一个集合设置多个权限时，集合之间需要使用逗号。

### Chmod八进制格式 [固定链接](#chmod-octal-format "固定链接")

要使用八进制格式，必须计算文件或目录各部分的权限。 上面提到的前十个字符将对应八进制的四位数。 执行权限等于数字一（1），写权限等于数字二（2），读权限等于数字四（4）。 因此，当您使用八进制格式时，将需要为权限的每个部分计算一个介于0和7之间的数字。 下表提供了澄清表。

![权限的八进制格式。](https://www.linode.com/docs/tools-reference/linux-users-and-groups/1502-octal-format-clarified.png)

尽管八进制格式似乎很难理解，但是一旦掌握了要点，就很容易使用。 但是，使用r，w和x设置权限可能更容易。 下面是有关如何同时使用字母和八进制格式来设置文件或目录权限的示例。

> 示例语法： `chmod <octal or letters> <file/directory name>`
>
> 信函格式：（ `chmod go-rwx Work` 该群组和其他群组的Deny rwx权限）

上面的chmod命令后，ls \-al的输出如下所示：

```
dr-------- 2 user user 4096 Dec 17 14:38 Work

```

八进制格式： `chmod 444 Work`

上面的chmod命令之后的ls \-al输出将如下所示：

```
dr--r--r-- 2 user user 4096 Dec 17 14:38 Work

```

下表提供了一个八进制表，其中显示了等效的数字权限。

![数字权限表。](https://www.linode.com/docs/tools-reference/linux-users-and-groups/1487-numeric-permissions.png)

### 附加文件权限 [固定链接](#additional-file-permissions "固定链接")

除了最常见的读/写/执行文件权限外，还有一些其他有用的模式，特别是 *\+ t* 模式（ *sticky bit* ）和 *\+ s* 模式（ *setuid bit* ）。 这些功能描述了多用户情况下文件和可执行文件的行为。

在目录上设置时， *粘滞位* 或 *\+ t* 模式表示只有所有者（或根）可以删除或重命名该目录中的文件，而不管哪个用户通过组成员身份或所有权对目录具有写访问权。 当目录归一个组所有，多个用户通过该目录共享对给定文件集的写访问权时，此功能很有用。

重要的是要注意，在 *文件* 上设置粘性位 不会阻止对封闭目录具有写权限的用户删除或重命名文件\-粘性位必须在封闭 *目录* 上设置 。 在文件上设置粘滞位在现代Linux系统上不起作用。

要在名为的目录上设置粘性位 `/root/sticky` ，请发出以下命令：

```
chmod +t /root/sticky

```

要从文件或目录中删除粘性位，请使用 `chmod -t` 命令。 注意，要更改粘性位，您需要是root或文件/目录所有者。 无论粘性位的状态如何，root用户都将能够删除其中的目录和文件。

该 *setuid的* 位，或 *\+ S* ，设置文件时，允许具有权限的用户执行特定文件，运行与文件所有者的权限，该文件的能力。 例如，如果文件 `work` 归 `root` 用户和 `marketing` 组 所有，则 该 组的成员 `marketing` 可以 `work` 像是root用户一样 运行该 程序。 在某些情况下，这可能会带来潜在的安全风险，在接收到该 `+s` 标志 之前，应该对可执行文件进行适当的评估 。 要 `+s` 在名为的文件上 设置该 位 `/usr/bin/work` ，请发出以下命令：

```
chmod g+s /usr/bin/work

```

与 文件所有权 的 *\+ s* 模式 相反， *\+ s* 模式对目录的影响有些不同。 在 *\+ s* 目录中 创建*的* 文件将获得该目录的用户和组的所有权，而不是创建该文件及其默认组的用户的所有权。 要 在目录上 设置 *setguid* （组ID）选项，请使用以下命令：

```
chmod g+s /var/doc-store/

```

要 为名为的目录 设置 *setuid* （用户ID） `/var/doc-store` ，请发出以下命令：

```
chmod u+s /var/doc-store/

```

### 更改文件所有权 [固定链接](#changing-file-ownership "固定链接")

默认情况下，所有文件都由创建它们的用户和该用户的默认组“拥有”。 要更改文件的所有权，请使用 `chown` 以下 `chown user:group /path/to/file` 格式 的 命令 。 在以下示例中，“ list.html”文件的所有权将更改为“市场营销”组中的“ cjones”用户：

```
chown cjones:marketing list.html

```

要更改目录和其中包含的所有文件的所有权，请使用带有 `-R` 标志 的递归选项 。 在以下示例中，将“所有者 `/srv/smb/leadership/` ” 的所有权更改 为“市场营销”组中的“ cjones”用户：

```
chown -R cjones:marketing /srv/smb/leadership/

```

## 利用用户和组 [固定链接](#leveraging-users-and-groups "固定链接")

在许多情况下，用户权限用于在没有任何直接交互的情况下为您的系统提供更高的安全性。 在安装过程中，许多操作系统都会为不同的软件包创建特定的系统用户帐户。

最佳做法是为每个用户提供自己的登录名。 这样可以保护每个用户的文件免受所有其他用户的攻击。 此外，为用户使用特定帐户可以实现更准确的系统日志记录，尤其是在与之类的工具结合使用时 `sudo` 。 我们建议避免这样的情况，即一个以上的人都知道一个用户帐户的密码，以实现最大的安全性。

相反，组对于允许多个独立用户帐户进行协作和共享文件很有用。 如果您在计算机上为每个任务（例如Web编辑器，贡献者，内容提交者，支持人员）创建用于常见任务的组，并将相关用户添加到相关组中，则这些用户都可以编辑和运行同一组文件而无需与世界分享这些文件。 使用 `chown` 文件权限为770和740 的 命令将有助于实现此目标。

## 更多信息 [固定链接](#more-information "固定链接")

您可能希望参考以下资源以获取有关此主题的其他信息。 虽然提供这些内容是希望它们会有用，但请注意，我们不能保证外部托管材料的准确性或及时性。

*   [Linux中的用户和组管理@ DebianAdmin](http://www.debianadmin.com/users-and-groups-administration-in-linux.html)
*   [在线Chmod计算器](http://www.onlineconversion.com/html_chmod_calculator.htm)