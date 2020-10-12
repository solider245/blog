---
title: Git合并冲突
date: 2020-10-12 12:09:51
permalink: /pages/be3cf0/
categories:
  - git入门
  - 使用分支
tags:
  - 
---
# Git合并冲突

版本控制系统都是关于管理多个分布式作者（通常是开发人员）之间的贡献的。 有时，多个开发人员可能会尝试编辑相同的内容。 如果开发人员A尝试编辑开发人员B正在编辑的代码，则可能会发生冲突。 为了减轻冲突的发生，开发人员将在单独的 [隔离分支中工作](https://www.atlassian.com/git/tutorials/using-branches) 。 该 `git merge` 命令的主要职责是合并单独的分支并解决所有冲突的编辑。

## 了解合并冲突

合并和冲突是Git体验的常见部分。 其他版本控制工具（如SVN）中的冲突可能既昂贵又耗时。 Git使合并变得非常容易。 大多数时候，Git会弄清楚如何自动集成新更改。

当两个人更改了文件中的相同行时，或者如果一个开发人员删除了文件而另一位开发人员正在修改文件时，通常会发生冲突。 在这些情况下，Git无法自动确定正确的内容。 冲突仅影响进行合并的开发人员，其余团队则不知道冲突。 Git会将文件标记为已冲突，并停止合并过程。 解决冲突是开发人员的责任。

## 合并冲突的类型

合并可以在两个单独的点进入冲突状态。 启动时以及在合并过程中。 以下是关于如何解决这些冲突情况中的每一个的讨论。

### Git无法启动合并

当Git看到当前项目的工作目录或临时区域中有更改时，合并将无法开始。 Git无法启动合并，因为这些待处理的更改可能会被合并的提交所覆盖。发生这种情况时，这并不是由于与其他开发人员的冲突，而是与暂挂的本地更改冲突。 当地的国家将需要使用稳定 `git stash` ， `git checkout` ， `git commit` 或 `git reset` 。 启动时合并失败将输出以下错误消息：

```
error: Entry '<fileName>' not uptodate. Cannot merge. (Changes in working directory)
```

### 合并期间Git失败

合并期间的失败表示当前本地分支与正在合并的分支之间存在冲突。 这表明与另一个开发人员代码冲突。 Git将尽最大努力合并文件，但会在冲突的文件中让您手动解决问题。 合并中失败将输出以下错误消息：

```
error: Entry '<fileName>' would be overwritten by merge. Cannot merge. (Changes in staging area)
```

## 产生合并冲突

为了真正熟悉合并冲突，下一节将模拟冲突以供以后检查和解决。 该示例将使用类似Unix的命令行Git接口来执行示例仿真。

```
$ mkdir git-merge-test$ cd git-merge-test$ git init .$ echo "this is some content to mess with" > merge.txt$ git add merge.txt$ git commit -am"we are commiting the inital content"[master (root-commit) d48e74c] we are commiting the inital content1 file changed, 1 insertion(+)create mode 100644 merge.txt
```

此代码示例执行一系列命令来完成以下任务。

*   创建一个名为 `git-merge-test,` change 的新目录 ，并将其初始化为新的Git存储库。
*   创建一个新的文本文件 `merge.txt` ，其中包含一些内容。
*   添加 `merge.txt` 到仓库并提交。

现在我们有了一个带有一个分支的新仓库， `master` 以及一个 `merge.txt` 包含内容 的文件 。 接下来，我们将创建一个新分支，以用作冲突合并。

```
$ git checkout -b new_branch_to_merge_later$ echo "totally different content to merge later" > merge.txt$ git commit -am"edited the content of merge.txt to cause a conflict"[new_branch_to_merge_later 6282319] edited the content of merge.txt to cause a conflict1 file changed, 1 insertion(+), 1 deletion(-)
```

前进的命令序列实现以下目的：

*   创建并签出一个名为的新分支 `new_branch_to_merge_later`
*   覆盖内容 `merge.txt`
*   提交新内容

有了这个新分支： `new_branch_to_merge_later` 我们创建了一个覆盖以下内容的提交： `merge.txt`

```
git checkout masterSwitched to branch 'master'echo "content to append" >> merge.txtgit commit -am"appended content to merge.txt"[master 24fbe3c] appended content to merge.tx1 file changed, 1 insertion(+)
```

此命令链签出 `master` 分支，将内容追加到 `merge.txt` ，然后提交。 现在，这会将我们的示例存储库置于一个有2个新提交的状态。 一个在 `master` 分支中，一个在 `new_branch_to_merge_later` 分支中。 这时让我们 `git merge new_branch_to_merge_later` 看看会发生什么！

```
$ git merge new_branch_to_merge_laterAuto-merging merge.txtCONFLICT (content): Merge conflict in merge.txtAutomatic merge failed; fix conflicts and then commit the result.
```

OM。 出现冲突。 感谢Git，让我们知道这一点！

## 如何识别合并冲突

正如我们从后面的示例中所经历的那样，Git将产生一些描述性的输出，从而使我们知道发生了冲突。 我们可以通过运行 `[git status](https://www.atlassian.com/git/tutorials/inspecting-a-repository)` 命令 来获得更多的见解

```
$ git statusOn branch masterYou have unmerged paths.(fix conflicts and run "git commit")(use "git merge --abort" to abort the merge)Unmerged paths:(use "git add <file>..." to mark resolution)both modified:   merge.txt
```

来自的输出 `git status` 指示由于冲突而存在未合并的路径。 该 `merge.text` 文件现在显示为已修改状态。 让我们检查文件，看看有什么修改。

```
$ cat merge.txt<<<<<<< HEADthis is some content to mess withcontent to append=======totally different content to merge later>>>>>>> new_branch_to_merge_later
```

在这里，我们使用了 `cat` 命令来放置 `merge.txt ` 文件 的内容 。 我们可以看到一些奇怪的新添加

*   `<<<<<<< HEAD`
*   `=======`
*   `>>>>>>> new_branch_to_merge_later`

将这些新行视为“冲突分隔符”。 这 `=======` 条线是冲突的“中心”。 中心和 `<<<<<<< HEAD` 线 之间的所有内容 都是 `HEAD` 引用所指向 的当前分支母版中存在的内容 。 或者，中心与之间的所有内容 `>>>>>>> new_branch_to_merge_later` 都是合并分支中存在的内容。

## 如何使用命令行解决合并冲突

解决合并冲突的最直接方法是编辑冲突的文件。 `merge.txt` 在您喜欢的编辑器中 打开 文件。 对于我们的示例，只需删除所有冲突分隔符即可。 修改后的 `merge.txt` 内容应如下所示：

```
this is some content to mess withcontent to appendtotally different content to merge later
```

编辑完文件后，可 `git add merge.txt` 用于暂存新的合并内容。 要完成合并，请通过执行以下操作创建一个新的提交：

```
git commit -m "merged and resolved the conflict in merge.txt"
```

Git将看到冲突已解决，并创建一个新的合并提交以完成合并。

## 可以帮助解决合并冲突的Git命令

### 通用工具

```
git status
```

当使用Git进行合并时，经常使用status命令，这将有助于识别冲突的文件。

```
git log --merge
```

将 `--merge` 参数 传递 给 `git log` 命令将产生一个日志，其中包含合并分支之间冲突的提交列表。

```
git diff
```

`diff` 帮助查找存储库/文件状态之间的差异。 这对于预测和防止合并冲突很有用。

### git无法启动合并的工具

```
git checkout
```

`checkout` 可用于 *撤消* 对文件的更改或更改分支

```
git reset --mixed
```

`reset` 可用于撤消对工作目录和登台区域的更改。

### 合并期间发生git冲突时的工具

```
git merge --abort
```

`git merge` 使用该 `--abort` 选项 执行 将退出合并过程，并使分支返回到合并开始之前的状态。

```
git reset
```

`Git reset` 可以在合并冲突期间用于将冲突的文件重置为已知状态

## 摘要

合并冲突可能是一个令人生畏的经历。 幸运的是，Git提供了强大的工具来帮助导航和解决冲突。 Git可以利用自动合并功能自行处理大多数合并。 当两个单独的分支对文件中的同一行进行编辑时，或者当一个分支中的文件被删除而另一个分支中的文件被编辑时，就会发生冲突。 在团队环境中工作时很可能会发生冲突。

有许多工具可帮助解决合并冲突。 Git有很多我们在这里讨论过的命令行工具。 有关这些工具的更多详细信息，请访问单机网页 `[git log](https://www.atlassian.com/git/tutorials/git-log)` ， `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)` ， `[git status](https://www.atlassian.com/git/tutorials/inspecting-a-repository)` ， `[git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)` ，和 `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)` 。 除了Git外，许多第三方工具还提供了简化的合并冲突支持功能。