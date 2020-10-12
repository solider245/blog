---
title: git branch
date: 2020-10-12 12:09:51
permalink: /pages/1971d4/
categories:
  - git入门
  - 使用分支
tags:
  - 
---
# git分支

该文档是对该 `git branch` 命令 的深入回顾， 并讨论了整个Git分支模型。 分支是大多数现代版本控制系统中可用的功能。 在其他VCS中进行分支在时间和磁盘空间上都是一项昂贵的操作。 在Git中，分支机构是您日常开发过程的一部分。 Git分支实际上是指向更改快照的指针。 当您想添加新功能或修复错误时（无论大小），都可以生成一个新分支来封装您的更改。 这使得不稳定的代码很难合并到主代码库中，并且使您有机会在将其合并到主分支之前清理将来的历史记录。

![Git教程：git分支](https://wac-cdn.atlassian.com/dam/jcr:746be214-eb99-462c-9319-04a4d2eeebfa/01.svg?cdnVersion=1084)

上图通过两个独立的开发线对存储库进行了可视化处理，一个开发线用于一个小功能，另一个开发线用于一个长期运行的功能。 通过在分支中进行开发，不仅可以并行处理它们，而且还可以使主 `master` 分支摆脱可疑的代码。

Git分支后面的实现比其他版本控制系统模型轻得多。 Git不会将文件从一个目录复制到另一个目录，而是存储一个分支作为对提交的引用。 从这个意义上讲，分支代表了一系列提交的尖端，它不是提交的容器。 分支的历史记录通过提交关系来推断。

在阅读时，请记住，Git分支与SVN分支不同。 SVN分支仅用于捕获偶尔的大规模开发工作，而Git分支则是您日常工作流程中不可或缺的一部分。 以下内容将在内部Git分支架构上进行扩展。

## 这个怎么运作

分支代表独立的发展线。 分支充当编辑/阶段/提交过程的抽象。 您可以将它们视为请求全新的工作目录，暂存区和项目历史记录的方式。 新的提交记录在当前分支的历史记录中，这将导致项目历史记录中出现分支。

该 `git branch` 命令使您可以创建，列出，重命名和删除分支。 它不允许您在分支之间进行切换，也不能再次将分支的历史放回原处。 因此， `git branch` 与 `[git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)` 和 `[git merge](https://www.atlassian.com/git/tutorials/using-branches/git-merge)` 命令 紧密集成 。

## 常用选项

```
git branch
```

列出存储库中的所有分支。 这是同义的 `git branch --list.`

```
git branch <branch>
```

创建一个名为的新分支 `<branch>` 。 这并 *没有* 检查出新的分支。

```
git branch -d <branch>
```

删除指定的分支。 这是一个“安全”的操作，因为如果分支具有未合并的更改，Git会阻止您删除它。

```
git branch -D <branch>
```

强制删除指定的分支，即使该分支具有未合并的更改。 如果要永久丢弃与特定开发线相关的所有提交，则可以使用此命令。

```
git branch -m <branch>
```

将当前分支重命名为 `<branch>` 。

```
git branch -a
```

列出所有远程分支。

## 创建分支

重要的是要了解分支只是提交的指针。 创建分支时，Git所需要做的就是创建一个新的指针，它不会以任何其他方式更改存储库。 如果从如下所示的存储库开始：

![Git教程：没有任何分支的存储库](https://wac-cdn.atlassian.com/dam/jcr:80aa77d2-c28f-415e-ab10-e3612456a9c1/02.svg?cdnVersion=1084)

然后，使用以下命令创建分支：

```
git branch crazy-experiment
```

存储库历史记录保持不变。 您所获得的只是指向当前提交的新指针：

![Git教程：创建新分支](https://wac-cdn.atlassian.com/dam/jcr:b0e2f237-9337-4385-be22-43f623e133d0/03.svg?cdnVersion=1084)

请注意，这只会 *创建* 新分支。 要开始向其添加提交，您需要使用进行选择 `git checkout` ，然后使用标准 `git add` 和 `git commit` 命令。

## 创建远程分支

到目前为止，这些示例都已证明了本地分支机构的运作。 该 `git branch` 命令还可以在远程分支上使用。 为了在远程分支上进行操作，必须首先配置远程存储库并将其添加到本地存储库配置中。

```
$ git remote add new-remote-repo https://bitbucket.com/user/repo.git
# Add remote repo to local repo config
$ git push <new-remote-repo> crazy-experiment~
# pushes the crazy-experiment branch to new-remote-repo
```

此命令会将本地分支的副本推 `crazy-experiment` 送到远程仓库 `<remote>.`

## 删除分支

一旦完成分支工作并将其合并到主代码库中，就可以自由删除分支，而不会丢失任何历史记录：

```
git branch -d crazy-experiment
```

但是，如果分支尚未合并，则以上命令将输出错误消息：

```
error: The branch 'crazy-experiment' is not fully merged.
If you are sure you want to delete it, run 'git branch -D crazy-experiment'.
```

这样可以防止您失去对整个开发线的访问权限。 如果您确实要删除分支（例如，实验失败），则可以使用大写 `-D` 标志：

```
git branch -D crazy-experiment
```

这会删除分支，而无论其状态如何且没有警告，因此请谨慎使用。

前面的命令将删除分支的本地副本。 该分支可能仍存在于远程存储库中。 要删除远程分支，请执行以下操作。

```
git push origin --delete crazy-experiment
```

要么

```
git push origin :crazy-experiment
```

这会将删除信号推送到远程原始存储库，从而触发远程 `crazy-experiment` 分支 的删除 。

## 摘要

在本文档中，我们讨论了Git的分支行为和 `git branch` 命令。 该 `git branch` 命令主要功能是创建，列出，重命名和删除分支。 为了进一步在结果分支上操作，该命令通常与其他命令一起使用 `git checkout` 。 了解有关 `git checkout` 分支机构运营的 更多信息 ； 例如 `[git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)` 页面 上的切换分支和合并分支 。

与其他VCS相比，Git的分支操作便宜且经常使用。 这种灵活性使功能强大的 [Git工作流](https://www.atlassian.com/git/tutorials/comparing-workflows) 定制成为可能。 有关Git的工作流程，请访问我们的扩展工作讨论页面的详细信息： [该
功能科的工作流程](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow) ， [GitFlow工作流程](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) 和 [分岔工作流](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow) 。

准备尝试分支了吗？

试试这个交互式教程。

[现在就开始](https://www.atlassian.com/git/tutorials/learn-branching-with-bitbucket-cloud)