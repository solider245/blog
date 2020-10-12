---
title: git clone
date: 2020-10-12 12:09:51
permalink: /pages/4af61c/
categories:
  - git
  - git入门
tags:
  - 
---
# git克隆

在这里，我们将 `git clone` 深入 研究该 命令。 `git clone` 是Git命令行实用程序，用于定位现有存储库并创建目标存储库的副本或副本。 在此页面中，我们将讨论的扩展配置选项和常见用例 `git clone` 。 我们将在此处介绍以下几点：

*   克隆本地或远程存储库
*   克隆裸仓库
*   使用浅层选项部分克隆存储库
*   Git URL语法和支持的协议

关于 [建立存储库指南](https://www.atlassian.com/git/tutorials/setting-up-a-repository) ，我们讨论了一个基本的用例 `git clone` 。 该页面将探讨更复杂的克隆和配置方案。

## 目的：回购协作开发副本

如果已经在中央存储库中设置了项目，则该 `git clone` 命令是用户获取开发副本的最常用方法。 像一样 `git init` ，克隆通常是一次性操作。 开发人员获得工作副本后，所有版本控制操作和协作都将通过其本地存储库进行管理。

### 回购协作

重要的是要理解，Git的“工作副本”与通过从SVN存储库中签出代码而获得的工作副本有很大不同。 与SVN不同，Git在工作副本和中央存储库之间没有区别，它们都是成熟的 [Git存储库](http://bitbucket.org/code-repository) 。

这使得与Git的协作与SVN的协作从根本上不同。 SVN取决于中央存储库和工作副本之间的关系，而Git的协作模型则基于存储库到存储库的交互。 您无需将工作副本检入SVN的中央存储库中，而是 [将](https://www.atlassian.com/git/tutorials/syncing/git-push) 提交从一个存储库 [推入](https://www.atlassian.com/git/tutorials/syncing/git-push) 或 [拉](https://www.atlassian.com/git/tutorials/syncing/git-pull) 入另一个存储库。

![Git教程：回购到工作副本协作](https://wac-cdn.atlassian.com/dam/jcr:e5228129-76b1-4b2c-8f10-af789f2ea6c0/03.svg?cdnVersion=1084) ![Git教程：从仓库到仓库的协作](https://wac-cdn.atlassian.com/dam/jcr:5d68ce55-59a7-4840-a896-eb2014a9f17b/02.svg?cdnVersion=1084)

当然，没有什么可以阻止您赋予某些Git仓库特殊的意义。 例如，只需将一个Git存储库指定为“中央”存储库，就可以 使用Git 复制 [集中式工作流程](https://www.atlassian.com/git/tutorials/comparing-workflows) 。 关键是，这是通过约定完成的，而不是硬连接到VCS本身。

## 用法

`git clone` 主要用于指向现有存储库，并在另一个位置的新目录中创建该存储库的克隆或副本。 原始存储库可以位于本地文件系统上，也可以位于远程计算机可访问的受支持协议上。 该 `git clone` 命令将复制现有的Git存储库。 这类似于SVN签出，除了“工作副本”是功能完善的Git存储库\-它具有自己的历史记录，管理自己的文件，并且是与原始存储库完全隔离的环境。

为了方便起见，克隆会自动创建一个称为“源”的远程连接，该连接指向原始存储库。 这使得与中央存储库进行交互非常容易。 通过在 `refs/remotes/origin` 初始化 分支 `remote.origin.url` 和 `remote.origin.fetch` 配置变量 下创建到远程分支头的Git引用来建立这种自动连接 。

`git clone` 可以在 [建立存储库指南中](https://www.atlassian.com/git/tutorials/setting-up-a-repository) 找到 一个演示使用的示例 。 下面的示例演示了如何获取中央存储库的本地副本，该存储库存储在 `example.com` 使用SSH用户名john 可以访问的服务器上 ：

```
git clone ssh://john@example.com/path/to/my-project.git
cd my-project
# Start working on the project
```

第一条命令 `my-project` 在本地计算机上 的 文件夹中 初始化一个新的Git存储库， 并使用中央存储库的内容填充它。 然后，您可以进入项目并开始编辑文件，提交快照以及与其他存储库进行交互。 另请注意， `.git` 克隆存储库中省略 了该 扩展名。 这反映了本地副本的非裸状态。

### 克隆到特定文件夹

```
git clone <repo> <directory>
```

将位于的存储库克隆 `<repo>` 到 `~<directory>!` 本地计算机上 调用的文件夹中 。

### 克隆特定标签

```
git clone --branch <tag> <repo>
```

克隆位于的存储库 `<repo>` ，仅克隆的引用 `<tag>` 。

### 浅克隆

```
git clone -depth=1 <repo>
```

克隆位于的存储库 `<repo>` ，仅克隆
选项depth = 1指定的提交历史。 在此示例中，创建了一个克隆， `<repo>` 并且新克隆的回购中仅包含最新提交。 当使用具有广泛提交历史的存储库时，浅克隆最有用。 广泛的提交历史记录可能会导致扩展问题，例如磁盘空间使用限制和克隆时的漫长等待时间。 浅克隆可以帮助缓解这些扩展问题。

## 配置选项

### git clone\-分支

该 `-branch` 参数使您可以指定要克隆的特定分支，而不是远程 `HEAD` 指向 的分支 ，通常是master分支。 另外，您可以传递标签而不是分支以达到相同的效果。

```
git clone -branch new_feature git://remoterepository.git
```

上面的示例仅从 `new_feature` 远程Git存储库中 克隆 分支。 这纯粹是一个令人信服的实用程序，可以节省您下载 `HEAD` 存储库引用的 时间， 而不必另外获取所需的引用。

### git clone \-mirror与git clone \-bare

#### git clone\-裸

类似于 `git init --bare,` 将 `-bare` 参数传递到 `git clone,` 远程存储库副本时，将使用省略的工作目录。 这意味着将使用项目的历史记录来建立一个存储库，该历史记录可以从中推送和拉出，但不能直接进行编辑。 此外，不会使用 `-bare` 存储库 配置 仓库的 远程分支 。 像 `git init --bare,` 这样用于创建托管存储库，开发人员将不会直接对其进行编辑。

#### git clone \-\-mirror

传递 `--mirror` 参数也隐式传递 `--bare` 参数。 这表示的行为 `--bare` 是由继承的 `--mirror` 。 导致没有可编辑工作文件的裸仓库。 另外， `--mirror` 将克隆远程存储库的所有扩展引用，并维护远程分支跟踪配置。 然后，您可以 `git remote` 在镜像上 运行 update，它将覆盖原始存储库中的所有引用。 为您提供确切的“镜像”功能。

### 其他配置选项

有关其他git clone选项的完整列表，请访问 [官方Git文档](https://git-scm.com/docs/git-clone) 。 在本文档中，我们将介绍其他一些常见选项。

#### git clone\-模板

```
git clone --template=<template_directory> <repo location>
```

克隆存储库， `<repo location>` 并将模板从 `<template directory>` 应用于新创建的本地分支。 有关Git模板的完整介绍，请参见我们的 [`git init`页面](http://www.atlassian.com/git/tutorials/setting-up-a-repository/git-init) 。

## Git URL

Git有自己的URL语法，该语法用于将远程存储库位置传递给Git命令。 因为 `git clone` 是远程存储库上最常用的，所以我们将在这里检查Git URL语法。

### Git URL协议

**\-SSH**

安全外壳（SSH）是普遍存在的经过身份验证的网络协议，通常在大多数服务器上默认配置。 由于SSH是经过身份验证的协议，因此在连接之前，您需要与托管服务器建立凭据。 `ssh://[user@]host.xz[:port]/path/to/repo.git/`

**\-GIT**

git特有的协议。 Git带有在端口（9418）上运行的守护程序。 该协议与SSH相似，但是没有身份验证。 `git://host.xz[:port]/path/to/repo.git/`

**\-HTTP**

超文本传输​​协议。 网络协议，最常用于通过Internet传输网页HTML数据。 可以将Git配置为通过HTTP进行通信 `http[s]://host.xz[:port]/path/to/repo.git/`

## 摘要

在本文档中，我们深入研究了 `git clone` 。 最重要的要点是：

1\. `git clone` 用于创建目标存储库的副本

2.目标存储库可以是本地或远程的

3\. Git支持一些网络协议来连接到远程仓库

4.有许多不同的配置选项可用于更改克隆的内容

有关功能的更多更深入的参考 `git clone` ，请查阅 [官方的Git文档](https://git-scm.com/docs/git-clone) 。 在 [设置存储库指南中，](https://www.atlassian.com/git/tutorials/setting-up-a-repository) 我们还将介绍git clone的实际示例 。