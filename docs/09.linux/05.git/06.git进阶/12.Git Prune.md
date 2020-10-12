---
title: Git Prune
date: 2020-10-12 12:09:51
permalink: /pages/90a68e/
categories:
  - git
  - git进阶
tags:
  - 
---
# Git Prune

该 `git prune` 命令是内部清理实用程序，用于清理无法访问或“孤立”的Git对象。 无法访问的对象是所有引用都无法访问的对象。 无法通过分支或标记访问的任何提交均被视为不可访问。 `git prune` 通常不会直接执行。 Prune被视为垃圾收集命令，并且是该命令的子 `[git gc](https://www.atlassian.com/git/tutorials/git-gc)` 命令。

## Git Prune概述

为了了解 `git prune` 我们 的影响， 我们需要模拟无法实现提交的情况。 以下是将模拟这种体验的一系列命令行执行。

```
~ $ cd git-prune-demo/~/git-prune-demo $ git init .Initialized empty Git repository in /Users/kev/Dropbox/git-prune-demo/.git/~/git-prune-demo $ echo "hello git prune" > hello.txt~/git-prune-demo $ git add hello.txt~/git-prune-demo $ git commit -am "added hello.txt"
```

前面的命令序列将在名为的目录中创建一个新的存储库 `git-prune-demo` 。 一个包含新文件的提交 `hello.text` 将添加到回购中，其基本内容为“ hello git prune”。 接下来，我们将创建修改， `hello.txt` 并根据这些修改创建一个新的提交。

```
~/git-prune-demo $ echo "this is second line txt" >> hello.txt~/git-prune-demo $ cat hello.txthello git prunethis is second line txt~/git-prune-demo $ git commit -am "added another line to hello.txt"[master 5178bec] added another line to hello.txt1 file changed, 1 insertion(+)
```

现在，此示例存储库中有2次提交历史记录。 我们可以使用 `git log` 以下 方法进行验证 ：

```
~/git-prune-demo $ git logcommit 5178becc2ca965e1728554ce1cb8de2f2c2370b1Author: kevzettler <kevzettler@gmail.com>Date:   Sun Sep 30 14:49:59 2018 -0700        added another line to hello.txtcommit 994b122045cf4bf0b97139231b4dd52ea2643c7eAuthor: kevzettler <kevzettler@gmail.com>Date:   Sun Sep 30 09:43:41 2018 -0700        added hello.txt
```

该 `[git log](https://www.atlassian.com/git/tutorials/git-log)` 输出显示2个提交和对应提交即将进行的编辑的消息 `hello.txt` 。 下一步是让我们使提交之一不可到达。 我们将通过使用 `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)` 命令 来执行此操作 。 我们将仓库的状态重置为第一次提交。 “添加的hello.txt”提交。

```
~/git-prune-demo $ git reset --hard 994b122045cf4bf0b97139231b4dd52ea2643c7eHEAD is now at 994b122 added hello.txt
```

如果现在使用 `git log` 检查存储库的状态，可以看到我们只有一次提交

```
~/git-prune-demo $ git logcommit 994b122045cf4bf0b97139231b4dd52ea2643c7eAuthor: kevzettler <kevzettler@gmail.com>Date:   Sun Sep 30 09:43:41 2018 -0700        added hello.txt
```

演示存储库现在处于包含分离提交的状态。 我们用消息“在hello.txt中添加了另一行”消息进行的第二次提交不再显示在 `git log` 输出中，现在已分离。 看起来好像我们已经丢失或删除了提交，但是Git对于不删除历史记录非常严格。 我们可以通过 `[git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)` 直接访问它 来确认它仍然可用，但已分离 ：

```
~/git-prune-demo $ git checkout 5178becc2ca965e1728554ce1cb8de2f2c2370b1Note: checking out '5178becc2ca965e1728554ce1cb8de2f2c2370b1'.You are in 'detached HEAD' state. You can look around, make experimentalchanges and commit them, and you can discard any commits you make in thisstate without impacting any branches by performing another checkout.If you want to create a new branch to retain commits you create, you maydo so (now or later) by using -b with the checkout command again. Example:      git checkout -b <new-branch-name>HEAD is now at 5178bec... added another line to hello.txt~/git-prune-demo $ git logcommit 5178becc2ca965e1728554ce1cb8de2f2c2370b1Author: kevzettler <kevzettler@gmail.com>Date:   Sun Sep 30 14:49:59 2018 -0700      added another line to hello.txtcommit 994b122045cf4bf0b97139231b4dd52ea2643c7eAuthor: kevzettler <kevzettler@gmail.com>Date:   Sun Sep 30 09:43:41 2018 -0700      added hello.txt
```

