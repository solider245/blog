---
title: Linux中的Chown命令（文件所有权)
date: 2020-10-12 12:09:51
permalink: /pages/1e8788/
categories:
  - 常用命令
  - chown命令
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 17:54:22
 * @LastEditTime: 2020-07-17 17:54:23
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\常用命令\chown命令\Linux中的Chown命令（文件所有权).md
 * @日行一善，每日一码
--> 
该 `chown` 命令允许您更改给定文件，目录或符号链接的用户和/或组所有权。

在Linux中，所有文件都与一个所有者和一个组相关联，并为文件所有者，组成员和其他人分配了权限访问权限。

在本教程中，我们将 `chown` 通过实际示例 向您展示如何使用该 命令。

## 如何使用 `chown` [＃](#how-to-use-chown)

在开始使用 `chown` 命令之前，让我们先回顾一下基本语法。

该 `chown` 命令表达式采用以下形式：

```sh
chown [OPTIONS] USER[:GROUP] FILE(s)

```

复制

`USER` 是新所有者的用户名或用户ID（UID）。 `GROUP` 是新组的名称或组ID（GID）。 `FILE(s)` 是一个或多个文件，目录或链接的名称。 数字ID应该以 `+` 符号 为前缀 。

*   `USER` \-如果仅指定用户，则指定的用户将成为给定文件的所有者，组所有权不会更改。
*   `USER:` \-当用户名后跟冒号 `:` ，并且未提供组名时，用户将成为文件的所有者，并且文件组的所有权更改为用户的登录组。
*   `USER:GROUP` \-如果同时指定了用户和组（在它们之间没有空格），则文件的用户所有权更改为给定的用户，而组所有权更改为给定的组。
*   `:GROUP` \-如果省略了User且该组以冒号作为前缀 `:` ，则仅文件的组所有权更改为给定的组。
*   `:` 如果仅 `:` 给出 一个冒号 ，而不指定用户和组，则不会进行任何更改。

默认情况下，成功时 `chown` 不产生任何输出并返回零。

使用 [`ls -l`](https://linuxize.com/post/how-to-list-files-in-linux-using-the-ls-command/) 命令查找谁拥有文件或文件所属的组：

```
ls -l filename.txt
```

```output
-rw-r--r-- 12 linuxize users 12.0K Apr  8 20:51 filename.txt
|[-][-][-]-   [------] [---]
                |       |
                |       +-----------> Group
                +-------------------> Owner

```

普通用户只有在拥有文件的情况下才能更改文件组，并且只能更改为他们所属的组。 管理用户可以更改所有文件的组所有权。

## 如何更改文件的所有者 [＃](#how-to-change-the-owner-of-a-file)

要更改文件的所有者，请使用 `chown` 命令，后跟新所有者的用户名和目标文件作为参数：

```sh
chown USER FILE

```

复制

例如，以下命令会将名为的文件的所有权更改为名为 `file1` 的新所有者 `linuxize` ：

```
chown linuxize file1
```

要更改多个文件或目录的所有权，请将它们指定为以空格分隔的列表。 下面的命令将名为 `file1` 和目录 的文件的所有权更改为名为 `dir1` 的新所有者 `linuxize` ：

```
chown linuxize file1 dir1
```

可以使用数字用户ID（UID）代替用户名。 以下示例将把文件的所有权更改为 `file2` UID为的新所有者 `1000` ：

```
chown 1000 file2
```

如果数字所有者作为用户名存在，则所有权将转移到用户名。 为了避免在ID前面加上前缀 `+` ：

```
chown 1000 file2
```

## 如何更改文件的所有者和组 [＃](#how-to-change-the-owner-and-group-of-a-file)

要更改文件的所有者和组，请使用 `chown` 命令，然后是新的所有者和组，并用冒号（ `:` ） 分隔， 中间没有空格和目标文件。

```sh
chown USER:GROUP FILE

```

复制

以下命令会将名为的文件的所有权更改为 `file1` 名为 `linuxize` 和组 的新所有者 `users` ：

```
chown linuxize:users file1
```

如果在冒号（ `:` ） 后面省略组名 ，则文件组将更改为指定用户的登录组：

```
chown linuxize: file1
```

## 如何更改文件组 [＃](#how-to-change-the-group-of-a-file)

要仅更改文件的组，请使用以下 `chown` 命令，后跟冒号（ `:` ）和新的组名（它们之间没有空格），并将目标文件作为参数：

```sh
chown :GROUP FILE

```

复制

以下命令将更改名为文件的所属组 `file1` 到 `www-data` ：

```
chown :www-data file1
```

可以用来更改文件组所有权的另一个命令是 [`chgrp`](https://linuxize.com/post/chgrp-command-in-linux/) 。

## 如何更改符号链接的所有权 [＃](#how-to-change-symbolic-links-ownership)

当不使用递归选项时， `chown` 命令将更改符号链接指向的文件的组所有权，而不是 [符号链接](https://linuxize.com/post/how-to-create-symbolic-links-in-linux-using-the-ln-command/) 本身。

例如，如果您尝试更改所有者和 `symlink1` 指向 的符号链接的组 `/var/www/file1` ， `chown` 则将更改 符号链接 指向 的文件或目录的所有权：

```
chown www-data: symlink1
```

很有可能您会收到“无法取消引用'symlink1'：权限被拒绝”错误，而不是更改目标所有权。

发生该错误是因为默认情况下，大多数Linux发行版上的符号链接均受保护，并且您无法对目标文件进行操作。 此选项在中指定 `/proc/sys/fs/protected_symlinks` 。 `1` 表示启用和 `0` 禁用。 我们建议不要禁用符号链接保护。

要更改符号链接本身的组所有权，请使用以下 `-h` 选项：

```
chown -h www-data symlink1
```

## 如何递归更改文件所有权 [＃](#how-to-recursively-change-the-file-ownership)

要对给定目录下的所有文件和目录进行递归操作，请使用 `-R` （ `--recursive` ）选项：

```sh
chown -R USER:GROUP DIRECTORY

```

复制

以下示例将目录下所有文件和子目录的所有权更改 `/var/www` 为名为的新所有者和组 `www-data` ：

```
chown -R www-data: /var/www
```

如果目录包含符号链接，请传递以下 `-h` 选项：

```
chown -hR www-data: /var/www
```

递归更改目录所有权时可以使用的其他选项是 `-H` 和 `-L` 。

如果传递给 `chown` 命令 的参数 是指向目录的符号链接，则该 `-H` 选项将导致命令遍历该目录。 `-L` 告诉 `chown` 遍历每个符号链接到遇到的目录。 通常，您不应使用这些选项，因为这可能会破坏系统或造成安全风险。

## 使用参考文件 [＃](#using-a-reference-file)

该 `--reference=ref_file` 选项使您可以将给定文件的用户和组所有权更改为与指定参考文件（ `ref_file` ）相同。 如果参考文件是符号链接， `chown` 则将使用目标文件的用户和组。

```sh
chown --reference=REF_FILE FILE

```

复制

例如，以下命令将的用户和组所有权分配 `file1` 给 `file2`

```
chown --reference=file1 file2
```

## 结论 [＃](#conclusion)

`chown` 是用于更改文件的用户和/或组所有权的Linux / UNIX命令行实用程序。

要了解有关该 `chown` 命令的 更多信息， 请访问 [chown手册](https://linux.die.net/man/1/chown) 页或 `man chown` 在终端中 键入 。

如果您有任何疑问或反馈，请随时发表评论。