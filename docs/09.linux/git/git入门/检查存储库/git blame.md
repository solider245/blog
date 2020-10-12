---
title: git blame
date: 2020-10-12 12:09:51
permalink: /pages/2993fd/
categories:
  - git入门
  - 检查存储库
tags:
  - 
---
# 吉特怪

[git status](https://www.atlassian.com/git/tutorials/inspecting-a-repository) [git标签](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-tag) [git怪](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-blame)

该 `git blame` 命令是一种通用的故障排除实用程序，具有广泛的使用选项。 的高级功能 `git blame` 是显示附加到文件中特定提交行的作者元数据。 这用于检查文件历史记录的特定点，并获取有关谁是最后一位修改该行的作者的上下文。 这用于探究特定代码的历史，并回答有关将代码添加到存储库的内容，方式和原因的问题。

`Git blame` 通常与GUI显示器一起使用。 像 [Bitbucket](http://bitbucket.org/) 这样的在线Git托管网站 提供了 *怪异的视图* ，这些都是UI的包装 `git blame` 。 这些视图在关于拉取请求和提交的协作讨论中被引用。 此外，大多数具有Git集成的IDE也具有动态的责备视图。

## 这个怎么运作

为了演示， `git blame` 我们需要一个具有一定历史记录的存储库。 我们将使用开源项目 [git\-blame\-example](https://bitbucket.org/kevzettler/git-blame-example) 。 这个开源项目是一个简单的存储库，其中包含README.md文件，该文件包含来自不同作者的一些提交。 我们的 `git blame` 用法示例的 第一步 是进入 `git clone` 示例存储库。

```
git clone https://kevzettler@bitbucket.org/kevzettler/git-blame-example.git && cd git-blame-example

```

现在我们有了示例代码的副本，我们可以开始使用 `git blame` 。 可以使用来检查示例存储库的状态 `[git log](https://www.atlassian.com/git/tutorials/git-log)` 。 提交历史记录应如下所示：

```
$ git log
commit 548dabed82e4e5f3734c219d5a742b1c259926b2
Author: Juni Mukherjee <jmukherjee@atlassian.com>
Date: Thu Mar 1 19:55:15 2018 +0000
Another commit to help git blame track the who, the what, and the when
commit eb06faedb1fdd159d62e4438fc8dbe9c9fe0728b
Author: Juni Mukherjee <jmukherjee@atlassian.com>
Date: Thu Mar 1 19:53:23 2018 +0000
Creating the third commit, along with Kev and Albert, so that Kev can get git blame docs.
commit 990c2b6a84464fee153253dbf02e845a4db372bb
Merge: 82496ea 89feb84
Author: Albert So <aso@atlassian.com>
Date: Thu Mar 1 05:33:01 2018 +0000
Merged in albert-so/git-blame-example/albert-so/readmemd-edited-online-with-bitbucket-1519865641474 (pull request #2)
README.md edited online with Bitbucket
commit 89feb84d885fe33d1182f2112885c2a64a4206ec
Author: Albert So <aso@atlassian.com>
Date: Thu Mar 1 00:54:03 2018 +0000
README.md edited online with Bitbucket
```

`git blame` 仅对单个文件起作用。 任何有用的输出都需要文件路径。 默认执行 `git blame` 将仅输出命令帮助菜单。 对于此示例，我们将对README.MD文件进行操作。 在git信息库的根目录中包含README文件作为项目的文档源是一种常见的开源软件实践。

```
git blame README.MD

```

执行以上命令将为我们提供第一个非常规输出示例。 以下输出是README的全部指责输出的子集。 此外，此输出是静态的，反映了在撰写本文时回购的状态。

```
$ git blame README.md
82496ea3 (kevzettler 2018-02-28 13:37:02 -0800 1) # Git Blame example
82496ea3 (kevzettler 2018-02-28 13:37:02 -0800 2)
89feb84d (Albert So 2018-03-01 00:54:03 +0000 3) This repository is an example of a project with multiple contributors making commits.
82496ea3 (kevzettler 2018-02-28 13:37:02 -0800 4)
82496ea3 (kevzettler 2018-02-28 13:37:02 -0800 5) The repo use used elsewhere to demonstrate `git blame`
82496ea3 (kevzettler 2018-02-28 13:37:02 -0800 6)
89feb84d (Albert So 2018-03-01 00:54:03 +0000 7) Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod TEMPOR incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum
89feb84d (Albert So 2018-03-01 00:54:03 +0000 8)
eb06faed (Juni Mukherjee 2018-03-01 19:53:23 +0000 9) Annotates each line in the given file with information from the revision which last modified the line. Optionally, start annotating from the given revision.
eb06faed (Juni Mukherjee 2018-03-01 19:53:23 +0000 10)
548dabed (Juni Mukherjee 2018-03-01 19:55:15 +0000 11) Creating a line to support documentation needs for git blame.
548dabed (Juni Mukherjee 2018-03-01 19:55:15 +0000 12)
548dabed (Juni Mukherjee 2018-03-01 19:55:15 +0000 13) Also, it is important to have a few of these commits to clearly reflect the who, the what and the when. This will help Kev get good screenshots when he runs the git blame on this README.

```

这是README.md文件的前13行的示例。 为了更好地理解此输出，请分解一行。 下表显示了第3行的内容，该表的各列指示该列的内容。

| ID | 作者 | 时间戳记 | 电话号码 | 行内容 |
| 89feb84d | 苏伟业 | 2018\-03\-01 00:54:03 +0000 | 3 | 该存储库是具有多个贡献者进行提交的项目的示例。 |

如果我们查看非常规输出列表，则可以得出一些结论。 列出了三位作者。 除了项目的维护者Kev Zettler之外，Albert So和Juni Mukherjee也被列出。 作者通常是 `git blame` 产出中 最有价值的部分 。 时间戳列也主要有帮助。 更改内容由行内容列指示。

## 常用选项

```
git blame -L 1,5 README.md

```

该 `-L` 选项会将输出限制在请求的行范围内。 在这里，我们将输出限制为第1至5行。

```
git blame -e README.md

```

该 `-e` 选项显示作者的电子邮件地址，而不是用户名。

```
git blame -w README.md

```

该 `-w` 选项将忽略空格更改。 如果以前的作者通过从制表符切换到空格或添加新行来修改了文件的间距，那么不幸的是，这将 `git blame` 通过显示这些更改来 掩盖输出 。

```
git blame -M README.md

```

该 `-M` 选项检测同一文件中的已移动或复制的行。 这将报告这些行的原始作者，而不是最后一个移动或复制这些行的作者。

```
git blame -C README.md

```

该 `-C` 选项检测从其他文件移动或复制的行。 这将报告这些行的原始作者，而不是最后一个移动或复制这些行的作者。

## Git Blame vs Git Log

当 `git blame` 显示最后修改行的作者时，通常您会想知道最初添加行的时间。 使用可能会很麻烦 `git blame` 。 它需要的组合 `-w` ， `-C` 和 `-M` 选项。 使用该 `[git log](https://www.atlassian.com/git/tutorials/git-log) ` 命令 可以更加方便 。

要列出所有原始提交（添加或修改了特定代码段），请 `git log` 使用该 `-S` 选项 执行 。 在 `-S` 选项中 添加所需 的代码。 让我们以上面的README输出中的其中一行作为示例。 让我们从README输出的第12行获取文本“ CSS3D和WebGL渲染器”。

```
$ git log -S"CSS3D and WebGL renderers." --pretty=format:'%h %an %ad %s'
e339d3c85 Mario Schuettel Tue Oct 13 16:51:06 2015 +0200 reverted README.md to original content
509c2cc35 Daniel Tue Sep 8 13:56:14 2015 +0200 Updated README
cb20237cc Mr.doob Mon Dec 31 00:22:36 2012 +0100 Removed DOMRenderer. Now with the CSS3DRenderer it has become irrelevant.

```

此输出向我们展示了自述文件的内容是由3位不同的作者添加或修改的3次。 它最初是由doob先生在commit cb20237cc中添加的。 在此示例中， `git log` 该 `--pretty-format` 选项 也已添加 。 此选项将默认的输出格式转换为 `git log` 与的格式匹配的格式 `git log` 。 有关使用和配置选项的更多信息，请访问 `[git log](https://www.atlassian.com/git/tutorials/git-log)` 页面。

## 摘要

该 `git blame` 命令用于逐行检查文件的内容，并查看每行的最后修改时间以及修改的作者。 的输出格式 `git blame` 可以通过各种命令行选项进行更改。 诸如Bitbucket之类的在线Git托管解决方案提供了非常 *规视图* ，从而为命令行 `git blame` 使用 提供了卓越的用户体验 。 `git blame` 和git log可以组合使用，以帮助发现文件内容的历史记录。 该 `git log` 命令具有一些类似的功能，要了解更多信息，请访问 `[git log](https://www.atlassian.com/git/tutorials/git-log)`  概述页面。