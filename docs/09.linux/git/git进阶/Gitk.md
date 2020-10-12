---
title: Gitk
date: 2020-10-12 12:09:51
permalink: /pages/4ec229/
categories:
  - git
  - git进阶
tags:
  - 
---
# 吉特克

[返回目录](https://www.atlassian.com/git/tutorials)

Gitk是图形存储库浏览器。 这是同类产品中的第一个。 可以将它视为的GUI包装 `[git log](https://www.atlassian.com/git/tutorials/git-log)` 。 这对于探索和可视化存储库的历史非常有用。 它是用tcl / tk编写的，因此可以跨操作系统移植。 `gitk` 由Paul Mackerras维护，是一个独立于Git核心的独立项目。 稳定版作为Git套件的一部分分发，以方便最终用户。 Gitk可以为Git新手提供有用的学习帮助。

## Gitk概述

对于刚接触版本控制的人或从其他版本控制系统（如Subversion）过渡的用户，Gitk可能是有用的学习工具。 Gitk是与Git核心打包在一起的便捷实用程序。 它提供了图形用户界面，有助于可视化Git的内部机制。 其他流行的Git GUI是git\-gui和Atlassian自己的 [Sourcetree](http://www.sourcetreeapp.com/) 。

## 用法

Gitk的调用方式与相似 `git log` 。 执行该 `gitk` 命令将启动Gitk UI，其外观类似于以下内容：

![](https://wac-cdn.atlassian.com/dam/jcr:a9bd0f27-7144-4563-85dd-2ac1d56af0b4/initial.png?cdnVersion=1084)

左上方的窗格显示对存储库的提交，最新的显示在顶部。 右下方显示受所选提交影响的文件列表。 左下方的窗格显示提交详细信息和完整差异。 单击右下窗格中的文件，将左下窗格中的差异集中到相关部分。

Gitk将反映存储库的当前状态。 如果通过单独的命令行用法（例如更改分支）修改了存储库状态，则需要重新加载Gitk。 可以在文件菜单\->重新加载中重新加载Gitk。

默认情况下，Gitk将呈现当前的提交历史记录。 Gitk具有各种命令行选项，可以在初始化时传递。 这些选项主要限制了呈现给Gitk顶级视图的提交列表。 这些修订选项的一般执行形式如下：

## 选件

```
    gitk [<options>] [<revision range>] [--] [<path>…]    <revision range>
```

`"<from>..<to>"` 可以传递 表格中的修订范围， 以显示之间 `<from>` 和返回的 所有修订 `<to>` 。 或者，可以传递单个修订版。

```
    <path>…
```

限制提交到特定的文件路径。 要从修订名称中隔离路径，请使用“\-”将路径与任何先前的选项分开。

```
--all
```

显示所有分支，标签，参考。

```
--branches[=<pattern>] --tags[=<pattern>] --remotes[=<pattern>]
```

显示所选项目（分支，标签，远程），就像它们是主线提交一样。 当 `<pattern>`  通过时，进一步限制参到那些与指定模式匹配

```
    --since=<date>
```

渲染的提交比指定的日期更晚。

```
    --until=<date>
```

渲染的提交早于指定的日期。

```
    --date-order
```

按日期排序提交。

```
    --merge
```

显示修改在合并期间标识的冲突文件的提交

```
    --left-right
```

渲染信息标签，指示差异提交来自哪一侧。 左侧的提交以<符号为前缀，右侧的提交以>符号为前缀。

```
    --ancestry-path
```

当给定一个范围提交到显示器（例如 `commit1..commit2 or commit2 commit1` ），只显示直接存在于之间的祖先链提交的 `commit1` 和 `commit2` ，即，提交那些的两个后代 `commit1` ，和祖先 `commit2` 。 （有关 `git-log(1)` 详细说明， 请参阅“历史记录简化” 。）

```
L<start>,<end>:<file>
```

强大的选项使您可以跟踪给定代码行号范围的历史记录。

## 讨论与范例

为了提供任何有价值的输出，Gitk需要具有提交历史记录的基础存储库。 以下代码是一系列的bash命令，这些命令将创建一个具有两个分支的新仓库，这些分支具有提交并已 [合并](https://www.atlassian.com/git/tutorials/using-branches/git-merge) 到一个 分支中 。

```
    mkdir gitkdemo &&    cd gitkdemo &&    git init . &&    echo "hello world" > index.txt &&    git add index.txt &&    git commit -m "added index.txt with hello world content"
```

该演示存储库将是与Gitk一起探索的一个很好的例子。 此命令序列将创建一个具有1个提交和一个 `index.txt` 文件 的新 存储库。 现在让我们调用 `gitk` 以检查存储库。

![](https://wac-cdn.atlassian.com/dam/jcr:a2e9dbcf-78a4-473a-9536-781ba6b32c2a/first-commit.png?cdnVersion=1084)

## Gitk可以比较两个提交吗？

继续我们的演示存储库，现在让我们创建一个附加提交：

```
    echo "prpended content to index" >> index.txt &&    git commit -am "prepended content to index"
```

一旦执行了命令， `gitk` 将需要重新加载。 `gitk` 从命令行 重新加载 或使用GUI并导航到 `File -> Reload` 。 重新加载后，我们应该会看到新的 `commit` 。

![](https://wac-cdn.atlassian.com/dam/jcr:4e35bf18-2e16-41e2-a364-bdecbea42b43/next-commit.png?cdnVersion=1084)

我们可以看到， `master` 分支引用现在指向新提交。 为了比较这两个提交，我们使用左上方的历史面板。 在“历史记录”面板中，单击将成为差异基础的提交。 选择后，右键单击第二个提交以打开上下文菜单。

![](https://wac-cdn.atlassian.com/dam/jcr:9bc62cda-cd6d-473f-a984-0c122ef78393/commit-diff.png?cdnVersion=1084)

此上下文菜单将提供以下选项：

```
    Diff this -> selected    Diff selected -> this
```

选择这些选项之一将导致两次提交之间的差异出现在左下方窗格中，在我们的示例中将如下所示：

![](https://wac-cdn.atlassian.com/dam/jcr:2f861a4d-e966-4a15-9727-4baa1f906c42/diff-output.png?cdnVersion=1084)

diff输出向我们展示了 `index.txt` 在两次提交之间添加了新行的“要索引的内容”。

## 如何使用Gitk比较两个分支

继续我们的示例存储库，让我们创建一个新分支。

```
    git checkout -b new_branch &&    echo "new branch content" > new_branch_file.txt &&    git add new_branch_file.txt &&    git commit -m "new branch commit with new file and prepended content" &&    echo "new branch index update" >> index.txt &&    git commit -am "new branch commit to index.txt with new content"
```

后续命令序列将创建一个名为的新分支， `new_branch` 并向其中添加文件 `new_branch_file.txt` 。 此外，新内容已添加到 `index.txt` 该更新中 ， 并进行了其他提交。 现在，我们有了一个新分支，该分支比master提前2次提交。 我们必须重新加载Gitk以反映这些更改。

![](https://wac-cdn.atlassian.com/dam/jcr:bc3a3b91-faa3-4cb3-a0b3-62976ecc3f80/new-branch.png?cdnVersion=1084)

这是讨论Git分支机制的绝佳学习机会。 Gitk将提交显示为一条直线的提交序列。 术语“分支”表示我们应该在时间轴上出现“分支”或“分支”。 Git分支不同于其他版本控制系统。 在Git中，分支是指向提交的指针。 指针将在创建时移至提交。 创建时 `git branch` ，您不会更改存储库或源树的结构中的任何内容。 您只是在创建一个新的指针。

为了比较两个分支之间不同的提交，需要在指定的修订范围内启动Gitk。 执行 `gitk master..new_branch` 将仅使用两个分支引用之间的提交来打开Gitk。

![](https://wac-cdn.atlassian.com/dam/jcr:78065ec1-395e-45df-a8ec-9860221cfaae/branch-compare.png?cdnVersion=1084)

这是比较分支的强大工具。

## 吉特克vs吉特吉

Git Gui是Git的另一个基于Tcl / Tk的图形用户界面。 Gitk专注于导航和可视化存储库的历史记录，而Git Gui专注于完善 `commits` 单个文件注释，并且不显示项目历史记录。 Git Gui还提供菜单操作以启动Gitk进行历史探索。 还可以通过执行从命令行调用Git Gui `git gui` 。

## Gitk摘要

总之，Gitk是的图形界面包装 `git log` 。 Gitk非常强大，可以可视化和探索存储库的历史。 Gitk还是学习Git内部知识的有用工具。