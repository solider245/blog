---
title: git rm
date: 2020-10-12 12:09:51
permalink: /pages/0e8516/
categories:
  - git入门
  - 撤销更改
tags:
  - 
---
# Git RM

[git checkout](https://www.atlassian.com/git/tutorials/undoing-changes) [git clean](https://www.atlassian.com/git/tutorials/undoing-changes/git-clean) [git恢复](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert) [git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset) [git rm](https://www.atlassian.com/git/tutorials/undoing-changes/git-rm)

开始使用Git时，一个常见的问题是“如何告诉Git不再跟踪文件？” 该 `git rm` 命令用于从Git存储库中删除文件。 可以将其视为 `[git add](https://www.atlassian.com/git/tutorials/saving-changes)`  命令 的逆函数 。

## Git rm概述

该 `git rm` 命令可用于删除单个文件或文件集合。 的主要功能 `git rm` 是从Git索引中删除跟踪的文件。 此外， `git rm` 可用于从登台索引和工作目录中删除文件。 没有选择仅从工作目录中删除文件的选项。 正在操作的文件必须与当前文件相同 `HEAD` 。 如果 `HEAD` 文件版本与登台索引或工作树版本 之间存在差异 ，则Git将阻止删除。 此块是一种安全机制，可防止删除正在进行的更改。

请注意， `git rm` 这不会删除分支。 了解有关 [使用git分支的](https://www.atlassian.com/git/tutorials/using-branches) 更多信息[](https://www.atlassian.com/git/tutorials/using-branches)

## 用法

```
<file>…​
```

指定要删除的目标文件。 选项值可以是单个文件，以空格分隔的文件列表 `file1 file2 file3` 或通配符文件glob `(~./directory/*)` 。

```
-f--force
```

该 `-f` 选项用于覆盖Git进行的安全检查，以确保文件 `HEAD` 与暂存索引和工作目录中的当前内容匹配。

```
-n--dry-run
```

“空运行”选项是一种安全措施，可以执行 `git rm` 命令但实际上不会删除文件。 相反，它将输出将要删除的文件。

```
-r
```

该 `-r` 选项是“递归”的简写。 在递归模式下运行时， `git rm` 将删除目标目录和该目录的所有内容。

```
--
```

分隔符选项用于显式区分文件名列表和传递给的参数 `git rm` 。 如果某些文件名的语法可能会误认为其他选项，这将很有用。

```
--cached
```

cached选项指定删除仅应在登台索引上进行。 工作目录文件将被保留。

```
--ignore-unmatch
```

即使没有文件匹配，这也会导致命令以0 sigterm状态退出。 这是Unix级别的状态代码。 代码0表示命令成功调用。 `--ignore-unmatch` 当 `git rm` 作为需要正常失败的更大的Shell脚本的一部分 使用时， 该 选项可能会有所帮助 。

```
-q--quiet
```

quiet选项隐藏 `git rm` 命令 的输出 。 该命令通常为每个删除的文件输出一行。

## 如何撤消git rm

执行 `git rm` 不是永久更新。 该命令将更新登台索引和工作目录。 在创建新的提交并将更改添加到提交历史记录之前，这些更改将不会保留。 这意味着可以使用通用的Git命令“撤消”此处的更改。

```
git reset HEAD
```

重置会将当前的登台索引和工作目录还原回 `HEAD` 提交。 这将撤消 `git rm` 。

```
git checkout .
```

检出将具有相同的效果，并从中恢复文件的最新版本 `HEAD` 。

如果 `git rm` 已执行并且创建了新的提交（该删除将持久删除）， `git reflog` 则可以使用 该提交 来查找 `git rm` 执行 之前的引用 。 了解有关 [使用git reflog的](https://www.atlassian.com/git/tutorials/rewriting-history/git-reflog) 更多信息 。

## 讨论区

`file>` 赋予命令 的< 参数可以是精确路径，通配符文件glob模式或精确目录名称。 该命令仅删除当前提交到Git存储库的路径。

通配符文件遍历在目录之间匹配。 使用通配符时要小心，这一点很重要。 考虑以下示例： `directory/*` 和 `directory*` 。 第一个示例将删除的所有子文件， `directory/` 而第二个示例将删除所有的兄弟目录，例如 `directory1` `directory2` `directory_whatever` 可能会导致意外的结果。

## git rm的范围

该 `git rm` 命令仅在当前分支上运行。 删除事件仅应用于工作目录和暂存索引树。 在创建新的提交之前，文件删除不会一直保留到存储库历史记录中。

## 为什么用git rm代替rm

Git存储库将识别 `rm` 出它正在跟踪的文件上 何时执行了常规Shell 命令。 它将更新工作目录以反映删除。 它不会使用删除操作更新登台索引。 `git add` 必须在已删除的文件路径上执行 一条附加 命令，以将更改添加到登台索引。 该 `git rm` 命令充当快捷方式，因为它将通过删除来更新工作目录和登台索引。

## 例子

```
git rm Documentation/\*.txt
```

本例中使用通配符文件名匹配删除所有 `*.txt files` 属于儿童 `Documentation` 目录及其所有子目录。

请注意，在此示例中，星号\*以斜杠转义； 这是防止外壳扩展通配符的防护措施。 然后，通配符将扩展目录下文件和子目录的路径名 `Documentation/` 。

```
git rm -f git-*.sh
```

本示例使用force选项，并定位所有通配符 `git-*.sh` 文件。 force选项可从工作目录和登台索引中显式删除目标文件。

## 如何删除不再在文件系统中的文件

如上文“为什么要使用 `git rm` 而不是 `rm` ”中所述， `git rm` 实际上是一个便捷命令，它结合了标准Shell `rm` 并 `git add` 从工作目录中删除文件并将该删除提升为暂存索引。 如果仅使用标准shell `rm` 命令 删除了几个文件，则存储库可能会陷入繁琐的状态 。

如果打算记录所有明确删除的文件作为下一次提交的一部分， `git commit -a` 则将所有删除事件添加到登台索引中以准备下一次提交。

但是，如果打算永久删除用shell删除的文件 `rm` ，请使用以下命令：

```
git diff --name-only --diff-filter=D -z | xargs -0 git rm --cached
```

该命令将生成一个从工作目录中删除的文件的列表，并通过管道将该列表 `git rm --cached` 更新登台索引。

## Git rm摘要

`git rm` 是在两个主要的Git [内部状态管理树上](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset) 运行的命令 ：工作目录和登台索引。 `git rm` 用于从Git存储库中删除文件。 这是一种方便的方法，将默认shell `rm` 命令 的效果与结合 在一起 `git add` 。 这意味着它将首先从文件系统中删除目标，然后将该删除事件添加到暂存索引中。 该命令是可用于 [撤消Git更改](https://www.atlassian.com/git/tutorials/undoing-changes) 的众多命令之一 [。](https://www.atlassian.com/git/tutorials/undoing-changes)