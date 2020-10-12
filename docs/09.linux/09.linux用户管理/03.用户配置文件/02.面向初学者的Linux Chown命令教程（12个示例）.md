---
title: 面向初学者的Linux Chown命令教程（12个示例）
date: 2020-10-12 12:09:51
permalink: /pages/27f9ca/
categories:
  - linux用户管理
  - 用户配置文件
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 17:52:20
 * @LastEditTime: 2020-07-17 17:52:20
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\用户配置文件\面向初学者的Linux Chown命令教程（12个示例）.md
 * @日行一善，每日一码
--> 
在Linux中，有时您可能想更改文件或目录的所有者和与组有关的信息。 如果您是命令行新手，并且想知道如何通过命令行进行此类更改，那么您将很高兴知道存在一个名为 **chown** 的命令，该命令 可以使您执行此操作。

在开始chown命令教程之前，值得一提的是，这里提到的所有示例和说明已在Ubuntu 18.04 LTS和Debian 10上进行了测试。

## Linux chown命令说明

如开头所述，chown命令可让您通过命令行更改文件所有者和组。 以下是命令的通用语法：

```
chown [OPTION]... [OWNER][:[GROUP]] FILE...
```

这是该工具的手册页对此的说明：

```
If only  an  owner  (a user  name or numeric user ID) is given, that user is made the owner of eachgiven file, and the files' group is not changed.  If the owner  is followed  by  a  colon  and a group name (or numeric group ID), with no spaces between them, the group ownership of the  files  ischanged  as well.  If a colon but no group name follows the user name, that user is made the owner of the files and the group of the files  is  changed  to that  user's  login  group. If the colon and group are given, but the owner is omitted, only the group of the files is changed; in this case,chown  performs  the same function as chgrp.  If only a colon is given, or if the entire operand is empty, neither the owner nor the  group  is changed.
```

以下Q＆A类型的示例将使您很好地了解chown命令的工作方式：

## Q1。 如何更改文件的所有者？

考虑以下示例：

