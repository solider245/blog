---
title: git commit
date: 2020-10-12 12:09:51
permalink: /pages/0c5f9d/
categories:
  - git入门
  - git保存更改
tags:
  - 
---
# Git提交

[git添加](https://www.atlassian.com/git/tutorials/saving-changes) [git commit](https://www.atlassian.com/git/tutorials/saving-changes/git-commit) [git diff](https://www.atlassian.com/git/tutorials/saving-changes/git-diff) [git stash](https://www.atlassian.com/git/tutorials/saving-changes/git-stash) [.gitignore](https://www.atlassian.com/git/tutorials/saving-changes/gitignore)

该 `git commit` 命令捕获项目当前暂存的更改的快照。 可以将已提交的快照视为项目的“安全”版本\-Git绝不会更改它们，除非您明确要求。 在执行之前 `git commit` ，该 `[git add](https://www.atlassian.com/git/tutorials/saving-changes)` 命令用于促进或“暂存”将存储在提交中的项目更改。 这两个命令 `git commit` 和 `git add` 是最常用的两个。

## Git提交与SVN提交

虽然它们具有相同的名称， `git commit` 却没有什么比 `svn commit` 。 对于拥有svn背景的Git新手来说，这个共同的术语可能会引起混淆。重要的是要强调两者之间的区别。 比较 `git commit` vs `svn commit` 是比较集中式应用程序模型（svn）与分布式应用程序模型（Git）。 在SVN中，提交会将更改从本地SVN客户端推送到远程集中式共享SVN存储库。 在Git中，存储库是分布式的，快照被提交到本地存储库，这绝对不需要与其他Git存储库进行交互。 以后可以将Git提交推送到任意远程存储库。

## 这个怎么运作

在高层次上，可以将Git视为时间轴管理实用程序。 提交是Git项目时间表的核心构建单元。 可以将提交视为Git项目时间轴上的快照或里程碑。 使用 `git commit` 命令 创建提交 以捕获该时间点的项目状态。 Git快照始终被提交到本地存储库。 这与SVN根本不同，后者将工作副本提交到中央存储库。 相反，直到准备就绪，Git才会强迫您与中央存储库进行交互。 正如暂存区是工作目录和项目历史记录之间的缓冲区一样，每个开发人员的本地资源库也是他们的贡献和中央资源库之间的缓冲区。

这改变了Git用户的基本开发模型。 Git开发人员不必进行更改并将其直接提交给中央存储库，而是有机会在其本地存储库中累积提交。 与SVN样式的协作相比，它具有许多优点：可以更轻松地将功能拆分为原子提交，将相关提交分组在一起，并在将本地历史发布到中央存储库之前清除本地历史记录。 它还使开发人员可以在隔离的环境中工作，将集成推迟到他们可以方便地与其他用户合并之前。 尽管隔离和延迟集成对每个人都是有益的，但频繁地并在较小的单元中进行集成符合团队的最大利益。 有关Git团队协作的最佳做​​法的更多信息，请阅读团队的结构 [Git工作流程](https://www.atlassian.com/git/tutorials/comparing-workflows) 。

## 快照，无差异

除了SVN和Git之间的实际区别外，它们的底层实现还遵循完全不同的设计理念。 SVN跟踪文件的差异，而Git的版本控制模型则基于快照。 例如，与添加到存储库的原始文件相比，SVN提交包含一个差异。 另一方面，Git记录每次提交中每个文件的全部内容。

![Git教程：快照，无差异](https://wac-cdn.atlassian.com/dam/jcr:7406fe56-d36d-44cf-92e3-b28e4bae36f8/02.svg?cdnVersion=1084)

这使得许多Git操作比SVN快得多，因为不必从其差异“组合”文件的特定版本\-每个文件的完整修订版都可以从Git的内部数据库中立即获得。

Git的快照模型几乎对其版本控制模型的各个方面都具有深远的影响，影响到从分支和合并工具到协作工作流程的所有方面。

## 常用选项

```
git commit
```

提交暂存的快照。 这将启动文本编辑器，提示您输入提交消息。 输入消息后，保存文件并关闭编辑器以创建实际的提交。

```
git commit -a
```

提交工作目录中所有更改的快照。 这仅包括对跟踪文件的修改（已 `git add` 在其历史记录的某个时刻 添加的文件 ）。

```
git commit -m "commit message"
```

快捷方式命令，可使用传递的提交消息立即创建提交。 默认情况下， `git commit` 将打开本地配置的文本编辑器，并提示输入提交消息。 传递该 `-m` 选项将放弃文本编辑器提示，而偏向于内联消息。

```
git commit -am "commit message"
```

结合了 `-a` 和 `-m` 选项的 超级用户快捷方式命令 。 这种组合会立即创建所有已暂存的更改的提交，并接受内联提交消息。

```
git commit --amend
```

此选项将另一级功能添加到commit命令。 传递此选项将修改最后的提交。 代替创建新的提交，分阶段的更改将添加到上一个提交中。 该命令将打开系统配置的文本编辑器，并提示您更改先前指定的提交消息。

## 例子

### 通过提交保存更改

下面的示例假定您已经 `hello.py` 在当前分支上的 文件中编辑了一些内容 ，并准备将其提交到项目历史记录中。 首先，您需要使用 `git add` 暂存 文件 ，然后可以提交暂存的快照。

```
git add hello.py
```

该命令将添加 `hello.py` 到Git暂存区域。 我们可以使用 `git status` 命令 检查此操作的结果 。

```
git status
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
  new file: hello.py

```

绿色输出新文件： `hello.py` 表示 `hello.py` 将在下次提交时保存。 通过执行以下操作从提交中创建：

```
git commit
```

这将打开一个文本编辑器（可通过定制 `git config` ），询问提交日志消息以及所提交内容的列表：

```
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
# Changes to be committed:
# (use "git reset HEAD ..." to unstage)
#
#modified: hello.py
```

Git不需要提交消息遵循任何特定的格式约束，但是规范格式是将第一行的整个提交总结为少于50个字符，留空行，然后详细说明已更改的内容。 例如：

```
Change the message displayed by hello.py
- Update the sayHello() function to output the user's name
- Change the sayGoodbye() function to a friendlier message
```

通常将提交消息的第一行用作主题行，类似于电子邮件。 日志消息的其余部分被视为正文，并用于传达提交更改集的详细信息。 注意，许多开发人员还喜欢在提交消息中使用现在时。 这使他们在存储库上的阅读更像是操作，这使许多历史记录重写操作更加直观。

## 如何更新（修改）提交

继续 `hello.py` 上面 的 示例。 让我们进一步更新 `hello.py` 并执行以下操作：

```
git add hello.py
git commit --amend
```

这将再次打开配置的文本编辑器。 但是，这次将使用我们先前输入的提交消息进行预填充。 这表明我们不是在创建新的提交，而是在编辑最后一个。

## 摘要

该 `git commit` 命令是Git的核心主要功能之一。 `git add` 需要先 使用该 命令才能选择将在下一次提交中进行的更改。 然后 `git commit` 用于沿着Git项目历史记录的时间线创建阶段性更改的快照。 `[git add](https://www.atlassian.com/git/tutorials/saving-changes) ` 在随附的页面上 了解有关 用法的 更多信息 。 该 `[git status](https://www.atlassian.com/git/tutorials/inspecting-a-repository)`  命令可用于浏览暂存区和挂起提交的状态。

SVN和Git的提交模型有很大的不同，但是由于术语的共享，常常会造成混淆。 如果您是从个人使用SVN的历史中学到Git的，那么很高兴得知在Git中，提交很便宜，应该经常使用。 SVN提交是一个昂贵的操作，它会发出远程请求，而Git提交则是在本地使用更有效的算法完成的。