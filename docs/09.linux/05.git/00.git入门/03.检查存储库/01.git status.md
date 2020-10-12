---
title: git status
date: 2020-10-12 12:09:51
permalink: /pages/733fe7/
categories:
  - git入门
  - 检查存储库
tags:
  - 
---
# Git状态：检查存储库

[git status](https://www.atlassian.com/git/tutorials/inspecting-a-repository) [git标签](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-tag) [git怪](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-blame)

## git状态

该 `git status` 命令显示工作目录和暂存区的状态。 它使您可以查看已进行的更改，尚未进行的更改以及Git尚未跟踪的文件。 状态输出并 *不能* 告诉你关于承诺的项目历史的任何信息。 为此，您需要使用 [`git log`](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-log) 。

### 相关的git命令

*   [git标签  ](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-tag)
    *   标签是指向Git历史记录中特定点的引用。 `git tag` 通常用于捕获历史记录中用于标记版本发布（即v1.0.1）的点。
*   **`[git blame](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-blame)`**
    *   的高级功能 `git blame` 是显示附加到文件中特定提交行的作者元数据。 这用于探究特定代码的历史，并回答有关将代码添加到存储库的内容，方式和原因的问题。
*   [git日志  ](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-tag)
    *   该 `git log` 命令显示已提交的快照。 它使您可以列出项目历史记录，对其进行过滤并搜索特定的更改。

### 用法

```
git status
```

列出已暂存，未暂存和未跟踪的文件。

### 讨论区

该 `git status` 命令是相对简单的命令。 它只是向您显示 `git add` and 发生了什么 `git commit` 。 状态消息还包括有关暂存/取消暂存文件的相关说明。 下面显示了显示 `git status` 呼叫 的三个主要类别的示例输出 ：

```
# On branch master
# Changes to be committed:
# (use "git reset HEAD <file>..." to unstage)
#
#modified: hello.py
#
# Changes not staged for commit:
# (use "git add <file>..." to update what will be committed)
# (use "git checkout -- <file>..." to discard changes in working directory)
#
#modified: main.py
#
# Untracked files:
# (use "git add <file>..." to include in what will be committed)
#
#hello.pyc
```

#### 忽略文件

未跟踪的文件通常分为两类。 他们是刚刚被添加到项目和尚未提交任何文件，或他们是编译好的二进制文件一样 `.pyc` ， `.obj` ， `.exe` 等。虽然这绝对是有益的，包括在前者 `git status` 的输出，后者可以使很难看到存储库中的实际情况。

因此，Git允许您通过将路径放在称为的特殊文件中来完全忽略文件 [`.gitignore`](https://www.atlassian.com/git/tutorials/gitignore) 。 您要忽略的所有文件都应放在单独的行中，并且\*符号可以用作通配符。 例如，将以下内容添加到 `.gitignore` 项目根目录中 的 文件中将防止编译的Python模块出现在中 `git status` ：

```
*.pyc
```

### 例

最好在提交更改之前检查存储库的状态，以免意外提交您不想要的内容。 此示例显示暂存和提交快照前后的存储库状态：

```
# Edit hello.py
git status
# hello.py is listed under "Changes not staged for commit"
git add hello.py
git status
# hello.py is listed under "Changes to be committed"
git commit
git status
# nothing to commit (working directory clean)
```

第一个状态输出将显示该文件为未暂存状态。 该 `git add` 操作将在第二个中反映出来， `git status` 最终状态输出将告诉您没有要提交的内容\-工作目录与最近的提交相匹配。 一些Git命令（例如 [`git merge`](https://www.atlassian.com/git/tutorials/using-branches/git-merge) ）要求工作目录是干净的，以便您不会意外覆盖更改。

## git日志

该 `git log` 命令显示已提交的快照。 它使您可以列出项目历史记录，对其进行过滤并搜索特定的更改。 虽然 `git status` 可以检查工作目录和暂存区，但 `git log` 只能对提交的历史记录进行操作。

![Git教程：git状态与git日志](https://wac-cdn.atlassian.com/dam/jcr:52d530ce-7f51-48e3-920b-a18f776048d3/01.svg?cdnVersion=1084)

日志输出可以通过多种方式进行自定义，从简单过滤提交到以完全用户定义的格式显示它们。 下面介绍了一些最常见的配置 `git log` 。

### 用法

```
git log
```

使用默认格式显示整个提交历史记录。 如果输出占用一个以上的屏幕，则可以使用 `Space` 滚动和 `q` 退出。

```
git log -n <limit>
```

将提交次数限制为 `<limit>` 。 例如， `git log -n 3` 将仅显示3次提交。

```
git log --oneline
```

将每个提交压缩为一行。 这对于获得项目历史的高级概述很有用。

```
git log --stat
```

除普通 `git log` 信息外，还包括更改的文件以及从每个文件中添加或删除的相对行数。

```
git log -p
```

显示代表每个提交的补丁。 这将显示每个提交的完整差异，这是您可以查看的项目历史记录的最详细视图。

```
git log --author="<pattern>"
```

搜索特定作者的提交。 所述 `<pattern>` 参数可以是纯字符串或正则表达式。

```
git log --grep="<pattern>"
```

搜索带有与匹配的提交消息的提交 `<pattern>` ，可以是纯字符串或正则表达式。

```
git log <since>..<until>
```

仅显示在 `<since>` 和 之间发生的提交 `<until>` 。 这两个参数都可以是提交ID，分支名称 `HEAD` 或任何其他类型的 [修订引用](http://www.kernel.org/pub/software/scm/git/docs/gitrevisions.html) 。

```
git log <file>
```

仅显示包含指定文件的提交。 这是查看特定文件历史记录的简便方法。

```
git log --graph --decorate --oneline
```

一些有用的选项可供考虑。 \-\-graph标志将在提交消息的左侧绘制基于文本的提交图。 \-\-decorate添加显示的提交的分支或标记的名称。 \-\-oneline在一行上显示提交信息，使浏览概览一目了然。

### 讨论区

该 `git log` 命令是Git探索存储库历史的基本工具。 当您需要查找项目的特定版本或通过合并功能分支来确定将引入哪些更改时，将使用此功能。

```
commit 3157ee3718e180a9476bf2e5cab8e3f1e78a73b7
Author: John Smith
```

其中大多数非常简单； 但是，第一行需要一些解释。 之后的40个字符的字符串 `commit` 是提交内容的SHA\-1校验和。 这有两个目的。 首先，它确保提交的完整性\-如果提交曾经被破坏，则提交将生成不同的校验和。 其次，它用作提交的唯一ID。

此ID可以在命令中使用，例如 `git log <since>..<until>` 引用特定的提交。 例如， `git log 3157e..5ab91` 将显示ID为 `3157e` 和 的提交之间的所有内容 `5ab91` 。 除了校验和之外，分支名称（在 [分支模块中](https://www.atlassian.com/git/tutorials/using-branches) 讨论 ）和HEAD关键字是引用单个提交的其他常用方法。 `HEAD` 总是指当前提交，无论是分支还是特定提交。

〜字符可用于对提交的父项进行相对引用。 例如， `3157e~1` 在之前引用提交 `3157e` ，并且 `HEAD~3` 是当前提交的曾祖父母。

所有这些标识方法的思想是让您根据特定的提交执行操作。 该 `git log` 命令通常是这些交互的起点，因为它使您可以找到要使用的提交。

### 例

“ *用法”* 部分提供的许多示例 `git log` ，但请记住，可以将多个选项组合成一个命令：

```
git log --author="John Smith" -p hello.py
```

这将显示John Smith对文件所做的所有更改的完整差异 `hello.py` 。

..语法是比较分支的非常有用的工具。 下一个示例显示了所有 `some-feature` 不在中 的提交的简要概述 `master` 。

```
git log --oneline master..some-feature
```