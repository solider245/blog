---
title: git add
date: 2020-10-12 12:09:51
permalink: /pages/5ac277/
categories:
  - git入门
  - git保存更改
tags:
  - 
---
# 保存更改

[git添加](https://www.atlassian.com/git/tutorials/saving-changes) [git commit](https://www.atlassian.com/git/tutorials/saving-changes/git-commit) [git diff](https://www.atlassian.com/git/tutorials/saving-changes/git-diff) [git stash](https://www.atlassian.com/git/tutorials/saving-changes/git-stash) [.gitignore](https://www.atlassian.com/git/tutorials/saving-changes/gitignore)

在Git或其他版本控制系统中工作时，“保存”的概念比在文字处理器或其他传统文件编辑应用程序中进行保存的过程更为细微。 传统的“保存”软件表达与Git术语“提交”同义。 提交相当于“保存”的Git。 传统保存应被认为是用于覆盖现有文件或写入新文件的文件系统操作。 另外，Git commit是对文件和目录的集合进行操作的操作。

在Git vs SVN中保存更改也是一个不同的过程。 SVN提交或“签入”是对远程推送到集中式服务器的操作。 这意味着SVN提交需要Internet访问才能完全“保存”项目更改。 可以在本地捕获和构建Git提交，然后根据需要使用 `git push -u origin master` 命令 将其提交到远程服务器 。 两种方法之间的差异是体系结构设计之间的根本差异。 Git是分布式应用程序模型，而SVN是集中式模型。 分布式应用程序通常更稳定，因为它们没有像集中式服务器那样的单点故障。

命令： `git add` ， `[git status](https://www.atlassian.com/git/tutorials/inspecting-a-repository)` ，和 `[git commit](https://www.atlassian.com/git/tutorials/saving-changes/git-commit)`  都结合使用，以节省一个Git项目的当前状态的快照。

Git还有一个额外的保存机制，称为“隐藏”。 存放区是临时存储区，用于存储尚未准备好提交的更改。 存储 [在三个](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset) 目录 [树中](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset) 的第一个目录的工作目录上运行， 并具有广泛的使用选项。 要了解更多信息，请访问 `[git stash](https://www.atlassian.com/git/tutorials/saving-changes/git-stash)` 页面。

可以将Git存储库配置为忽略特定的文件或目录。 这将防止Git将更改保存到任何忽略的内容。 Git有多种配置方法来管理忽略列表。 在 `[git ignore](https://www.atlassian.com/git/tutorials/saving-changes/gitignore)`  页面 上将进一步详细讨论Git ignore configure 。

## git添加

该 `git add` 命令将工作目录中的更改添加到登台区域。 它告诉Git您想在下一次提交中包括对特定文件的更新。 但是， `git add` 并不会以任何重大方式真正影响存储库\-直到您运行，更改才会被实际记录 `[git commit](https://www.atlassian.com/git/tutorials/saving-changes/git-commit)` 。

结合这些命令，您还需要 `[git status](https://www.atlassian.com/git/tutorials/inspecting-a-repository)` 查看工作目录和暂存区的状态。

## 这个怎么运作

该 `git add` 和 `[git commit](https://www.atlassian.com/git/tutorials/saving-changes)`  命令组成的基本Git的工作流程。 这是每个Git用户都需要理解的两个命令，而不管其团队的协作模型如何。 它们是将项目版本记录到存储库历史中的方法。

开发项目围绕基本的编辑/阶段/提交模式。 首先，您在工作目录中编辑文件。 准备好保存项目当前状态的副本时，可以使用进行更改 `git add` 。 对暂存的快照满意后，可使用将其提交到项目历史记录中 `git commit` 。 该 `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)`  命令用于撤消提交或暂存快照。

除了 `git add` 和以外 `git commit` ，第三条命令 `[git push](https://www.atlassian.com/git/tutorials/syncing)` 对于完整的协作Git工作流程也是必不可少的。 `git push` 用于将已提交的更改发送到远程存储库以进行协作。 这使其他团队成员可以访问一组已保存的更改。

![Git教程：git add Snapshot](https://wac-cdn.atlassian.com/dam/jcr:0f27e004-f2f5-4890-921d-65fa77ba2774/01.svg?cdnVersion=1084)

该 `git add` 命令不应与混淆 `svn add` ，后者会将文件添加到存储库。 而是 `git add` 在更抽象的更改级别上工作。 这意味着 `git add` 每次更改文件都 `svn add` 需要调用一次，而每个文件只需要调用一次。 听起来可能有些多余，但是此工作流程使保持项目井井有条变得容易得多。

## 暂存区

该 `git add` 命令 的主要功能 是将工作目录中的待定更改升级到该 `git staging` 区域。 临时区域是Git更为独特的功能之一，如果您来自SVN（甚至是Mercurial）背景，则可能需要花费一些时间来解决。 它有助于将其视为工作目录和项目历史记录之间的缓冲区。 暂存区域 以及工作目录和提交历史记录 被视为 [Git](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset) 的 [“三棵树”](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset) 之一。

通过此阶段，您可以将相关的更改分组为高度集中的快照，然后再将其实际提交到项目历史记录中，而不用提交自上次提交以来所做的所有更改。 这意味着您可以对不相关的文件进行各种编辑，然后返回并通过将相关更改添加到阶段将它们分成逻辑提交，然后逐个提交。 像在任何版本控制系统中一样，创建原子提交非常重要，这样就可以轻松地查找错误并还原更改，而对项目的其余部分的影响最小。

## 常用选项

```
git add <file>
```

暂存所有更改以 `<file>` 进行下一次提交。

```
git add <directory>
```

暂存所有更改以 `<directory>` 进行下一次提交。

```
git add -p
```

开始一个交互式暂存会话，使您可以选择文件的各个部分以添加到下一个提交中。 这将为您提供大量更改，并提示您输入命令。 使用 `y` 阶段性块， `n` 忽略块， `s` 将其分割成小块， `e` 手工编辑块，并 `q` 退出。

## 例子

开始新项目时， `git add` 其功能与相同 `svn import` 。 要创建当前目录的初始提交，请使用以下两个命令：

```
git add .
git commit
```

项目启动并运行后，可以通过将路径传递到来添加新文件 `git add` ：

```
git add hello.py
git commit
```

上述命令还可以用于记录对现有文件的更改。 同样，Git不会区分新文件中的暂存更改与已添加到存储库中的文件更改。

## 摘要

回顾中，它 `git add` 是一系列操作中的第一条命令 ， 该命令指导Git将当前项目状态的快照“保存”到提交历史记录中。 单独使用时， `git add` 会将未完成的更改从工作目录升级到暂存区。 该 `[git status](https://www.atlassian.com/git/tutorials/inspecting-a-repository)` 命令用于检查存储库的当前状态，并可用于确认 `git add` 升级。 该 `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)` 命令用于撤消a `git add` 。 `[git commit](https://www.atlassian.com/git/tutorials/saving-changes/git-commit)`  然后， 该 命令用于将登台目录的快照提交到存储库提交历史记录。