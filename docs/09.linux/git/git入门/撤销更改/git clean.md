---
title: git clean
date: 2020-10-12 12:09:51
permalink: /pages/4afc63/
categories:
  - git入门
  - 撤销更改
tags:
  - 
---
# Git清洁

[git checkout](https://www.atlassian.com/git/tutorials/undoing-changes) [git clean](https://www.atlassian.com/git/tutorials/undoing-changes/git-clean) [git恢复](https://www.atlassian.com/git/tutorials/undoing-changes/git-revert) [git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset) [git rm](https://www.atlassian.com/git/tutorials/undoing-changes/git-rm)

在本节中，我们将集中于 `git clean` 命令 的详细讨论 。 `Git clean` 在某种程度上是“撤消”命令。 `Git clean` 可以被认为是对其他命令（例如 `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)` 和）的 补充 `[git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)` 。 这些其他命令对先前添加到Git跟踪索引的 `git clean` 文件进行操作 ，而该 命令对未跟踪的文件进行操作。 未跟踪的文件是在仓库的工作目录中创建但尚未使用 `[git add](https://www.atlassian.com/git/tutorials/saving-changes)` 命令 添加到存储库的跟踪索引中的文件 。 为了更好地说明跟踪文件和未跟踪文件之间的区别，请考虑以下命令行示例：

```
$ mkdir git_clean_test
$ cd git_clean_test/
$ git init .
Initialized empty Git repository in /Users/kev/code/git_clean_test/.git/
$ echo "tracked" > ./tracked_file
$ git add ./tracked_file
$ echo "untracked" > ./untracked_file
$ mkdir ./untracked_dir && touch ./untracked_dir/file
$ git status
On branch master
Initial commit
Changes to be committed: (use "git rm --cached <file>..." to unstage)
new file: tracked_file
Untracked files: (use "git add <file>..." to include in what will be committed) untracked_dir/ untracked_file
```

该示例在 `git_clean_test` 目录中 创建一个新的Git存储库 。 然后，它继续创建一个 `tracked_file` ，将其添加到Git索引中，此外， `untracked_file` 还创建了一个和 `untracked_dir` 。 然后 `git status` ， 该示例调用 ，显示显示指示Git跟踪和未跟踪更改的内部状态的输出。 在存储库处于此状态的情况下，我们可以执行 `git clean` 命令以证明其预期目的。

```
$ git clean fatal: clean.requireForce defaults to true and neither -i, -n, nor -f given; refusing to clean
```

此时，执行默认 `git clean` 命令可能会产生致命错误。 上面的示例演示了它的外观。 默认情况下，Git全局配置为要求 `git clean` 传递“强制”选项来启动。 这是重要的安全机制。 最终执行时 `git clean` 不可撤消。 完全执行后， `git clean` 将 执行 硬文件系统删除，类似于执行命令行rm实用程序。 在运行之前，请确保您确实要删除未跟踪的文件。

## 常用选项和用法

鉴于先前对默认 `git clean` 行为和警告的 解释 ，以下内容演示了各种 `git clean` 用例及其操作所需的随附命令行选项。

```
-n
```

该 `-n` 选项将执行“空运行” `git clean` 。 这将向您显示要删除的文件，而不实际删除它们。 最佳做法是始终先执行 `git clean` 。 我们可以在我们先前创建的演示仓库中演示该选项。

```
$ git clean -n
Would remove untracked_file
```

输出告诉我们 `untracked_file` 在 `git clean` 执行命令 时将其删除 。 请注意， `untracked_dir` 此处未在输出中报告。 默认情况下， `git clean` 不会对目录进行递归操作。 这是防止意外永久删除的另一安全机制。

```
-f or --force
```

force选项启动从当前目录中实际删除未跟踪文件的操作。 除非 `clean.requireForce` 配置选项设置为false， 否则需要强制 。 这不会删除所指定的未跟踪文件夹或文件 `.gitignore` 。 现在让我们 `git clean` 在示例回购中 执行实时操作 。

```
$ git clean -f
Removing untracked_file
```

该命令将输出已删除的文件。 您可以在此处看到 `untracked_file` 已删除的内容。 此时执行 `git status` 或执行 `ls` 遗嘱将显示 `untracked_file` 已删除且无处可寻。 默认情况下 `git clean -f` 将对所有当前目录中未跟踪的文件进行操作。 另外，可以使用<path>值传递 `-f` 选项， 该 选项将删除特定文件。

```
git clean -f <path>
-d include directories
```

该 `-d` 选项 `git clean` 表明您还希望删除所有未跟踪的目录，默认情况下它将忽略目录。 我们可以将 `-d` 选项 添加 到前面的示例中：

```
$ git clean -dn
Would remove untracked_dir/
$ git clean -df
Removing untracked_dir/
```

在这里，我们使用 `-dn` 组合来 执行“空运行”， 其输出将 `untracked_dir` 被移除。 然后，我们执行强制清理，并接收 `untracked_dir` 已删除的 输出 。

```
-x force removal of ignored files
```

常见的软件发行模式是具有未提交到存储库跟踪索引的构建或发行目录。 构建目录将包含从提交的源代码生成的临时构建工件。 通常将此构建目录添加到存储库 `.gitignore` 文件中。 也可以使用其他未跟踪的文件来清理此目录，这很方便。 该 `-x` 选项指示 `git clean` 还包括所有忽略的文件。 与以前的 `git clean` 调用一样，最佳实践是在最终删除之前先执行“空运行”。 该 `-x` 选项将作用于所有被忽略的文件，而不仅仅是项目构建特定的文件。 这可能是意外的事情，例如./.idea IDE配置文件。

```
git clean -xf

```

喜欢的 `-d` 选项 `-x` 可以传递并与其他选项组成。 本示例演示了一种与的组合， `-f` 该 组合 将从当前目录中删除未跟踪的文件以及Git通常忽略的所有文件。

## 交互模式或git clean交互

到目前为止，我们已经演示了除了临时命令行执行之外， `git clean` 还具有“交互”模式，您可以通过传递 `-i` 选项 来启动该 模式。 让我们回顾一下本文介绍中的示例存储库。 在初始状态下，我们将开始一个交互式的干净会话。

```
$ git clean -di
Would remove the following items:
untracked_dir/ untracked_file
*** Commands ***
1: clean 2: filter by pattern 3: select by numbers 4: ask each 5: quit 6: help
What now>
```

我们已经启动了带有 `-d` 选项 的交互式会话， 因此它也将对我们起作用 `untracked_dir` 。 交互模式将显示 `What now>` 提示，提示要求命令将其应用于未跟踪的文件。 这些命令本身很容易说明。 我们将以command开头的随机顺序对它们进行简要介绍 `6: help` 。 选择命令6将进一步说明其他命令：

```
What now> 6
clean - start cleaning
filter by pattern - exclude items from deletion
select by numbers - select items to be deleted by numbers
ask each - confirm each deletion (like "rm -i")
quit - stop cleaning
help - this screen
? - help for prompt selection
```

```
5: quit
```

很简单，将退出交互式会话。

```
1: clean
```

将删除指示的项目。 如果我们要 `1: clean` 在这一点 执行 ， `untracked_dir/ untracked_file`  将被删除。

```
4: ask each
```

将遍历每个未跟踪的文件并显示 `Y/N`  删除提示。 看起来如下：

```
*** Commands ***
1: clean 2: filter by pattern 3: select by numbers 4: ask each 5: quit 6: help
What now> 4
Remove untracked_dir/ [y/N]? N
Remove untracked_file [y/N]? N
```

```
2: filter by pattern
```

将显示一个附加提示，该提示接受用于过滤未跟踪文件列表的输入。

```
Would remove the following items:
untracked_dir/ untracked_file
*** Commands ***
1: clean 2: filter by pattern 3: select by numbers 4: ask each 5: quit 6: help
What now> 2
untracked_dir/ untracked_file
Input ignore patterns>> *_file
untracked_dir/
```

在这里，我们输入 `*_file` 通配符模式，然后将未跟踪的文件列表限制为just `untracked_dir` 。

```
3: select by numbers
```

与命令2相似，命令3用于完善未跟踪文件名的列表。 交互式会话将提示输入与未跟踪的文件名相对应的数字。

```
Would remove the following items:
untracked_dir/ untracked_file
*** Commands ***
1: clean 2: filter by pattern 3: select by numbers 4: ask each 5: quit 6: help
What now> 3
1: untracked_dir/ 2: untracked_file
Select items to delete>> 2
1: untracked_dir/ * 2: untracked_file
Select items to delete>>
Would remove the following item:
untracked_file
*** Commands ***
1: clean 2: filter by pattern 3: select by numbers 4: ask each 5: quit 6: help
```

## 摘要

概括地说，这 `git clean` 是一种用于删除存储库工作目录中未跟踪文件的便捷方法。 未跟踪的文件是位于存储库目录中但尚未使用添加到存储库索引中的文件 `[git add](https://www.atlassian.com/git/tutorials/saving-changes)` 。 总体上， `git clean` 可以使用 `[git status](https://www.atlassian.com/git/tutorials/inspecting-a-repository)` 和操作系统本机删除工具 来实现 的效果 。 `Git clean` 可以与之一起使用， `[git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset)` 以完全撤消存储库中的任何添加和提交。