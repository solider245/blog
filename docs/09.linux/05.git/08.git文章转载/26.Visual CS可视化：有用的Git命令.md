---
title: Visual CS可视化：有用的Git命令
date: 2020-10-12 12:09:51
permalink: /pages/180c8c/
categories:
  - git
  - git文章转载
tags:
  - 
---
# Visual CS可视化：有用的Git命令

[＃混帐](https://dev.to/t/git) [＃计算机科学](https://dev.to/t/computerscience) [＃教程](https://dev.to/t/tutorial)

 [![lydiahallie的头像](https://res.cloudinary.com/practicaldev/image/fetch/s--nmvhuKA7--/c_fill,f_auto,fl_progressive,h_50,q_auto,w_50/https://dev-to-uploads.s3.amazonaws.com/uploads/user/profile_image/198900/f497603e-77e4-4cfc-ae1a-a9214062aac4.jpeg) 莉迪亚·哈莉（Lydia Hallie）](https://dev.to/lydiahallie)  4月1 ・阅读9分钟

尽管Git是一个非常强大的工具，但我认为大多数人都会同意我的话……一场噩梦😐我一直觉得将Git的使用情况可视化非常有用：当我执行某个命令时，分支交互，这将如何影响历史？ 为什么在我进行硬重置 `master` ， `force push` 原始设置和 `rimraf` “ d” `.git` 文件夹 时同事会哭泣 ？

我认为这是创建最常见和最有用命令的可视化示例的完美用例！ I我要介绍的许多命令都有可选参数，您可以使用这些参数来更改其行为。 在我的示例中，我将介绍这些命令的默认行为，而无需添加（太多）配置选项！ 😄

| [合并](#merge) | [变基](#rebase) | [重启](#reset) | [还原](#revert) | [樱桃采摘](#cherry-pick) | [取](#fetch) | [拉](#pull) | [刷新日志](#reflog) |

---

## [](#merging)合并中

拥有多个分支机构非常方便，以使新的变更彼此分开，并确保您不会意外将未经批准或破损的变更推到生产中。 更改获得批准后，我们​​希望在生产部门中获得这些更改！

将更改从一个分支转移到另一个分支的一种方法是执行 `git merge` !！ Git可以执行两种类型的合并： **快进** 或 **无快进** 🐢

现在这可能没有多大意义，所以让我们看一下差异！

### [](#fastforward-raw-ff-endraw-)快进（ `--ff` ）

一个 **快进合并** 相比，我们正在合并分支当前分支已经没有多余的提交可能发生。 Git是... *懒惰，* 并且首先会尝试执行最简单的选择：快速前进！ 这种类型的合并不会创建新的提交，而是在我们当前分支中要合并的分支上合并提交🥳

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--cT4TSe48--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/894znjv4oo9agqiz4dql.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--cT4TSe48--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/894znjv4oo9agqiz4dql.gif)

完善！ 现在，我们 `dev` 可以在分支上获得对 `master` 分支 所做的所有更改 。 那么，什么 **都不是快进** 呢？

### [](#nofastfoward-raw-noff-endraw-)不速前进（ `--no-ff` ）

如果您当前的分支与您要合并的分支相比没有任何额外的提交，那就太好了，但是不幸的是，这种情况很少！ 如果我们在当前分支上提交了要合并的分支所没有的更改，则git将执行 *no\-fast\-forward* 合并。

通过无快进合并，Git 在活动分支上 创建了一个新的 *合并提交* 。 提交的父提交既指向活动分支又指向我们要合并的分支！

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--zRZ0x2Vc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/rf1o2b6eduboqwkigg3w.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--zRZ0x2Vc--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/rf1o2b6eduboqwkigg3w.gif)

没什么大不了的，完美的合并！ `master` branch现在 ， 分支包含我们在 `dev` 分支 上所做的所有更改 。

### [](#merge-conflicts)合并冲突

尽管Git擅长决定如何合并分支并向文件中添加更改，但是它不能总是自己一个人做出决定decision当我们尝试合并的两个分支在同一文件中的同一行上有更改时，可能会发生这种情况，或者一个分支删除了另一个分支修改的文件，依此类推。

在这种情况下，Git将要求您帮助确定我们要保留的两个选项中的哪一个！ 假设在两个分支上，我们都编辑了第一行 `README.md` 。

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--jXqGWUai--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/m3nxmp67mqof5sa3iik9.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--jXqGWUai--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/m3nxmp67mqof5sa3iik9.png)

如果要合并 `dev` 到 `master` ，将导致合并冲突：您希望标题是 `Hello!` 还是 `Hey!` ？

尝试合并分支时，Git将向您显示冲突发生的位置。 我们可以手动删除不想保留的更改，保存更改，再次添加更改的文件，然后提交更改🥳

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--7lBksXwA--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/bcd5ajtoc0g5dxzmpfbq.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--7lBksXwA--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/bcd5ajtoc0g5dxzmpfbq.gif)

