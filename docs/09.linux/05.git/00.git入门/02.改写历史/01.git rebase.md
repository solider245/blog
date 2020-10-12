---
title: git rebase
date: 2020-10-12 12:09:51
permalink: /pages/8f4d7d/
categories:
  - git入门
  - 改写历史
tags:
  - 
---
# git rebase

本文档将作为对该 `git rebase` 命令 的深入讨论 。 还可以在 [设置存储库](https://www.atlassian.com/git/tutorials/setting-up-a-repository) 和 [重写历史记录](https://www.atlassian.com/git/tutorials/rewriting-history) 页面 上查看Rebase命令 。 该页面将更详细地介绍 `git rebase` 配置和执行。 此处将介绍常见的Rebase用例和陷阱。

Rebase是两个Git实用程序之一，专门用于将更改从一个分支集成到另一个分支。 另一个变更集成实用程序是 `git merge` 。 合并始终是向前移动的更改记录。 另外，rebase具有强大的历史记录重写功能。 有关合并与变基的详细信息，请访问我们的 [合并与变基指南](https://www.atlassian.com/git/tutorials/merging-vs-rebasing) 。 Rebase本身有2种主要模式：“手动”和“交互”模式。 我们将在下面详细介绍不同的Rebase模式。

## 什么是git rebase？

变基是将一系列提交或移动到新的基本提交中的过程。 在功能分支工作流的上下文中，重新定基最有用，并且很容易可视化。 一般过程可以如下所示：

![Git教程：Git变基](https://wac-cdn.atlassian.com/dam/jcr:e4a40899-636b-4988-9774-eaa8a440575b/02.svg?cdnVersion=1084)

从内容的角度来看，重新定基将分支的基础从一次提交更改为另一次提交，使其看起来就像您是从另一次提交创建分支一样。 在内部，Git通过创建新的提交并将它们应用于指定的基础来实现这一点。 重要的是要理解，即使分支看起来相同，它也由全新的提交组成。

## 用法

进行基础调整的主要原因是要保持线性的项目历史记录。 例如，考虑自您开始处理功能分支以来master分支已进行的情况。 您希望获得功能分支中master分支的最新更新，但您希望保持分支的历史记录整洁，因此看起来好像您正在使用最新的master分支。 这提供了以后将功能分支完全合并回master分支的好处。 我们为什么要保持“干净的历史”？ 执行Git运算以研究回归的引入时，拥有干净的历史记录的好处变得明显。 一个更真实的场景是：

1.  在master分支中发现了一个错误。 成功运行的功能现在已损坏。
2.  `git log` 由于“干净的历史记录”，因此开发人员可以快速推断出项目的历史记录，从而 检查master分支 的历史记录。
3.  开发人员无法识别何时使用引入了错误， `git log` 因此开发人员执行 `git bisect` 。
4.  由于git历史记录是干净的， `git bisect` 因此在查找回归时具有一组完善的提交进行比较。 开发人员可以迅速找到引入该错误的提交，并能够采取相应的措施。

在各自的用法页面上 了解有关 [git log](https://www.atlassian.com/git/tutorials/git-log) 和 [git bisect的](https://git-scm.com/docs/git-bisect) 更多信息 。

将功能集成到master分支有两种选择：直接合并或重新设置基础，然后合并。 前一个选项将导致三向合并和合并提交，而后一个选项将导致快速前进合并和完美的线性历史记录。 下图说明了重新建立到master分支的基础如何促进快速合并。

![Git变基：分支到母版](https://wac-cdn.atlassian.com/dam/jcr:d3b2abde-d06a-47b6-8955-5f3ef34e0237/03.svg?cdnVersion=1084)

变基是将上游更改集成到本地存储库中的常用方法。 每当您想查看项目进展情况时，使用Git合并引入上游更改都会导致多余的合并提交。 另一方面，变基就像是说：“我想基于每个人已经做的事情来进行更改。”

### 不要重新建立公共历史

正如我们在 [重写历史记录中](https://www.atlassian.com/git/tutorials/rewriting-history) 先前讨论的那样， 一旦将提交推送到公共存储库后，您就不应 [重新设置](https://www.atlassian.com/git/tutorials/rewriting-history) 提交的基准。 重新建立基础将用新提交替换旧提交，并且看起来项目历史的那部分突然消失了。

### Git Rebase Standard与Git Rebase Interactive

git rebase交互式是git rebase接受 `-- i` 参数时。 这代表“交互式”。 不带任何参数的命令将以标准模式运行。 在这两种情况下，假设我们都创建了一个单独的功能分支。

```
# Create a feature branch based off of master
git checkout -b feature_branch master
# Edit files
git commit -a -m "Adds new feature"

```

标准模式下的Git rebase将自动在当前工作分支中获取提交，并将其应用到传递的分支的头部。

```
git rebase <base>
```

这会自动将当前分支重新设置为 `<base>` ，可以是任何类型的提交引用（例如ID，分支名称，标记或的相对引用 `HEAD` ）。

`git rebase` 与该 `-i` 标志 一起 运行 将 开始一个交互式重新基准化会话。 交互式重定基础不是盲目地将所有提交移至新的基础，而是使您有机会在流程中更改单个提交。 这使您可以通过删除，拆分和更改现有的一系列提交来清理历史记录。 这就像 `Git commit --amend` 类固醇。

```
git rebase --interactive <base>
```

这将当前分支重新建立基础， `<base>` 但使用了交互式重新基准化会话。 这将打开一个编辑器，您可以在其中输入命令（如下所述）以重新确定每次提交的提交。 这些命令确定如何将单个提交转移到新的基础上。 您还可以重新排列提交列表的顺序，以更改提交本身的顺序。 在为rebase中的每个提交指定命令后，Git将开始播放应用rebase命令的提交。 变基编辑命令如下：

```

pick 2231360 some old commit
pick ee2adc2 Adds new feature
# Rebase 2cf755d..ee2adc2 onto 2cf755d (9 commands)
#
# Commands:
# p, pick = use commit
# r, reword = use commit, but edit the commit message
# e, edit = use commit, but stop for amending
# s, squash = use commit, but meld into previous commit
# f, fixup = like "squash", but discard this commit's log message
# x, exec = run command (the rest of the line) using shell
# d, drop = remove commit

```

#### 其他变基命令

如 [重写历史记录页面中所述](https://www.atlassian.com/git/tutorials/rewriting-history) ，重定基础可用于更改较旧的提交和多个提交，已提交的文件以及多个消息。 尽管这些是最常见的应用程序，但 `git rebase` 也具有其他命令选项， 这些 选项在更复杂的应用程序中很有用。

*   `git rebase -- d` 意味着在回放期间，提交将从最终的合并提交块中被丢弃。
*   `git rebase -- p`  保持提交不变。 它不会修改提交的消息或内容，并且仍然是分支历史中的单个提交。
*   `git rebase -- x`  在回放期间，将在每个标记的提交上执行命令行外壳脚本。 一个有用的示例是在特定的提交上运行您的代码库的测试套件，这可能有助于确定在进行重新设置期间的回归。

### 回顾

交互式重新定型使您可以完全控制项目历史记录。 这为开发人员提供了很多自由，因为它使他们在专注于编写代码时提交“混乱的”历史记录，然后回过头来对事实进行清理。

大多数开发人员喜欢在将功能分支合并到主代码库之前使用交互式基础库来完善功能分支。 这使他们有机会压缩微不足道的提交，删除过时的提交，并在提交“正式”项目历史记录之前确保其他一切都按顺序进行。 对其他人来说，整个功能似乎是在一系列精心计划的提交中开发的。

交互基础的真正力量可以在生成的主分支的历史中看到。 对其他人来说，您似乎是一位出色的开发人员，他在第一时间就以完美的提交量实施了新功能。 这就是交互式基础调整可以使项目的历史保持整洁和有意义的方式。

### 配置选项

可以使用设置一些变基属性 `git config` 。 这些选项将改变 `git rebase` 输出的外观。

*   **`rebase.stat`** ：默认情况下设置为false的布尔值。 该选项切换可视化diffstat内容的显示，以显示自上次降级以来发生的变化。

*   **`rebase.autoSquash:`** 切换 `--autosquash` 行为的 布尔值 。

*   **`rebase.missingCommitsCheck:`** 可以设置为多个值，这些值将更改丢失的提交周围的基准行为。

| `warn` | 以交互方式打印警告输出，警告已删除的提交 |
|

`error`

 | 停止变基并打印已删除的提交警告消息 |
|

`ignore`

 | 默认设置为忽略任何丢失的提交警告 |

*   **`rebase.instructionFormat:`** 一个 `git log` 将被用于格式化交互式的rebase显示格式字符串

### 高级基础应用程序

命令行参数 ` --onto` 可以传递给 `git rebase` 。 在git rebase `--onto` 模式下，命令扩展为：

```
 git rebase --onto <newbase> <oldbase>

```

该 `--onto` 命令将启用更强大的表单或变基，它允许传递特定的引用作为变基的技巧。
假设我们有一个带有分支的示例仓库：

```

   o---o---o---o---o master
        \
         o---o---o---o---o featureA
              \
               o---o---o featureB

```

FeatureB基于FeatureA，但是，我们意识到FeatureB不依赖于featureA的任何更改，而可以从master分支出来。

```
 git rebase --onto master featureA featureB

```

featureA是 `<oldbase>` 。 `master` 成为 `<newbase>` 与featureB是为了什么参考 `HEAD` 的 `<newbase>` 将指向。 结果为：

```

                      o---o---o featureB
                     /
    o---o---o---o---o master
     \
      o---o---o---o---o featureA

```

## 了解变基的危险

使用Git Rebase时要考虑的一个警告是合并冲突在rebase工作流程中可能会变得更加频繁。 如果您的分支的寿命长于master，则会发生这种情况。 最终，您将需要以master为基础，这时它可能包含分支更改可能与之冲突的许多新提交。 可以通过经常根据主分支重新分支分支并进行更频繁的提交来轻松地解决此问题。 该 `--continue` 和 `--abort` 命令行参数可以传递到 `git rebase` 推进或冲突时重置的底垫。

更为严重的rebase警告是交互式历史记录重写丢失了提交。 以交互方式运行rebase并执行squash或drop之类的子命令将从您分支的立即日志中删除提交。 乍一看，这似乎使提交永久消失了。 使用 `git reflog` 这些提交可以还原，并且整个撤消基准可以撤消。 有关 `git reflog` 用于查找丢失的提交的 更多信息 ，请访问我们的 [Git reflog文档页面](https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog) 。

Git Rebase本身并不严重危险。 当执行历史记录重写交互式rebase并强行将结果推送到其他用户共享的远程分支时，就会出现真正的危险情况。 应避免这种模式，因为它具有在拉动其他远程用户的工作时将其覆盖的功能。

## 从上游基准恢复

如果另一个用户已经重新建立基础并强行推送到您要提交的分支，则a `git pull` 将用强行推送的提示覆盖基于该先前分支的所有提交。 幸运的是，使用 `git reflog` 您可以获得远程分支的引用日志。 在远程分支的reflog上，您可以在重新建立基准之前找到它。 然后，您可以使用 `--onto` 上面“高级基础应用程序”部分中讨论 的 选项， 根据该远程引用对分支进行基础化 。

## 摘要

在本文中，我们介绍了 `git rebase` 用法。 我们讨论了基本和高级用例以及更多高级示例。 一些关键的讨论要点是：

*   git rebase标准vs交互模式
*   git rebase配置选项
*   git rebase \-\-onto
*   git rebase丢失的提交

我们期待在 `git rebase` 使用与其他工具一样 [`git reflog`](https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog) ， [`git fetch`](https://www.atlassian.com/git/tutorials/syncing#git-fetch) 和 [`git push`](https://www.atlassian.com/git/tutorials/syncing#git-push) 。 访问他们相应的页面以获取更多信息。