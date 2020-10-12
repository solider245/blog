---
title: 如何在Linux系统上创建硬链接和软链接（符号链接）
date: 2020-10-12 12:09:51
permalink: /pages/116dc3/
categories:
  - 常用命令
  - 软连接与硬链接
tags:
  - 
---
在任何基于Linux / Unix的操作系统中，很多时候理解其基本概念是明智的，然后只有一个人才能体会到命令的美妙之处以及如何实现它们。

如果我们事先对这些命令和相关概念有所了解，那么一些小细节将对我们在调试和故障排除许多具有挑战性的情况方面大有帮助。

[![硬-软件-链接-Linux](https://www.linuxtechi.com/wp-content/uploads/2019/02/Hard-Soft-Links-Linux.jpg)](https://www.linuxtechi.com/wp-content/uploads/2019/02/Hard-Soft-Links-Linux.jpg)

在本主题中，我将介绍什么是链接，不同类型，区分字符以及如何更好地将它们与所需的概念一起使用。

[![HardLink-SoftLink-Linux之间的差异](https://www.linuxtechi.com/wp-content/uploads/2019/02/Difference-between-HardLink-SoftLink-Linux.jpg)](https://www.linuxtechi.com/wp-content/uploads/2019/02/Difference-between-HardLink-SoftLink-Linux.jpg)

通过执行“ man ln”命令，您可以看到它说的是“在文件之间建立链接”，而不是关于软链接或硬链接。

shashi@linuxtechi ~}$ man ln

同样，命令“ man link”被描述为“创建文件的调用链接功能”。

#### 软链接：

顾名思义，软链接只是创建到新文件的新链接。 在这种情况下，新文件的索引节点号将指向旧文件。

[![软链接图](https://www.linuxtechi.com/wp-content/uploads/2019/02/SoftLink-Figure.jpg)](https://www.linuxtechi.com/wp-content/uploads/2019/02/SoftLink-Figure.jpg)

#### 硬链接：

在这种情况下，旧文件和新文件都将指向相同的inode号。

[![硬链接图](https://www.linuxtechi.com/wp-content/uploads/2019/02/HardLink-Figure.jpg)](https://www.linuxtechi.com/wp-content/uploads/2019/02/HardLink-Figure.jpg)

#### 符号链接：

在某些Unix / Linux版本中，符号链接和软链接都被视为相同。 但是实际的区别在于，新文件和旧文件的索引号都将指向新的索引号。 这将完全取决于实现。

[![SymbolicLink图](https://www.linuxtechi.com/wp-content/uploads/2019/02/SymbolicLink-Figure.jpg)](https://www.linuxtechi.com/wp-content/uploads/2019/02/SymbolicLink-Figure.jpg)

**注1** ：\-在许多情况下，符号和软链接术语可以互换使用。 但是必须知道何时使用什么。

**使用“ ln”命令创建硬链接和软链接**

#### 创建硬链接

**1）** “ man ln”命令将提供以下输出。

shashi@linuxtechi ~}$ man ln
ln  \- make links between files

**2）** 如果传递不带任何参数的“ ln”命令，则会引发“缺少文件操作数”错误。

shashi@linuxtechi ~}$ln
ln: missing file operand
Try 'ln \-\-help' for more information.

**3）** 在两个文件之间创建硬链接。 首先检查任何现有文件（如果有），否则重新创建一个或多个文件，然后链接它们。 以下是分步方法，

shashi@linuxtechi ~}$ ls \-la
total 24
drwx\-\-\-\-\-\-  4 root root 4096 Feb  6 15:23 .
drwxr\-xr\-x 23 root root 4096 Jan 25 16:39 ..
\-rw\-r\-\-r\-\-  1 root root 3122 Jan 25 16:41 .bashrc
drwx\-\-\-\-\-\-  2 root root 4096 Feb  6 15:23 .cache
\-rw\-r\-\-r\-\-  1 root root    0 Jan 25 16:41 .hushlogin
\-rw\-r\-\-r\-\-  1 root root  148 Aug 17  2015 .profile
drwxr\-xr\-x  2 root root 4096 Jan 25 16:41 .ssh

**i）**   使用“ touch”命令创建文件

shashi@linuxtechi ~}$ touch 123.txt
shashi@linuxtechi ~}$ ls \-l
total 0
\-rw\-r\-\-r\-\- 1 root root 0 Feb  6 15:51 123.txt

**ii）** 使用“ cat”命令将内容输入文件，然后单击“ ctrl + c”以保存并退出。

shashi@linuxtechi ~}$ cat > 123.txt
Welcome to this World!
^C

**iii）** 在文件“ 123.txt”和“ 321.txt”之间创建硬链接。 在这种情况下，“ 123.txt”已经存在，内容为“欢迎来到这个世界”。

shashi@linuxtechi ~}$ ln 123.txt 321.txt
shashi@linuxtechi ~}$ ls \-l
total 8
\-rw\-r\-\-r\-\- 2 root root 23 Feb  6 15:52 123.txt
\-rw\-r\-\-r\-\- 2 root root 23 Feb  6 15:52 321.txt

**iv）** 检查文件的索引节点号。 这两个文件的inode编号都相同，即794583。还要检查新文件“ 321.txt”的内容，该文件也与“ 123.txt”相同。

shashi@linuxtechi ~}$ ls \-li
total 8
794583 \-rw\-r\-\-r\-\- 2 root root 23 Feb  6 15:52 123.txt
794583 \-rw\-r\-\-r\-\- 2 root root 23 Feb  6 15:52 321.txt
$ cat 321.txt
Welcome to this World!

**注2** ：\-索引节点号是为在Linux / unix操作系统中创建的任何文件生成的唯一索引号。 这些索引节点号存储在/ proc目录中的目录/文件属性中。 但是在链接的情况下，这些索引节点号是黑白共享文件，并且文件表中仅路径被更新。

**v）再** 创建一个名为“ 456.txt”的文件，并使用ln命令将该文件链接到“ 321.txt”。 现在，所有三个文件都具有相同的inode编号。 “ 456.txt”的内容将与原始文件的内容相同。

shashi@linuxtechi ~}$  ls \-li
total 12
794583 \-rw\-r\-\-r\-\- 3 root root 23 Feb  6 15:52 123.txt
794583 \-rw\-r\-\-r\-\- 3 root root 23 Feb  6 15:52 321.txt
794583 \-rw\-r\-\-r\-\- 3 root root 23 Feb  6 15:52 456.txt
$ cat 456.txt
Welcome to this World!
shashi@linuxtechi ~}$   ls \-l
total 12
\-rw\-r\-\-r\-\- 3 root root 23 Feb  6 15:52 123.txt
\-rw\-r\-\-r\-\- 3 root root 23 Feb  6 15:52 321.txt
\-rw\-r\-\-r\-\- 3 root root 23 Feb  6 15:52 456.txt

**vi）**  删除源文件或任何这些文件时，不会影响其他文件。 可以使用“ rm”命令删除源文件。 其他文件的内容也不会有任何影响。

shashi@linuxtechi ~}$ rm 123.txt
shashi@linuxtechi ~}$ ls \-l
total 8
\-rw\-r\-\-r\-\- 2 root root 23 Feb  6 15:52 321.txt
\-rw\-r\-\-r\-\- 2 root root 23 Feb  6 15:52 456.txt
shashi@linuxtechi ~}$ ls \-li
total 8
794583 \-rw\-r\-\-r\-\- 2 root root 23 Feb  6 15:52 321.txt
794583 \-rw\-r\-\-r\-\- 2 root root 23 Feb  6 15:52 456.txt
shashi@linuxtechi ~}$ cat 456.txt
Welcome to this World!

**vii）** 不允许跨目录创建硬链接。

shashi@linuxtechi ~}$ls \-l
total 8
\-rw\-r\-\-r\-\- 2 root root 23 Feb  6 15:52 321.txt
\-rw\-r\-\-r\-\- 2 root root 23 Feb  6 15:52 456.txt
shashi@linuxtechi ~}$ mkdir abc
shashi@linuxtechi ~}$ ln abc def
ln: abc: hard link not allowed for directory

**viii）** 对一个文件内容的任何更改都会影响并相应更改另一个文件的内容，以下是解释的步骤，

shashi@linuxtechi ~}$ vi 321.txt
Welcome to this World!
You are welcomed to this new world
:wq
shashi@linuxtechi ~}$ ls \-l
total 12
\-rw\-r\-\-r\-\- 2 root root   59 Feb  6 16:24 321.txt
\-rw\-r\-\-r\-\- 2 root root   59 Feb  6 16:24 456.txt
drwxr\-xr\-x 2 root root 4096 Feb  6 16:18 abc
shashi@linuxtechi ~}$ cat 456.txt
Welcome to this World!
You are welcomed to this new world

#### 创建软链接：

**1） ** 使用“ touch”命令创建文件“ src.txt”，然后使用cat命令将内容输入为“ Hello World”，然后单击“ ctrl + c”进行保存并退出。

shashi@linuxtechi ~}$ touch src.txt
shashi@linuxtechi ~}$ cat > src.txt
Hello World
^C
shashi@linuxtechi ~}$ ls \-l
total 4
\-rw\-r\-\-r\-\- 1 root root 12 Feb  6 16:32 src.txt