当我们检查分离的提交时，Git会考虑周全，以向我们提供详细的消息，以说明我们处于分离状态。 如果我们在这里检查日志，我们可以看到“在hello.txt中添加了另一行”提交现在又返回了日志输出！ 现在，我们知道存储库处于良好的仿真状态，并且具有分离的提交，我们可以练习使用 `git prune` 。 首先，让我们 `master` 使用 `git checkout`

```
~/git-prune-demo $ git checkout masterWarning: you are leaving 1 commit behind, not connected toany of your branches:      5178bec added another line to hello.txtIf you want to keep it by creating a new branch, this may be a good timeto do so with:     git branch <new-branch-name> 5178becSwitched to branch 'master'
```

当通过 `git checkout` 再次 回到master时 ，Git再次深思熟虑，让我们知道我们将留下一个独立的提交。 现在是时候修剪分离的提交了！ 接下来，我们将执行， `git prune` 但必须确保将一些选项传递给它。 `--dry-run` 并 `--verbose` 会显示输出，指示要修剪但实际上不修剪的内容。

```
~/git-prune-demo $ git prune --dry-run --verbose
```

该命令很可能返回空输出。 空输出表示该修剪实际上不会删除任何内容。 为什么会这样？ 好吧，提交很有可能没有完全脱离。 Git仍然在某个地方对其进行引用。 这是为什么 `git prune` 不能在之外单独使用的 一个很好的例子 `git gc` 。 这也是使用Git很难完全丢失数据的一个很好的例子。

Git最有可能在引用日志中存储对我们的分离提交的引用。 我们可以通过运行进行调查 `[git reflog](https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog)` 。 您应该看到一些输出，描述了我们为到达此处所采取的操作顺序。 有关更多信息， `git reflog` 请访问 `[git reflog](https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog)` 页面。 除了在reflog中保留历史记录外，Git还具有内部到期日期，该日期可用于修剪分离的提交的时间。 同样，这些都是可以 `git gc` 处理的 实现细节， `git prune` 不应单独使用。

要结束我们的 `git prune` 模拟演示，我们必须清除reflog

```
~/git-prune-demo $ git reflog expire --expire=now --expire-unreachable=now --all
```

上面的命令将强制使所有比现在更旧的条目过期。 这是一个残酷而危险的命令，您永远不应该用作Git临时用户。 我们正在执行此命令以演示成功 `git prune` 。 在完全清除reflog之后，我们现在可以执行 `git prune` 。

```
~/git-prune-demo $ git prune --dry-run --verbose --expire=now1782293bdfac16b5408420c5cb0c9a22ddbdd985 blob5178becc2ca965e1728554ce1cb8de2f2c2370b1 commita1b3b83440d2aa956ad6482535cbd121510a3280 commitf91c3433eae245767b9cd5bdb46cd127ed38df26 tree
```

此命令应输出类似于上面的Git SHA对象引用列表。

## 用法

`git prune` 有一个简短的选项列表，我们将在概述部分中介绍。

```
-n --dry-run
```

不要执行修剪。 只需显示其功能的输出即可

```
-v --verbose
```

显示修剪所有对象和动作的输出

```
--progress
```

显示指示修剪进度的输出

```
--expire <time>
```

强制过期的对象过期 `<time>`

```
<head>…
```

指定a `<head>` 将保留该标头参考中的所有选项

## 讨论区

### Git Prune，Git Fetch \-\-prune和Git Remote Prune有什么区别？

`git remote prune` 并 `git fetch --prune` 执行相同的操作：删除对远程上不存在的分支的引用。 当在团队工作流程中工作时（合并到后删除远程分支），这是非常理想的 `master` 。 第二个命令 `git fetch --prune` 将连接到远程并在修剪之前获取最新的远程状态。 它本质上是命令的组合：

```
git fetch --all && git remote prune
```

通用 `git prune` 命令完全不同。 如概述部分所述，git prune将删除本地分离的提交。

### 如何清理过时的分支？

`git fetch --prune` 是清理过时的树枝的最佳工具。 它将连接到远程共享的远程存储库，并获取所有远程分支引用。 然后，它将删除远程资源库上不再使用的远程引用。

### Git远程剪枝来源会删除本地分支吗？

否 `git remote prune origin` 只会删除对不再存在的远程分支的引用。 Git存储本地和远程引用。 存储库将具有 `local/origin` 和 `remote/origin` ref集合。 `git remote prune origin` 只会删节中的引用 `remote/origin` 。 这样可以安全地将本地工作留在 `local/origin` 。

## Git Prune摘要

该 `git prune` 命令旨在作为的子命令调用 `git gc` 。 您极不可能需要 `git prune` 使用日常的软件工程能力。 需要其他命令来了解的影响 `git prune` 。 在这篇文章中使用的一些命令是 `git log` ， `git reflog` 和 `git checkout` 。