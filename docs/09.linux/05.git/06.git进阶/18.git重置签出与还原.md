---
title: git重置签出与还原
date: 2020-10-12 12:09:51
permalink: /pages/c7ffec/
categories:
  - git
  - git进阶
tags:
  - 
---
# 重置，签出和还原

的 `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)` ， `[git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)` 和 `[git revert](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert)` 命令是一些使用Git的工具箱中最有用的工具。 它们都使您可以撤消存储库中的某种更改，并且前两个命令可用于处理提交或单个文件。

因为它们是如此相似，所以很容易混淆在任何给定的开发方案中应该使用哪个命令。 在这篇文章中，我们将比较的最常见的配置 `git reset` ， `git checkout` 和 `git revert` 。 希望您可以放心使用这些命令中的任何一个来导航您的存储库。

![吉特的三棵树](https://wac-cdn.atlassian.com/dam/jcr:0c5257d5-ff01-4014-af12-faf2aec53cc3/01.svg?cdnVersion=1084)

考虑到每个命令对Git存储库的三种状态管理机制的影响，有助于考虑每个命令：工作目录，暂存快照和提交历史记录。 这些组件有时被称为Git的“三棵树”。 我们在 `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)` 页面 上深入探讨了三棵树 。 阅读本文时，请牢记这些机制。

签出是将 `HEAD` ref指针移至指定提交的操作。 为了说明这一点，请考虑以下示例。

![将HEAD ref指针移至指定的提交](https://wac-cdn.atlassian.com/dam/jcr:5db5291a-98ea-4ebc-bb99-a40dd23eaf62/git-sequence-transparent.png?cdnVersion=1084)

此示例演示了 `master` 分支 上的一系列提交 。 该 `HEAD` ref和 `master` 分支参考目前指向承诺d。 现在让我们执行 `git checkout b`

![master分支上的提交顺序](https://wac-cdn.atlassian.com/dam/jcr:f0e14908-e692-470e-a8c0-21150831f332/2497537634-git-checkout-transparent.png?cdnVersion=1084)

这是对“提交历史记录”树的更新。 该 `git checkout` 命令可以在提交或文件级别范围内使用。 文件级别检出会将文件内容更改为特定提交的内容。

还原是一种操作，该操作接受指定的提交并创建一个与指定提交相反的新提交。 `git revert` 只能在提交级范围内运行，并且没有文件级功能。

重置是接受指定提交并重置“三棵树”以匹配该指定提交处存储库状态的操作。 可以用三种不同的方式来调用复位，这三种方式分别对应于三个树。

签出和重置通常用于进行本地或私有“撤消”。 它们修改存储库的历史记录，当推送到远程共享存储库时，该历史记录可能会导致冲突。 恢复操作被认为是“公共撤消”操作的安全操作，因为它创建了可以远程共享的新历史记录，并且不会覆盖远程团队成员可能依赖的历史记录。

## Git重置vs还原vs Checkout参考

下表总结了所有这些命令的最常用用例。 请确保随时随地使用此参考，因为在Git的职业生涯中，无疑将需要至少使用其中一些。

| 命令 | 范围 | 常见用例 |
| --- | --- | --- |
| `git reset` | 提交级别 | 放弃在私有分支中的提交或丢弃未提交的更改 |
| --- | --- | --- |
| `git reset` | 文件级 | 取消暂存文件 |
| --- | --- | --- |
| `git checkout` | 提交级别 | 在分支之间切换或检查旧快照 |
| --- | --- | --- |
| `git checkout` | 文件级 | 放弃工作目录中的更改 |
| --- | --- | --- |
| `git revert` | 提交级别 | 撤消在公共分支中提交 |
| --- | --- | --- |
| `git revert` | 文件级 | （不适用） |
| --- | --- | --- |

## 提交级别操作

您传递给 `git reset` 并 `git checkout` 确定其范围 的参数 。 如果您不包括文件路径作为参数，则它们将对整个提交进行操作。 这就是我们将在本节中探讨的内容。 请注意， `git revert` 没有文件级副本。

### 重置特定的提交

在提交级别，重置是一种将分支的尖端移动到其他提交的方法。 这可用于从当前分支中删除提交。 例如，以下命令将 `hotfix` 分支向后 移动 两次提交。

```
git checkout hotfix
git reset HEAD~2
```

`hotfix` 现在， 结尾处的两个提交 是悬空的或孤立的提交。 这意味着它们将在Git下次执行垃圾回收时被删除。 换句话说，您是说要丢弃这些提交。 可以如下所示：

![将修补程序分支重置为HEAD-2](https://wac-cdn.atlassian.com/dam/jcr:4c7d368e-6e40-4f82-a315-1ed11316cf8b/02-updated.png?cdnVersion=1084)

这种用法 `git reset` 是撤消尚未与其他任何人共享的更改的简单方法。 当您开始使用某个功能并发现自己在想，“噢，我在做什么？”时，这是您的首选命令。 我应该重新开始。”

除了移动当前分支外，还可以通过 `git reset` 向暂存快照和/或工作目录传递以下标志之一来更改暂存快照和/或工作目录：

*   `--soft` –暂存快照和工作目录不会以任何方式更改。
*   `--mixed` –已更新暂存快照以匹配指定的提交，但是工作目录不受影响。 这是默认选项。
*   `--hard` –暂存快照和工作目录均已更新以匹配指定的提交。

将这些模式视为定义 `git reset` 操作 范围会更容易 。 有关更多详细信息，请访问 `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)` 页面。

### 检出旧提交

该 `git checkout` 命令用于将存储库的状态更新为项目历史记录中的特定点。 当传递分支名称时，它使您可以在分支之间切换。

```
git checkout hotfix
```

在内部，以上所有命令的作用是移动 `HEAD` 到另一个分支并更新工作目录以进行匹配。 由于这已覆盖当地的电位变化，Git会迫使你提交或 [藏匿](https://www.atlassian.com/git/tutorials/saving-changes/git-stash) 在将结账操作过程中失去了工作目录中的任何改变。 不像 `git reset` ， `git checkout` 不会移动任何分支。

![将HEAD从主服务器移动到修补程序](https://wac-cdn.atlassian.com/dam/jcr:607f1b83-ee7d-494a-b7e2-338d810059fb/04-updated.png?cdnVersion=1084)

您还可以通过传递提交引用而不是分支来签出任意提交。 这与签出分支完全相同：将 `HEAD` 引用移至指定的提交。 例如，以下命令将签出当前提交的祖父母：

```
git checkout HEAD~2
```

![将“ HEAD”移至任意提交](https://wac-cdn.atlassian.com/dam/jcr:3034be0a-fc7b-4c64-b9cd-3ebc8abf3833/05.svg?cdnVersion=1084)

这对于快速检查项目的旧版本很有用。 但是，由于没有分支引用current `HEAD` ，这使您处于分离 `HEAD` 状态。 如果您开始添加新的提交，这将很危险，因为切换到另一个分支后将无法重新获得它们。 因此，您应该始终创建一个新分支，然后再向detached中添加提交 `HEAD` 。

### 通过还原撤消公共承诺

还原通过创建新的提交撤消提交。 这是撤消更改的安全方法，因为它没有机会重写提交历史记录。 例如，以下命令将找出从第二到最后一次提交中包含的更改，创建一个撤消这些更改的新提交，并将新提交添加到现有项目上。

```
git checkout hotfix
git revert HEAD~2
```

可以如下所示：

![将第二次还原为最后一次提交](https://wac-cdn.atlassian.com/dam/jcr:73d36b14-72a7-4e96-a5bf-b86629d2deeb/06.svg?cdnVersion=1084)

将此与进行对比 `git reset` ，这 *确实* 会更改现有的提交历史记录。 因此， `git revert` 应将其用于撤消公共分支上的更改，而 `git reset` 应保留以撤消对私有分支上的更改。

您也可以将其 `git revert` 视为撤消已 *提交的* 更改 的工具 ，而 `git reset HEAD` 将其作为撤消 *未提交的* 更改的工具。

像一样 `git checkout` ， `git revert` 可能会覆盖工作目录中的文件，因此它将要求您提交或 [隐藏](https://www.atlassian.com/git/tutorials/saving-changes/git-stash) 在还原操作期间丢失的 [更改](https://www.atlassian.com/git/tutorials/saving-changes/git-stash) 。

## 文件级操作

该 `git reset` 和 `git checkout` 命令也接受作为参数，一个可选的文件路径。 这极大地改变了他们的行为。 而不是对整个快照进行操作，这迫使它们将其操作限制在单个文件中。

### Git重置特定文件

当使用文件路径调用时， `git reset` 更新 *暂存快照* 以匹配指定提交中的版本。 例如，此命令将获取 `foo.py` 倒数第二次提交中 的版本， 并为下一次提交 暂存该版本 ：

```
git reset HEAD~2 foo.py
```

与的提交级别版本一样 `git reset` ，它更常用于 `HEAD` 而不是任意提交。 跑步 `git reset HEAD foo.py` 会 停止 `foo.py` 。 它包含的更改仍将存在于工作目录中。

![将文件从提交历史记录移到暂存快照中](https://wac-cdn.atlassian.com/dam/jcr:1a010f5a-c90d-49ee-a0e6-31054433e2d4/07.svg?cdnVersion=1084)

的 `--soft` ， `--mixed` 和 `--hard` 标志不具有对文件级版本有任何影响 `git reset` ，因为上演快照 *总是* 更新，和工作目录是 *永远不会* 更新。

### Git结帐文件

检出文件与使用 `git reset` 文件路径 相似 ，不同之处 在于检出文件 会更新 *工作目录* 而不是阶段。 与该命令的提交级版本不同，它不会移动 `HEAD` 引用，这意味着您不会切换分支。

![将文件从提交历史记录移到工作目录中](https://wac-cdn.atlassian.com/dam/jcr:cc252fc0-fc76-4740-8458-9c0d7af94bca/08.svg?cdnVersion=1084)

例如，以下命令使 `foo.py` 工作目录中的第二个到最后一个提交匹配：

```
git checkout HEAD~2 foo.py
```

就像的提交级别调用一样 `git checkout` ，它可以用于检查项目的旧版本\-但范围仅限于指定的文件。

如果暂存并提交已签出的文件，则具有“还原”到该文件的旧版本的效果。 请注意，这将删除文件的 *所有* 后续更改，而该 `git revert` 命令仅撤消由指定提交引入的更改。

像一样 `git reset` ，通常与 `HEAD` 提交参考一起使用。 例如， `git checkout HEAD foo.py` 具有丢弃对的未分段更改的效果 `foo.py` 。 这与的行为类似 `git reset HEAD --hard` ，但仅对指定的文件起作用。

## 摘要

现在，您应该拥有撤消Git存储库中的更改所需的所有工具。 的 `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)` ， `[git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)` 和 `[git revert](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert)` 命令可能会造成混淆，但是当你想想自己的工作目录下的效果，上演快照，并提交历史，它应该是更容易辨别哪些命令适合手头的开发任务。