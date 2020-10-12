---
title: git tag
date: 2020-10-12 12:09:51
permalink: /pages/199266/
categories:
  - git入门
  - 检查存储库
tags:
  - 
---
# Git标签

[git status](https://www.atlassian.com/git/tutorials/inspecting-a-repository) [git标签](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-tag) [git怪](https://www.atlassian.com/git/tutorials/inspecting-a-repository/git-blame)

## 标记

本文档将讨论Git标记和 `git tag` 命令的 概念 。 标签是指向Git历史记录中特定点的引用。 标记通常用于捕获历史记录中用于标记版本发布（即v1.0.1）的点。 标签就像不变的分支。 与分支不同，标签在创建之后就没有进一步的提交历史了。 有关分支机构的更多信息，请访问 `git branch` 页面。 本文档将介绍不同类型的标签，如何创建标签，列出所有标签，删除标签，共享标签等。

## 创建标签

要创建新标签，请执行以下命令：

```
git tag <tagname>

```

`<tagname>` 在创建标签时，用语义标识符 替换存储库 状态。 一种常见的模式是使用版本号，例如 `git tag v1.4` 。 Git支持两种不同类型的标签，带注释的标签和轻量级标签。 前面的示例创建了一个轻量级标签。 轻量级标签和带注释的标签在它们存储的伴随元数据的数量上有所不同。 最佳做法是将带注释的标签视为公共标签，并将轻量级标签视为私人标签。 带注释的标签存储额外的元数据，例如：标记者名称，电子邮件和日期。 这是公开发布的重要数据。 轻量级标签本质上是提交的“书签”，它们只是提交的名称和指针，对于创建指向相关提交的快速链接很有用。

## 带注释的标签

带注释的标签作为完整对象存储在Git数据库中。 重申一下，它们存储额外的元数据，例如：标记者名称，电子邮件和日期。 与提交和提交消息相似，带注释的标记具有标记消息。 另外，为了安全起见，可以使用GNU Privacy Guard（GPG）对带注释的标签进行签名和验证。 建议的git标记最佳做法是优先使用带注释的标记，而不是轻量级的标记，以便您可以获取所有关联的元数据。

```
git tag -a v1.4

```

执行此命令将创建一个新的带注释的标记，用标识 `v1.4` 。 然后，该命令将打开配置的默认文本编辑器，以提示进一步的元数据输入。

```
git tag -a v1.4 -m "my version 1.4"

```

执行此命令与先前的调用类似，但是，此版本的命令会传递 `-m` 选项和一条消息。 这是一种类似于便利方法的方法，类似于 `git commit -m` 立即创建一个新标签并放弃打开本地文本编辑器，而是保存使用该 `-m` 选项 传递的消息的方法 。

## 轻量级标签

```
git tag v1.4-lw

```

执行此命令创建作为确定一个轻量级标签 `v1.4-lw.` 轻量级标签与缺少的创建 `-a` ， `-s` 或 `-m` 选项。 轻量级标签创建一个新的标签校验和，并将其存储在 `.git/` 项目 存储库的 目录中。

## 清单标签

要列出存储库中的标签，请执行以下操作：

```
git tag

```

这将输出标签列表：

```
v0.10.0
v0.10.0-rc1
v0.11.0
v0.11.0-rc1
v0.11.1
v0.11.2
v0.12.0
v0.12.0-rc1
v0.12.1
v0.12.2
v0.13.0
v0.13.0-rc1
v0.13.0-rc2

```

要优化标签列表， `-l` 可以使用通配符表达式传递选项：

```
$ git tag -l *-rc*
v0.10.0-rc1
v0.11.0-rc1
v0.12.0-rc1
v0.13.0-rc1
v0.13.0-rc2
v0.14.0-rc1
v0.9.0-rc1
v15.0.0-rc.1
v15.0.0-rc.2
v15.4.0-rc.3

```

前面的示例使用 `-l` 选项和通配符表达式， `-rc` 该 选项 返回所有标记有 `-rc` 前缀的 标签的列表，这些标签 通常用于标识 *发行候选* 。

## 标记旧提交

前面的标记示例已经演示了对隐式提交的操作。 默认情况下， `git tag` 将在 `HEAD` 引用 的提交上创建一个标签 。 或者， `git tag` 可以将其作为对特定提交的引用传递。 这将标记传递的提交，而不是默认为。 `HEAD.` 要收集较早提交的列表，请执行 `git log` 命令。

```
$ git log --pretty=oneline
15027957951b64cf874c3557a0f3547bd83b3ff6 Merge branch 'feature'
a6b4c97498bd301d84096da251c98a07c7723e65 add update method for thing
0d52aaab4479697da7686c15f77a3d64d9165190 one more thing
6d52a271eda8725415634dd79daabbc4d9b6008e Merge branch 'experiment'

```

执行 `git log` 将输出提交列表。 在此示例中，我们将为 `Merge branch 'feature'` 新标签 选择最高级的提交 。 我们将需要引用提交SHA哈希以传递给Git：

```
git tag -a v1.2 15027957951b64cf874c3557a0f3547bd83b3ff6

```

执行上面的 `git tag` 调用将创建一个新的带注释的提交 `v1.2` ，该提交与我们在前面的 `git log` 示例中 选择的提交相同 。

## 重新标记/替换旧标记

如果您尝试创建一个与现有标签具有相同标识符的标签，则Git将引发类似以下错误：

```
fatal: tag 'v0.4' already exists

```

另外，如果尝试使用现有标签标识符对较旧的提交进行标签，则Git会抛出相同的错误。

如果必须更新现有标签，则 `-f FORCE` 必须使用 该 选项。

```
git tag -a -f v1.4 15027957951b64cf874c3557a0f3547bd83b3ff6

```

执行上述命令会将 `15027957951b64cf874c3557a0f3547bd83b3ff6` 提交 映射 到 `v1.4` 标签标识符。 它将覆盖 `v1.4` 标签的 所有现有内容 。

## 共享：将标签推送到远程

共享标签类似于推送分支。 默认情况下， `git push` 不会推送标签。 标签必须明确传递给 `git push` 。

```
$ git push origin v1.4
Counting objects: 14, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (12/12), done.
Writing objects: 100% (14/14), 2.05 KiB | 0 bytes/s, done.
Total 14 (delta 3), reused 0 (delta 0)
To git@bitbucket.com:atlasbro/gittagdocs.git
* [new tag] v1.4 -> v1.4

```

要同时推送多个标签，请将 `--tags` 选项 传递 给 `git push` command。 当另一个用户克隆或提取仓库时，他们将收到新标签。

## 签出标签

您可以使用以下 `[git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)` 命令 在标记处查看回购的状态 。

```
git checkout v1.4

```

上面的命令将签出 `v1.4` 标签。 这使存储库处于分离 `HEAD` 状态。 这意味着所做的任何更改都不会更新标签。 他们将创建一个新的独立提交。 此新的分离的提交将不属于任何分支，并且只能由提交SHA哈希直接访问。 因此，最佳做法是在以分离 `HEAD` 状态 进行更改时随时创建一个新分支 。

## 删除标签

删除标签是一项简单的操作。 将 `-d` 选项和标签标识符 传递 给 `git tag` 将会删除所标识的标签。

```
$ git tag
v1
v2
v3
$ git tag -d v1
$ git tag
v2
v3

```

在此示例 `git tag` 中，执行以显示显示v1，v2，v3的标签列表，然后 `git tag -d v1` 执行删除v1标签的操作。

## 摘要

概括地说，标记是用于创建Git存储库快照的附加机制。 传统上，标记用于创建与软件发布周期相对应的语义版本号标识符标记。 该 `git tag` 命令是标记的主要驱动程序：创建，修改和删除。 标签有两种类型； 批注和轻巧。 带注释的标签通常是更好的做法，因为它们存储有关标签的其他有价值的元数据。 本文档中介绍的其他Git命令为 `[git push](https://www.atlassian.com/git/tutorials/syncing)` ，并 `[git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout).`  访问其相应的页面以讨论其扩展用途。