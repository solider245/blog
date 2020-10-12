---
title: git commit --amend
date: 2020-10-12 12:09:51
permalink: /pages/a85814/
categories:
  - git入门
  - 改写历史
tags:
  - 
---
# 改写历史

###### Git commit \-\-amend和其他重写历史记录的方法

## 介绍

本教程将介绍重写和更改Git历史记录的各种方法。 Git使用几种不同的方法来记录更改。 我们将讨论不同方法的优点和缺点，并举例说明如何使用它们。 本教程讨论了覆盖已提交快照的一些最常见原因，并向您展示了如何避免这样做的陷阱。

Git的主要工作是确保您永远不会丢失所做的更改。 但它也旨在让您完全控制开发工作流程。 这包括让您准确定义项目历史记录的样子； 但是，这也可能会丢失提交。 Git在免责声明中提供了其历史记录重写命令，因为使用它们可能会导致内容丢失。

Git有几种存储历史记录和保存更改的机制。 这些机制包括：提交 `--amend` ， `git rebase` 和 `git reflog` 。 这些选项为您提供了强大的工作流程自定义选项。 在本教程结束时，您将熟悉使您重构Git提交的命令，并能够避免重写历史记录时经常遇到的陷阱。

## 更改最后提交： `git commit --amend`

该 `git commit --amend` 命令是修改最新提交的便捷方法。 它使您可以将分阶段的更改与先前的提交结合在一起，而无需创建全新的提交。 它也可以用于简单地编辑前一个提交消息而无需更改其快照。 但是，修改不仅会更改最近的提交，还会将其完全替换，这意味着修改后的提交将是具有自己引用的新实体。 对于Git来说，它看起来像是一个全新的提交，在下图中用星号（\*）可视化。 有几种常见的使用场景 `git commit --amend` 。 我们将在以下各节中介绍用法示例。

