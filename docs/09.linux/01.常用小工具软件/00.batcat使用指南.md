---
title: batcat使用指南
date: 2020-10-12 12:09:51
permalink: /pages/05d39d/
categories:
  - linux
  - 常用小工具软件
tags:
  - 
---
# bat Linux命令–用Rust编写的cat克隆

最近更新时间 2020年5月18日 在 分类目录 [命令行技巧](https://www.cyberciti.biz/topics/open-source/command-line-hacks/) ， [Howto](https://www.cyberciti.biz/topics/howto/) ， [开源](https://www.cyberciti.biz/topics/open-source/)

Ť 他 [的猫（concatenate的简写）命令](https://www.cyberciti.biz/faq/linux-unix-appleosx-bsd-cat-command-examples/ "Linux / Unix中的cat命令示例
") 是Linux和最经常使用的灵活的命令类Unix操作系统之一。 向bat Linux命令打个招呼，这是用Rust编程语言编写的cat命令。 bat命令带有语法高亮显示，git集成，并且可以直接用作替换cat命令。 让我们看看如何在Linux和Unix系统上安装bat以获取乐趣和收益。

广告

## 向bat Linux命令打个招呼

让我们看看bat命令的一些很酷的功能：

1.  **语法突出显示** – Bat支持针对大量编程和标记语言的语法突出显示。
2.  **Git集成** – Bat与git通信以在左侧显示修改。
3.  **自动分页** –如果输出对于一个屏幕来说太大，则该命令可以将其自身的输出通过管道传递给更少的管道。
4.  显示并突出显示不可打印的字符。
5.  用户友好的命令行界面。
6.  当然，对于文件串联，包括所有 [cat命令](https://www.cyberciti.biz/faq/linux-unix-appleosx-bsd-cat-command-examples/ "有关更多信息，请参见Linux / Unix cat命令示例。") 功能。

## 安装

我们需要使用系统软件包管理器。 让我们看一些著名的Linux发行示例来安装bat命令。 首先打开终端应用程序，然后根据您的操作系统键入命令。

### 在Ubuntu和Debian Linux上安装bat

只需运行以下 [apt命令](https://www.cyberciti.biz/faq/ubuntu-lts-debian-linux-apt-command-examples/ "有关更多信息，请参见Linux / Unix apt命令示例。") / [apt\-get命令](https://www.cyberciti.biz/tips/linux-debian-package-management-cheat-sheet.html "有关更多信息，请参见Linux / Unix apt-get命令示例。") ：
`$ sudo apt install bat`

\[sudo\] password for vivek:
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following additional packages will be installed:
  libgit2\-28 libhttp\-parser2.9 libmbedcrypto3 libmbedtls12 libmbedx509\-0
The following NEW packages will be installed:
  bat libgit2\-28 libhttp\-parser2.9 libmbedcrypto3 libmbedtls12 libmbedx509\-0
0 upgraded, 6 newly installed, 0 to remove and 4 not upgraded.
Need to get 2,274 kB of archives.
After this operation, 6,279 kB of additional disk space will be used.
Do you want to continue? \[Y/n\] y
Get:1 http://archive.ubuntu.com/ubuntu focal/universe amd64 libhttp\-parser2.9 amd64 2.9.2\-2 \[21.8 kB\]
Get:2 http://archive.ubuntu.com/ubuntu focal/universe amd64 libmbedcrypto3 amd64 2.16.4\-1ubuntu2 \[150 kB\]
...
Fetched 2,274 kB in 4s (583 kB/s)
Selecting previously unselected package libhttp\-parser2.9:amd64.
(Reading database ... 285273 files and directories currently installed.)
Preparing to unpack .../0\-libhttp\-parser2.9\_2.9.2\-2\_amd64.deb ...
Unpacking libhttp\-parser2.9:amd64 (2.9.2\-2) ...
Selecting previously unselected package libmbedcrypto3:amd64.
Preparing to unpack .../1\-libmbedcrypto3\_2.16.4\-1ubuntu2\_amd64.deb ...
Unpacking libmbedcrypto3:amd64 (2.16.4\-1ubuntu2) ...
...
Selecting previously unselected package bat.
Preparing to unpack .../5\-bat\_0.12.1\-1build1\_amd64.deb ...
Unpacking bat (0.12.1\-1build1) ...
Setting up libmbedcrypto3:amd64 (2.16.4\-1ubuntu2) ...
....
Setting up bat (0.12.1\-1build1) ...
Processing triggers for man\-db (2.9.1\-1) ...
Processing triggers for libc\-bin (2.31\-0ubuntu9) ...

### 高山Linux

执行 [apk命令](https://www.cyberciti.biz/faq/10-alpine-linux-apk-command-examples/ "有关更多信息，请参见Linux / Unix apk命令示例。")
`$ sudo apk add bat`

### Arch Linux安装蝙蝠

运行pacman命令：
`$ sudo pacman -S bat`

### Fedora Linux用户尝试以下dnf命令

`sudo dnf install bat`

### 在Gentoo Linux上

我们可以使用emerge命令：
`$ sudo emerge sys-apps/bat`

### 对于Void Linux

尝试xbps\-install：
`$ sudo xbps-install -S bat`

### FreeBSD在pkg命令的帮助下安装bat

`$ sudo pkg install bat`
当然。 FreeBSD用户也可以从FreeBSD端口构建它：
`# cd /usr/ports/textproc/bat
# make install`

### openSUSE用户尝试zypper命令

`$ sudo zypper install bat`

### Apple macOS Unix用户尝试以下任何一种方法

您可以使用Homebrew安装bat：
`brew install bat`
或使用MacPorts安装bat：
`port install bat`

### MS Windows用户

打开Windows提示符，然后键入：
`choco install bat`
##或##
`scoop install bat`

## 在Linux和Unix上使用bat

像cat命令一样，bat通常在Linux或Unix上开箱即用。 无需额外的配置。 因此，您要做的就是键入： 请注意，在某些发行版中，它称为batcat，以避免与名为bat的其他工具混淆。 例如，让我们尝试显示一个名为〜/ bin / backupme的文件
`batcat filename
bat filename`

`$ batcat ~/bin/backupme
$ bat ~/bin/backupme`

![bat Linux command in action on my Ubuntu desktop](https://www.cyberciti.biz/media/new/cms/2020/05/bat-Linux-command-in-action-on-my-Ubuntu-desktop.png)

![在我的Ubuntu桌面上运行bat Linux命令](https://www.cyberciti.biz/media/new/cms/2020/05/bat-Linux-command-in-action-on-my-Ubuntu-desktop.png)
我将使用 [alias命令](https://www.cyberciti.biz/tips/bash-aliases-mac-centos-linux-unix.html "有关更多信息，请参见Linux / Unix别名命令示例。") 定义bash shell别名 ： 有关 更多信息， 请参见“ [如何在Linux / Unix上创建永久性Bash别名](https://www.cyberciti.biz/faq/create-permanent-bash-alias-linux-unix/) ”。
`$ alias cat="batcat"
$ cat /etc/passwd`
[](https://www.cyberciti.biz/faq/create-permanent-bash-alias-linux-unix/)

### 关闭装饰品

将 \-p 选项 传递 给batcat：
`$ cat -p ~/bin/backupme`

### 仅打印每个文件的指定行范围

在下面的示例中，仅显示第35至42
`$ cat -r 35:42 /etc/hosts`
行 ： 品脱第1至20行：
`$ cat -r :20 /etc/hosts`
要显示从第20行到EOF：
`$ cat -r 20: /etc/hosts`

![Installing bat command on Unix and using it for fun and profit](https://www.cyberciti.biz/media/new/cms/2020/05/Installing-bat-command-on-Unix-and-using-it-for-fun-and-profit.png)

![在Unix上安装bat命令并将其用于娱乐和获利](https://www.cyberciti.biz/media/new/cms/2020/05/Installing-bat-command-on-Unix-and-using-it-for-fun-and-profit.png)

### 主题

获取语法突出显示支持的主题列表：
`cat --list-themes`
将名为ansi\-dark的主题设置为语法突出显示
`cat --theme ansi-dark /path/to/file`

### 获得帮助

使用man命令或将 \-\-help 选项 传递 给batcat：
`$ cat --help
$ batcat --help
$ man batcat`

## 结论

在这篇快速文章中，我们学习了如何使用CLI在Linux和类似Unix的系统上安装和使用bat命令。 Bat是台式机用户的理想现代工具，但我不会在服务器上安装它。 试试看，让我们知道您对 用Rust编程语言编写 的 [炫酷工具的](https://github.com/sharkdp/bat) 看法 。