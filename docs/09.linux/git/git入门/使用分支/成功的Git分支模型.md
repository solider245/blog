---
title: 成功的Git分支模型
date: 2020-10-12 12:09:51
permalink: /pages/1ecae1/
categories:
  - git入门
  - 使用分支
tags:
  - 
---
> ### 反思笔记 （2020年3月5日）
>
> 这个模型是在2010年构思出来的，而现在距今已有10多年了，而Git本身才诞生不久。 在那10年中，git\-flow（本文介绍的分支模型）在许多软件团队中变得非常流行，以至于人们开始将其视为某种标准，但不幸的是，它也被当作教条或灵丹妙药。 。
>
> 在那10年中，Git本身就席卷了整个世界，并且与Git一起开发的最流行的软件类型正在越来越多地转向Web应用程序\-至少在我的过滤泡中。 Web应用程序通常是连续交付的，不会回滚，并且您不必支持在野外运行的软件的多个版本。
>
> 这不是我十年前写博客时想到的那种软件。 如果您的团队正在持续交付软件，我建议您采用更简单的工作流程（例如 [GitHub flow](https://guides.github.com/introduction/flow/) ），而不是尝试将git\-flow引入您的团队。
>
> 但是，如果您正在构建显式版本的软件，或者如果您需要狂野地支持软件的多个版本，那么git\-flow仍然可能像适合您团队的人一样适合您的团队最近10年。 在这种情况下，请继续阅读。
>
> 总而言之，请始终记住万灵药不存在。 考虑您自己的情况。 别讨厌 自行决定。

在这篇文章中，我介绍了大约一年前为我的一些项目（在工作中和在私人项目中）引入的开发模型，事实证明该模型非常成功。 我一直想写一阵子，但是直到现在，我还没有真正找到彻底这样做的时间。 我不会谈论任何项目的细节，而只会谈论分支策略和发布管理。

![](https://nvie.com/img/git-model@2x.png)

## 为什么是git？ [¶](#why-git)

有关Git与集中式源代码控制系统相比的优缺点的详尽讨论，请参见 [Web](http://git.or.cz/gitwiki/GitSvnComparsion) 。 那里发生了许多火焰大战。 作为开发人员，我比今天所有其他工具都更喜欢Git。 Git确实改变了开发人员对合并和分支的看法。 从我来自经典的CVS / Subversion的世界来看，合并/分支一直被认为有点吓人（“当心合并冲突，它们会咬你！”），而您却偶尔会做一次。

但是，使用Git，这些操作非常便宜且简单，实际上，它们被视为 *日常* 工作流程 的核心部分之一 。 例如，在CVS / Subversion [书籍中](http://svnbook.red-bean.com) ，分支和合并首先在后面的章节中（针对高级用户）进行讨论，而在 [每本](http://book.git-scm.com) [Git](http://pragprog.com/titles/tsgit/pragmatic-version-control-using-git) [书籍中](http://github.com/progit/progit) ，它都已在第3章（基础知识）中进行了讨论。

由于其简单性和重复性，分支和合并不再是令人害怕的事情。 版本控制工具应该比其他任何工具都更有助于分支/合并。

足够了解这些工具，让我们进入开发模型。 我将在此处介绍的模型实质上不过是每个团队成员必须遵循的一组程序才能进入托管软件开发过程。

## 分散但集中化 [¶](#decentralized-but-centralized)

我们使用的存储库设置与该分支模型一起很好地使用，它是一个中央“真实”存储库。 请注意，此回购仅 *被视为* 中心 回购 （由于Git是DVCS，因此在技术层面上没有中央回购之类的东西）。 我们将此仓库称为 `origin` ，因为所有Git用户都熟悉该名称。

![](https://nvie.com/img/centr-decentr@2x.png)

每个开发人员都将其拉到原点。 但是，除了集中的推拉关系之外，每个开发人员还可以从其他同伴那里拉出变更以组成子团队。 例如，在将进行中的工作 `origin` 提前 进行之前，与两个或多个开发人员一起使用一项重要的新功能可能会很有用 。 在上图中，有Alice和Bob，Alice和David以及Clair和David的子团队。

从技术上讲，这仅意味着Alice定义了一个Git远程服务器，名为 `bob` ，指向Bob的存储库，反之亦然。

## 主要分支 [¶](#the-main-branches)

![](https://nvie.com/img/main-branches@2x.png)

从根本上说，开发模型的灵感来自那里的现有模型。 中央存储库拥有两个无限生命的主要分支：

*   `master`
*   `develop`

每个Git用户都应该熟悉 `master` at 的 分支 `origin` 。 与 `master` 分支 平行 ，存在另一个分支，称为 `develop` 。

我们认为 `origin/master` 它是源代码 `HEAD` 始终反映 *生产就绪* 状态 的主要分支 。

我们认为 `origin/develop` 这是主要分支，在该分支中，源代码 `HEAD` 始终反映状态以及下一版本最新交付的开发更改。 有人将其称为“整合分支”。 这是构建任何夜间自动构建的地方。

当 `develop` 分支中 的源代码 达到稳定点并准备发布时，所有更改都应以 `master` 某种方式 合并回去 ，然后用发布号进行标记。 如何进一步详细地进行讨论。

因此，每次将更改合并回时 `master` ， *根据定义* ，这是一个新的生产版本 。 我们通常对此非常严格，因此从理论上讲，每次提交时，我们都可以使用Git钩子脚本自动将软件构建和推出到生产服务器 `master` 。

## 支持分支 [¶](#supporting-branches)

在主要分支 `master` 和 旁边 `develop` ，我们的开发模型使用各种支持分支来协助团队成员之间的并行开发，简化功能跟踪，为产品发布做准备并协助快速解决生产中的问题。 与主要分支不同，这些分支的生命周期总是有限的，因为它们最终将被删除。

我们可能使用的不同类型的分支机构是：

*   功能分支
*   发布分支
*   修补程序分支

这些分支中的每一个都有特定的用途，并受严格的规则约束，即哪些分支可能是其原始分支，哪些分支必须是其合并目标。 我们将在一分钟内通过它们。

从技术角度来看，这些分支绝不是“特殊的”。 分支类型根据我们的 *使用方式* 进行分类 。 它们当然是普通的旧Git分支。

### 功能分支 [¶](#feature-branches)

![](https://nvie.com/img/fb@2x.png)

可能从以下分支：

`develop`

必须合并回：

`develop`

分支命名约定：

任何东西，除了 `master` ， `develop` ， `release-*` ，或者 `hotfix-*`

功能分支（或有时称为主题分支）用于为即将发布或遥远的将来版本开发新功能。 当开始开发功能时，此时可能不知道将合并该功能的目标版本。 功能分支的本质是只要功能正在开发中就存在，但是最终会合并回去 `develop` （以确保将新功能添加到即将发布的版本中）或丢弃（以防实验失败）。

功能分支通常仅存在于开发人员存储库中，而不存在于中 `origin` 。

#### 创建一个功能分支 [¶](#creating-a-feature-branch)

当开始使用新功能时，请从 `develop` 分支分支。

$ git checkout \-b myfeature develop
Switched to a new branch "myfeature"

#### 在development上包含完成的功能 [¶](#incorporating-a-finished-feature-on-develop)

可以将完成的功能合并到 `develop` 分支中，以确保将它们添加到即将发布的版本中：

$ git checkout develop
Switched to branch 'develop'
$ git merge \-\-no\-ff myfeature
Updating ea1b82a..05e9557
(Summary of changes)
$ git branch \-d myfeature
Deleted branch myfeature (was 05e9557).
$ git push origin develop

该 `--no-ff` 标志使合并始终创建一个新的提交对象，即使合并可以通过快进来执行。 这样可以避免丢失有关要素分支历史存在的信息，并将所有添加了要素的提交分组在一起。 比较：

![](https://nvie.com/img/merge-without-ff@2x.png)

在后一种情况下，无法从Git历史记录中看到哪些提交对象一起实现了功能—您将不得不手动读取所有日志消息。 在后一种情况下，还原整个功能（即一组提交）确实很头疼，而如果使用了 `--no-ff` 标志 ，则很容易做到 。

是的，它将创建更多（空）提交对象，但收益远大于成本。

### 发布分支 [¶](#release-branches)

可能从以下分支：

`develop`

必须合并回：

`develop` 和 `master`

分支命名约定：

`release-*`

发布分支支持新产品版本的准备。 他们允许我在最后一刻加点i和越过t。 此外，它们允许进行较小的错误修复并为发布准备元数据（版本号，构建日期等）。 通过在发行分支上完成所有这些工作，该 `develop` 分支将被清除以接收下一个大型发行版的功能。

从新分支中分支出来的关键时刻 `develop` 是开发（几乎）何时反映新版本的所需状态。 此时至少必须将要构建的发行版的所有目标功能合并到其中 `develop` 。 面向将来发行版的所有功能可能都不会—它们必须等到发行分支分支出来之后。

正是在发行分支的开始，才为即将发布的发行分配了版本号，而不是更早的版本号。 直到那一刻，该 `develop` 分支反映了“下一个发行版”的更改，但是直到发行分支开始之前，尚不清楚该“下一个发行版”最终将变为0.3还是1.0。 该决定是在版本分支的开始处做出的，并由项目的版本号增加规则来执行。

#### 创建一个发布分支 [¶](#creating-a-release-branch)

从 `develop` 分支 创建发行 分支。 例如，说版本1.1.5是当前的生产版本，我们即将发布一个大版本。 的状态 `develop` 准备好了“下一个版本”，我们已经决定，这将成为版本1.2（而不是1.1.6或2.0）。 因此，我们分支并为发布分支命名以反映新版本号：

$ git checkout \-b release\-1.2 develop
Switched to a new branch "release\-1.2"
$ ./bump\-version.sh 1.2
Files modified successfully, version bumped to 1.2.
$ git commit \-a \-m "Bumped version number to 1.2"
\[release\-1.2 74d9424\] Bumped version number to 1.2
1 files changed, 1 insertions(+), 1 deletions(\-)

创建新分支并切换到该分支后，我们更改版本号。 这里 `bump-version.sh` 是一个虚构的shell脚本，它更改了工作副本中的某些文件以反映新版本。 （当然，这可以是手动更改\-关键是 *某些* 文件会更改。）然后，提交 被 修改的版本号。

这个新分支可能在那里存在了一段时间，直到可以肯定地发布该版本为止。 在此期间，错误修复程序可能会应用于此分支（而不是 `develop` 分支）。 严格禁止在此处添加大型新功能。 它们必须合并到中 `develop` ，因此，请等待下一个重要版本。

#### 完成发布分支 [¶](#finishing-a-release-branch)

当发布分支的状态准备好成为真实发布时，需要执行一些操作。 首先，将release分支合并到其中 `master` （因为每次提交 `master` 都是 *定义* 上 的新发行版 ，请记住）。 接下来， `master` 必须标记 该提交， 以方便将来参考此历史版本。 最后，需要将在release分支上所做的更改重新合并到中 `develop` ，以便将来的发行版中也包含这些错误修复。

Git的前两个步骤：

$ git checkout master
Switched to branch 'master'
$ git merge \-\-no\-ff release\-1.2
Merge made by recursive.
(Summary of changes)
$ git tag \-a 1.2

该版本现已完成，并已标记以供将来参考。

> **编辑：** 您可能还想使用 `-s` 或 `-u <key>` 标志对您的标签进行加密签名。

为了保留在release分支中所做的更改，我们需要将这些更改重新合并到中 `develop` 。 在Git中：

$ git checkout develop
Switched to branch 'develop'
$ git merge \-\-no\-ff release\-1.2
Merge made by recursive.
(Summary of changes)

此步骤很可能导致合并冲突（可能甚至发生，因为我们已经更改了版本号）。 如果是这样，请修复它并提交。

现在我们真的完成了，可以删除发布分支，因为我们不再需要它了：

$ git branch \-d release\-1.2
Deleted branch release\-1.2 (was ff452fe).

### 修补程序分支 [¶](#hotfix-branches)

![](https://nvie.com/img/hotfix-branches@2x.png)

可能从以下分支：

`master`

必须合并回：

`develop` 和 `master`

分支命名约定：

`hotfix-*`

修补程序分支与发布分支非常相似，尽管它们是计划外的，但它们也旨在为新的生产版本做准备。 它们源于对不期望的实时生产版本状态立即采取行动的必要性。 当必须立即解决生产版本中的严重错误时，可以从标记生产版本的master分支上的相应标记中分支出一个修补程序分支。

本质是团队成员（ `develop` 分支机构）的工作可以继续进行，而另一个人正在准备快速生产修复。

#### 创建hotfix分支 [¶](#creating-the-hotfix-branch)

修补程序分支是从 `master` 分支 创建的 。 例如，说1.2版是当前的生产版本，正在运行，并且由于严重的错误而引起麻烦。 但是变化 `develop` 仍然不稳定。 然后，我们可能会分支出一个修补程序分支并开始解决问题：

$ git checkout \-b hotfix\-1.2.1 master
Switched to a new branch "hotfix\-1.2.1"
$ ./bump\-version.sh 1.2.1
Files modified successfully, version bumped to 1.2.1.
$ git commit \-a \-m "Bumped version number to 1.2.1"
\[hotfix\-1.2.1 41e61bb\] Bumped version number to 1.2.1
1 files changed, 1 insertions(+), 1 deletions(\-)

别忘了在分支后增加版本号！

然后，修复该错误并在一个或多个单独的提交中提交此修复程序。

$ git commit \-m "Fixed severe production problem"
\[hotfix\-1.2.1 abbe5d6\] Fixed severe production problem
5 files changed, 32 insertions(+), 17 deletions(\-)

#### 完成修补程序分支 [¶](#finishing-a-hotfix-branch)

完成后，该bugfix需要合并回 `master` ，但也需要合并回 `develop` ，以确保该bugfix也包含在下一发行版中。 这与释放分支的完成方式完全相似。

首先，更新 `master` 并标记发布。

$ git checkout master
Switched to branch 'master'
$ git merge \-\-no\-ff hotfix\-1.2.1
Merge made by recursive.
(Summary of changes)
$ git tag \-a 1.2.1

> **编辑：** 您可能还想使用 `-s` 或 `-u <key>` 标志对您的标签进行加密签名。

接下来，在 `develop` 中也 包含错误修正 ：

$ git checkout develop
Switched to branch 'develop'
$ git merge \-\-no\-ff hotfix\-1.2.1
Merge made by recursive.
(Summary of changes)

该规则的一个例外是， **当当前存在发行分支时，需要将修补程序更改合并到该发行分支中，而不是`develop`** 。 在发行分支完成后，将错误修正回合并到发行分支中，最终会导致将修正修正也合并到 `develop` 发行分支中。 （如果 `develop` 立即进行 工作 需要此错误修正，并且不能等待发布分支完成，则也可以安全地将错误修正合并到 `develop` 现在。）

最后，删除临时分支：

$ git branch \-d hotfix\-1.2.1
Deleted branch hotfix\-1.2.1 (was abbe5d6).

## 总结 [¶](#summary)

尽管此分支模型没有什么真正令人震惊的新东西，但本文开头的“全局”图在我们的项目中被证明非常有用。 它形成了一个易于理解的优雅思维模型，并允许团队成员对分支和发布过程形成共识。

此处提供了该图的高质量PDF版本。 快将它挂在墙上，以便随时参考。

**更新：** 对于要求它的任何人：这是 主图图像（Apple Keynote） 的 [gitflow\-model.src.key](http://github.com/downloads/nvie/gitflow/Git-branching-model-src.key.zip) 。