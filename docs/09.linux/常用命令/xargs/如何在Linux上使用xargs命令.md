---
title: 如何在Linux上使用xargs命令
date: 2020-10-12 12:09:51
permalink: /pages/320d67/
categories:
  - 常用命令
  - xargs
tags:
  - 
---
需要将一些Linux命令串在一起，但是其中一个不接受管道输入吗？ `xargs`  可以将一个命令的输出作为参数发送给另一个命令。

所有标准Linux实用程序都具有 与之关联的 [三个数据流](https://en.wikipedia.org/wiki/Standard_streams) 。 它们是标准输入流（stdin），标准输出流（stdout）和标准错误流（stderr）。

这些流使用文本。 我们使用文本将输入（stdin）发送到命令，然后将响应（stdout）作为文本写入终端窗口。 错误消息也以文本（stderr）的形式写入终端窗口。

Linux和 [类Unix操作系统的](https://www.howtogeek.com/182649/htg-explains-what-is-unix/) 一大功能 是能够将标准输出从一个命令传递到第二个命令的stdin输入。 第一个命令不在乎其输出不会进入终端窗口，第二个命令不在乎其输入不是来自键盘。

尽管所有Linux命令都具有三个标准流，但是并非所有命令都接受另一个命令的stdout作为其stdin的输入。 这意味着您无法通过管道将输入传递给他们。

`xargs` 是用于使用标准数据流构建执行管道的命令。 通过使用， `xargs` 我们可以制作诸如 `echo` ，的 命令 `rm` ，并 `mkdir`  接受标准输入作为参数。

## xargs命令

`xargs` 将接受管道输入。 它还可以接受来自文件的输入。 `xargs` 使用该输入作为我们告诉它使用的命令的参数。 如果我们不告诉 `xargs` 您使用特定命令，则默认使用 `echo` 。

我们可以用它来演示如何 `xargs` 始终生成单行输出，即使是多行输入也是如此。

如果我们使用 `-1` （每行列出一个文件）选项 `ls` ，则会得到一 [列filenames](http://man7.org/linux/man-pages/man1/ls.1.html) 。

ls \-1 ./\*.sh

![v在终端窗口中](https://www.howtogeek.com/wp-content/uploads/2019/07/4-8.png)

这列出了当前目录中的Shell脚本文件。

![在终端窗口中输出ls](https://www.howtogeek.com/wp-content/uploads/2019/07/5-4.png)

我们得到了预期的单列。 如果我们通过它 `xargs` 得到什么， 该 怎么办？

ls \-1 ./\*.sh | xargs

![ls -1 ./*.sh |  终端窗口中的xargs](https://www.howtogeek.com/wp-content/uploads/2019/07/6-3.png)

输出作为一长串文本写入终端窗口。

![ls通过终端窗口中的xargs传递](https://www.howtogeek.com/wp-content/uploads/2019/07/7-3.png)

正是这种功能让我们 `xargs` 将参数输入其他命令。

## 在wc中使用xargs

我们可以 `xargs` 轻松地 `wc` 计算 多个文件中 的 [单词，字符和行数](http://man7.org/linux/man-pages/man1/wc.1.html) 。

ls \*.page | xargs wc

![ls * .page |  终端窗口中的xargs wc](https://www.howtogeek.com/wp-content/uploads/2019/07/8-3.png)

这是发生了什么：

*   `ls` 列出\* .page文件，并将列表传递给 `xargs` 。
*   `xargs` 将文件名传递给 `wc` 。
*   `wc`  将文件名视为已将其作为命令行参数接收。

![终端窗口中的wc输出](https://www.howtogeek.com/wp-content/uploads/2019/07/9-2.png)

将显示每个文件的统计信息以及总数。

## 使用带有确认的xargs

我们可以使用 `-p` （交互）选项来 `xargs` 提示我们确认我们很高兴继续进行。

如果我们通过文件名的字符串 `touch` ，通过 `xargs` ， `touch` 将 [创建的文件](http://man7.org/linux/man-pages/man1/touch.1.html) 我们。

echo 'one two three' | xargs \-p touch

![回声“一二三” |  xargs -p在终端窗口中触摸](https://www.howtogeek.com/wp-content/uploads/2019/07/x23-1.png.pagespeed.gp+jp+jw+pj+ws+js+rj+rp+rw+ri+cp+md.ic.GodYwE5qlY.png)

显示将要执行的命令，并 `xargs` 等待我们通过键入“ y”或“ Y”，“ n”或“ N”并按Enter来响应。

如果仅按Enter，则将其视为“ n”。 仅当键入“ y”或“ Y”时才执行该命令。

![xargs提示在终端窗口中进行确认](https://www.howtogeek.com/wp-content/uploads/2019/07/24-1.png)

我们按“ y”，然后按Enter。 我们可以 `ls` 用来检查文件是否已经创建。

ls one two three

![在终端窗口中输出ls](https://www.howtogeek.com/wp-content/uploads/2019/07/25-1.png)

## 将xargs与多个命令一起使用

`xargs` 通过使用 `-I`  （初始参数）选项， 我们可以使用多个命令 。

此选项定义“替换字符串”。 替换字符串的令牌出现在命令行中的任何位置，都会 `xargs` 插入 提供的值 。

让我们使用 `tree` 命令查看当前目录中的子目录。 该 `-d` （目录）选项导致 `tree` 忽略文件和目录上只报告。

tree \-d

![终端窗口中的树-d](https://www.howtogeek.com/wp-content/uploads/2019/07/26-1.png)

有一个名为“ images”的子目录。

在名为“ directories.txt”的文件中，我们具有要创建的某些目录的名称。 我们可以使用来查看其内容 `cat` 。

cat directories.txt

![终端窗口中的cat directory.txt](https://www.howtogeek.com/wp-content/uploads/2019/07/27-3.png)

我们将使用它作为的输入数据 `xargs` 。 我们要执行的命令是这样的：

cat directories.txt | xargs \-I % sh \-c 'echo %; mkdir %'

像这样分解：

*   *猫目录.txt |* ：这会将directrories.txt文件的内容（所有新目录名称）压入 `xargs` 。
*   *xargs \-I％* ：这定义了带有标记“％”的“替换字符串”。
*   *sh \-c* ：这将启动一个新的子shell。 的 `-c` （命令）告诉shell读取来自命令行的命令。
*   *回声％; mkdir％'* ：每个“％”标记都将由传递的目录名称替换 `xargs` 。 该 `echo` 命令将打印目录名称； 该 `mkdir` 命令将创建目录。

![猫目录.txt |  xargs -I％sh -c'echo％;  终端窗口中的mkdir％'](https://www.howtogeek.com/wp-content/uploads/2019/07/28.png)

目录被一一列出。

![在终端窗口中输出xargs](https://www.howtogeek.com/wp-content/uploads/2019/07/29-2.png)

我们可以 `tree` 再次 使用 以验证目录已创建。

tree \-d

![在终端窗口中从树输出](https://www.howtogeek.com/wp-content/uploads/2019/07/30-2.png)

## 将文件复制到多个位置

我们可以 `xargs` 用来允许我们通过一个命令将文件复制到多个位置。

我们将通过管道将两个目录的名称 `xargs` 作为输入参数。 我们将告诉 `xargs` 您一次仅将这些参数之一传递给正在使用的命令。

在这种情况下，命令为 `cp` 。 因此，效果是调用 `cp` 两次，每次都使用两个目录之一作为命令行参数。 `xargs` 允许发生这种情况 的 参数是 `-n` （最大数量）选项。 我们将其设置为一个。

我们还使用 `-v` （详细）选项， `cp` 以便它报告正在发生的事情。

echo ~/Backups/ ~/Documents/page\-files/ | xargs \-n 1 cp \-v ./\*.page

![回声〜/ Backups /〜/ Documents / page-files / |  xargs -n 1 cp -v ./*.page在终端窗口中](https://www.howtogeek.com/wp-content/uploads/2019/07/16-1.png)

将文件复制到两个目录，一次复制一个目录。 `cp` 报告每个文件复制操作，以便我们可以看到它们正在发生。

![在终端窗口中输出xargs和cp](https://www.howtogeek.com/wp-content/uploads/2019/07/17-1.png)

## 删除嵌套目录中的文件

如果文件名中包含空格并包含奇怪的字符（例如换行符）， `xargs` 将无法正确解释它们。 我们可以通过使用\-0（空终止符）选项来解决该问题。 这告诉 `xargs` 使用空字符作为文件名的最终定界符。

我们将 `find` 在此示例中 使用 。 `find` 有自己的选项来 [处理](http://man7.org/linux/man-pages/man1/find.1.html) 文件名中的 [空格](http://man7.org/linux/man-pages/man1/find.1.html) 和奇怪字符。 它是 `-print0` （全名，空字符）选项。

find . \-name "\*.png" \-type f \-print0 | xargs \-0 rm \-v \-rf "{}"

像这样分解：

*   *找 。\-name“ \* .png”* ： `find` 将从当前目录“。”搜索 名称与文件（ `type -f` ） 相匹配的“ \* .png”对象 。
*   *\-print0* ：名称将以空字符结尾，并且将保留空格和奇怪的字符。
*   *xargs \-0* ： *xargs* 还将考虑文件名以null结尾，并且空格和奇怪字符不会引起问题。
*   *rm \-v \-rf“ {}”* ：rm将很冗长，并报告正在发生的事情（ `-v` ）。 这将是递归（\-r）并浏览嵌套的子目录，并且将删除文件而不会提示（ `-f` ）。 每个文件名将替换“ {}”。

![找 。 -name“ * .png” -type f -print0 |  xargs -0 rm -v -rf“ {}”在终端窗口中](https://www.howtogeek.com/wp-content/uploads/2019/07/14-1.png)

搜索所有子目录，并删除与搜索模式匹配的文件。

![在终端窗口中输出rm](https://www.howtogeek.com/wp-content/uploads/2019/07/15-1.png)

## 删除嵌套目录

假设我们要删除一组嵌套的子目录。 `tree` 让我们看到他们。

tree \-d

![终端窗口中的树-d](https://www.howtogeek.com/wp-content/uploads/2019/07/10-1.png)

find . \-name "level\_one" \-type d printo | xargs \-o rm \-v \-rf "{}"

此命令将使用find在当前目录中递归搜索。 搜索目标是名为“ level\_one”的目录。 目录名通过传递 `xargs` 给 `rm` 。

![找 。 -name“ level_one”-键入d printo |  xargs -o rm -v -rf“ {}”在终端窗口中](https://www.howtogeek.com/wp-content/uploads/2019/07/11-1.png)

这个命令和前面的命令之间的唯一显著的变化是，搜索项是最顶层目录的名称，并 `-type d` 告诉 `find` 要查找的目录，而不是文件。

![在终端窗口中从find和xargs和rm输出](https://www.howtogeek.com/wp-content/uploads/2019/07/12-1.png)

每个目录的名称在删除时都会打印出来。 我们可以检查 `tree` ：

tree \-d

![终端窗口中的树-d](https://www.howtogeek.com/wp-content/uploads/2019/07/13-1.png)

所有嵌套的子目录都将被删除。

## 删除一种文件类型以外的所有文件

我们可以使用 `find` ， `xargs` 并且 `rm` 从一个类型，我们要保留除了删除所有文件。 这有点违反直觉，但是我们提供了要 *保留* 的文件类型 的名称，而不是我们要删除 的文件类型 的名称。

该 `-not` 选项告诉 `find` 您返回 与搜索模式 *不* 匹配的 文件名 。 我们 再次 使用 `-I` （初始参数）选项 `xargs` 。 这次，我们定义的替换字符串标记为“ {}”。 这将与我们之前生成的替换字符串标记完全相同，该标记恰好是“％”。

find . \-type f \-not \- name "\*.sh" \-print0 | xargs \-0 \-I {} rm \-v {}

![找 。 -f -not-名称“ * .sh” -print0 |  xargs -0 -I {} rm -v {}在终端窗口中](https://www.howtogeek.com/wp-content/uploads/2019/07/18-2.png)

我们可以通过进行确认 `ls` 。 目录中剩下的唯一文件是与“ \* .sh”搜索模式匹配的文件。

ls \-l

![在终端窗口中从ls输出](https://www.howtogeek.com/wp-content/uploads/2019/07/19-2.png)

## 使用Xargs创建档案文件

我们可以 `find` 用来搜索文件，并将它们传递 `xargs` 给 `tar` ，以创建档案文件。

我们将在当前目录中搜索。 搜索模式为“ \* .page”，因此我们将查找“ .page”文件。

find ./ \- name "\*.page" \-type f \-print0 | xargs \-0 \-tar \-cvzf page\_files.tar.gz

![查找./-名称“ * .page” -type f -print0 |  终端窗口中的xargs -0 -tar -cvzf page_files.tar.gz](https://www.howtogeek.com/wp-content/uploads/2019/07/1-11.png)

创建存档文件后，文件将按预期列出。

![终端窗口中tar的输出](https://www.howtogeek.com/wp-content/uploads/2019/07/2-8.png)

## 数据中介者

有时，当您将东西堆叠在一起时，需要一些脚手架。 `xargs` 弥合了可以抽出信息的命令与并非旨在接收信息的命令之间的鸿沟。

双方 `xargs` 并 `find` 有选择数量巨大。 鼓励您查看他们的手册页以了解更多信息。

继续阅读

*   › [如何将Stadia控制器无线链接到Android设备](https://www.howtogeek.com/680250/how-to-wirelessly-link-a-stadia-controller-to-an-android-device/)
*   › [排序文件夹后如何重新打开Microsoft Outlook的对话视图](https://www.howtogeek.com/677670/how-to-return-to-microsoft-outlooks-conversation-view-if-it-disappeared/)
*   › [如何在Google Chrome浏览器中查看已保存的密码](https://www.howtogeek.com/678453/how-to-view-a-saved-password-in-google-chrome/)
*   › [什么是Patreon，它如何工作？](https://www.howtogeek.com/675800/what-is-patreon-and-how-does-it-work/)
*   › [PSA：所有应用程序都可以读取您的iPhone和Android剪贴板](https://www.howtogeek.com/680147/psa-all-apps-can-read-your-iphone-and-android-clipboard/)

[![戴夫·麦凯](data:image/jpeg;base64,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)](https://www.howtogeek.com/author/davidmckay/)  [戴夫·麦凯（](https://www.howtogeek.com/author/davidmckay/)
Dave McKay）在打孔纸带风行时，他首先使用计算机，从那时起，他就开始编程。在IT行业工作了30多年之后，他现在是一名全职技术记者。在他的职业生涯中，他曾担任自由程序员，国际软件开发团队经理，IT服务项目经理，以及最近的数据保护官。Dave是Linux的宣传者和开源倡导者。
[阅读完整的传记»](https://www.howtogeek.com/author/davidmckay/)Git 基础 - 打标签