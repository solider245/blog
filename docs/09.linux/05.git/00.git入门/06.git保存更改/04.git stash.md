---
title: git stash
date: 2020-10-12 12:09:51
permalink: /pages/cd77f7/
categories:
  - git入门
  - git保存更改
tags:
  - 
---
# Git藏匿处

[git添加](https://www.atlassian.com/git/tutorials/saving-changes) [git commit](https://www.atlassian.com/git/tutorials/saving-changes/git-commit) [git diff](https://www.atlassian.com/git/tutorials/saving-changes/git-diff) [git stash](https://www.atlassian.com/git/tutorials/saving-changes/git-stash) [.gitignore](https://www.atlassian.com/git/tutorials/saving-changes/gitignore)

`git stash` 暂时搁置（或 *隐藏* ）您对工作副本所做的更改，以便您可以处理其他内容，然后再返回并稍后重新应用它们。 如果您需要快速切换上下文并进行其他操作，则存储很方便，但是您正处于代码更改的中间，还没有准备好提交。

*   吉特·斯塔什
    *   [藏匿工作](#stashing-your-work)
    *   [重新应用隐藏的更改](#re-applying-your-stashed-changes)
    *   [隐藏未跟踪或忽略的文件](#stashing-untracked-or-ignored)
    *   [管理多个存储](#managing-multiple-stashes)
    *   [查看隐藏差异](#viewing-stash-diffs)
    *   [部分藏匿处](#partial-stashes)
    *   [从您的藏身处创建一个分支](#creating-a-branch-from-your-stash)
    *   [清理你的藏匿处](#cleaning-up-your-stash)
    *   [git stash如何工作](#how-git-stash-works)

## 藏匿工作

该 `git stash` 命令将您未提交的更改（暂存的和未暂存的）进行保存，将其保存以备后用，然后从工作副本中将其还原。 例如：

```
$ git status
On branch master
Changes to be committed:
new file: style.css
Changes not staged for commit:
modified: index.html
$ git stash
Saved working directory and index state WIP on master: 5002d47 our new homepage
HEAD is now at 5002d47 our new homepage
$ git status
On branch master
nothing to commit, working tree clean
```

此时，您可以自由进行更改，创建新的提交，切换分支以及执行任何其他Git操作。 然后回来，准备好后重新套上你的藏匿处。

请注意，该存储区在您的Git存储库本地； 推送时，存储的资源不会转移到服务器。

## 重新应用隐藏的更改

您可以使用以下方法重新应用先前隐藏的更改 `git stash pop` ：

```
$ git status
On branch master
nothing to commit, working tree clean
$ git stash pop
On branch master
Changes to be committed:
new file: style.css
Changes not staged for commit:
modified: index.html
Dropped refs/stash@{0} (32b3aa1d185dfe6d57b3c3cc3b32cbf3e380cc6a)
```

*弹出* 存储库会将更改从存储库中删除，然后将其重新应用到您的工作副本中。

或者，您可以将更改重新应用于工作副本， *并通过以下方式* 将其保存在存储中 `git stash apply` ：

```
$ git stash apply
On branch master
Changes to be committed:
new file: style.css
Changes not staged for commit:
modified: index.html
```

如果要将相同的隐藏更改应用于多个分支，这将很有用。

既然您了解了存储的基础知识，那么 `git stash` 您需要意识到 一个警告 ：默认情况下，Git *不会* 存储对未跟踪或忽略的文件所做的更改。

## 隐藏未跟踪或忽略的文件

默认情况下，运行 `git stash` 将隐藏：

*   已添加到索引的更改（分阶段更改）
*   对Git当前跟踪的文件所做的更改（未暂存的更改）

但这 **不会** 藏起来：

*   工作副本中尚未暂存的新文件
*   被 [忽略的](https://www.atlassian.com/git/tutorials/gitignore) 文件[](https://www.atlassian.com/git/tutorials/gitignore)

因此，如果我们在上面的示例中添加了第三个文件，但是不暂存（即，我们不运行 `git add` ）， `git stash` 则不会将其存放。

```
$ script.js
$ git status
On branch master
Changes to be committed:
new file: style.css
Changes not staged for commit:
modified: index.html
Untracked files:
script.js
$ git stash
Saved working directory and index state WIP on master: 5002d47 our new homepage
HEAD is now at 5002d47 our new homepage
$ git status
On branch master
Untracked files:
script.js
```

添加 `-u` 选项（或 `--include-untracked` ） `git stash` 还可以隐藏未跟踪的文件：

```
$ git status
On branch master
Changes to be committed:
new file: style.css
Changes not staged for commit:
modified: index.html
Untracked files:
script.js
$ git stash -u
Saved working directory and index state WIP on master: 5002d47 our new homepage
HEAD is now at 5002d47 our new homepage
$ git status
On branch master
nothing to commit, working tree clean
```

您还可以 通过 在运行时 传递 选项（或 ） 来包括对 [忽略](https://www.atlassian.com/git/tutorials/gitignore) 文件的 更改 。 `-a` `--all` `git stash`

![Git Stash选项](https://wac-cdn.atlassian.com/dam/jcr:d6fec41a-dc66-4af6-8b0f-c23d271eaf8e/01.svg?cdnVersion=1084)

## 管理多个存储

您不仅限于一个存储区。 您可以运行 `git stash` 几次以创建多个存储，然后使用 `git stash list` 它们来查看它们。 默认情况下，存储区在分支顶部被简单标识为“ WIP”（正在进行中），并提交您从中创建存储区的提交。 一段时间后，可能很难记住每个存储区包含的内容：

```
$ git stash list
stash@{0}: WIP on master: 5002d47 our new homepage
stash@{1}: WIP on master: 5002d47 our new homepage
stash@{2}: WIP on master: 5002d47 our new homepage
```

为了提供更多的上下文信息，一个很好的做法是使用以下说明对存储进行注释 `git stash save "message"` ：

```
$ git stash save "add style to our site"
Saved working directory and index state On master: add style to our site
HEAD is now at 5002d47 our new homepage
$ git stash list
stash@{0}: On master: add style to our site
stash@{1}: WIP on master: 5002d47 our new homepage
stash@{2}: WIP on master: 5002d47 our new homepage
```

默认情况下， `git stash pop` 将重新应用最近创建的存储： `stash@{0}`

您可以通过将其标识符作为最后一个参数传递来选择要重新应用的存储，例如：

```
$ git stash pop stash@{2}
```

## 查看隐藏差异

您可以使用以下方式查看存储的摘要 `git stash show` ：

```
$ git stash show
index.html | 1 +
style.css | 3 +++
2 files changed, 4 insertions(+)
```

或通过 `-p` 选项（或 `--patch` ）查看隐藏的完整差异：

```
$ git stash show -p
diff --git a/style.css b/style.css
new file mode 100644
index 0000000..d92368b
--- /dev/null
+++ b/style.css
@@ -0,0 +1,3 @@
+* {
+ text-decoration: blink;
+}
diff --git a/index.html b/index.html
index 9daeafb..ebdcbd2 100644
--- a/index.html
+++ b/index.html
@@ -1 +1,2 @@
+<link rel="stylesheet" href="style.css"/>
```

## 部分藏匿处

您也可以选择隐藏一个文件，一个文件集合或文件中的单个更改。 如果将 `-p` 选项（或 `--patch` ） 传递 给 `git stash` ，它将在工作副本中遍历每个已更改的“大块”，并询问是否要存储它：

```
$ git stash -p
diff --git a/style.css b/style.css
new file mode 100644
index 0000000..d92368b
--- /dev/null
+++ b/style.css
@@ -0,0 +1,3 @@
+* {
+ text-decoration: blink;
+}
Stash this hunk [y,n,q,a,d,/,e,?]? y
diff --git a/index.html b/index.html
index 9daeafb..ebdcbd2 100644
--- a/index.html
+++ b/index.html
@@ -1 +1,2 @@
+<link rel="stylesheet" href="style.css"/>
Stash this hunk [y,n,q,a,d,/,e,?]? n
```

![Git Stash -p](https://wac-cdn.atlassian.com/dam/jcr:4f32476c-e84f-41b3-a7d9-1b5a70acb22b/02.svg?cdnVersion=1084)

你可以打 **吗？** 有关大块命令的完整列表。 常用的是：

| **命令** | **描述** |
| --- | --- |
| */* | 用正则表达式搜索大块 |
| --- | --- |
| *？* | 救命 |
| --- | --- |
| *ñ* | 不要藏起来 |
| --- | --- |
| *q* | 退出（将隐藏所有已选择的大块头） |
| --- | --- |
| *s* | 分割成较小的块 |
| --- | --- |
| *ÿ* | 藏起来这个大块头 |
| --- | --- |

没有显式的“中止”命令，但单击 `CTRL-C` （SIGINT）将中止存储过程。

## 从您的藏身处创建一个分支

如果分支上的更改与存储中的更改有所不同，则在弹出或应用存储时可能会发生冲突。 相反，您可以使用 `git stash branch` 创建一个新分支，将已保存的更改应用于：

```
$ git stash branch add-stylesheet stash@{1}
Switched to a new branch 'add-stylesheet'
On branch add-stylesheet
Changes to be committed:
new file: style.css
Changes not staged for commit:
modified: index.html
Dropped refs/stash@{1} (32b3aa1d185dfe6d57b3c3cc3b32cbf3e380cc6a)
```

这将基于您创建存储的提交签出一个新分支，然后将隐藏的更改弹出到该分支。

## 清理你的藏匿处

如果您决定不再需要特定的存储，可以使用以下命令将其删除 `git stash drop` ：

```
$ git stash drop stash@{1}
Dropped stash@{1} (17e2697fd8251df6163117cb3d58c1f62a5e7cdb)
```

或者，您可以使用以下方法删除所有存储空间：

```
$ git stash clear
```

## git stash如何工作

如果您只是想知道如何使用 `git stash` ，可以在这里停止阅读。 但是，如果您对Git（和 `git stash` ）的工作原理 感到好奇 ，请继续阅读！

缓存实际上在您的存储库中被编码为提交对象。 `.git/refs/stash` 指向您最近创建的存储区以及以前创建的存储区 的特殊ref 被该 `stash` 引用的reflog引用。 这就是为什么您通过 `stash@{n}:` 实际引用引用引用第n个引用日志条目来 `stash` 引用存储的原因。 由于隐藏只是一个提交，因此可以使用以下命令进行检查 `git log` ：

```
$ git log --oneline --graph stash@{0}
*-. 953ddde WIP on master: 5002d47 our new homepage
|\ \
| | * 24b35a1 untracked files on master: 5002d47 our new homepage
| * 7023dd4 index on master: 5002d47 our new homepage
|/
* 5002d47 our new homepage
```

根据您所藏的东西，一个 `git stash` 操作可以创建两个或三个新的提交。 上图中的提交为：

*   `stash@{0}` ，新提交用于存储运行时工作副本中的跟踪文件 `git stash`
*   `stash@{0}` 的第一个父对象，即您运行时在HEAD处的先前提交 `git stash`
*   `stash@{0}` 的第二个父级，当您运行时代表索引的新提交 `git stash`
*   `stash@{0}` 的第三个父级，一个新提交，表示运行时工作副本中未跟踪的文件 `git stash` 。 仅在以下情况下创建此第三个父级：
    *   您的工作副本实际上包含未跟踪的文件； 和
    *   您 在调用时 指定了 `--include-untracked` 或 `--all` 选项 `git stash` 。

如何 `git stash` 将工作树和索引编码为提交：

*   存放之前，您的工作树可能包含对跟踪文件，未跟踪文件和忽略文件的更改。 其中一些更改也可能在索引中进行。

    ![存放之前](https://wac-cdn.atlassian.com/dam/jcr:3a2ede93-1f2d-45ae-9e0b-167cc0362f37/03.2017-12-12-00-28-29.svg)

*   调用 `git stash` 会将对跟踪文件的所有更改编码为DAG中的两个新提交：一个用于未暂存的更改，另一个用于在索引中暂存的更改。 特殊 `refs/stash` 参考已更新为指向它们。

    ![Git藏匿处](https://wac-cdn.atlassian.com/dam/jcr:35edaf68-e8b1-484e-b5f0-292c532f048a/04.2017-12-12-00-28-29.svg)

*   使用该 `--include-untracked` 选项还将对未跟踪文件的所有更改编码为附加提交。

    ![Git隐藏--include-untracked](https://wac-cdn.atlassian.com/dam/jcr:f7dd5493-a98d-449e-ae37-146d6270ccf7/05.2017-12-12-00-28-29.svg)

*   使用该 `--all` 选项包括对所有忽略文件的更改以及对同一提交中未跟踪文件的更改。

    ![Git Stash-全部](https://wac-cdn.atlassian.com/dam/jcr:446fad60-0ff5-4383-8177-a5fc2813364d/06.2017-12-12-00-28-29.svg "Git Stash-全部")

运行时 `git stash pop` ，将使用上述提交中的更改来更新您的工作副本和索引，并且将存储引用日志改编以删除弹出的提交。 请注意，弹出的提交不会立即删除，但会成为将来垃圾回收的候选对象。