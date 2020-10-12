---
title: Git merge
date: 2020-10-12 12:09:51
permalink: /pages/b019dd/
categories:
  - git入门
  - 使用分支
tags:
  - 
---
# Git合并

合并是Git重新将分叉的历史重新整合在一起的方式。 该 `git merge` 命令使您可以采用由创建的独立开发线， `git branch` 并将它们集成到单个分支中。

请注意，下面显示的所有命令都合并到当前分支中。 当前分支将被更新以反映合并，但是目标分支将完全不受影响。 同样，这意味着 `git merge` 通常与 `git checkout` 选择当前分支和 `git branch -d` 删除过时的目标分支结合使用。

## 这个怎么运作

`Git merge` 将多个提交序列合并为一个统一的历史记录。 在最常用的情况下， `git merge` 用于合并两个分支。 本文档中的以下示例将重点介绍此分支合并模式。 在这些情况下， `git merge` 需要两个提交指针（通常是分支技巧），并将在它们之间找到一个公共的基本提交。 一旦Git找到一个通用的基本提交，它将创建一个新的“合并提交”，它将每个排队的合并提交序列的更改组合在一起。

假设我们有一个基于分支的新分支功能 `master` 。 现在，我们希望将此功能分支合并到中 `master` 。

![](https://wac-cdn.atlassian.com/dam/jcr:86eba9ec-9391-45ea-800a-948cec1f2ed7/Branch-2.png?cdnVersion=1084)

假定此命令，将把指定的分支功能合并到当前分支中 `master` 。 Git将自动确定合并算法（在下面讨论）。

![](https://wac-cdn.atlassian.com/dam/jcr:83323200-3c57-4c29-9b7e-e67e98745427/Branch-1.png?cdnVersion=1084)

合并提交相对于其他提交是唯一的，因为它们具有两个父提交。 创建合并提交时，Git会尝试自动为您自动合并各个历史记录。 如果Git遇到一条在两个历史记录中都发生过更改的数据，它将无法自动合并它们。 这种情况是版本控制冲突，Git将需要用户干预才能继续。

## 准备合并

在执行合并之前，需要执行几个准备步骤以确保合并顺利进行。

## 确认接收分支

执行 `git status ` 以确保 `HEAD` 指向正确的合并接收分支。 如果需要，执行 `git checkout <receiving>` 以切换到接收分支。 在我们的情况下，我们将执行 `git checkout master.`

## 获取最新的远程提交

确保接收分支和合并分支是最新的最新远程更改。 执行 `git fetch` 以提取最新的远程提交。 提取完成后， `master` 通过执行以下命令来 确保 分支具有最新更新 `git pull.`

## 合并中

一旦已经采取了合并之前讨论的“准备合并”步骤可以由执行启动 `git merge <branch name>` 哪里 `<branch name>` 是将要合并到接收支路的分支的名称。

## 快进合并

当存在从当前分支尖端到目标分支的线性路径时，会发生快速合并。 并非“实际”合并分支，Git整合历史记录所需要做的就是将当前分支尖端（即“快进”）移动到目标分支尖端。 这有效地结合了历史记录，因为从目标分支可到达的所有提交现在都可以通过当前分支获得。 例如，将某些功能快速合并到 `master` 以下内容中：

![](https://wac-cdn.atlassian.com/dam/jcr:b87df050-2a3a-4f17-bb80-43c5217b4947/07%20(1).svg?cdnVersion=1084)

但是，如果分支分歧，则无法进行快速合并。 当没有到目标分支的线性路径时，Git别无选择，只能通过三向合并将它们合并。 三向合并使用专用提交将两个历史联系在一起。 命名法来自以下事实：Git使用三个提交来生成合并提交：两个分支提示及其共同祖先。

![](https://wac-cdn.atlassian.com/dam/jcr:91b1bdf5-fda3-4d20-b108-0bb9eea402b2/08.svg?cdnVersion=1084)

虽然您可以使用这两种合并策略中的任何一种，但许多开发人员喜欢将快速前进合并（通过 [rebasing](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase) 促成 ）用于小功能或错误修复，而保留三路合并以集成运行时间更长的功能。 在后一种情况下，生成的合并提交充当两个分支的符号连接。

我们的第一个示例演示了快速合并。 下面的代码创建一个新分支，向其添加两个提交，然后通过快速合并将其集成到主行中。

```
# Start a new feature
git checkout -b new-feature master
# Edit some files
git add <file>
git commit -m "Start a feature"
# Edit some files
git add <file>
git commit -m "Finish a feature"
# Merge in the new-feature branch
git checkout master
git merge new-feature
git branch -d new-feature

```

这是用于短暂主题分支的通用工作流程，这些主题分支更多地用作独立开发，而不是用于功能长期运行的组织工具。

另请注意，Git不应抱怨 `git branch -d` ，因为现在可以从master分支访问new功能。

如果在快速前进合并过程中需要进行合并提交以保持记录，则可以 `git merge` 使用该 `--no-ff` 选项 执行 。

```
git merge --no-ff <branch>

```

该命令将指定的分支合并到当前分支，但始终生成合并提交（即使它是快速合并）。 这对于记录存储库中发生的所有合并很有用。

## 3路合并

下一个示例非常相似，但是需要进行三向合并，因为 `master`  在功能进行中会不断进行。 对于大型功能部件，或者当几个开发人员同时从事一个项目时，这是一种常见的情况。

```
Start a new feature
git checkout -b new-feature master
# Edit some files
git add <file>
git commit -m "Start a feature"
# Edit some files
git add <file>
git commit -m "Finish a feature"
# Develop the master branch
git checkout master
# Edit some files
git add <file>
git commit -m "Make some super-stable changes to master"
# Merge in the new-feature branch
git merge new-feature
git branch -d new-feature
```

请注意，这是不可能的Git的执行快进合并，因为没有办法移动 `master` 最多 `new-feature` 不回溯。

对于大多数工作流程而言， `new-feature` 这将是一个很大的功能，需要花费很长的时间才能开发出来，这就是为什么 `master` 同时 出现新提交的原因 。 如果您的功能分支实际上和上面的示例中的分支一样小，则最好将其重新部署到基础上 `master` 并进行快速合并。 这样可以防止多余的合并提交使项目历史变得混乱。

## 解决冲突

如果您要合并的两个分支都更改了同一文件的相同部分，则Git将无法确定要使用哪个版本。 发生这种情况时，它会在合并提交之前停止，因此您可以手动解决冲突。

Git合并过程的很大一部分是，它使用熟悉的edit / stage / commit工作流程来解决合并冲突。 遇到合并冲突时，运行 `git status` 命令将显示需要解析的文件。 例如，如果两个分支都修改了的同一部分 `hello.py` ，您将看到类似以下内容：

```
On branch master
Unmerged paths:
(use "git add/rm ..." as appropriate to mark resolution)
both modified: hello.py

```

## 冲突如何呈现

当Git在合并过程中遇到冲突时，它将使用视觉标记来编辑受影响文件的内容，这些视觉标记标记了冲突内容的两面。 这些视觉标记是：<<<<<<<，=======和>>>>>>>。 在合并期间在项目中搜索这些指标很有帮助，以查找需要解决冲突的地方。

```
here is some content not affected by the conflict
<<<<<<< master
this is conflicted text from master
=======
this is conflicted text from feature branch

```

通常， `=======` 标记 之前的内容 是接收分支，之后的部分是合并分支。

一旦确定了冲突的部分，就可以按照自己的喜好修复合并。 当您准备好完成合并时，您要做的就是 `git add` 在有冲突的文件上 运行 ，以告知Git它们已解决。 然后，您运行法线 `git commit` 以生成合并提交。 这与提交普通快照的过程完全相同，这意味着普通开发人员可以轻松管理自己的合并。

请注意，只有在三向合并的情况下才会发生合并冲突。 在快速合并中不可能有冲突的更改。

## 摘要

本文档是 `git merge` 命令 的概述 。 使用Git时，合并是必不可少的过程。 我们讨论了合并背后的内部机制以及快速前向合并和三路真实合并之间的区别。 一些关键要点是：

1.  Git合并将提交序列合并到一个统一的提交历史中。
2.  Git合并的主要方式有两种：快速前进和三种方式
3.  除非两个提交序列中的更改都发生冲突，否则Git可以自动合并提交。

本文档集成和参考像其他Git命令： `[git branch](https://www.atlassian.com/git/tutorials/using-branches)` ， `[git pull](https://www.atlassian.com/git/tutorials/syncing#git-pull)` ，和 `[git fetch](https://www.atlassian.com/git/tutorials/syncing#git-fetch)` 。 访问其相应的独立页面以获取更多信息。