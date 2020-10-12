---
title: git gc
date: 2020-10-12 12:09:51
permalink: /pages/3761e7/
categories:
  - git
  - git进阶
tags:
  - 
---
# Git Gc

该 `git gc` 命令是存储库维护命令。 “ gc”代表垃圾收集。 执行 `git gc` 实际上是告诉Git清除它在当前存储库中造成的混乱。 垃圾收集是一个源自解释程序语言的概念，该语言进行动态内存分配。 解释语言中的垃圾回收用于恢复执行程序无法访问的内存。

Git存储库会累积各种类型的垃圾。 Git垃圾的一种类型是孤立的或无法访问的提交。 执行历史更改命令（例如 `[git resets](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)` 或） 时，Git提交可能变得不可访问 `[git rebase](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase)` 。 为了保留历史记录并避免数据丢失，Git不会删除分离的提交。 仍然可以检出分离的提交，挑选樱桃并通过进行检查 `git log` 。

除了清理分离的提交外， `git gc` 还将对存储的Git对象执行压缩，以释放宝贵的磁盘空间。 当Git识别出一组相似的对象时，它将把它们压缩成一个“包装”。 包就像Git bject的zip文件一样，位于 `./git/objects/pack` 目录库 中的 目录中。

## git gc实际做什么？

在执行之前， `git gc` 首先检查几个 `[git config](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config) ` 值。 这些价值将有助于阐明其余 `git gc` 责任。

### git gc配置

```
gc.reflogExpire
```

可选变量，默认为90天。 它用于设置分支reflog中的记录应保留多长时间。

```
gc.reflogExpireUnreachable
```

可选变量，默认为30天。 它用于设置不可访问的reflog记录应保留多长时间。

```
gc.aggressiveWindow
```

一个可选变量，默认为250。它控制 `git gc` 使用该 `--aggressive` 选项 执行 时在对象打包的增量压缩阶段花费了多少时间 。

```
gc.aggressiveDepth
```

可选变量，默认为50。它控制 执行 `git-repack` 期间 压缩 使用 的深度 `git gc --aggresive`

```
gc.pruneExpire
```

可选变量，默认为“ 2周前”。 它设置修剪前不可访问对象的保留时间

```
gc.worktreePruneExpire
```

可选变量，默认为“ 3个月前”。 它设置了过时的工作树在删除之前将保留多长时间。

### git gc执行

幕后 `git gc` 实际执行像其他内部子束 `[git prune](https://www.atlassian.com/git/tutorials/git-prune)` ， `git repack` ， `git pack` 和 `git rerere` 。 这些命令的高级职责是识别超出 `git gc` 配置 设置的阈值级别的任何Git对象 。 一旦确定，这些对象将被压缩或相应地修剪。

## git gc最佳做法和常见问题解答

垃圾回收会自动在几个常用命令上运行：

*   `[git pull](https://www.atlassian.com/git/tutorials/making-a-pull-request)`
*   `[git merge](https://www.atlassian.com/git/tutorials/git-merge)`
*   `[git rebase](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase)`
*   `[git commit](https://www.atlassian.com/git/tutorials/saving-changes)`

`git gc` 手动执行 的频率 对应于存储库的活动级别。 与 `git gc` 经常更新的多用户存储库相比 ，只有一个贡献开发者的存储库执行 的频率要少得多。

## git gc与git prune

`git gc` 是父命令， `git prune` 是子 命令 。 `git gc` 将在内部触发 `git prune` 。 `git prune` 用于删除 `git gc` 配置 认为不可访问的Git对象 。 了解更多有关 `[git prune](https://www.atlassian.com/git/tutorials/git-prune)` 。

## 什么是git gcgressive？

`git gc` 可以使用 `--aggressive` 命令行选项 来调用 。 该 `--aggressive` 选件导致 `git gc` 其优化工作花费更多时间。 这将导致 `git gc` 运行速度变慢，但完成后将节省更多磁盘空间。 的影响 `--aggressive` 是持久的，仅在对存储库进行大量更改后才需要运行。

## 什么是git gc auto？

所述 `git gc --auto` ，如果在执行之前，需要在回购任何内务命令变体首先检查。 如果发现不需要家政服务，则不做任何工作就退出。 一些Git命令 `git gc --auto` 在执行后 隐式运行 ，以清理它们创建的任何松散对象。

在执行之前， `git gc --auto` 将检查 `git` 配置中松散物体的阈值和填料压缩尺寸。 这些值可以用设置 `[git config](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config)` 。 如果存储库超过任何管家阈值， `git gc --auto` 则将执行 该阈值 。

## git gc入门

您可能已经在使用 `git gc` 而没有注意到。 如最佳实践部分中所述，它是通过常用命令自动调用的。 如果要手动调用它，只需执行即可 `git gc`  ，您应该会看到一个输出，指示它已经执行了工作。