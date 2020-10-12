---
title: git checkout
date: 2020-10-12 12:09:51
permalink: /pages/6ba832/
categories:
  - git入门
  - 撤销更改
tags:
  - 
---
# 撤消承诺和更改

[git checkout](https://www.atlassian.com/git/tutorials/undoing-changes) [git clean](https://www.atlassian.com/git/tutorials/undoing-changes/git-clean) [git恢复](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert) [git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset) [git rm](https://www.atlassian.com/git/tutorials/undoing-changes/git-rm)

在本节中，我们将讨论可用的“撤消” Git策略和命令。 首先要注意的是，Git没有像在文字处理应用程序中那样的传统“撤消”系统。 避免将Git操作映射到任何传统的“撤消”思维模型将是有益的。 此外，Git对于“撤消”操作有自己的命名法，最好在讨论中加以利用。 该术语包括重置，还原，签出，清除等术语。

一个有趣的隐喻是将Git视为时间轴管理实用程序。 提交是沿项目历史时间轴的某个时间点或兴趣点的快照。 此外，可以通过使用分支来管理多个时间轴。 在Git中“撤消”时，您通常会回到过去，或者回到没有发生错误的另一个时间表。

本教程提供了与软件项目的先前版本一起使用的所有必要技能。 首先，它向您展示了如何探索旧提交，然后说明了在项目历史记录中还原公共提交与在本地计算机上重置未发布的更改之间的区别。

## 查找丢失的内容：查看旧提交

任何版本控制系统背后的整个思想都是存储项目的“安全”副本，这样您就不必担心无法修复的代码库了。 建立提交的项目历史记录后，您可以查看和重新访问历史记录中的所有提交。 该 `git log` 命令 是检查Git存储库历史的最佳实用工具之一 。 在下面的示例中，我们用于 `[git log](https://www.atlassian.com/git/tutorials/git-log)` 获取对流行的开源图形库的最新提交的列表。

```
git log --oneline
e2f9a78fe Replaced FlyControls with OrbitControls
d35ce0178 Editor: Shortcuts panel Safari support.
9dbe8d0cf Editor: Sidebar.Controls to Sidebar.Settings.Shortcuts. Clean up.
05c5288fc Merge pull request #12612 from TyLindberg/editor-controls-panel
0d8b6e74b Merge pull request #12805 from harto/patch-1
23b20c22e Merge pull request #12801 from gam0022/improve-raymarching-example-v2
fe78029f1 Fix typo in documentation
7ce43c448 Merge pull request #12794 from WestLangley/dev-x
17452bb93 Merge pull request #12778 from OndrejSpanel/unitTestFixes
b5c1b5c70 Merge pull request #12799 from dhritzkiv/patch-21
1b48ff4d2 Updated builds.
88adbcdf6 WebVRManager: Clean up.
2720fbb08 Merge pull request #12803 from dmarcos/parentPoseObject
9ed629301 Check parent of poseObject instead of camera
219f3eb13 Update GLTFLoader.js
15f13bb3c Update GLTFLoader.js
6d9c22a3b Update uniforms only when onWindowResize
881b25b58 Update ProjectionMatrix on change aspect

```

每个提交都有一个唯一的SHA\-1标识哈希。 这些ID用于遍历已提交的时间轴并重新访问提交。 默认情况下， `git log` 将仅显示当前所选分支的提交。 您要查找的提交完全有可能在另一个分支上。 您可以通过执行查看所有分支上的所有提交 `git log --branches=*` 。 该命令 `[git branch](https://www.atlassian.com/git/tutorials/using-branches)` 用于查看和访问其他分支。 调用该命令， `git branch -a` 将返回所有已知分支名称的列表。 然后可以使用记录这些分支名称之一 `git log <branch_name>` 。

当找到要访问的历史记录的提交引用时，可以使用 `git checkout` 命令来访问该提交。 `Git checkout` 是将所有这些保存的快照“加载”到开发计算机上的简便方法。 在正常的开发过程中， `HEAD` 通常指向 `master` 或其他一些本地分支，但是当您签出上一个提交时， `HEAD` 不再指向分支，而是直接指向一个提交。 这称为“分离 `HEAD` ”状态，可以将其可视化如下：

![Git教程：检出上一个提交](https://wac-cdn.atlassian.com/dam/jcr:362f3b15-9e74-4fe5-b97d-784e296880ad/01.svg?cdnVersion=1084)

检出旧文件不会移动 `HEAD` 指针。 它保持在相同的分支和相同的提交上，避免了“分离头”状态。 然后，您可以像执行其他任何更改一样，在新快照中提交文件的旧版本。 因此，实际上， `git checkout` 在文件上的 这种用法 可以用作还原为单个文件的旧版本的方式。 有关这两种模式的更多信息，请访问 `[git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)` 页面

## 查看旧版本

本示例假定您已开始开发疯狂的实验，但是不确定是否要保留它。 为了帮助您做出决定，您想在开始实验之前先查看项目的状态。 首先，您需要找到要查看的修订的ID。

```
git log --oneline
```

假设您的项目历史记录如下所示：

```
b7119f2 Continue doing crazy things
872fa7e Try something crazy
a1e8fb5 Make some important changes to hello.txt
435b61d Create hello.txt
9773e52 Initial import
```

您可以使用以下 `git checkout` 方法查看“对hello.txt进行一些导入更改”提交：

```
git checkout a1e8fb5
```

这使您的工作目录与 `a1e8fb5` 提交 的确切状态相匹配 。 您可以查看文件，编译项目，运行测试甚至编辑文件，而不必担心丢失项目的当前状态。 您在此处所做的任何操作都不会保存在存储库中。 要继续开发，您需要回到项目的“当前”状态：

```
git checkout master
```

假设您正在默认 `master` 分支 上进行开发 。 返回 `master` 分支后，可以使用 `[git revert ](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert)` 或 `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)` 撤消任何不需要的更改。

## 撤消已提交的快照

从技术上讲，有几种不同的策略可以“撤消”提交。 以下示例假定我们的提交历史如下：

```
git log --oneline
872fa7e Try something crazy
a1e8fb5 Make some important changes to hello.txt
435b61d Create hello.txt
9773e52 Initial import
```

我们将专注于撤消 `872fa7e Try something crazy` 提交。 也许事情变得太疯狂了。

## 如何使用git checkout撤消提交

使用该 `git checkout` 命令，我们可以签出先前的提交， `a1e8fb5,` 从而使存储库处于疯狂提交之前的状态。 检出特定的提交将使存储库处于“分离的 HEAD ”状态。 这意味着您不再在任何分支上工作。 在分离状态下，当您将分支改回已建立的分支时，您所做的任何新提交都会被孤立。 孤立提交将由Git的垃圾收集器删除。 垃圾收集器以配置的间隔运行，并永久销毁孤立的提交。 为了防止孤立的提交被垃圾回收，我们需要确保我们在分支上。

从分离的 HEAD 状态，我们可以执行 `git checkout -b new_branch_without_crazy_commit` 。 这将创建一个名为的新分支， `new_branch_without_crazy_commit` 并切换到该状态。 现在，存储库位于新的历史记录时间轴上，其中 `872fa7e` 不再存在提交。 此时，我们可以继续在该 `872fa7e` 不再存在提交的 新分支上进行工作， 并认为它已“撤消”。 不幸的是，如果您需要上一个分支，也许是您的 `master` 分支，则此撤消策略是不合适的。 让我们看一下其他一些“撤消”策略。 有关更多信息和示例，请查看我们的深入 `[git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)`  讨论。

## 如何使用git revert撤消公共提交

假设我们回到了原始提交历史记录示例。 包含 `872fa7e` 提交 的历史记录 。 这次让我们尝试还原“撤消”。 如果执行 `git revert HEAD` ，Git将创建一个与最后一次提交相反的新提交。 这将向当前分支历史记录添加新的提交，并且现在使其类似于：

```
git log --oneline
e2f9a78 Revert "Try something crazy"
872fa7e Try something crazy
a1e8fb5 Make some important changes to hello.txt
435b61d Create hello.txt
9773e52 Initial import
```

此时，我们在技术上再次“撤消”了 `872fa7e` 提交。 尽管 `872fa7e` 历史记录中仍然存在，但是新 `e2f9a78` 提交与中的更改相反 `872fa7e` 。 与我们以前的结帐策略不同，我们可以继续使用同一分支。 此解决方案是令人满意的撤消。 这是使用公共共享存储库的理想“撤消”方法。 如果您需要保留精选的Git历史记录，则此策略可能并不令人满意。

## 如何使用git reset撤消提交

对于此撤消策略，我们将继续我们的工作示例。 `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)` 是具有多种用途和功能的广泛命令。 如果我们调用， `git reset --hard a1e8fb5` 则提交历史将重置为指定的提交。 `git log` 现在 检查提交历史记录 如下：

```
git log --oneline
a1e8fb5 Make some important changes to hello.txt
435b61d Create hello.txt
9773e52 Initial import
```

日志输出显示 `e2f9a78` 和 `872fa7e` 历史记录中不再存在 和 提交。 此时，我们可以继续工作并创建新的提交，就像从未发生过“疯狂”提交一样。 这种撤消更改的方法对历史记录的影响最大。 重置对于本地更改非常有用，但是在使用共享远程存储库时会增加复杂性。 如果我们有一个共享的远程存储库，该存储库中已 `872fa7e` 提交 了 提交，并且尝试到 `git push` 一个重置历史记录的分支，则Git将捕获此错误并抛出错误。 Git会假设由于缺少提交而被推送的分支不是最新的。 在这些情况下， `git revert` 应该是首选的撤消方法。

## 撤消上一次提交

在上一节中，我们讨论了撤消提交的不同策略。 这些策略也都适用于最新提交。 但是在某些情况下，您可能不需要删除或重置上一次提交。 也许只是过早地制作了。 在这种情况下，您可以修改最近的提交。 一旦在工作目录中进行了更多更改并通过使用将它们暂存为提交 `[git add](https://www.atlassian.com/git/tutorials/saving-changes)` ，就可以执行 `git commit --amend` 。 这将使Git打开配置的系统编辑器，并让您修改最后的提交消息。 新的更改将添加到修订的提交中。

## 撤消未提交的更改

在将更改提交到存储库历史记录之前，它们位于暂存索引和工作目录中。 您可能需要撤消这两个区域中的更改。 暂存索引和工作目录是内部Git状态管理机制。 有关这两种机制如何工作的更多详细信息，请访问对该 `[git reset](https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting)` 页面进行深入探讨 的 页面。

## 工作目录

工作目录通常与本地文件系统同步。 要撤消工作目录中的更改，您可以像平时使用自己喜欢的编辑器一样编辑文件。 Git有几个实用程序，可帮助管理工作目录。 有一个 `[git clean](https://www.atlassian.com/git/tutorials/undoing-changes/git-clean)` 命令，它是用于撤消对工作目录所做更改的便捷实用程序。 此外， `git reset` 可以使用 `--mixed` 或 `--hard` 选项 调用，并将 重置应用于工作目录。

## 阶段索引

该 `[git add](https://www.atlassian.com/git/tutorials/saving-changes)` 命令用于将更改添加到登台索引。 `Git reset` 主要用于撤消登台索引更改。 一个 `--mixed` 复位将移动从分段指数回工作目录中的所有未决更改。

## 撤消公开更改

在具有远程存储库的团队中工作时，撤消更改时需要格外考虑。 `Git reset` 通常应被视为“本地”撤消方法。 撤消对专用分支的更改时，应使用重置。 这样可以安全地将删除提交与其他开发人员可能正在使用的其他分支隔离开来。 在共享分支上执行重置，然后使用将该分支远程推送时，会出现问题 `git push` 。 在这种情况下，Git会阻止推送，因为它抱怨正在推送的分支与远程分支相比已经过期，因为它缺少提交。

取消共享历史记录的首选方法是 `git revert` 。 还原比复位更安全，因为它不会从共享历史记录中删除任何提交。 还原将保留您要撤消的提交，并创建一个新的提交来反转不需要的提交。 此方法对于共享的远程协作更安全，因为远程开发人员可以拉出分支并接收新的还原提交，从而撤消了不需要的提交。

## 摘要

我们介绍了许多用于撤消Git中事物的高级策略。 重要的是要记住，在Git项目中有不止一种“撤消”方法。 此页面上的大多数讨论都涉及更深层次的主题，这些主题在有关Git命令的特定页面上有更详尽的说明。 最常用的“撤消”工具是 和 。 要记住的一些关键点是： `[git checkout,](https://www.atlassian.com/git/tutorials/using-branches/git-checkout) [git revert](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert)` `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)`

*   一旦做出更改，它们通常是永久的
*   用于 `git checkout` 四处浏览并查看提交历史记录
*   `git revert` 是撤消共享公共更改的最佳工具
*   `git reset` 最适用于撤消本地私有更改

除了主要的undo命令之外，我们还查看了其他Git实用程序： `[git log](https://www.atlassian.com/git/tutorials/git-log)` 查找丢失的提交， `[git clean](https://www.atlassian.com/git/tutorials/undoing-changes/git-clean)` 以撤消 `[git add](https://www.atlassian.com/git/tutorials/saving-changes)` 用于更改登台索引的 未提交的更改 。

每个命令都有其自己的深入文档。 要了解有关此处提到的特定命令的更多信息，请访问相应的链接。