[![](https://www.howtoforge.com/images/linux_chown_command/chown-fileowner-group.png?ezimgfmt=rs:471x35/rscb1/ng:webp/ngcb1)](https://www.howtoforge.com/images/linux_chown_command/big/chown-fileowner-group.png)

在这里，文件的所有者是“ himanshu”，它所属的组也是“ himanshu”。 现在，要将所有者更改为“ root”，请使用以下命令：

```
chown root file1
```

以下屏幕截图确认了所有者现已更改为“ root”。

[![](https://www.howtoforge.com/images/linux_chown_command/chown-user-changed.png?ezimgfmt=rs:434x36/rscb1/ng:webp/ngcb1)](https://www.howtoforge.com/images/linux_chown_command/big/chown-user-changed.png)

## Q2。 如何更改文件组？

更改组类似于更改所有者。 唯一的区别在于命令的语法，如下所示：

```
chown :[group-name] [file-name]
```

因此，假设要求是将“ file1”的组更改为“ root”。 那么命令将是：

```
chown :root file1
```

以下屏幕截图显示了该组已成功从“ himanshu”更改为“ root”。

[![](https://www.howtoforge.com/images/linux_chown_command/chown-group-changed.png?ezimgfmt=rs:443x87/rscb1/ng:webp/ngcb1)](https://www.howtoforge.com/images/linux_chown_command/big/chown-group-changed.png)

***注意**：如果您想知道为什么使用'sudo'命令，或者如果您不熟悉'sudo'，则应该首先 [阅读](https://www.howtoforge.com/tutorial/sudo-beginners-guide/)此工具[的教程](https://www.howtoforge.com/tutorial/sudo-beginners-guide/)。*

## Q3。 如何同时更改文件的所有者和组？

要更改文件的所有者和组，请使用以下语法：

```
chown [new-owner]:[new-group] [file-name]
```

因此，在本例中，要将现有所有者和组从“ root”更改为“ himanshu”，我们将使用以下命令：

```
chown himanshu:himanshu file1
```

以下屏幕截图显示了上面的命令：

[![](https://www.howtoforge.com/images/linux_chown_command/chown-change-owner-group.png?ezimgfmt=rs:500x79/rscb1/ng:webp/ngcb1)](https://www.howtoforge.com/images/linux_chown_command/big/chown-change-owner-group.png)

## Q4。 检查现有所有者/组后如何更改所有者或组（或两者）？

在某些情况下，您可能需要先进行交叉检查，然后再进行文件的现有所有者/组的检查。 因此，对于这些情况，可以使用 **\-\-from** 命令行选项。 此选项要求您提及要验证的所有者/组名称。 广告

```
chown --from=[curr-own]:[curr-group] [new-owner]:[new-group] [filename]
```

例如：

```
chown --from=root:himanshu himanshu:root file1
```

上面的命令将检查现有所有者是否为“ root”，组是否为“ himanshu”。 如果是，则所有者将更改为“ himanshu”，而组将变为“ root”。

## Q5。 如何从参考文件中选择所有者/组信息？

在某些情况下，您可能希望chown从文件中提取所有者和与组有关的信息，而不是在命令行上手动输入。 对于这些情况，可以使用 **\-\-reference** 命令行选项。 此选项要求您输入参考文件的名称。

```
chown --reference=[ref-file-name] [filename]
```

例如：

```
chown --reference=file2 file1
```

因此，以上命令会将所有者和组信息从file2复制到file1。 广告

## Q6。 如何使chown递归地处理文件和目录？

要使chown命令对文件和目录进行递归操作，请使用 **\-R** 命令行选项。

```
chown -R [new-owner]:[new-group] [directory-name-or-path]
```

对于那些不知道的人，递归意味着将对给定目录中的所有文件以及所有子目录中的文件和目录执行该操作。

## Q7。 如何使chown抑制错误消息？

有时您运行的chown命令会出现错误。 例如，以下命令在我的系统上执行时：

```
chown --from=himanshu:himanshu himanshu:root file4
```

给出以下错误：

```
chown: cannot access 'file4': No such file or directory
```

[![](https://www.howtoforge.com/images/linux_chown_command/chown-error-message.png?ezimgfmt=rs:500x26/rscb1/ng:webp/ngcb1)](https://www.howtoforge.com/images/linux_chown_command/big/chown-error-message.png)

现在假设要求是该工具不应显示此类错误。 然后，可以使用 **\-f** 命令行选项 使之成为可能 。

[![](https://www.howtoforge.com/images/linux_chown_command/chown-supress-error.png?ezimgfmt=rs:500x37/rscb1/ng:webp/ngcb1)](https://www.howtoforge.com/images/linux_chown_command/big/chown-supress-error.png)

前面的屏幕快照确认 **\-f** 命令行选项可以抑制错误/警告。

## Q8。 如何将组所有权更改为指定用户的登录组？

可以使用 **\[user / owner\]：** 语法来完成。 例如，以下命令：

```
chown himanshu: file1
```

将确保所有权已授予“ himanshu”，并且该组将更改为“ himanshu”的登录组。 请注意，这与不使用冒号（:)的情况不同，因为在这种情况下（在上面的第一季度中进行了解释），组保持不变。

这里值得一提的另一件事是，如果仅使用冒号（:)而未指定所有者或组，则不会进行任何更改。 例如：

```
chown : file1
```

该命令对文件的用户或组所有权均无效。

## Q9。 chown如何与符号链接一起工作？

默认情况下，如果您尝试更改符号链接的用户和组所有权，则不会进行任何更改。 相反，它链接到的文件将获得这些更改。

例如，下面的屏幕快照显示我创建了一个符号链接“ link1”，其用户和组所有权设置为“ himanshu”。 然后，我执行chown命令将用户和组更改为“ root”。 但是该命令对符号链接文件没有影响\-而是更改了用户和组所有权的“ file1”（符号链接指向该文件）。

[![Chown命令符号链接](https://www.howtoforge.com/images/linux_chown_command/chown-sym-links.png?ezimgfmt=rs:500x164/rscb1/ng:webp/ngcb1)](https://www.howtoforge.com/images/linux_chown_command/big/chown-sym-links.png)

但是，如果需要，可以使用\-h选项覆盖此默认行为。

## Q10。 如何更改目录的所有者和组？

就像处理文件一样。 以下是一个示例：

```
chown root:root ./test-dir/
```

请注意，您可以使用 [stat](https://www.howtoforge.com/linux-stat-command/) 命令 交叉验证目录的所有者和组更改 \-输出中的UID和GID字段显示用户名和组名。

例如，在我的案例中，输出清楚地显示了更改的用户组所有权。

```
  File: test-dir  Size: 4096          Blocks: 8          IO Block: 4096   directoryDevice: 808h/2056d    Inode: 11928001    Links: 2Access: (0755/drwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)Access: 2018-08-07 10:31:04.867467573 +0530Modify: 2018-08-07 10:30:53.651807123 +0530Change: 2018-08-07 10:32:49.644427930 +0530 Birth: -
```

请注意，如果要进行递归更改（请参阅“问答”中的\-R选项），并且正在处理符号链接，则可以使用以下选项：

```
       The following options modify how a hierarchy is traversed when  the  -R       option  is  also  specified.   If  more than one is specified, only the       final one takes effect.       -H     if a command line argument is a symbolic link  to  a  directory,              traverse it       -L     traverse every symbolic link to a directory encountered       -P     do not traverse any symbolic links (default)
```

## Q11。 可以使用UID和GID代替用户名和组名吗？

是的，您可以使用用户ID和组ID代替名称。 该命令的语法仍然相同。

例如：

```
chown 1000:1000 file1
```

上面的命令会将用户和组所有权更改为UID为1000的用户和GID为1000的用户。

## Q12。 如何在输出中使chown显示操作的详细信息？

如果要让chown命令显示其执行的操作的详细信息，请使用\-v命令行选项。

例如，此命令：

```
sudo chown himanshu:himanshu link1 -v
```

产生以下输出：

```
changed ownership of 'link1' from root:root to himanshu:himanshu
```

现在，还有另一个选项\-c也和\-v一样，只是当没有任何更改时它不显示任何细节。

## 结论

正如大多数人可能会同意的那样，chown命令并不难使用。 更好的是， [该工具的手册页](https://linux.die.net/man/1/chown) 包含了许多可能对用户（尤其是新手）有帮助的详细信息。 尝试我们在这里说明的示例，对于其余的功能/选项，请参阅chown手册页。 如有任何疑问或疑问，请在下面留下评论。