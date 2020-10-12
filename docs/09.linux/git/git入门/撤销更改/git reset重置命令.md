---
title: git reset重置命令
date: 2020-10-12 12:09:51
permalink: /pages/8e5f6b/
categories:
  - git入门
  - 撤销更改
tags:
  - 
---
# Git重置

[git checkout](https://www.atlassian.com/git/tutorials/undoing-changes) [git clean](https://www.atlassian.com/git/tutorials/undoing-changes/git-clean) [git恢复](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert) [git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset) [git rm](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)

该 `git reset` 命令是用于撤消更改的复杂而通用的工具。 它具有三种主要的调用形式。 这些形式对应于命令行参数 `--soft, --mixed, --hard` 。 这三个参数分别对应于Git的三个内部状态管理机制：提交树（ `HEAD` ），登台索引和工作目录。

## Git重置和三棵Git树

为了正确理解 `git reset` 用法，我们必须首先了解Git的内部状态管理系统。 有时，这些机制称为Git的“三棵树”。 树可能是用词不当，因为它们并不是严格意义上的传统树数据结构。 但是，它们是Git用来跟踪编辑时间轴的基于节点和指针的数据结构。 演示这些机制的最好方法是在存储库中创建一个变更集，并遵循三棵树。

首先，我们将使用以下命令创建一个新的存储库：

```
$ mkdir git_reset_test
$ cd git_reset_test/
$ git init .
Initialized empty Git repository in /git_reset_test/.git/
$ touch reset_lifecycle_file
$ git add reset_lifecycle_file
$ git commit -m"initial commit"
[master (root-commit) d386d86] initial commit
1 file changed, 0 insertions(+), 0 deletions(-)
create mode 100644 reset_lifecycle_file
```

上面的示例代码使用一个空文件来创建一个新的git存储库 `reset_lifecycle_file` 。 至此，示例存储库中只有一个 `d386d86` 来自 commit的commit（ ） `reset_lifecycle_file` 。

## 工作目录

我们将检查的第一棵树是“工作目录”。 该树与本地文件系统同步，代表对文件和目录中内容的立即更改。

```

$ echo 'hello git reset' > reset_lifecycle_file
$ git status
On branch master
Changes not staged for commit:
(use "git add ..." to update what will be committed)
(use "git checkout -- ..." to discard changes in working directory)
modified: reset_lifecycle_file

```

在我们的演示存储库中，我们修改了一些内容并将其添加到中 `reset_lifecycle_file` 。 调用 `git status` 表明Git知道文件的更改。 这些更改当前是第一棵树“工作目录”的一部分。 `Git status` 可用于显示对工作目录的更改。 它们将以红色显示，并带有“修改”前缀。

## 分期指数

接下来是“暂存索引”树。 该树正在跟踪工作目录更改，这些更改已通过进行了升级，并将 `git add` 存储在下一次提交中。 该树是一个复杂的内部缓存机制。 Git通常试图向用户隐藏登台索引的实现细节。

为了准确查看暂存索引的状态，我们必须使用鲜为人知的Git命令 `git ls-files` 。 该 `git ls-files` 命令实质上是一个调试实用程序，用于检查暂存索引树的状态。

```
git ls-files -s
100644 e69de29bb2d1d6434b8b29ae775ad8c2e48c5391 0 reset_lifecycle_file
```

在这里，我们 `git ls-files` 使用 `-s` 或 `--stage` 选项 执行 。 如果没有该 `-s` 选项，则 `git ls-files` 输出仅是当前属于索引的文件名和路径的列表。 该 `-s` 选项在暂存索引中显示文件的其他元数据。 该元数据是分段内容的模式位，对象名称和分段号。 在这里，我们对对象名称（第二个值（ `d7d77c1b04b5edd5acfc85de0b592449e5303770` ）） 感兴趣 。 这是标准的Git对象SHA\-1哈希。 它是文件内容的哈希。 提交历史记录存储自己的对象SHA，用于标识指向提交和引用的指针，而暂存索引具有自己的对象SHA，用于跟踪索引中的文件版本。

接下来，我们将把修改后的内容推广 `reset_lifecycle_file` 到暂存索引中。

```

$ git add reset_lifecycle_file
$ git status
On branch master Changes to be committed:
(use "git reset HEAD ..." to unstage)
modified: reset_lifecycle_file

```

在这里，我们调用 `git add reset_lifecycle_file` 了将文件添加到暂存索引的方法。 `git status` 现在 `reset_lifecycle_file` ， 调用 将以绿色 显示 在“要更改的更改”下。 重要的是要注意，这 `git status` 并不是分期索引的真实表示。 该 `git status` 命令的输出显示提交历史和分段指数之间的变化。 现在让我们检查暂存索引的内容。

```
$ git ls-files -s
100644 d7d77c1b04b5edd5acfc85de0b592449e5303770 0 reset_lifecycle_file
```

我们可以看到，对象SHA `reset_lifecycle_file` 已从更新 `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` 为 `d7d77c1b04b5edd5acfc85de0b592449e5303770` 。

## 提交历史

最后一棵树是“提交历史”。 该 `git commit` 命令将更改添加到位于“提交历史记录”中的永久快照。 该快照还包括提交时暂存索引的状态。

```
$ git commit -am"update content of reset_lifecycle_file"
[master dc67808] update content of reset_lifecycle_file
1 file changed, 1 insertion(+)
$ git status
On branch master
nothing to commit, working tree clean
```

在这里，我们创建了一个新提交，消息为 `"update content of resetlifecyclefile"` 。 变更集已添加到“提交历史记录”中。 此时调用 `git status` 表明对任何树都没有挂起的更改。 执行 `git log` 将显示提交历史记录。 现在，我们已经在三棵树上遵循了这个变更集，可以开始使用了 `git reset` 。

## 这个怎么运作

从表面上看， `git reset` 其行为与相似 `git checkout` 。 如果 `git checkout` 仅对 `HEAD` ref指针进行操作， `git reset` 则将移动 `HEAD` ref指针和当前分支的ref指针。 为了更好地演示此行为，请考虑以下示例：

![](https://wac-cdn.atlassian.com/dam/jcr:b02e7b60-742a-449d-921d-53c32410576d/git-sequence-transparent.png?cdnVersion=1084)

此示例演示了 `master` 分支 上的一系列提交 。 该 `HEAD` ref和 `master` 分支参考目前指向承诺d。 现在让我们执行和比较，无论是 `git checkout b` 和 `git reset b.`

### git checkout b

![](https://wac-cdn.atlassian.com/dam/jcr:73e231c7-ddee-4f32-94d6-a3e31e835690/git-checkout-transparent.png?cdnVersion=1084)

随着 `git checkout` 中， `master` 裁判仍然指向 `d` 。 在 `HEAD` 裁判已经被移动，现在点提交 `b` 。 回购现在处于“分离 `HEAD` ”状态。

### git reset b

![](https://wac-cdn.atlassian.com/dam/jcr:29e29d3d-dddd-480b-afd9-77169a7b0230/git-reset-transparent.png?cdnVersion=1084)

相比较而言，， 和分支引用 `git reset` 都移动 `HEAD` 到指定的提交。

除了更新commit ref指针外， `git reset` 还将修改三棵树的状态。 ref指针修改总是发生，并且是对第三棵树（提交树）的更新。 命令行参数 `--soft, --mixed` ，并 `--hard` 指示如何修改暂存索引和工作目录树。

## 主要选项

默认调用 `git reset` 具有的隐含参数 `--mixed` 和 `HEAD` 。 这意味着执行 `git reset` 等同于执行 `git reset --mixed HEAD` 。 以这种形式 `HEAD` 指定的提交。 代替 `HEAD` 任何Git SHA\-1提交哈希都可以使用。

![](https://wac-cdn.atlassian.com/dam/jcr:7fb4b5f7-a2cd-4cb7-9a32-456202499922/03%20(8).svg?cdnVersion=1084)

## \- 硬

这是最直接，最危险且最常用的选项。 通过后， `--hard` “提交历史记录”引用指针将更新为指定的提交。 然后，将暂存索引和工作目录重置为匹配指定提交的索引。 对暂存索引和工作目录的任何先前未决的更改将重置为匹配提交树的状态。 这意味着暂挂在暂挂索引和工作目录中的所有待处理工作都将丢失。

为了证明这一点，让我们继续前面建立的三棵树示例存储库。 首先，让我们对仓库进行一些修改。 在示例存储库中执行以下命令：

```
$ echo 'new file content' > new_file
$ git add new_file
$ echo 'changed content' >> reset_lifecycle_file
```

这些命令创建了一个名为的新文件 `new_file` ，并将其添加到存储库中。 此外，的内容 `reset_lifecycle_file` 将被修改。 完成这些更改后，现在让我们使用来检查回购的状态 `git status` 。

```
$ git status
On branch master
Changes to be committed:
(use "git reset HEAD ..." to unstage)
new file: new_file
Changes not staged for commit:
(use "git add ..." to update what will be committed)
(use "git checkout -- ..." to discard changes in working directory)
modified: reset_lifecycle_file
```

我们可以看到现在仓库中有待处理的更改。 暂存索引树中有一个待添加的更改， `new_file` 而工作目录中有一个待更改的更改 `reset_lifecycle_file` 。

在继续之前，让我们还检查暂存索引的状态：

```
$ git ls-files -s
100644 8e66654a5477b1bf4765946147c49509a431f963 0 new_file
100644 d7d77c1b04b5edd5acfc85de0b592449e5303770 0 reset_lifecycle_file
```

我们可以看到 `new_file` 已将其添加到索引中。 我们已进行了更新， `reset_lifecycle_file` 但暂存索引SHA（ `d7d77c1b04b5edd5acfc85de0b592449e5303770` ）保持不变。 这是预期的行为，因为尚未习惯于 `git add` 将这些更改促进到登台索引。 这些更改存在于工作目录中。

现在让我们执行a `git reset --hard` 并检查存储库的新状态。

```
$ git reset --hard
HEAD is now at dc67808 update content of reset_lifecycle_file
$ git status
On branch master
nothing to commit, working tree clean
$ git ls-files -s
100644 d7d77c1b04b5edd5acfc85de0b592449e5303770 0 reset_lifecycle_file
```

在这里，我们使用该 `--hard` 选项 执行了“硬重置” 。 Git显示输出，表明它 `HEAD` 指向最新提交 `dc67808` 。 接下来，我们使用来检查仓库的状态 `git status` 。 Git指示没有挂起的更改。 我们还检查了暂存索引的状态，并发现它已被重置到 `new_file` 添加 之前的状态 。 我们对 `reset_lifecycle_file` 和的 修改 `new_file` 已被销毁。 此数据丢失无法撤消，请务必注意。

## \-混合

这是默认的操作模式。 ref指针将更新。 暂存索引将重置为指定提交的状态。 从暂存索引撤消的所有更改都将移至工作目录。 让我们继续。

```
$ echo 'new file content' > new_file
$ git add new_file
$ echo 'append content' >> reset_lifecycle_file
$ git add reset_lifecycle_file
$ git status
On branch master
Changes to be committed:
(use "git reset HEAD ..." to unstage)
new file: new_file
modified: reset_lifecycle_file
$ git ls-files -s
100644 8e66654a5477b1bf4765946147c49509a431f963 0 new_file
100644 7ab362db063f9e9426901092c00a3394b4bec53d 0 reset_lifecycle_file
```

在上面的示例中，我们对存储库进行了一些修改。 同样，我们添加了 `new_file` 并修改了的内容 `reset_lifecycle_file` 。 然后，将这些更改应用到暂存索引 `git add` 。 在仓库处于此状态的情况下，我们现在将执行重置。

```
$ git reset --mixed
$ git status
On branch master
Changes not staged for commit:
(use "git add ..." to update what will be committed)
(use "git checkout -- ..." to discard changes in working directory)
modified: reset_lifecycle_file
Untracked files:
(use "git add ..." to include in what will be committed)
new_file
no changes added to commit (use "git add" and/or "git commit -a")
$ git ls-files -s
100644 d7d77c1b04b5edd5acfc85de0b592449e5303770 0 reset_lifecycle_file
```

在这里，我们执行了“混合重置”。 重申 `--mixed` 一下 ， 它是默认模式，与执行效果相同 `git reset` 。 检查来自 `git status` 和 的输出 `git ls-files` ，表明登台索引已重设为 `reset_lifecycle_file` 索引中唯一文件 的状态 。 SHA对象 `reset_lifecycle_file` 已被重置为先前版本。

这里要注意的重要事情是， `git status` 向我们表明对进行了修改 `reset_lifecycle_file` 并且有一个未跟踪的文件： `new_file` 。 这是显式的 `--mixed` 行为。 暂存索引已重置，并且即将进行的更改已移至工作目录。 将此与 `--hard` 重置阶段索引和工作目录也重置而丢失这些更新 的 重置情况 进行比较 。

## \- 柔软的

当 `--soft` 参数传递，裁判指针更新和复位停在那里。 暂存索引和工作目录保持不变。 这种行为可能很难清楚地证明。 让我们继续我们的演示仓库，并准备进行软重置。

```

$ git add reset_lifecycle_file
$ git ls-files -s
100644 67cc52710639e5da6b515416fd779d0741e3762e 0 reset_lifecycle_file
$ git status
On branch master
Changes to be committed:
(use "git reset HEAD ..." to unstage)
modified: reset_lifecycle_file
Untracked files:
(use "git add ..." to include in what will be committed)
new_file

```

在这里，我们再次用来 `git add` 将修改后的内容升级 `reset_lifecycle_file` 为暂存索引。 我们确认索引已用 `git ls-files` 输出 更新 。 `git status` 现在 的输出 以绿色显示“要落实的更改”。 在 `new_file` 我们前面的例子是在工作目录中漂浮的未跟踪文件。 让我们快速执行 `rm new_file` 删除文件的操作，因为在接下来的示例中我们将不需要它。

在存储库处于此状态的情况下，我们现在执行软重置。

```
$ git reset --soft
$ git status
On branch master
Changes to be committed:
(use "git reset HEAD ..." to unstage)
modified: reset_lifecycle_file
$ git ls-files -s
100644 67cc52710639e5da6b515416fd779d0741e3762e 0 reset_lifecycle_file
```

我们执行了“软重置”。 使用 `git status` 和 检查回购状态 `git ls-files` 表明没有任何变化。 这是预期的行为。 软重置只会重置提交历史记录。 默认情况下， 作为目标提交 `git reset` 调用 `HEAD` 。 由于我们的提交历史已经存在， `HEAD` 因此我们隐式重置为未 `HEAD` 发生任何实际事情。

为了更好地理解和利用 `--soft` 我们，我们需要的目标提交不是 `HEAD` 。 我们正在 `reset_lifecycle_file` 等待登台索引。 让我们创建一个新的提交。

```
$ git commit -m"prepend content to reset_lifecycle_file"
```

在这一点上，我们的回购应该有三个提交。 我们将及时回到第一次提交。 为此，我们将需要第一个提交的ID。 可以通过查看的输出找到 `git log` 。

```
$ git log
commit 62e793f6941c7e0d4ad9a1345a175fe8f45cb9df
Author: bitbucket
Date: Fri Dec 1 15:03:07 2017 -0800
prepend content to reset_lifecycle_file
commit dc67808a6da9f0dec51ed16d3d8823f28e1a72a
Author: bitbucket
Date: Fri Dec 1 10:21:57 2017 -0800
update content of reset_lifecycle_file
commit 780411da3b47117270c0e3a8d5dcfd11d28d04a4
Author: bitbucket
Date: Thu Nov 30 16:50:39 2017 -0800
initial commit
```

请记住，提交历史ID对于每个系统都是唯一的。 这意味着该示例中的提交ID将与您在个人计算机上看到的不同。 我们对此示例感兴趣的提交ID是 `780411da3b47117270c0e3a8d5dcfd11d28d04a4` 。 这是与“初始提交”相对应的ID。 找到该ID后，我们会将其用作我们的软重置目标。

在返回之前，让我们先检查回购的当前状态。

```
$ git status && git ls-files -s
On branch master
nothing to commit, working tree clean
100644 67cc52710639e5da6b515416fd779d0741e3762e 0 reset_lifecycle_file
```

在这里，我们执行一个combo命令， `git status and ``git ls-files -s` 该 命令 显示仓库中有待处理的更改，并且 `reset_lifecycle_file` 暂存索引的版本为 `67cc52710639e5da6b515416fd779d0741e3762e` 。 考虑到这一点，让我们执行软重置回到我们的第一次提交。

```
$git reset --soft 780411da3b47117270c0e3a8d5dcfd11d28d04a4
$ git status && git ls-files -s
On branch master
Changes to be committed:
(use "git reset HEAD ..." to unstage)
modified: reset_lifecycle_file
100644 67cc52710639e5da6b515416fd779d0741e3762e 0 reset_lifecycle_file
```

上面的代码执行“软重置”，还调用 `git status` and `git ls-files` 组合命令，该命令输出存储库的状态。 我们可以检查回购状态输出，并注意一些有趣的观察。 首先， `git status` 指示对它们有修改 `reset_lifecycle_file` 并突出显示它们，指示它们是为下一次提交而进行的更改。 其次， `git ls-files` 输入表明暂存索引没有更改，并保留了我们之前拥有的SHA 67cc52710639e5da6b515416fd779d0741e3762e。

为了进一步说明这次重置发生了什么，让我们检查一下 `git log:`

```
$ git log
commit 780411da3b47117270c0e3a8d5dcfd11d28d04a4
Author: bitbucket
Date: Thu Nov 30 16:50:39 2017 -0800
initial commit
```

现在，日志输出显示在“提交历史记录”中只有一个提交。 这有助于清楚地说明 `--soft` 已完成的操作。 与所有 `git reset` 调用一样，重置的第一个操作是重置提交树。 我们与 `--hard` 和的 先前示例均与 和 `--mixed` 背道而驰， `HEAD` 并且没有将提交树移回原处。 在软复位期间，这就是所有发生的情况。

这样一来，为什么 `git status` 指示存在已修改的文件 可能会造成混淆 。 `--soft` 不会触及暂存索引，因此对暂存索引的更新使我们可以追溯到提交历史。 这可以通过 `git ls-files -s` 显示SHA的 `reset_lifecycle_file` 值不变 的输出来确认 。 提醒一下， `git status` 它没有显示“三棵树”的状态，实际上显示了它们之间的差异。 在这种情况下，它显示登台索引在提交历史记录的更改之前，就好像我们已经登台了它们一样。

## 重置与还原

如果 `[git revert](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert)` 是撤消更改的“安全”方法，则可以将其 `git reset` 视为危险的方法。 确实有失去与一起工作的风险 `git reset` 。 `Git reset` 永远不会删除提交，但是，提交可能会变成“孤立的”，这意味着没有从引用访问它们的直接路径。 这些孤立的提交通常可以使用查找和恢复 `[git reflog](https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog)` 。 Git运行内部垃圾收集器后，将永久删除所有孤立的提交。 默认情况下，Git配置为每30天运行一次垃圾收集器。 提交历史记录是“三棵git树”之一，另外两个则是暂存索引和工作目录不如Commits持久。 使用此工具时必须小心，因为它是仅有的可能会丢失工作的Git命令之一。

还原旨在安全撤消公共提交，而还原旨在撤消 `git reset` 对登台索引和工作目录的本地更改。 由于它们的目标截然不同，因此这两个命令的实现方式有所不同：重置会完全删除更改集，而还原会保留原始更改集并使用新提交来应用撤消。

## 不要重置公共历史

将 `git reset <commit>` <commit>之后的任何快照推送到公共存储库时， 切勿使用 。 发布提交后，您必须假定其他开发人员都依赖它。

删除其他团队成员不断发展的承诺会给协作带来严重问题。 当他们尝试与您的存储库同步时，项目历史的一部分似乎突然消失了。 下面的序列演示了当您尝试重置公共提交时会发生的情况。 该 `origin/master` 分行是当地的中央资料库的版本 `master` 分支。

![](https://wac-cdn.atlassian.com/dam/jcr:b616f03d-5257-4ea8-a6eb-db1a0207a78a/07%20(1).svg?cdnVersion=1084)

重置后添加新的提交后，Git会认为您的本地历史记录已与分开 `origin/master` ，并且同步存储库所需的合并提交可能会使团队感到困惑和沮丧。

关键是，请确保您使用的 `git reset <commit>` 是发生错误的本地实验，而不是已发布的更改。 如果您需要修复公共提交，则该 `git revert` 命令是专门为此目的而设计的。

## 例子

```
git reset <file>
```

从暂存区中删除指定的文件，但保持工作目录不变。 这将取消登台文件而不会覆盖任何更改。

```
git reset
```

重置登台区域以匹配最新的提交，但保持工作目录不变。 这样可以取消暂存所有文件而不会覆盖任何更改，从而使您有机会从头开始重建暂存的快照。

```
git reset --hard
```

重置登台区域和工作目录以匹配最新提交。 除了取消暂存更改外，该 `--hard` 标志还告诉Git覆盖工作目录中的所有更改。 换句话说，这消除了所有未提交的更改，因此请确保您确实要在使用之前丢弃本地开发。

```
git reset <commit>
```

将当前分支提示向后移动到 `commit` ，重置登台区域以匹配，但不理会工作目录。 此后进行的所有更改都 `<commit> ` 将驻留在工作目录中，使您可以使用更清晰，更原子的快照重新提交项目历史记录。

```
git reset --hard <commit>
```

向后移动当前分支提示， `<commit> ` 并重置临时区域和工作目录以匹配。 这不仅消除了未提交的更改，而且消除了之后的所有提交。

## 取消暂存文件

`git reset` 准备暂存快照时经常遇到 该 命令。 下一个示例假定您有两个名为的文件， `hello.py` 并且 `main.py` 已经将其添加到存储库中。

```
# Edit both hello.py and main.py
# Stage everything in the current directory
git add .
# Realize that the changes in hello.py and main.py
# should be committed in different snapshots
# Unstage main.py
git reset main.py
# Commit only hello.py
git commit -m "Make some changes to hello.py"
# Commit main.py in a separate snapshot
git add main.py
git commit -m "Edit main.py"
```

如您所见， `git reset` 通过让您取消与下一次提交无关的更改 ， 可以帮助您使提交高度集中。

## 删除本地提交

下一个示例显示了一个更高级的用例。 它演示了一段时间您在进行新实验时会发生什么，但是在提交一些快照后决定完全丢弃它。

```
# Create a new file called `foo.py` and add some code to it
# Commit it to the project history
git add foo.py
git commit -m "Start developing a crazy feature"
# Edit `foo.py` again and change some other tracked files, too
# Commit another snapshot
git commit -a -m "Continue my crazy feature"
# Decide to scrap the feature and remove the associated commits
git reset --hard HEAD~2
```

该 `git reset HEAD~2` 命令将当前分支向后移动两次提交，从而有效地从项目历史记录中删除了我们刚刚创建的两个快照。 请记住，这种重置仅应用于未发布的提交。 如果已经将提交推送到共享存储库，则不要执行上述操作。

## 摘要

要查看，它 `git reset` 是一个功能强大的命令，用于撤消对Git存储库状态的本地更改。 `Git reset` 在“ Git的三棵树”上运行。 这些树是提交历史记录（ `HEAD` ），暂存索引和工作目录。 有三个与三个树对应的命令行选项。 选项 `--soft, --mixed` 和 `--hard` 可以传递给 `git reset` 。

在本文中，我们利用了其他几个Git命令来帮助演示重置过程。 在 和 的单独页面上了解有关这些命令的更多信息 。 `[git status](https://www.atlassian.com/git/tutorials/inspecting-a-repository), [git log](https://www.atlassian.com/git/tutorials/git-log), [git add](https://www.atlassian.com/git/tutorials/saving-changes), [git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout), [git reflog](https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog),` `[git revert](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert)`