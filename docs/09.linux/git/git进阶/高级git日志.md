---
title: 高级git日志
date: 2020-10-12 12:09:51
permalink: /pages/d5f8f2/
categories:
  - git
  - git进阶
tags:
  - 
---
# 高级Git日志

[格式化日志输出](#formatting-log-output) [过滤提交历史记录](#filtering-the-commit-history) [摘要](#summary)

任何版本控制系统的目的都是记录对代码的更改。 这使您能够返回到项目历史记录中，查看谁贡献了什么，找出错误的出处以及还原有问题的更改。 但是，如果您不知道如何浏览所有历史记录，那将毫无用处。 那就是git log命令出现的地方。

到目前为止，您应该已经知道用于显示提交的基本git log命令。 但是，您可以通过将许多不同的参数传递给git log来更改此输出。

git log的高级功能可以分为两类：格式化每个提交的显示方式，以及过滤输出中包含哪些提交。 这两种技能一起使您能够重新进入项目并查找您可能需要的任何信息。

## 格式化日志输出

首先，本文将介绍 `git log` 可以格式化输出 的多种方式 。 其中大多数以标志的形式出现，使您可以从中请求更多或更少的信息 `git log` 。

如果您不喜欢默认 `git log` 格式，则可以使用 `git config` 的别名功能为下面讨论的任何格式设置选项创建快捷方式。 有关如何设置别名的信息， 请参见 [git config命令](https://www.atlassian.com/git/tutorials/setting-up-a-repository#git-config) 。

### 一条线

该 `--oneline` 标志将每个提交压缩到一行。 默认情况下，它仅显示提交ID和提交消息的第一行。 您的典型 `git log --oneline` 输出如下所示：

```
0e25143 Merge branch 'feature'
ad8621a Fix a bug in the feature
16b36c6 Add a new feature
23ad9ad Add the initial code base
```

这对于获得项目的高级概述非常有用。

### 装潢

很多时候了解每​​个提交与哪个分支或标签相关联很有用。 该 `--decorate` 标志 `git log` 显示指向每个提交的所有引用（例如，分支，标签等）。

可以将其与其他配置选项结合使用。 例如，运行 `git log --oneline --decorate` 将格式化提交历史记录，如下所示：

```
0e25143 (HEAD, master) Merge branch 'feature'
ad8621a (feature) Fix a bug in the feature
16b36c6 Add a new feature
23ad9ad (tag: v0.9) Add the initial code base
```

这样一来，您就知道最前面的提交也已签出（由表示 `HEAD` ），并且它也是 `master` 分支 的尖端 。 第二个提交有另一个指向它的分支，称为 `feature` ，最后第四个提交被标记为 `v0.9` 。

分支，标签， `HEAD` 和提交历史记录几乎是Git存储库中包含的所有信息，因此，您可以更全面地了解存储库的逻辑结构。

### 差异

该 `git log` 命令包括许多用于在每次提交时显示差异的选项。 最常见的两个选项是 `--stat` 和 `-p` 。

该 `--stat` 选项显示每个提交更改的每个文件的插入和删除次数（请注意，修改一行表示为1次插入和1次删除）。 当您希望简要概述每次提交所引入的更改时，此功能很有用。 例如，以下提交在 `hello.py` 文件中 添加了67行， 并删除了38行：

```
commit f2a238924e89ca1d4947662928218a06d39068c3
Author: John <john@example.com>
Date: Fri Jun 25 17:30:28 2014 -0500
Add a new feature
hello.py | 105 ++++++++++++++++++++++++-----------------
1 file changed, 67 insertion(+), 38 deletions(-)
```

文件名旁边 的 `+` 和 `-` 符号数量显示由提交更改的每个文件的相对更改数量。 这使您了解可以在何处找到每个提交的更改。

如果您想查看每次提交所引入的实际更改，可以将该 `-p` 选项 传递 给 `git log` 。 这将输出代表该提交的整个补丁：

```
commit 16b36c697eb2d24302f89aa22d9170dfe609855b
Author: Mary <mary@example.com>
Date: Fri Jun 25 17:31:57 2014 -0500
Fix a bug in the feature
diff --git a/hello.py b/hello.py
index 18ca709..c673b40 100644
--- a/hello.py
+++ b/hello.py
@@ -13,14 +13,14 @@ B
-print("Hello, World!")
+print("Hello, Git!")
```

对于具有大量更改的提交，结果输出可能变得很长且难以处理。 通常，如果要显示完整的补丁程序，则可能是在寻找特定的更改。 为此，您要使用镐选项。

### 简短日志

该 `git shortlog` 命令是 `git log` 用于创建发行公告 的特殊版本 。 它按作者对每个提交进行分组，并显示每个提交消息的第一行。 这是查看谁在做什么的一种简单方法。

例如，如果两个开发人员为一个项目贡献了5次提交，则 `git shortlog` 输出可能如下所示：

```
Mary (2):
Fix a bug in the feature
Fix a serious security hole in our framework
John (3):
Add the initial code base
Add a new feature
Merge branch 'feature'
```

默认情况下， `git shortlog` 按作者姓名对输出进行排序，但是您也可以传递该 `-n` 选项，以按每个作者的提交次数进行排序。

### 图表

该 `--graph` 选项绘制一个ASCII图，表示提交历史的分支结构。 这通常与 `--oneline` 和 `--decorate` 命令 结合使用 ， 以使查看哪个提交属于哪个分支变得更加容易：

```
git log --graph --oneline --decorate
```

对于只有两个分支的简单存储库，将产生以下内容：

```
* 0e25143 (HEAD, master) Merge branch 'feature'
|\
| * 16b36c6 Fix a bug in the new feature
| * 23ad9ad Start a new feature
* | ad8621a Fix a critical security issue
|/
* 400e4b7 Fix typos in the documentation
* 160e224 Add the initial code base
```

星号显示了提交所在的分支，因此上图告诉我们， `23ad9ad` 和 `16b36c6` 提交位于主题分支上，其余位于 `master` 分支上。

虽然这对于简单的存储库来说是一个不错的选择， [但是](https://www.atlassian.com/software/sourcetree/overview)  对于功能强大的分支项目，使用 功能更 [强大的](https://www.atlassian.com/software/sourcetree/overview) 可视化工具（例如 [Sourcetree）](https://www.atlassian.com/software/sourcetree/overview) `gitk` 或 [SourceTree](https://www.atlassian.com/software/sourcetree/overview) 可能会更好 。

### 自定义格式

对于所有其他 `git log` 格式需求，可以使用该 `--pretty=format:"<string>"` 选项。 这样，您就可以使用 `printf` \-style占位符 来显示每个提交 。

例如， `%cn` ， `%h` 并 `%cd` 在下面的命令字符被分别替换为提交者名称，简称提交散列，并且提交者日期，。

```
git log --pretty=format:"%cn committed %h on %cd"
```

每次提交的结果为以下格式：

```
John committed 400e4b7 on Fri Jun 24 12:30:04 2014 -0500
John committed 89ab2cf on Thu Jun 23 17:09:42 2014 -0500
Mary committed 180e223 on Wed Jun 22 17:21:19 2014 -0500
John committed f12ca28 on Wed Jun 22 13:50:31 2014 -0500
```

占位符的完整列表可以 在 手册页 的“ [漂亮格式”](https://www.kernel.org/pub/software/scm/git/docs/git-log.html#_pretty_formats) 部分中 `git log` 找到。

除了只让您查看您感兴趣的信息外， `--pretty=format:"<string>"` 在尝试将 `git log` 输出 通过管道传递 到另一个命令 时 ，该 选项特别有用 。

## 过滤提交历史

格式化每个提交的显示方式仅是学习的一半 `git log` 。 另一半是了解如何浏览提交历史记录。 本文的其余部分介绍了一些高级方法，可使用来选择项目历史记录中的特定提交 `git log` 。 所有这些都可以与上面讨论的任何格式设置选项结合使用。

### 按金额

最基本的过滤选项 `git log` 是限制显示的提交数量。 当您仅对最后几次提交感兴趣时，这可以省去查看页面中所有提交的麻烦。

您可以 `git log` 通过包含 `-<n>` 选项 来限制 的输出 。 例如，以下命令将仅显示3个最新提交。

```
git log -3
```

### 按日期

如果您要查找特定时间范围内的提交，则可以使用 `--after` 或 `--before` 标志按日期过滤提交。 它们都接受各种日期格式作为参数。 例如，以下命令仅显示 *在* 2014年7月1日（含）*之后* 创建的提交 ：

```
git log --after="2014-7-1"
```

您还可以传递相对引用，例如 `"1 week ago"` 和 `"yesterday"` ：

```
git log --after="yesterday"
```

要搜索在两个日期之间创建的提交，可以同时提供 `--before` 和 `--after` 日期。 例如，要显示2014年7月1日至2014年7月4日之间添加的所有提交，请使用以下命令：

```
git log --after="2014-7-1" --before="2014-7-4"
```

请注意， `--since` 和 `--until` 标志分别是 `--after` 和的 同义词 `--before` 。

### 按作者

当您仅查找由特定用户创建的提交时，请使用该 `--author` 标志。 这接受一个正则表达式，并返回其作者与该模式匹配的所有提交。 如果您确切地知道要寻找的人，则可以使用普通的旧字符串代替正则表达式：

```
git log --author="John"
```

这将显示所有提交者包括姓名 *John* 的提交 。 作者姓名不必 *完全* 匹配\-只需 *包含* 指定的短语即可。

您还可以使用正则表达式来创建更复杂的搜索。 例如，以下命令搜索 *Mary* 或 *John的* 提交 。

```
git log --author="John\|Mary"
```

请注意，作者的姓名中也包含作者的电子邮件，因此您也可以使用此选项通过电子邮件进行搜索。

如果您的工作流将提交者和作者分开，则该 `--committer` 标志的运行方式相同。

### 通过消息

要通过提交消息过滤提交，请使用 `--grep` 标志。 这就像 `--author` 上面讨论 的 标志 一样工作 ，但是它与提交消息而不是作者匹配。

例如，如果您的团队在每条提交消息中都包含相关的问题编号，则可以使用类似以下的内容来提取与该问题相关的所有提交：

```
git log --grep="JRA-224:"
```

您还可以传入 `-i` 参数以 `git log` 使其在模式匹配时忽略大小写差异。

### 按文件

很多时候，您只对特定文件发生的更改感兴趣。 要显示与文件相关的历史记录，您要做的就是传递文件路径。 例如，以下代码返回影响 `foo.py` 或 `bar.py` 文件的 所有提交 ：

```
git log -- foo.py bar.py
```

该 `--` 参数用于告知 `git log` 后续参数是文件路径，而不是分支名称。 如果没有机会将其与分支混淆，则可以忽略 `--` 。

### 按内容

也可以搜索引入或删除特定源代码行的提交。 这称为 *镐* ，其形式为 `-S"<string>"` 。 例如，如果您想知道字符串 *Hello，World！的时间。* 被添加到项目中的任何文件中，您将使用以下命令：

```
git log -S"Hello, World!"
```

如果要使用正则表达式而不是字符串进行搜索，则可以改用 `-G"<regex>"` 标志。

这是一个非常强大的调试工具，它使您可以找到影响特定代码行的所有提交。 它甚至可以显示行何时被复制或移动到另一个文件。

### 按范围

您可以传递一系列提交， `git log` 以仅显示该范围内包含的提交。 该范围以以下格式指定，其中 `<since>` 和 `<until>` 是提交引用：

```
git log <since>..<until>
```

当您使用分支引用作为参数时，此命令特别有用。 这是显示两个分支之间差异的简单方法。 考虑以下命令：

```
git log master..feature
```

该 `master..feature` 范围包含 `feature` 分支 中所有 但不在分支 中的提交 `master` 。 换句话说，这是 `feature` 自从分支以来的进展 `master` 。 您可以将其形象化如下：

![使用范围检测历史记录中的分叉](https://wac-cdn.atlassian.com/dam/jcr:b443a307-2df4-4080-948b-f5b9a1f8fd40/01.svg?cdnVersion=1084)

请注意，如果您切换范围（ `feature..master` ） 的顺序 ，则会在中获得所有提交 `master` ，而在中则不会 `feature` 。 如果 `git log` 两个版本的输出都提交，则表明您的历史记录有所不同。

### 筛选合并提交

默认情况下， `git log` 在其输出中包括合并提交。 但是，如果您的团队有一个始终合并的策略（也就是说，您将上游更改合并到主题分支中，而不是将主题分支重新定位到上游分支中），那么在项目历史记录中将有很多无关的合并提交。

您可以 `git log` 通过传递 `--no-merges` 标志 来阻止 显示这些合并提交 ：

```
git log --no-merges
```

另一方面，如果您 *仅对* 合并提交感兴趣，则可以使用 `--merges` 标志：

```
git log --merges
```

这将返回具有至少两个父级的所有提交。

## 摘要

现在，您应该可以轻松使用 `git log` 的高级参数来格式化其输出并选择要显示的提交。 这使您能够从项目历史记录中准确提取所需的内容。

这些新技能是Git工具包的重要组成部分，但请记住，这些技能 `git log` 通常与其他Git命令结合使用。 一旦你找到了提交你要找的，你通常将其传递给 `git checkout` ， `git revert` 或者操纵你的提交历史上的一些其他工具。 因此，一定要继续学习Git的高级功能。