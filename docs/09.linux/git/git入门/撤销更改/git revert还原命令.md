---
title: git revert还原命令
date: 2020-10-12 12:09:51
permalink: /pages/817ae7/
categories:
  - git入门
  - 撤销更改
tags:
  - 
---
# Git还原

[git checkout](https://www.atlassian.com/git/tutorials/undoing-changes) [git clean](https://www.atlassian.com/git/tutorials/undoing-changes/git-clean) [git恢复](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert) [git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset) [git rm](https://www.atlassian.com/git/tutorials/undoing-changes/git-rm)

该 `git revert` 命令可以被视为“撤消”类型的命令，但是，它不是传统的撤消操作。 而不是从项目历史记录中删除提交，而是弄清楚如何反转提交所引起的更改，并在新提交中附加所产生的反向内容。 这可以防止Git丢失历史记录，这对于确保修订历史记录的完整性和可靠的协作非常重要。

当您要应用项目历史记录中的提交逆操作时，应使用还原。 例如，这在跟踪错误并发现它是由一次提交引入时很有用。 您可以使用 `git revert` 自动为您完成所有这些 操作，而不必手动进行修复，修复并提交新的快照 。

![Git还原-Atlassian Git教程](https://wac-cdn.atlassian.com/dam/jcr:b6fcf82b-5b15-4569-8f4f-a76454f9ca5b/03%20(7).svg?cdnVersion=1084)

## 这个怎么运作

该 `git revert` 命令用于撤消对存储库提交历史的更改。 其他“撤消”命令，例如 `[git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)` 和 `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)` ，将 `HEAD` 和分支引用指针移至指定的提交。 `Git revert` 也接受指定的提交，但是 `git revert` 不会将引用指针移到该提交。 还原操作将采用指定的提交，将来自该提交的更改反向，并创建一个新的“还原提交”。 然后，将ref指针更新为指向新的还原提交，使其成为分支的尖端。

为了演示，让我们使用以下命令行示例创建示例存储库：

```
$ mkdir git_revert_test
$ cd git_revert_test/
$ git init .
Initialized empty Git repository in /git_revert_test/.git/
$ touch demo_file
$ git add demo_file
$ git commit -am"initial commit"
[master (root-commit) 299b15f] initial commit
1 file changed, 0 insertions(+), 0 deletions(-)
create mode 100644 demo_file
$ echo "initial content" >> demo_file
$ git commit -am"add new content to demo file"
[master 3602d88] add new content to demo file
n 1 file changed, 1 insertion(+)
$ echo "prepended line content" >> demo_file
$ git commit -am"prepend content to demo file"
[master 86bb32e] prepend content to demo file
1 file changed, 1 insertion(+)
$ git log --oneline
86bb32e prepend content to demo file
3602d88 add new content to demo file
299b15f initial commit
```

在这里，我们在名为的新创建目录中初始化了一个存储库 `git_revert_test` 。 我们对仓库进行了3次提交，在其中添加了文件 `demo_file` 并对其内容进行了两次修改。 在回购设置过程的最后，我们调用 `git log` 以显示提交历史记录，总共显示3次提交。 在此状态下，我们准备启动一个 `git revert.`

```
$ git revert HEAD
[master b9cd081] Revert "prepend content to demo file"
1 file changed, 1 deletion(-)
```

`Git revert` 期望传递一个提交引用，并且没有一个提交引用将不会执行。 在这里，我们通过了 `HEAD` 裁判。 这将还原最新的提交。 这与我们恢复为commit时的行为相同 `3602d8815dbfa78cd37cd4d189552764b5e96c58` 。 类似于合并，还原将创建一个新的提交，它将打开配置的系统编辑器，提示输入新的提交消息。 输入提交消息并保存后，Git将恢复操作。 现在，我们可以使用来检查存储库的状态， `git log` 并看到在先前的日志中添加了新的提交：

```
$ git log --oneline
1061e79 Revert "prepend content to demo file"
86bb32e prepend content to demo file
3602d88 add new content to demo file
299b15f initial commit
```

请注意，还原后，第3次提交仍在项目历史记录中。 而不是删除它，而是 `git revert` 添加了一个新的提交来撤消其更改。 结果，第二次提交和第四次提交代表了完全相同的代码库，而第三次提交仍在我们的历史中，以防万一我们想追溯到此。

## 常用选项

```
-e
--edit
```

这是默认选项，不需要指定。 此选项将打开已配置的系统编辑器，并提示您在提交还原之前编辑提交消息。

```
--no-edit
```

这与 `-e` 选项 相反 。 还原将不会打开编辑器。

```
-n
--no-commit
```

传递此选项将阻止 `git revert` 创建与目标提交相反的新提交。 代替创建新的提交，该选项将反向更改添加到暂存索引和工作目录中。 这些是Git用于管理存储库状态的其他树。 有关更多信息，请访问 `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)` 页面。

## 重置与还原

重要的是要了解 `git revert` 撤消单个提交\-它不会通过删除所有后续提交而“恢复”到项目的先前状态。 在Git中，这实际上称为重置，而不是还原。

![Git恢复与Git重置-Atlassian Git教程](https://wac-cdn.atlassian.com/dam/jcr:a6a50d78-48e3-4765-8492-9e48dec8fd2f/04%20(2).svg?cdnVersion=1084)

与重置相比，还原具有两个重要优点。 首先，它不会更改项目历史记录，这使其成为已发布到共享存储库中的提交的“安全”操作。 有关为何更改共享历史记录很危险的详细信息，请参见 [git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset) 页面。

其次， `git revert` 能够在历史记录中的任意点定位单个提交，而 `git reset` 只能从当前提交向后进行。 例如，如果要使用撤消旧的提交 `git reset` ，则必须删除目标提交之后发生的所有提交，将其删除，然后重新提交所有后续提交。 不用说，这不是一个优雅的撤消解决方案。 有关之间差异的更详细讨论 `git revert` 和其他“撤消”命令，请参见“ [重置，签出和还原”。](https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting)

## 摘要

该 `git revert` 命令是向前移动的撤消操作，提供了撤消更改的安全方法。 还原操作不会删除提交历史记录中的孤立提交，而是会创建一个与指定更改相反的新提交。 对于失业， `Git revert` 是一种更安全的选择 `git reset` 。 为了演示的效果 `git revert` ，我们利用的是对他们的个人网页更深入的文档其他命令： `[git log](https://www.atlassian.com/git/tutorials/git-log)` ， `[git commit](https://www.atlassian.com/git/tutorials/saving-changes#git-commit), and` `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset).`