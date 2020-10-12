---
title: git checkout
date: 2020-10-12 12:09:51
permalink: /pages/fb8038/
categories:
  - git入门
  - 使用分支
tags:
  - 
---
# Git结帐

此页面是对该 `git checkout` 命令 的检查 。 它将涵盖用法示例和边缘案例。 用Git术语来说，“签出”是在目标实体的不同版本之间切换的动作。 该 `git checkout` 命令对三个不同的实体进行操作：文件，提交和分支。 除了“签出”的定义外，短语“签出”通常用于暗示执行 `git checkout` 命令 的动作 。 在“ [撤消更改”](https://www.atlassian.com/git/tutorials/undoing-changes) 主题中，我们看到了如何 `git checkout` 用于查看旧提交。 本文档大部分内容的重点是分支机构的签出操作。

签出分支类似于签出旧的提交和文件，因为工作目录已更新为与所选分支/修订版匹配。 但是，新的更改会保存在项目历史记录中，也就是说，这不是只读操作。

## 签出分支

该 `git checkout` 命令使您可以在由创建的分支之间导航 `git branch` 。 检出一个分支会更新工作目录中的文件，以匹配该分支中存储的版本，并告诉Git记录该分支上的所有新提交。 可以将其视为选择您正在从事的开发路线的一种方式。

与传统的SVN工作流程相比，为每个新功能提供专门的分支是一个巨大的转变。 它使尝试新实验变得非常容易，而又不必担心破坏现有功能，并且使同时处理许多不相关的功能成为可能。 此外，分支机构还促进了几个协作工作流程。

该 `git checkout` 命令有时可能会与混淆 `git clone` 。 这两个命令之间的区别在于，clone可以从远程存储库中获取代码，而checkout可以在本地系统上已经存在的代码版本之间进行切换。

## 用法：现有分支

假设您正在使用的存储库包含预先存在的分支，则可以使用来在这些分支之间切换 `git checkout` 。 要找出可用的分支以及当前的分支名称是什么，请执行 `git branch` 。

```
$> git branch
master
another_branch
feature_inprogress_branch
$> git checkout feature_inprogress_branch

```

上面的示例演示了如何通过执行 `git branch` 命令 查看可用分支的列表 ，以及如何切换到指定的分支（在这种情况下为） `feature_inprogress_branch` 。

## 新分支

`Git checkout` 与携手合作 `[git branch](https://www.atlassian.com/git/tutorials/using-branches)` 。 该 `git branch` 命令可用于创建新分支。 当你要开始一个新的功能，您可以创建一个新的分支关闭 `master` 使用 `git branch new_branch` 。 创建完成后，您可以 `git checkout new_branch` 用来切换到该分支。 此外，该 `git checkout` 命令接受一个 `-b` 用作便捷方法 的 参数， 该 参数将创建新分支并立即切换到该分支。 通过使用可以在单个存储库中切换多个功能 `git checkout` 。

```
git checkout -b <new-branch>
```

上面的示例同时创建和签出 `<new-branch>` 。 该 `-b` 选项是一个便利标志，告诉Git在运行 `git branch <new-branch>` 之前运行 `git checkout <new-branch>` 。

```
git checkout -b <new-branch> <existing-branch>
```

默认情况下 `git checkout -b` 将 `new-branch` 关闭当前 `HEAD` 。 可以将一个可选的附加分支参数传递给 `git checkout` 。 在上面的示例中， `<existing-branch>` 通过，然后 `new-branch` 以 `existing-branch` 而不是current为基础 `HEAD` 。

## 切换分支

切换分支是一项简单的操作。 执行以下将指向 `HEAD` 到的尖端 `<branchname>.`

```
git checkout <branchname>
```

Git在reflog中跟踪结帐操作的历史记录。 您可以执行 `git reflog` 以查看历史记录。

## Git检出远程分支

与团队合作时，通常使用远程存储库。 这些存储库可以托管和共享，也可以是其他同事的本地副本。 每个远程存储库将包含其自己的分支集。 为了签出远程分支，您必须首先获取分支的内容。

```
git fetch --all
```

在现代版本的Git中，您可以像本地分支一样签出远程分支。

```
git checkout <remotebranch>
```

较旧的Git版本需要基于 `remote` 。

```
git checkout <remotebranch> origin/<remotebranch>
```

另外，您可以签出新的本地分支并将其重置为远程分支的最后一次提交。

```
git checkout -b <branchname>
git reset --hard origin/<branchname>
```

## 分离头

既然我们已经了解了 `git checkout` on分支 的三种主要用法 ，那么讨论 `“detached HEAD”` 状态 非常重要 。 请记住，这 `HEAD` 是Git引用当前快照的方式。 在内部，该 `git checkout` 命令仅更新 `HEAD` 使其指向指定的分支或提交。 当它指向一个分支时，Git不会抱怨，但是当您检出一个提交时，它将切换到一种 `“detached HEAD”` 状态。

这是一条警告，告诉您正在做的一切都与项目开发的其余部分“分离”。 如果要在分离 `HEAD` 状态下 开始开发功能 ，则没有分支可以让您返回到该功能。 当您不可避免地签出另一个分支（例如，合并功能）时，将无法引用您的功能：

![](https://wac-cdn.atlassian.com/dam/jcr:8c2753f6-5942-4ce1-8660-79a1100535ee/05%20(4).svg?cdnVersion=1084)

关键是，您的开发应始终在分支上进行，而不应在独立的上进行 `HEAD` 。 这样可以确保您始终引用新提交。 但是，如果您只是在查看旧的提交，则是否处于分离 `HEAD` 状态并不重要。

## 摘要

此页面重点介绍 `git checkout` 更改分支时命令的 用法 。 总而言之 `git checkout` ，当在分支上使用时，会更改 `HEAD` 参考 的目标 。 它可用于创建分支，切换分支和签出远程分支。 该 `git checkout` 命令是用于标准Git操作的基本工具。 它是的对应项 `[git merge](https://www.atlassian.com/git/tutorials/using-branches/git-merge)` 。 该 `git checkout` 和 `git merge` 命令来实现的重要工具 `[git workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)` [。](https://www.atlassian.com/git/tutorials/comparing-workflows)