好极了！ 尽管合并冲突通常很烦人，但这是完全有意义的：Git不应该仅仅 *假设* 我们要保留哪个更改。

---

## [](#rebasing)变基

我们刚刚看到了如何通过执行可以将更改从一个分支应用于另一个分支 `git merge` 。 将更改从一个分支添加到另一个分支的另一种方法是执行 `git rebase` 。

一个 `git rebase` *副本* 从当前分支的提交，并提出这些复制提交指定的分支上。

[![](https://res.cloudinary.com/practicaldev/image/fetch/s--EIY4OOcE--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/dwyukhq8yj2xliq4i50e.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--EIY4OOcE--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/dwyukhq8yj2xliq4i50e.gif)

完美，我们现在可以在 `master` 分支上使用 `dev` 分支 上 所做的所有更改 ！ 🎊

与合并相比，Git的最大区别是Git不会尝试找出要保留和不保留的文件。 我们要重新定位的分支始终具有我们要保留的最新更改！ 这样您就不会遇到任何合并冲突，并且可以保持良好的线性Git历史记录。

此示例显示了在 `master` 分支 上的基础 。 但是，在较大的项目中，您通常不想这样做。 当 为复制的提交创建新的哈希值时 `git rebase` **，** A会**更改项目的历史记录** ！

每当您在功能分支上工作并且主分支已更新时，重新设置功能都很棒。 您可以在分支上获取所有更新，这将防止将来发生合并冲突！ 😄

### [](#interactive-rebase)互动基础

在重新提交之前，我们可以对其进行修改！ can我们可以通过 *交互式基础* 来做到这一点 。 交互式基础也可以在您当前正在使用的分支上使用，并且希望修改某些提交。

我们可以对要重定的提交执行6个操作：

*   `reword` ：更改提交消息
*   `edit` ：修改此提交
*   `squash` ：将提交合并到上一个提交中
*   `fixup` ：将提交合并到上一个提交中，而不保留提交的日志消息
*   `exec` ：对要重新设置基准的每个提交运行命令
*   `drop` ：删除提交

太棒了！ 这样，我们可以完全控制提交。 如果我们想删除一个提交，就可以 `drop` 了。

[![替代文字](https://res.cloudinary.com/practicaldev/image/fetch/s--P6jr7igd--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/msofpv7k6rcmpaaefscm.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--P6jr7igd--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/msofpv7k6rcmpaaefscm.gif)

或者，如果我们要压缩多个提交以获取更清晰的历史记录，那没问题！

[![替代文字](https://res.cloudinary.com/practicaldev/image/fetch/s--VSQt4g1V--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/bc1r460xx1i0blu0lnnm.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--VSQt4g1V--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/bc1r460xx1i0blu0lnnm.gif)

交互式重定基础使您可以对要重定基础的提交（即使在当前活动分支上）进行很多控制！

---

## [](#resetting)重设

可能发生了我们提交了以后不想要的更改。 也许是一个 `WIP` 提交，或者一个引入了错误的提交！ that在这种情况下，我们可以执行 `git reset` 。

一个 `git reset` 摆脱当前的所有筹备的文件，对我们的控制权，其中 `HEAD` 应指向。

### [](#soft-reset)软重置

一个 *软复位* 移动 `HEAD` 到指定的提交（或相对于提交的指数 `HEAD` ），没有摆脱被引入于事后提交的变化！

假设我们不想保留 `9e78i` 添加 `style.css` 文件 的提交 ， 也不想保留 `035cc` 添加 `index.js` 文件 的提交 。 但是，我们要保持最新添加 `style.css` 和 `index.js` 档案！ 软复位的理想用例。

[![](https://res.cloudinary.com/practicaldev/image/fetch/s---GveiZe---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/je5240aqa5uw9d8j3ibb.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s---GveiZe---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/je5240aqa5uw9d8j3ibb.gif)

输入时 `git status` ，您会看到我们仍然可以访问对先前提交所做的所有更改。 太好了，因为这意味着我们可以修复这些文件的内容，以后再提交！

### [](#hard-reset)硬重置

有时，我们不想保留某些提交所引入的更改。 与软重置不同，我们不再需要访问它们。 Git应该简单地将其状态重置为指定提交时的状态：这甚至包括工作目录和暂存文件中的更改！ 💣

[![替代文字](https://res.cloudinary.com/practicaldev/image/fetch/s--GqjwnYkF--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/hlh0kowt3hov1xhcku38.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--GqjwnYkF--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/hlh0kowt3hov1xhcku38.gif)

Git放弃了在 `9e78i` 和 上引入的更改 `035cc` ，并将其状态重置为提交时的状态 `ec5be` 。

---

### [](#reverting)正在还原

取消更改的另一种方法是执行 `git revert` 。 通过还原某个提交，我们创建一个 包含还原更改 的 *新提交* ！

假设 `ec5be` 添加了一个 `index.js` 文件。 后来，我们实际上意识到我们不再希望此提交引入此更改！ 让我们还原 `ec5be` 提交。

[![替代文字](https://res.cloudinary.com/practicaldev/image/fetch/s--eckmvr2M--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/3kkd2ahn41zixs12xgpf.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--eckmvr2M--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/3kkd2ahn41zixs12xgpf.gif)

完善！ 提交 `9e78i` 还原了 提交 所引入的更改 `ec5be` 。 执行a `git revert` 对于撤消特定提交而不修改分支的历史记录非常有用。

---

## [](#cherrypicking)采摘樱桃

当某个分支包含一个引入了我们活动分支所需的更改的提交时，我们可以执行 `cherry-pick` 该命令！ 通过 `cherry-pick` 提交，我们在活动分支上创建了一个新的提交，其中包含 `cherry-pick` ed提交 所引入的更改 。

假设 `76d12` 在 `dev` 分支 上的 提交 将更改添加到 `index.js` 我们想要在 `master` 分支中 的 文件 。 我们不想 *整个* 我们只关心一次提交！

[![替代文字](https://res.cloudinary.com/practicaldev/image/fetch/s--9vWP_K4S--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/2dkjx4yeaal10xyvj29v.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--9vWP_K4S--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/2dkjx4yeaal10xyvj29v.gif)

太酷了，master分支现在包含了 `76d12` 引入 的更改 ！

---

## [](#fetching)正在取得

如果我们有一个远程Git分支，例如Github上的一个分支，则可能发生该远程分支具有当前分支所没有的提交！ 也许另一个分支被合并了，您的同事提出了快速解决方案，依此类推。

通过 `git fetch` 在远程分支上 执行a，我们可以在本地获取这些更改 ！ 它不会以任何方式影响您的本地分支机构： `fetch` 只需下载新数据即可。

[![替代文字](https://res.cloudinary.com/practicaldev/image/fetch/s--38PuARw2--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/bulx1voegfji4vwgndh4.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--38PuARw2--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/bulx1voegfji4vwgndh4.gif)

现在，我们可以看到自上次推送以来所做的所有更改！ 现在，我们可以在本地拥有新数据，然后决定要处理的数据。

---

## [](#pulling)拉动

尽管a `git fetch` 对于获取分支的远程信息非常有用，但是我们也可以执行a `git pull` 。 A `git pull` 实际上是两个命令合二为一：a `git fetch` 和a `git merge` 。 当我们从原点提取更改时，我们首先要像使用一样获取所有数据 `git fetch` ，之后最新的更改会自动合并到本地分支中。

[![替代文字](https://res.cloudinary.com/practicaldev/image/fetch/s---X5AXldj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/zifpnl1h6a4tk4qdc9sy.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s---X5AXldj--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/zifpnl1h6a4tk4qdc9sy.gif)

太棒了，我们现在可以与远程分支完美同步，并具有所有最新更改！ 🤩

---

## [](#reflog)刷新日志

每个人都会犯错，那完全可以！ 有时，您可能会觉得自己已经严重破坏了git repo，以至于您只想完全删除它。

`git reflog` 为了显示已执行的所有操作的日志，这是一个非常有用的命令！ 这包括合并，重置，还原：基本上是对分支的任何更改。

[![替代文字](https://res.cloudinary.com/practicaldev/image/fetch/s--MMUdOS0P--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/1aqek1py1knwl926ele7.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--MMUdOS0P--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/1aqek1py1knwl926ele7.gif) ）

如果您输入有误，可以 `HEAD` 根据 `reflog` 提供给我们 的信息 进行重置，轻松地重做 ！

假设我们实际上不想合并origin分支。 当执行 `git reflog` 命令时，我们看到合并之前仓库的状态为 `HEAD@{1}` 。 让我们执行一个 `git reset` 将HEAD指向它所在的位置 `HEAD@{1}` ！

[![替代文字](https://res.cloudinary.com/practicaldev/image/fetch/s--A1UMM2AH--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/9z9rhtbw7mrigp0miijz.gif)](https://res.cloudinary.com/practicaldev/image/fetch/s--A1UMM2AH--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_66%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/9z9rhtbw7mrigp0miijz.gif)

我们可以看到最新动作已被推送到 `reflog` ！

---

Git有很多有用的瓷器和管道命令，我希望我能涵盖所有这些！ know我知道我现在还没有时间介绍许多其他命令或变更\-让我知道您最喜欢/最有用的命令是什么，我可能会在另一篇文章中介绍它们！

和往常一样，随时与我联系！ 😊