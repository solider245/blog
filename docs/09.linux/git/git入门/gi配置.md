---
title: gi配置
date: 2020-10-12 12:09:51
permalink: /pages/9739bb/
categories:
  - git
  - git入门
tags:
  - 
---
# git配置

在本文档中，我们将深入了解该 `git config` 命令。 我们 `git config` 在“ [设置存储库”](https://www.atlassian.com/git/tutorials/setting-up-a-repository) 页面 上 简要讨论了 用法 。 该 `git config` 命令是一种便捷功能，用于在全局或本地项目级别上设置Git配置值。 这些配置级别对应于 `.gitconfig` 文本文件。 执行 `git config` 将修改配置文本文件。 我们将介绍常见的配置设置，例如电子邮件，用户名和编辑器。 我们将讨论Git别名，它允许您为常用的Git操作创建快捷方式。 熟悉 `git config` 各种Git配置设置将有助于您创建功能强大的自定义Git工作流程。

## 用法

最基本的用例 `git config` 是使用配置名称来调用它，该配置名称将显示该名称下的设置值。 配置名称是由点分隔的字符串，由基于它们的层次结构的“节”和“键”组成。 例如： `user.email`

```
git config user.email
```

在此示例中，电子邮件是用户配置块的子属性。 这将返回Git将与本地创建的提交相关联的已配置电子邮件地址（如果有）。

### git config级别和文件

在进一步讨论 `git config` 用法 之前 ，让我们花点时间介绍一下配置级别。 该 `git config` 命令可以接受参数以指定要在哪个配置级别上进行操作。 提供以下配置级别：

*   `**--local**`

默认情况下， `git config` 如果未传递任何配置选项 ， 将写入本地级别。 本地级别配置应用于 `git config` 调用 上下文存储库 。本地配置值存储在文件中，该文件可在存储库的.git目录中找到： `.git/config`

*    `**--global**`

全局级别配置是特定于用户的，这意味着它将应用于操作系统用户。 全局配置值存储在用户主目录中的文件中。 `~ /.gitconfig` 在Unix系统和 `C:\Users\<username>\.gitconfig` Windows上

*    `**--system**`

系统级配置应用于整个计算机。 这涵盖了操作系统上的所有用户和所有存储库。 系统级配置文件位于 `gitconfig` 系统根路径之外 的 文件中。 `$(prefix)/etc/gitconfig` 在Unix系统上。 在Windows上，可以 `C:\Documents and Settings\All Users\Application Data\Git\config` 在Windows XP和 `C:\ProgramData\Git\config` Windows Vista及更高版本上 找到此文件 。

因此，配置级别的优先级顺序为：本地，全局，系统。 这意味着当寻找配置值时，Git将在本地级别启动并冒泡至系统级别。

### 写一个值

扩展我们已经知道的知识 `git config` ，让我们看一个编写值的示例：

```
git config --global user.email "your_email@example.com"
```

本示例将值写入 `your_email@example.com` 配置名称 `user.email` 。 它使用该 `--global` 标志，因此为当前操作系统用户设置了该值。

## git配置编辑器\-core.editor

许多Git命令将启动文本编辑器，以提示进一步的输入。 最常见的用例之一 `git config` 是配置Git应该使用的编辑器。 下面列出了常用编辑器和匹配 `git config` 命令 的表 ：

| 编辑 | config命令 |
| --- | --- |
| 原子 | `~ git config --global core.editor "atom --wait"~` |
| emacs | `~ git config --global core.editor "emacs"~` |
| 纳米 | `~ git config --global core.editor "nano -w"~` |
| vim | `~ git config --global core.editor "vim"~` |
| 崇高文字（Mac） | `~ git config --global core.editor "subl -n -w"~` |
| Sublime Text（Win，32位安装） | `~ git config --global core.editor "'c:/program files (x86)/sublime text 3/sublimetext.exe' -w"~` |
| Sublime Text（Win，64位安装） | `~ git config --global core.editor "'c:/program files/sublime text 3/sublimetext.exe' -w"~` |
| 文字伴侣 | `~ git config --global core.editor "mate -w"~` |

## 合并工具

如果发生合并冲突，Git将启动“合并工具”。 默认情况下，Git使用通用Unix diff程序的内部实现。 内部Git差异是最小合并冲突查看器。 有许多外部第三方合并冲突解决方案可以替代使用。 有关各种合并工具和配置的概述，请参阅我们的 [技巧和工具](https://developer.atlassian.com/blog/2015/12/tips-tools-to-solve-git-conflicts/) 指南， [以解决与Git的冲突](https://developer.atlassian.com/blog/2015/12/tips-tools-to-solve-git-conflicts/) 。

```
git config --global merge.tool kdiff3
```

## 彩色输出

Git支持彩色终端输出，有助于快速读取Git输出。 您可以自定义Git输出以使用个性化的颜色主题。 该 `git config` 命令用于设置这些颜色值。

### `color.ui`

这是Git颜色的主变量。 将其设置为false将禁用所有Git的彩色端子输出。

```
$ git config --global color.ui false
```

默认情况下， `color.ui` 设置为auto会将颜色应用到即时终端输出流。 如果将输出流重定向到文件或通过管道传输到另一个进程，则自动设置将忽略颜色代码输出。

您可以将 `color.ui` 值 设置 为always，当将输出流重定向到文件或管道时， 该 值还将应用颜色代码输出。 由于接收管道可能不期望使用颜色编码的输入，因此这可能会无意中引起问题。

### Git颜色值

除之外 `color.ui` ，还有许多其他颗粒颜色设置。 像一样 `color.ui` ，这些颜色设置都可以设置为false，auto或always。 这些颜色设置也可以设置特定的颜色值。 支持的颜色值的一些示例是：

*   正常
*   黑色
*   红
*   绿色
*   黄色
*   蓝色
*   品红
*   青色
*   白色

颜色也可以指定为十六进制颜色代码，例如＃ff0000，如果您的终端支持，则可以指定为ANSI 256颜色值。

### Git颜色配置设置

1。 `color.branch`

*   配置Git分支命令的输出颜色

2\. `color.branch.<slot` \>

*   此值也适用于Git分支输出。 < `slot` \>是以下之一：
    *   1.当前：当前分支
    *   2.本地：本地分支
    *   3\. remote：在refs / remotes中的远程分支ref
    *   4.上游：上游跟踪分支
    *   5.普通：其他任何参考

3。 `color.diff`

*   适用的颜色 `git diff` ， `git log` 和 `git show` 输出

4 `color.diff` .。< `slot` \>

*   在下面配置< `slot` \>值可以 `color.diff` 告诉git在补丁的哪个部分上使用特定的颜色。
    *   1\. context：diff的上下文文本。 Git上下文是在差异或补丁中显示的文本内容行，突出显示了更改。
    *   2.普通：上下文的同义词
    *   3\. meta：将颜色应用于差异的meta信息
    *   4.碎片：将颜色应用于“大标题”或“大标题中的功能”
    *   5.旧的：对差异中已删除的行应用颜色
    *   6\. new：为差异添加的行上色
    *   7\. commit：在diff中的颜色提交头
    *   8.空白：为差异中的任何空白错误设置颜色

5\. `color.decorate.<slot` \>

*   自定义 `git log --decorate` 输出 颜色 。 的支持的< `slot` \>的值是： `branch` ， `remoteBranch` ， `tag` ， `stash` ，或 `HEAD` 。 它们分别适用于本地分支机构，远程跟踪分支机构，标签，隐藏的更改和 `HEAD` 。

6。 `color.grep`

*   将颜色应用于git grep的输出。

7\. `color.grep.<slot` \>

*   也适用于git grep。 < `slot` \>变量指定grep输出的哪一部分应用颜色。
    *   1.上下文：上下文行中不匹配的文本
    *   2\. filename：文件名前缀
    *   3.功能：功能名称行
    *   4\. linenumber：行号前缀
    *   5.匹配：匹配文本
    *   6\. matchContext：在上下文行中匹配文本
    *   7\. matchSelected：匹配所选行中的文本
    *   8\. selected：所选行中不匹配的文本
    *   9.分隔符：行（：，\-和=）上的字段之间以及块（\-）之间的分隔符

8\. color.interactive

*   此变量将颜色应用于交互式提示和显示。 例子是 `git add --interactive` 和 `git clean --interactive `

9\. color.interactive。<slot>

*   可以指定<slot>变量以定位更特定的“交互式输出”。 可用的< `slot` \>值包括：提示，标题，帮助，错误； 并且每个都作用于相应的交互式输出。

10。 `color.pager`

*   使用寻呼机时启用或禁用彩色输出

11。 `color.showBranch `

*   为git show branch命令启用或禁用颜色输出

``` `` `12. color.status ` `` ```

*   一个布尔值，用于启用或禁用Git状态的颜色输出

```` ``` ``13. color.status.<`slot`>`` ``` ````

用于为指定的git status元素指定自定义颜色。 < `slot` \>支持以下值：

*   1.头
    *   定位到状态区域的标题文本
*   2.添加或更新
    *   已添加但未提交的两个目标文件
*   ``` `` `3. changed` `` ```
    *   定位已修改但未添加到git索引的文件
*   4.未追踪
    *   定位不被Git跟踪的文件
*   5.分支
    *   将颜色应用于当前分支
*   6\. nobranch
    *   “无分支”警告的颜色显示在
*   7.未合并

    *   上色具有未合并更改的文件

## 别名

您可能从操作系统命令行熟悉别名的概念； 如果不是，它们是自定义快捷方式，它们定义将哪个命令扩展为更长的命令或组合的命令。 别名为您节省了键入常用命令的时间和精力。 Git提供了自己的别名系统。 Git别名的一个常见用例是缩短commit命令。 Git别名存储在Git配置文件中。 这意味着您可以使用该 `git config` 命令来配置别名。

```
git config --global alias.ci commit
```

本示例为 `git commit` 命令 创建一个ci别名 。 然后可以 `git commit` 通过执行 进行调用 `git ci` 。 别名也可以引用其他别名来创建功能强大的组合。

```
git config --global alias.amend ci --amend
```

本示例创建一个别名修改，该修改将ci别名组成一个使用的新别名 `--amend flag` 。

## 格式和空格

Git有几个“空白”功能，可以配置为在使用git diff时突出显示空白问题。 空白问题将使用配置的颜色突出显示 `color.diff.whitespace`

默认情况下启用以下功能：

*   `blank-at-eol` 在行尾高亮显示孤立的空白
*   `space-before-tab` 突出显示缩进行时在制表符前面出现的空格字符
*   `blank-at-eof` 突出显示在文件末尾插入的空白行

默认情况下，以下功能处于禁用状态

*   `indent-with-non-tab` 高亮显示一行缩进而不是制表符的空格
*   `tab-in-indent` 突出显示初始制表符缩进作为错误
*   `trailing-space` 是Eol Blank和Eof Blank的简写
*   `cr-at-eol highlights` 行尾的回车
*   `tabwidth=<n>` 定义选项卡占用多少个字符位置。 默认值为8。允许值为1\-63。

## 摘要

在本文中，我们介绍了git的用法 `config command` 。 我们讨论了该命令如何成为 `git config` 在文件系统上 编辑原始 文件的有效 方法 。 我们研究了配置选项的基本读写操作。 我们看了常见的配置模式：

*   如何配置Git编辑器
*   如何覆盖配置级别
*   如何重置配置默认值
*   如何自定义git颜色

总体而言， `git config` 是一个帮助程序工具，它​​提供了编辑 `git config` 磁盘上 原始 文件 的快捷方式 。 我们深入介绍了个人定制选项。 git配置选项的基本知识是 [设置存储库](https://www.atlassian.com/git/tutorials/setting-up-a-repository) 的先决条件 。 请参阅我们的指南以了解基本知识。