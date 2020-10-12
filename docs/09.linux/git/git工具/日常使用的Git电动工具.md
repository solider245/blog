---
title: 日常使用的Git电动工具
date: 2020-10-12 12:09:51
permalink: /pages/76c361/
categories:
  - git
  - git工具
tags:
  - 
---
每个开发人员每天都有自己喜欢的Git技巧。 只要记得，这就是我一直在使用的一些我最喜欢的。

首先，我要提到的是，大多数命令都捆绑在我的 [git\-toolbelt](https://github.com/nvie/git-toolbelt#readme) 项目中。 如果您想使用它们，只需要做的就是安装它，如下所示：

$ brew install nvie/tap/git\-toolbelt

## 快速打开修改过的文件 [¶](#quickly-opening-modified-files)

在分支上工作时，我经常发现需要重新打开正在处理的文件。 Git工具带项目包含一个命令，向您显示所有本地修改的文件。 它只会报告本地仍然存在的文件，因此此概述将不包括已删除的文件。

$ git modified
controllers/foo.py
README.md

这对于在编辑器中快速打开所有本地修改的文件非常有用。 绝对是我一整天最常用的命令之一：

$ vim $(git modified)

退出编辑器后，您可以轻松地重新打开正在处理的文件。

要还包括索引中修改的所有文件（ `git add` 已编辑的 文件 ），请使用 `-i` 标志：

$ git modified \-i

您还可以向其传递提交SHA，它将打开在该提交中修改的所有文件：

$ git modified HEAD~1

我 [在shell中设置了](https://github.com/nvie/dotfiles/blob/master/.config/fish/aliases.fish#L112-L138) 以下别名 ，用于快速打开一组特定的文件：

*   `vc` ：vim本地修改的文件（未编制索引）
*   `vca` ：vim *所有* 本地修改的文件（包括索引文件）
*   `vch` ：在上一次提交（HEAD）中修改的vim文件
*   `vc HEAD~1` ：vim在倒数第二次提交中修改的所有文件

## 修正最后的提交 [¶](#fixing-up-the-last-commit)

您可能很熟悉 `git commit --amend` 将当前阶段的更改合并到lastcommit中，从而有效地重写了最后一次commit。 该工具带提供了一个类似的命令，称为 `git fixup` ，它将执行相同的操作，但不会提示输入提交消息。 因此，这类似于的更快版本 `commit --amend` 。

$ git fixup

这是逐步建立提交的好方法。 对我来说非常典型的流程如下：

$ git add \-p    # Pick bits to commit
$ git commit
$ git add \-p    # Pick more bits
$ git fixup     # Add those to the last commit

## “清空”最后一次提交 [¶](#emptying-the-last-commit)

有时我犯了一个错误，我不小心犯了太多，或者是我不打算犯的东西。 例如，我不小心添加了一个额外的文件，或者一个我不想包含的文件中的补丁。 这是我的解决方法：

$ git delouse

这“清空”了最后一次提交。 将“清空”视为保留提交消息和作者/日期信息，但将其所有更改“移动”回工作树中。

技术上：

*   软重置最后的提交，这意味着它将从分支中删除最后的提交，并将该提交的内容放回工作树中（基本上在提交之前恢复到状态）。 文件内容不会因此改变，只有Git提交会消失。
*   使用与刚刚删除的提交相同的提交消息和作者详细信息添加一个空提交。

**这些操作的最终结果是，好像分支上的最后一次提交被“清空”回到您的工作树中。** 该命令是非破坏性的，因为所有文件都保持不变。 现在，它们又只是局部更改。

这样可以再次重新添加所有更改。 只需使用 `git add -p` 选择要提交的位，然后 `git fixup` （请参阅上一节）来保持更改最后的提交，即可有效地从头开始重建它。

因为 `git delouse` 将提交消息和作者信息保留在该空提交中，所以原始提交信息永远不会丢失，并且您不必在每次运行时都重新输入提交消息 `git fixup` ，这使整个过程变得非常便宜。

典型流量：

$ git commit \-m 'Add login screen'

# Oops! Checked in a secret key with that... let's fix this mistake!
$ git delouse

# Retry adding stuff
$ git add \-p   # This time, don't add the secret key
$ git fixup    # Rewrites the previous commit

如果您输入有误，则可以根据需要多次 `git delouse` 重新 运行 并重新开始。 由于这些命令都不会破坏您的本地更改，因此，您可以精心制作提交内容，而不会丢失任何数据。

## 将提交分成几部分 [¶](#splitting-up-a-commit-into-pieces)

这也是拆分提交的好方法！ 例如，假设您要添加错误修正，但您还重命名了变量以使其含义更清晰。 在提交代码进行检查时，您意识到变量重命名会给实际更改带来很多干扰。 然后，您可能会认为将提交分为两部分是一个好主意：一个原子地仅在各处更改变量名，另一个修复该错误。 然后，您可以在要求进行代码审查时指向错误修正提交。

那将如何工作？

$ git commit \-m 'Bugfix for login screen'

# Oops, I should've split this one up. Let's start over!
$ git delouse
$ git add \-p     # Just pick the bugfix bits
$ git fixup
$ git add \-p     # Now pick the var rename bits
$ git commit \-m 'Rename variable name to be clearer'

这三个命令在我的日常Git例程中变得必不可少。 如果您喜欢，请告诉我！

## 此博客上的其他帖子

*   [**解码器简介**](https://nvie.com/posts/introducing-decoders/)
*   [**技术债务是实际债务**](https://nvie.com/posts/why-you-should-consider-technical-debt-to-be-real-debt/)
*   [**漂亮的代码**](https://nvie.com/posts/beautiful-code/)
*   [**美丽的地图**](https://nvie.com/posts/beautiful-map/)
*   [**成功的Git分支模型**](https://nvie.com/posts/a-successful-git-branching-model/)