**2）**   将目标文件创建为“ dst.txt”，并使用“ ln \-s”命令行选项创建符号链接（也称为软链接）。 检查“ dst.txt”文件的内容，可以看到与“ src.txt”相同的内容。

shashi@linuxtechi ~}$ ln \-s src.txt dst.txt
shashi@linuxtechi ~}$  ls \-l
total 4
lrwxrwxrwx 1 root root  7 Feb  6 16:33 dst.txt \-> src.txt
\-rw\-r\-\-r\-\- 1 root root 12 Feb  6 16:32 src.txt
shashi@linuxtechi ~}$  cat dst.txt
Hello World

**3）**   对于符号链接，源文件和目标文件的索引节点号不同。 同样，在权限字母中出现“ l”，表示这些是链接。 “ dst.txt–> src.txt”将是现在建立的新链接。

shashi@linuxtechi ~}$  ls \-li
total 4
794584 lrwxrwxrwx 1 root root  7 Feb  6 16:33 dst.txt \-> src.txt
794583 \-rw\-r\-\-r\-\- 1 root root 12 Feb  6 16:32 src.txt

**4）** 允许目录的符号创建。 在以下步骤中对此进行了解释

shashi@linuxtechi ~}$ mkdir abc
shashi@linuxtechi ~}$ ln \-s abc def
$ ls \-l
total 8
drwxr\-xr\-x 2 root root 4096 Feb  6 16:34 abc
lrwxrwxrwx 1 root root    3 Feb  6 16:34 def \-> abc
lrwxrwxrwx 1 root root    7 Feb  6 16:33 dst.txt \-> src.txt
\-rw\-r\-\-r\-\- 1 root root   12 Feb  6 16:32 src.txt

**5）** 所有文件/目录的索引节点号（源和目标不同）

shashi@linuxtechi ~}$  ls \-li
total 8
794585 drwxr\-xr\-x 2 root root 4096 Feb  6 16:34 abc
794586 lrwxrwxrwx 1 root root    3 Feb  6 16:34 def \-> abc
794584 lrwxrwxrwx 1 root root    7 Feb  6 16:33 dst.txt \-> src.txt
794583 \-rw\-r\-\-r\-\- 1 root root   12 Feb  6 16:32 src.txt

**6）** 如前所述，可以为目录创建符号链接。 一旦创建了这些带有符号链接的目录，就可以在这些目录内创建文件。 这将使它现在变得更有趣。 在源目录中创建文件时，目标目录中也会反映这些文件。 以下步骤清楚地说明了这一点。

shashi@linuxtechi ~}$ $ cd abc
shashi@linuxtechi ~}$  touch 123.txt
shashi@linuxtechi ~}$  vi 123.txt
Hello
:wq!
shashi@linuxtechi ~}$  touch 456.txt
shashi@linuxtechi ~}$  cd ..
shashi@linuxtechi ~}$  ls \-l
total 8
drwxr\-xr\-x 2 root root 4096 Feb  6 16:36 abc
lrwxrwxrwx 1 root root    3 Feb  6 16:34 def \-> abc
lrwxrwxrwx 1 root root    7 Feb  6 16:33 dst.txt \-> src.txt
\-rw\-r\-\-r\-\- 1 root root   12 Feb  6 16:32 src.txt
shashi@linuxtechi ~}$ cd def
shashi@linuxtechi ~}$ ls \-l
total 4
\-rw\-r\-\-r\-\- 1 root root 6 Feb  6 16:37 123.txt
\-rw\-r\-\-r\-\- 1 root root 0 Feb  6 16:36 456.txt
shashi@linuxtechi ~}$ cat 123.txt
Hello

**注意3** ：\-我们可以有任意数量的嵌套链接。 但是创建这些符号链接的用户/管理员应意识到这些事实会导致混淆。 有时可能会被遗忘，并可能导致不良结果。 因此，他们必须小心。

**注意4** ：\-有一些“符号”或“软”链接指向不存在的链接的可能性。 这称为“悬空链接”。 这将指向无处。

**注意5** ：\-在linux / unix中使用系统调用在编程级别（使用系统级别的C / C ++程序）创建符号或硬链接。 这些是1）symlink 2）symlinkat。

这些不应与我上面描述的命令行实用程序混淆。

#### 删除软链接/符号链接

使用'rm'和unlink命令删除软链接或符号链接。

句法：

＃rm <软链接文件名>

＃取消链接<soft\-link\-filename>

删除软链接目录

句法：

＃rm <软链接目录>

＃取消链接<soft\-link\-directory>

**结论：**

创建硬链接或软链接都将对管理员和开发人员非常有帮助。 在了解我们正在创建的链接类型及其帮助方式的同时，上述参考资料将非常有用。 此外，本文还将有助于理解链接的差异和利用。