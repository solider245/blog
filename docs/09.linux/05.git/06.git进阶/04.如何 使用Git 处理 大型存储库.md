---
title: 如何 使用Git 处理 大型存储库
date: 2020-10-12 12:09:51
permalink: /pages/36b2bf/
categories:
  - git
  - git进阶
tags:
  - 
---
![git分支的插图](https://wac-cdn.atlassian.com/dam/jcr:5562fce0-e73e-4c7d-9813-656aa1b36ca8/git-site-big-repository@2x.png?cdnVersion=1084)

# 如何
使用Git 处理 大型存储库

![尼古拉（Nicola Paolucci）](https://wac-cdn.atlassian.com/dam/jcr:1a355490-1c55-42a2-aa4a-30b260d0163e/nicola-paolucci.png?cdnVersion=1084)

###### 尼古拉（Nicola Paolucci）

[返回目录](https://www.atlassian.com/git/articles)

Git是跟踪您的代码库的演变并与您的同伴有效协作的绝佳选择。 但是，当您要跟踪的存储库 **非常** 大 时会发生什么 ？

在这篇文章中，我将为您提供一些处理它的技术。

## 两类大型存储库

如果您考虑一下，则存储库大量增长的主要原因有两个：

*   他们积累了非常长的历史（该项目在很长一段时间内不断发展，行李也不断积累）
*   它们包括巨大的二进制资产，需要与代码一起跟踪和配对。

…或者可能两者都有。

有时，第二种问题由于旧的，已弃用的二进制工件仍存储在存储库中而变得更加复杂。 但是，有一个相对容易的解决方法（即使很烦人）也可以解决此问题（请参阅下文）。

每个方案的技术和变通办法是不同的，尽管有时是互补的。 因此，我将分别介绍它们。

## 克隆历史悠久的存储库

即使将存储库定为“大规模”的门槛很高，但克隆仍然很麻烦。 而且您不能总是避免悠久的历史。 出于法律或法规原因，某些存储库必须保持原样。

### 简单的解决方案：git浅克隆

快速克隆并节省开发人员和系统时间以及磁盘空间的第一个解决方案是仅复制最新修订版。 Git的浅克隆选项允许您仅下拉回购历史记录的最新n次提交。

你怎么做呢？ 只需使用–depth选项。 例如：

`git clone --depth [depth] [remote-url] `

想象一下，您在存储库中积累了十多年的项目历史。 例如，我们将 [Jira](https://www.atlassian.com/software/jira) （ [已有](https://www.atlassian.com/software/jira) 11年历史的代码库） 迁移 到Git。 这样节省的时间可以累加起来，而且非常明显。

Jira的完整副本为677MB，工作目录为另一个320MB，由47,000多个提交组成。 仓库的浅克隆需要29.5秒，而具有所有历史记录的完整克隆则需要4分24秒。 随着时间的流逝，收益与项目中吞并了多少二进制资产成正比。

*提示：*  [连接到您的Git存储库的构建系统也](https://www.atlassian.com/continuous-delivery/continuous-integration/ci-friendly-git-repos) 将从浅层克隆中受益！

浅层克隆曾经在一定程度上削弱了Git世界的公民，因为几乎没有支持某些行动。 但是最新版本（ [1.9](https://www.atlassian.com/blog/archives/whats-new-git-1-9?_ga=2.85910233.1564368919.1571097409-1339596144.1562091064)  及更高 版本 ）已大大改善了这种情况，即使现在是浅表克隆，也可以正确地将其推入存储库。

### 手术方案：git filter分支

对于庞大的存储库，其中有很多二进制错误被错误提交，或者不再需要旧资产，一个很好的解决方案是使用 *git filter\-branch* 。 该命令使您可以遍历项目的整个历史记录，根据预定义的模式过滤，修改和跳过文件。

一旦确定了回购的重担，它就是一个非常强大的工具。 有可用于识别大对象的帮助程序脚本，因此该部分应该足够容易。
语法如下：

`git filter-branch --tree-filter 'rm -rf [/path/to/spurious/asset/folder]'`

*但是git filter\-branch*  有一个小缺点：一旦使用\_filter\-branch\_，就可以有效地重写项目的整个历史记录。 也就是说，所有提交ID都会更改。 这要求每个开发人员重新克隆更新的存储库。

因此，如果您打算使用 *git filter\-branch* 进行清理操作 ，则应提醒您的团队，在执行该操作时计划短暂的冻结，然后通知所有人他们应该再次克隆存储库。

*提示：* [这篇文章中有关](https://www.atlassian.com/blog/git/tear-apart-repository-git-way?_ga=2.116821446.1564368919.1571097409-1339596144.1562091064) git filter\-branch的更多 [信息，涉及将Git存储库拆解。](https://www.atlassian.com/blog/git/tear-apart-repository-git-way?_ga=2.116821446.1564368919.1571097409-1339596144.1562091064)

### git浅层克隆的替代方法：仅克隆一个分支

从git 1.7.10开始，您还可以通过克隆单个分支来限制克隆的历史记录数量，如下所示：

`git clone [remote url] --branch [branch_name] --single-branch [folder]`

当您使用长期运行且分散的分支，或者您有很多分支并且只需要使用其中几个分支时，此特定的技巧非常有用。 如果您只有几个分支，差异很小，那么使用此分支可能不会有太大差异。

## 管理具有巨大二进制资产的存储库

大存储库的第二种类型是具有巨大二进制资产的存储库。 这是 [许多不同类型的软件（和非软件！）团队所遇到的。](https://www.atlassian.com/blog/git/git-lfs-for-designers-game-developers-architects?_ga=2.42796773.1564368919.1571097409-1339596144.1562091064) 游戏团队必须四处寻找巨大的3D模型，Web开发团队可能需要跟踪原始图像资产，CAD团队可能需要操纵和跟踪二进制可交付成果的状态。

Git在处理二进制资产方面并不是特别糟糕，但是也不是特别好。 默认情况下，Git将压缩并存储二进制资产的所有后续完整版本，如果您拥有很多版本，这显然不是最佳选择。

有一些基本的调整可以改善这种情况，例如运行垃圾回收 *（'git gc'）* 或调整.gitattributes中某些二进制类型的增量提交的使用。

但是，重要的是要反思项目的二进制资产的性质，因为这将帮助您确定获胜的方法。 例如，以下是要考虑的几点：

*   对于变化很大的二进制文件（而不仅仅是一些元数据标题），增量压缩可能将无用。 因此， 对那些文件 使用 *“ delta off” * ，以避免在重新打包过程中不必要的delta压缩工作。
*   在上述情况下，这些文件很可能无法zlib很好地压缩，因此您可以使用 *'core.compression 0' * 或' *core.loosecompression 0'* 关闭压缩 。 这是一个全局设置，会对实际压缩良好的所有非二进制文件产生负面影响，因此，如果将二进制资产拆分到一个单独的存储库中，这是有道理的。
*   重要的是要记住， *'git gc' * 将“复制的”松散对象转换为单个pack文件。 但是同样，除非文件以某种方式压缩，否则在生成的打包文件中可能不会有任何显着差异。
*   探索 *“ core.bigFileThreshold”* 的调优 。 任何大于512MB的内容都不会进行增量压缩（无需设置.gitattributes），因此也许值得调整。

### 大文件夹树的解决方案：git sparse\-checkout

Git的稀疏签出选项（自Git 1.7.0起可用）对二进制资产问题有轻微的帮助。 通过显式详细说明要填充的文件夹，此技术可以使工作目录保持干净。 不幸的是，它不会影响整个本地存储库的大小，但是如果您有大量的文件夹树，则可能会有所帮助。

涉及的命令是什么？ 这是一个例子：

*   克隆完整的存储库一次： *'git clone'*
*   激活功能： *“ git config core.sparsecheckout true”*
*   添加显式需要的文件夹，而忽略资产文件夹：
    *   echo src /› .git / info / sparse\-checkout
*   读取指定的树：
    *   *git read\-tree \-m \-u头*

完成上述操作后，您可以返回使用常规的git命令，但是您的工作目录将仅包含您在上面指定的文件夹。

### 控制何时更新大文件的解决方案：子模块

处理巨大的二进制资产文件夹的另一种方法是将它们拆分为单独的存储库，并使用Gi​​t子模块将其提取到主项目中。 这使您可以控制何时更新资产。 这些帖子中有更多关于子模块的信息： [Git子模块的核心概念和技巧](https://www.atlassian.com/blog/git/git-submodules-core-concept-workflows-and-tips?_ga=2.41412194.1564368919.1571097409-1339596144.1562091064) ，以及 [Git子模块的替代品](https://www.atlassian.com/git/tutorials/git-subtree) 。

## \[更新\]…或者您可以跳过所有内容并使用Gi​​t LFS

如果您定期处理大文件，最好的解决方案可能是利用2015年与GitHub共同开发的Atlassian大文件支持（LFS）。（是的，您没看错。我们与GitHub合作，对Git项目的开源贡献。）

Git LFS是一种扩展，它可以自然地将指向大型文件的指针存储在存储库中，而不是将文件本身存储在其中。 实际文件存储在远程服务器上。 可以想象，这大大减少了克隆仓库的时间。

![](https://wac-cdn.atlassian.com/dam/jcr:72213c27-9025-432e-94db-b1df0fd150c3/GitLFSDiagram-1.png?cdnVersion=1084)

[Bitbucket](https://www.atlassian.com/blog/git/git-lfs-for-designers-game-developers-architects?_ga=2.39759587.1564368919.1571097409-1339596144.1562091064) 和GitHub一样都 [支持Git LFS](https://www.atlassian.com/blog/git/git-lfs-for-designers-game-developers-architects?_ga=2.39759587.1564368919.1571097409-1339596144.1562091064) 。 因此，您已经可以使用这项技术。 对于包括设计师，摄像师，音乐家或CAD用户的团队来说，这特别有用。

### 结论

不要仅仅因为您拥有大量的存储库历史或巨大的文件而放弃Git的强大功能。 对于这两个问题都有可行的解决方案。

查看我上面链接的其他文章，以获取有关子模块，项目依赖项和Git LFS的更多信息。 对于命令和工作流程的复习，我们的 [Git微型站点上](https://www.atlassian.com/git)  有大量的教程。 编码愉快！