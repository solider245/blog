---
title: 存储点文件的最佳方法：裸露的Git存储库
date: 2020-10-12 12:09:51
permalink: /pages/86caa1/
categories:
  - git
  - git进阶
tags:
  - 
---
# 吉特樱桃挑

`git cherry-pick` 是一个功能强大的命令，它允许通过引用选择任意Git提交并将其附加到当前工作的HEAD上。 樱桃选择是从分支中选择提交并将其应用于另一个的行为。 `git cherry-pick` 对于撤消更改很有用。 例如，假设一次提交是错误地对错误的分支进行的。 您可以切换到正确的分支，然后选择提交应属于的位置。

## 何时使用git cherry pick

`git cherry-pick` 是有用的工具，但并非总是最佳做法。 樱桃采摘会导致重复提交，并且在很多情况下可以使用樱桃采摘，而传统的合并则更为可取。 这样说 `git cherry-pick` 是 在某些 情况下的便捷工具...

## 团队合作。

通常，团队会发现使用相同代码或在同一代码中工作的单个成员。 也许新产品功能具有后端和前端组件。 两个产品部门之间可能存在一些共享代码。 后端开发人员可能会创建前端也需要利用的数据结构。 前端开发人员可以 `git cherry-pick` 用来选择在其中创建此假设数据结构的提交。 这种选择将使前端开发人员能够继续他们的项目进度。

## 错误修补程序

发现错误后，尽快将修补程序提供给最终用户非常重要。 对于一个示例场景，例如，开发人员已开始着手一项新功能。 在进行新功能开发时，他们会确定一个先前存在的错误。 开发人员创建了一个明确的提交来修补此错误。 可以将新提交的修补程序直接挑选到 `master` 分支机构中，以在影响更多用户之前修复该错误。

## 撤消更改并恢复丢失的提交

有时， `feature` 分支可能会过时并且无法合并到 `master` 。 有时，拉取请求可能会在不合并的情况下关闭。 混帐从来没有失去这些提交，并通过类似这样的命令 `[git log](https://www.atlassian.com/git/tutorials/git-log)` 和 `[git reflog](https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog)` 他们可以发现和樱桃采摘起死回生。

## 如何使用git cherry pick

为了演示如何使用， `git cherry-pick` 让我们假设我们有一个具有以下分支状态的存储库：

```
    a - b - c - d   Master         \           e - f - g Feature
```

`git cherry-pick` 用法很简单，可以像这样执行：

```
git cherry-pick commitSha
```

在此示例中， `commit` Sha是提交引用。 您可以使用找到提交参考 `git log` 。 在此示例中，我们构造了一个说要在中使用commit\`f\`的例子 `master` 。 首先，我们确保我们在 `master` 分支机构 上工作 。

```
git checkout master
```

然后，使用以下命令执行cherry\-pick：

```
git cherry-pick f
```

一旦执行，我们的Git历史将如下所示：

```
    a - b - c - d - f   Master         \           e - f - g Feature
```

f提交已成功进入功能分支

## git cherry pick的例子

 `git cherry pick` 也可以传递一些执行选项。

```
-edit
```

传递该 `-edit` 选项将导致git在应用cherry\-pick操作之前提示输入提交消息

```
--no-commit
```

该 `--no-commit` 选项将执行cherry pick，但不是进行新的提交，而是将目标提交的内容移动到当前分支的工作目录中。

```
--signoff
```

该 `--signoff` 选项将在Cherry\-Pick提交消息的末尾添加“ signoff”签名行。

除了这些有用的选项外， `git cherry-pick` 还接受各种合并策略选项。 在 [git合并策略](https://www.atlassian.com/git/tutorials/using-branches/merge-strategy)  文档中 了解有关这些选项的更多信息 。

另外，git cherry\-pick还接受用于合并冲突解决的选项输入，其中包括选项： `--abort --continue` 并且 `--quit` 关于 [git merge](https://www.atlassian.com/git/tutorials/using-branches/git-merge) 和 [git rebase](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase) 更加深入地介绍了此选项 。

## 摘要

Cherry Picking是一个功能强大且方便的命令，在某些情况下非常有用。 不应误用Cherry采摘代替 [git merge](https://www.atlassian.com/git/tutorials/using-branches/git-merge) 或 [git rebase](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase) 。 在 [git的日志](https://www.atlassian.com/git/tutorials/git-log)  命令被要求帮助寻找提交樱桃挑。