![Git提交修改](https://wac-cdn.atlassian.com/dam/jcr:a4de784b-3572-4d23-8c68-cea9ad4f205f/01.svg?cdnVersion=1084)

### 更改最新的Git提交消息

```
git commit --amend

```

假设您刚提交，而在提交日志消息中犯了一个错误。 在未暂存任何内容的情况下运行此命令，可以在不更改其快照的情况下编辑先前提交的消息。

在您的日常开发过程中，所有时间都会发生过早的提交。 很容易忘记以错误的方式暂存文件或格式化提交消息。 该 `--amend` 标志是解决这些小错误的便捷方法。

```
git commit --amend -m "an updated commit message"

```

添加该 `-m` 选项使您可以从命令行传递新消息，而不会提示您打开编辑器。

### 更改提交的文件

以下示例演示了基于Git的开发中的常见场景。 假设我们已经编辑了一些要在单个快照中提交的文件，但是随后我们忘记了第一次添加其中一个文件。 修复错误仅是暂存另一个文件并使用 `--amend` 标志 提交的问题 ：

```
# Edit hello.py and main.py git add hello.py git commit
# Realize you forgot to add the changes from main.py git add main.py
git commit --amend --no-edit

```

该 `--no-edit` 标志将允许您在不更改其提交消息的情况下对提交进行修改。 所得到的承诺将取代不完整的一个，它会像我们所犯下的变化 `hello.py` ，并 `main.py` 在一个单一的快照。

### 不要修改公共承诺

修改后的提交实际上是全新的提交，而先前的提交将不再位于您的当前分支上。 这具有与重置公共快照相同的结果。 避免修改其他开发人员基于其所做的提交。 对于开发人员来说，这是一个令人困惑的情况，并且要从中恢复很复杂。

### 回顾

要进行审查， `git commit --amend` 可让您进行最近的提交并向其添加新的阶段更改。 您可以在Git暂存区中添加或删除更改以应用 `--amend` 提交。 如果未进行任何更改， `--amend` 仍然会提示您修改最后的提交消息日志。 在 `--amend` 与其他团队成员共享的提交上 使用时要谨慎 。 修改与其他用户共享的提交可能会导致混乱且冗长的合并冲突解决方案。

## 更改较早或多次提交

要修改较旧的或多个提交，可以使用 `git rebase` 将一系列提交合并到一个新的基本提交中。 在标准模式下， `git rebase` 允许您从字面上重写历史记录\-将当前工作分支中的提交自动应用于传递的分支头。 由于您的新提交将替换旧提交，因此重要的是不要 `git rebase` 在已公开发布的提交上 使用 ，否则项目历史记录将消失。

在这些或类似情况下，保留干净的项目历史非常重要，请添加 `-i` 选项以 `git rebase` 允许您运行 `rebase interactive` 。 这使您有机会更改流程中的各个提交，而不是移动所有提交。 您可以在 [git rebase页面](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase) 上了解有关交互式变基和其他变基命令的更多信息 。

#### 更改提交的文件

在重新设置基准期间，edit或 `e` 命令将在提交时暂停重新基准的重放，并允许您使用 `git commit --amend` Git 进行其他更改 将中断重放并显示一条消息：

```
Stopped at 5d025d1... formatting
You can amend the commit now, with
git commit --amend
Once you are satisfied with your changes, run
git rebase --continue

```

#### 多条消息

每个常规的Git提交都会有一条日志消息，说明提交中发生了什么。 这些消息提供了对项目历史的宝贵见解。 在重新设置基准期间，可以对提交运行一些命令以修改提交消息。

*   Reword或“ r”将停止重新播放基准，并允许您在此期间重写单个提交消息。
*   在重新播放基准值期间压扁或“ s”，所有标记的提交 `s` 都将暂停，并且系统将提示您将单独的提交消息编辑为合并的消息。 有关此问题的更多信息，请参见下面的壁球提交部分。
*   Fixup或“ f”具有与壁球相同的结合效果。 与squash不同，修正提交不会中断rebase的回放以打开编辑器来合并提交消息。 标记为“ f”的提交将丢弃其消息，而不是上一次提交的消息。

#### 壁球致力于清洁历史

在 `s` “ squash”命令中，我们可以看到真正的rebase实用程序。 Squash允许您指定要合并到先前提交中的提交。 这就是启用“清除历史记录”的原因。 在重新播放基准时，Git将为每次提交执行指定的rebase命令。 如果是南瓜提交，Git将打开您配置的文本编辑器，并提示您合并指定的提交消息。 整个过程可以如下所示：

![Git教程：git rebase -i示例](https://wac-cdn.atlassian.com/dam/jcr:2d03f5b6-eaa6-4e78-9dd7-3686ba2a7665/05.svg?cdnVersion=1084)

请注意，使用rebase命令修改的提交具有与两个原始提交不同的ID。 如果先前的提交已被重写，则标记为pick的提交将具有新的ID。

像Bitbucket这样的现代Git托管解决方案现在在合并后提供“自动压缩”功能。 当使用托管解决方案用户界面时，这些功能将自动为您重新设置基础和压缩分支的提交。 有关更多信息，请参见“ [将Git分支与Bitbucket合并时，Squash提交](https://bitbucket.org/blog/git-squash-commits-merging-bitbucket) ”。

### 回顾

Git变基使您能够修改历史记录，而交互式变基则使您能够进行修改，而不会留下“混乱”的痕迹。 这样就可以自由地进行错误和更正错误，优化您的工作，同时仍保持干净，线性的项目历史记录。

## 安全网：git reflog

引用日志或“引用日志”是Git用来记录应用于分支提示和其他提交引用的更新的机制。 Reflog允许您返回到提交，即使它们没有被任何分支或标记引用。 重写历史记录后，刷新日志包含有关分支的旧状态的信息，并在必要时允许您返回到该状态。 每次由于任何原因（通过切换分支，引入新更改，重写历史记录或仅通过添加新提交）更新分支提示时，都会在reflog中添加新条目。 在本节中，我们将深入了解该 `git reflog` 命令并探索一些常见用法。

### 用法

```
git reflog

```

这将显示本地存储库的引用日志。

```
git reflog --relative-date

```

这显示带有相关日期信息的reflog（例如2周前）。

### 例

要了解 `git reflog` ，让我们来看一个例子。

```
0a2e358 HEAD@{0}: reset: moving to HEAD~2
0254ea7 HEAD@{1}: checkout: moving from 2.2 to master
c10f740 HEAD@{2}: checkout: moving from master to 2.2

```

上面的reflog显示了从master到2.2分支并返回的签出。 从那里开始，硬重置为较早的提交。 最近的活动显示在顶部的 `HEAD@{0}` 。

如果事实证明您不小心将其移回，则reflog中将包含 `(0254ea7)` 您意外删除2个提交之前 指向的提交主机 。

`git reset --hard 0254ea7`

使用Git reset，现在可以将master更改回之前的提交。 如果历史记录意外更改，这将提供一个安全网。

重要的是要注意，如果更改已提交到本地存储库，则reflog仅提供安全网，并且仅跟踪存储库分支提示的移动。 另外，刷新日志条目具有到期日期。 reflog条目的默认到期时间为90天。

有关更多信息，请参见我们的 `[git reflog](https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog)` 页面。

## 摘要

在本文中，我们讨论了几种更改git历史记录和撤消git更改的方法。 我们对git rebase流程进行了深入研究。 一些关键要点是：

*   有很多方法可以用git重写历史记录。
*   使用 `git commit --amend` 改变你的最新的日志信息。
*   用于 `git commit --amend` 修改最近的提交。
*   使用 `git rebase` 相结合的提交和修改分支的历史。
*   `git rebase -i` 与标准git rebase相比，对历史记录的修改提供了更为精细的控制。

了解有关我们在其各个页面上介绍的命令的更多信息：

*   [git rebase](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase)
*   [git reflog](https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog)