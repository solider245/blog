---
title: git subtree子树
date: 2020-10-12 12:09:51
permalink: /pages/dbbde8/
categories:
  - git
  - git进阶
tags:
  - 
---
# Git子树：Git子模块的替代品

![尼古拉（Nicola Paolucci）](https://wac-cdn.atlassian.com/dam/jcr:1a355490-1c55-42a2-aa4a-30b260d0163e/nicola-paolucci.png?cdnVersion=1084)

###### 尼古拉（Nicola Paolucci）

[返回目录](https://www.atlassian.com/git/articles)

互联网上充斥着有关为什么不应该使用Git子模块的文章。 虽然子模块在一些用例中很有用，但它们确实有一些缺点。

有其他选择吗？ 答案是：是的！ 至少有两个工具可以帮助跟踪项目中软件依赖关系的历史，同时允许您继续使用Git：

*   `git subtree`
*   Google回购

在这篇文章中，我们将研究 `git subtree ` 并展示为什么它比git子模块有改进（尽管并不完美）。

## 什么是 `git subtree` ，为什么要使用它？

`git subtree` 使您可以将一个存储库作为子目录嵌套在另一个存储库中。 这是Git项目可以管理项目依赖项的几种方法之一。

![该图显示了使用Git子树之前和之后两个存储库之间的交互。](https://wac-cdn.atlassian.com/dam/jcr:f5fcef58-5b93-4ff4-b9a1-3f721d29ead8/BeforeAfterGitSubtreeDiagram.png?cdnVersion=1084)

为什么您可能要考虑 `git subtree`

*   简单工作流程的管理很容易。
*   支持较旧的Git版本（甚至是v1.5.2之前的版本）。
*   超级项目的克隆完成后，就可以使用子项目的代码。
*   `git subtree` 不需要您存储库的用户学习任何新知识。 他们可以忽略您 `git subtree` 用来管理依赖项 的事实 。
*   `git subtree` 不会像git子模块一样添加新的元数据文件（即.gitmodule）。
*   可以修改模块的内容，而无需在其他地方具有依赖项的单独存储库副本。

缺点（但我们认为它们是可以接受的）：

*   您必须了解一种新的合并策略（例如 `git subtree` ）。
*   向子项目的上游贡献代码稍微复杂一些。
*   在提交中不混合上层项目代码和下层项目代码的责任在于您。

## 如何使用 `git subtree`

`git subtree`  自2012年5月起提供v1.7.11及更高版本的Git股票版本。 Homebrew在OSX上安装的版本已经正确连接了子树，但是在某些平台上，您可能需要按照安装说明进行操作。

这是使用以下方法跟踪vim插件的典型示例 `git subtree.`

### 快速而肮脏的方式，无需远程跟踪

如果您只想剪切和粘贴一对直线，请阅读本段。 首先 `git subtree`  在指定的前缀文件夹中 添加 ：

```
git subtree add --prefix .vim/bundle/tpope-vim-surround https://bitbucket.org/vim-plugins-mirror/vim-surround.git master --squash
```

（通常的做法是不将子项目的整个历史记录存储在主存储库中，但是如果要保留它，则可以忽略 *–squash*  标志。）

上面的命令产生以下输出：

```
git fetch https://bitbucket.org/vim-plugins-mirror/vim-surround.git master
warning: no common commits
remote: Counting objects: 338, done.
remote: Compressing objects: 100% (145/145), done.
remote: Total 338 (delta 101), reused 323 (delta 89)
Receiving objects: 100% (338/338), 71.46 KiB, done.
Resolving deltas: 100% (101/101), done.
From https://bitbucket.org/vim-plugins-mirror/vim-surround.git
* branch master -} FETCH_HEAD
Added dir '.vim/bundle/tpope-vim-surround'
```

如您所见，这通过将vim\-surround存储库的整个历史压缩为一个来记录合并提交：

```
1bda0bd [3 minutes ago] (HEAD, stree) Merge commit 'ca1f4da9f0b93346bba9a430c889a95f75dc0a83' as '.vim/bundle/tpope-vim-surround' [Nicola Paolucci]
ca1f4da [3 minutes ago] Squashed '.vim/bundle/tpope-vim-surround/' content from commit 02199ea [Nicola Paolucci]
```

如果过了一会儿您想从上游存储库更新插件的代码，则可以执行一次 `git subtree` pull：

```
git subtree pull --prefix .vim/bundle/tpope-vim-surround https://bitbucket.org/vim-plugins-mirror/vim-surround.git master --squash
```

这是非常快捷和轻松的，但是命令有些冗长并且难以记住。 通过将子项目添加为远程项目，我们可以使命令更短。

### 将子项目添加为远程项目

将子树添加为远程树可以使我们以较短的形式引用它：

```
git remote add -f tpope-vim-surround https://bitbucket.org/vim-plugins-mirror/vim-surround.git
```

现在我们可以像以前一样添加子树，但是现在我们可以简称为远程：

```
git subtree add --prefix .vim/bundle/tpope-vim-surround tpope-vim-surround master --squash
```

以后更新子项目的命令变为：

```
git fetch tpope-vim-surround master
git subtree pull --prefix .vim/bundle/tpope-vim-surround tpope-vim-surround master --squash
```

### 向上游贡献

现在，我们可以将修补程序自由提交给本地工作目录中的子项目。 当需要回馈上游项目时，我们需要分叉该项目并将其添加为另一个远程服务器：

```
git remote add durdn-vim-surround ssh://git@bitbucket.org/durdn/vim-surround.git
```

现在我们可以  像下面这样 使用 *subtree push* 命令：

```
git subtree push --prefix=.vim/bundle/tpope-vim-surround/ durdn-vim-surround master
git push using: durdn-vim-surround master
Counting objects: 5, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 308 bytes, done.
Total 3 (delta 2), reused 0 (delta 0)
To ssh://git@bitbucket.org/durdn/vim-surround.git
02199ea..dcacd4b dcacd4b21fe51c9b5824370b3b224c440b3470cb -} master
```

在此之后，我们就可以准备好了，我们可以向包装的维护者提出拉取请求。

### 我可以不使用 `git subtree` 命令 来执行此操作 吗？

是! 是的你可以。 `git subtree` 与子树合并策略不同。 即使由于某些原因 `git subtree`  不可用， 您仍然可以使用合并策略 。 这是您的处理方式。

添加依赖项很简单 `git remote` ：

```
git remote add -f tpope-vim-surround https://bitbucket.org/vim-plugins-mirror/vim-surround.git
```

在将依赖项的内容读入存储库之前，重要的是记录下一个合并，以便我们可以跟踪到现在为止插件的整个树历史：

```
git merge -s ours --no-commit tpope-vim-surround/master
```

哪个输出：

```
Automatic merge went well; stopped before committing as requested
```

然后，我们将最新树对象的内容读入插件存储库中，并准备提交：

```
git read-tree --prefix=.vim/bundle/tpope-vim-surround/ -u tpope-vim-surround/master
```

现在我们可以提交（这将是一个合并提交，它将保留我们读取的树的历史记录）：

```
git ci -m"[subtree] adding tpope-vim-surround"
[stree 779b094] [subtree] adding tpope-vim-surround
```

现在，当我们要更新项目时，可以使用 `git subtree`  合并策略进行 拉取 ：

```
git pull -s subtree tpope-vim-surround master
```

## `Git subtree` 是一个很好的选择

使用git子模块一段时间后，您将看到 `git subtree`  解决了git子模块的许多问题。 像往常一样，在Git的所有方面，都有一条学习曲线可以充分利用该功能。

在Twitter [@durdn](https://www.twitter.com/durdn) 上关注我，  了解有关Git的更多信息。  如果您正在寻找管理Git仓库的好工具， 请查看 [Atlassian Bitbucket](https://www.bitbucket.org/?_ga=2.71978451.1385799339.1568044055-1068396449.1567112770) 。

更新：发布本文之后，我还写了 [一篇有关的力量的文章 `Git subtree`](https://developer.atlassian.com/blog/2015/05/the-power-of-git-subtree?_ga=2.71978451.1385799339.1568044055-1068396449.1567112770)*。*