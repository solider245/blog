---
title: git reflog
date: 2020-10-12 12:09:51
permalink: /pages/915162/
categories:
  - git入门
  - 改写历史
tags:
  - 
---
# git reflog

此页面提供有关 `git reflog` 命令 的详细讨论 。 Git使用称为参考日志或“ reflogs”的机制跟踪分支尖端的更新。 许多Git命令都接受用于指定引用或“ ref”的参数，该参数是指向提​​交的指针。 常见的示例包括：

*   `git checkout`
*   `git reset`
*   `git merge`

Reflogs跟踪本地存储库中Git ref的更新时间。 除了分支提示刷新外，还为Git存储库保留了一个特殊的刷新。 引用日志存储在本地存储库目录下的 `.git` 目录中。 `git reflog` 目录可以在这里找到 `.git/logs/refs/heads/.` ， `.git/logs/HEAD` 和也 `.git/logs/refs/stash` ，如果 `git stash` 已经在回购使用。

我们 `git reflog` 在“ [重写历史记录”页](https://www.atlassian.com/git/tutorials/rewriting-history) 上进行了高层 讨论 。 本文档将涵盖：的扩展配置选项 `git reflog` ，的常见用例和陷阱 `git reflog` ，如何使用撤消更改 `git reflog` 等。

## 基本用法

最基本的Reflog用例是调用：

```
git reflog

```

这本质上是一条捷径，等效于：

```
git reflog show HEAD

```

这将输出 `HEAD` reflog。 您应该看到类似于以下内容的输出：

```
eff544f HEAD@{0}: commit: migrate existing content
bf871fd HEAD@{1}: commit: Add Git Reflog outline
9a4491f HEAD@{2}: checkout: moving from master to git_reflog
9a4491f HEAD@{3}: checkout: moving from Git_Config to master
39b159a HEAD@{4}: commit: expand on git context
9b3aa71 HEAD@{5}: commit: more color clarification
f34388b HEAD@{6}: commit: expand on color support
9962aed HEAD@{7}: commit: a git editor -> the Git editor

```

访问“ [重写历史记录”页面，](https://www.atlassian.com/git/tutorials/rewriting-history) 以获取另一个常见的reflog访问示例。

### Reflog参考

默认情况下， `git reflog` 将输出 `HEAD` 参考的参考 日志 。 `HEAD` 是对当前活动分支的符号引用。 引用日志也可用于其他引用。 访问git ref的语法为 `name@{qualifier}` 。 除了 `HEAD` 引用之外，还可以引用其他分支，标签，远程对象和Git存储。

您可以通过执行以下命令获取所有裁判的完整裁判日志：

```
 git reflog show --all

```

要查看特定分支的引用日志，请将该分支名称传递给 `git reflog show`

```
git reflog show otherbranch
9a4491f otherbranch@{0}: commit: seperate articles into branch PRs
35aee4a otherbranch{1}: commit (initial): initial commit add git-init and setting-up-a-repo docs

```

执行此示例将显示 `otherbranch` 分支 的引用日志 。 下面的示例假定您以前使用该 `git stash` 命令 进行了一些更改 。

```
git reflog stash
0d44de3 stash@{0}: WIP on git_reflog: c492574 flesh out intro

```

这将为Git隐藏输出一个刷新日志。 返回的ref指针可以传递给其他Git命令：

```
git diff stash@{0} otherbranch@{0}

```

执行后，此示例代码将显示Git diff输出，将 `stash@{0}` 更改与 `otherbranch@{0}` ref 进行比较 。

### 定时更新

每个reflog条目均附有时间戳。 这些时间戳可以用作 `qualifier` Git ref指针语法 的 标记。 这样可以按时间过滤Git reflog。 以下是可用时间限定符的一些示例：

*   `1.minute.ago`
*   `1.hour.ago`
*   `1.day.ago`
*   `yesterday`
*   `1.week.ago`
*   `1.month.ago`
*   `1.year.ago`
*   `2011-05-17.09:00:00`

时间限定符可以组合（例如 `1.day.2.hours.ago` ）。此外，可以接受多种形式（例如 `5.minutes.ago` ）。

时间限定符ref可以传递给其他git命令。

```
 git diff master@{0} master@{1.day.ago}

```

本示例将1天前将当前的master分支与master进行比较。 如果您想了解某个时间范围内发生的更改，此示例非常有用。

## 子命令和配置选项

`git reflog` 接受很少的附加参数，这些附加参数被视为子命令。

### 表演 \- `git reflog show`

`show` 默认情况下隐式传递。 例如，命令：

```
git reflog master@{0}

```

等效于命令：

```
git reflog show master@{0}

```

此外， `git reflog show` 是的别名 `git log -g --abbrev-commit --pretty=oneline` 。 执行 将显示所传递的<refid>的日志。 `git reflog show`

### 到期\- `git reflog expire`

expire子命令清除旧的或无法访问的引用日志条目。 该 `expire` 子命令可能会丢失数据。 最终用户通常不使用此子命令，但git在内部使用。 将 `-n` 或 `--dry-run` 选项 传递 给 `git reflog expire` Will将执行“空运行”，该命令将输出标记为已修剪的reflog条目，但实际上不会修剪它们。

默认情况下，reflog的过期日期设置为90天。 到期时间可以通过传递命令行参数来指定 `--expire=time` 到 `git reflog expire` 或通过设置的一个git配置名称 `gc.reflogExpire` 。

### 删除\- `git reflog delete`

该 `delete` 子命令是自我解释，并会删除引用日志条目的通过。 与一样 `expire` ， `delete` 可能会丢失数据，并且最终用户通常不会调用它。

## 恢复丢失的提交

即使执行历史记录重写操作（如变基或提交修改），Git也不会丢失任何东西。 对于下一个示例，假设我们对存储库进行了一些新更改。 我们的 `git log --pretty=oneline` 外观如下：

```
338fbcb41de10f7f2e54095f5649426cb4bf2458 extended content
1e63ceab309da94256db8fb1f35b1678fb74abd4 bunch of content
c49257493a95185997c87e0bc3a9481715270086 flesh out intro
eff544f986d270d7f97c77618314a06f024c7916 migrate existing content
bf871fd762d8ef2e146d7f0226e81a92f91975ad Add Git Reflog outline
35aee4a4404c42128bee8468a9517418ed0eb3dc initial commit add git-init and setting-up-a-repo docs

```

然后，我们提交这些更改并执行以下操作：

```
#make changes to HEAD
git commit -am "some WIP changes"

```

随着新的提交。 日志现在看起来像：

```
37656e19d4e4f1a9b419f57850c8f1974f871b07 some WIP changes
338fbcb41de10f7f2e54095f5649426cb4bf2458 extended content
1e63ceab309da94256db8fb1f35b1678fb74abd4 bunch of content
c49257493a95185997c87e0bc3a9481715270086 flesh out intro
eff544f986d270d7f97c77618314a06f024c7916 migrate existing content
bf871fd762d8ef2e146d7f0226e81a92f91975ad Add Git Reflog outline
35aee4a4404c42128bee8468a9517418ed0eb3dc initial commit add git-init and setting-up-a-repo docs

```

在这一点上，我们通过执行...针对master分支执行交互式基础。

```
git rebase -i origin/master

```

在重新基准化期间，我们使用 `s` rebase子命令 将南瓜的提交标记为 。 在重新设置期间，我们将一些提交压缩为最新的“某些WIP更改”提交。

因为我们压缩了提交，所以 `git log` 输出现在如下所示：

```
40dhsoi37656e19d4e4f1a9b419f57850ch87dah987698hs some WIP changes
35aee4a4404c42128bee8468a9517418ed0eb3dc initial commit add git-init and setting-up-a-repo docs

```

如果我们 `git log` 在这一点上进行 检查 ，则看来我们不再具有标记为压缩的提交。 如果我们要对压缩的提交之一进行操作怎么办？ 也许要从历史记录中删除其更改？ 这是利用引用日志的机会。

```
git reflog
37656e1 HEAD@{0}: rebase -i (finish): returning to refs/heads/git_reflog
37656e1 HEAD@{1}: rebase -i (start): checkout origin/master
37656e1 HEAD@{2}: commit: some WIP changes

```

我们可以看到有reflog条目的开始和结束，在此 `rebase` 之前是我们的“一些WIP更改”提交。 我们可以将reflog ref传递给 `git reset` 并重置为重新设置 基准 之前的提交。

```
git reset HEAD@{2}

```

执行此reset命令将移至 `HEAD` 添加了“某些WIP更改”的提交，从本质上恢复了其他压缩的提交。

## 摘要

在本教程中，我们讨论了该 `git reflog` 命令。 涵盖的一些关键点是：

*   如何查看特定分支的刷新日志
*   如何使用reflog撤消git rebase
*   如何指定和查看基于时间的reflog条目

我们简要提到了 `git reflog` 可以与其他git命令一起使用的命令，例如 [git checkout](https://www.atlassian.com/git/tutorials/using-branches#git-checkout) ， [git reset](https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting) 和 [git merge](https://www.atlassian.com/git/tutorials/git-merge) 。 在各自的页面上了解更多信息。 有关ref和reflog的其他讨论，请在 [此处了解更多信息](https://www.atlassian.com/git/tutorials/refs-and-the-reflog) 。