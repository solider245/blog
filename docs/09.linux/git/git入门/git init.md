---
title: git init
date: 2020-10-12 12:09:51
permalink: /pages/f3df8e/
categories:
  - git
  - git入门
tags:
  - 
---
# git init

该页面将 `git init` 深入 探讨该 命令。 在此页面结束时，您将了解的核心功能和扩展功能集 `git init` 。 这项探索包括：

*   `git init` 选项和用法
*   `.git` 目录概述
*   自定义 `git init` 目录环境值
*   `git init` 与 `git clone`
*   `git init` 裸仓库
*   `git init` 范本

该 `git init` 命令将创建一个新的Git存储库。 它可用于将现有的未版本化项目转换为Git存储库或初​​始化新的空存储库。 在初始化的存储库之外，大多数其他Git命令都不可用，因此这通常是您将在新项目中运行的第一个命令。

执行 `git init` 将 `.git` 在当前工作目录中 创建一个 子目录，其中包含新存储库的所有必需的Git元数据。 该元数据包括对象，引用和模板文件的子目录。 `HEAD` 还创建 一个 文件， 该 文件指向当前签出的提交。

除了 `.git` 目录 之外 ，在项目的根目录中，现有项目保持不变（与SVN不同，Git不需要 `.git` 每个子目录都有一个子目录）。

默认情况下， `git init` 会将Git配置初始化为 `.git` 子目录路径。 如果您希望子目录路径位于其他位置，则可以对其进行修改和自定义。 您可以将 `$GIT_DIR` 环境变量设置为自定义路径， `git init` 并将在那里初始化Git配置文件。 另外，您可以 `--separate-git-dir` 为相同的结果 传递 参数。 一个常见的情况单独的 `.git` 子目录，让您的系统配置“点文件”（ ， `.bashrc` ， `.vimrc` 等）的主目录，同时保持 `.git` 文件夹中的其他地方。

## 用法

与SVN相比，该 `git init` 命令是创建新版本控制项目的一种非常简单的方法。 Git不需要您创建存储库，导入文件和签出工作副本。 此外，Git不需要任何预先存在的服务器或管理员特权。 您所要做的只是将cd放入项目子目录并运行 `git init` ，您将拥有一个功能齐全的Git存储库。

```
git init
```

将当前目录转换为Git存储库。 这会将 `.git` 子目录 添加 到当前目录，并可以开始记录项目的修订。

```
git init <directory>
```

在指定目录中创建一个空的Git存储库。 运行此命令将创建一个新的子目录，名为 仅包含 `.git` 子目录。

如果您已经 `git init` 在项目目录上 运行 ，并且其中包含 `.git` 子目录，则可以安全地 `git init` 在同一项目目录上再次 运行 。 它不会覆盖现有 `.git` 配置。

### git init与git clone

快速注： `git init` 和 `git clone` 可以很容易混淆。 在较高的级别上，它们都可以用于“初始化新的git存储库”。 但是， `git clone` 取决于 `git init` 。 `git clone` 用于创建现有存储库的副本。 在内部， `git clone` 首先调用 `git init` 以创建一个新的存储库。 然后，它从现有存储库中复制数据，并签出一组新的工作文件。 在 [`git clone`页面](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone) 上了解更多信息 。

## 裸仓库\-\-\- git init \-\-bare

```
git init --bare <directory>
```

初始化一个空的Git存储库，但省略工作目录。 共享存储库应始终使用该 `--bare` 标志 创建 （请参见下面的讨论）。 按照惯例，以 `--bare` 标志结尾为的 存储库已初始化 `.git` 。 例如，名为的 `my-project` 存储 库的裸版本 应存储在名为的目录中 `my-project.git` 。

该 `--bare` 标志创建的存储库没有工作目录，因此无法在该存储库中编辑文件和提交更改。 您将创建一个裸仓库来进行git push和git pull的发布，但绝不要直接提交给它。 中央存储库应始终创建为裸存储库，因为将分支推送到非裸存储库可能会覆盖更改。 可以认为 `--bare` 这是将存储库标记为存储设施的一种方法，而不是开发环境。 这意味着对于几乎所有的Git工作流程，中央存储库都是裸露的，而开发人员本地存储库则是裸露的。

![Git教程：裸仓库](https://wac-cdn.atlassian.com/dam/jcr:88f08a3d-f34e-4c8e-974c-a01f25b2eca1/01.svg?cdnVersion=1084)

最常见的用例 `git init --bare` 是创建一个远程中央存储库：

```
ssh <user>@<host> cd path/above/repo git init --bare my-project.git
```

首先，您通过SSH进入将包含中央存储库的服务器。 然后，您导航至要存储项目的任何位置。 最后，使用该 `--bare` 标志创建一个中央存储库。 然后，开发人员将克隆 `my-project.git` 以在其开发计算机上创建本地副本。

## git init模板

```
git init <directory> --template=<template_directory>
```

初始化新的Git存储库，然后将文件从中复制 `<template_directory>` 到存储库中。

模板允许您使用预定义的 `.git` 子目录 初始化新的存储库 。 您可以将模板配置为具有默认目录和文件，这些目录和文件将被复制到新存储库的 `.git` 子目录中。 默认的Git模板通常位于 `` `/usr/share/git-core/templates` `` 目录中，但可能是您计算机上的其他路径。

默认模板是很好的参考，也是如何利用模板功能的示例。 默认模板中显示的模板的一项强大功能是Git Hook配置。 您可以创建带有预定义Git挂钩的模板，并使用准备就绪的通用挂钩初始化新的git存储库。 在 [Git Hook页面上](https://www.atlassian.com/git/tutorials/git-hooks) 了解有关Git Hooks的更多信息 。

## 组态

所有的配置都 `git init <directory>` 带有一个 `<directory>` 参数。 如果提供 `<directory>` ，则命令将在其中运行。 如果此目录不存在，将创建它。 除了已经讨论的选项和配置之外， `Git init` 还有其他一些命令行选项。 它们的完整列表如下：

`-Q`

`--QUIET`

仅打印“严重级别”消息，错误和警告。 所有其他输出均被静音。

`--BARE`

创建一个裸仓库。 （请参阅上面的“裸存储库”部分。）

`--TEMPLATE=<TEMPLATEDIRECTORY>`

指定将从中使用模板的目录。 （请参见上面的“ Git Init模板”部分。）

`--SEPARATE-GIT-DIR=<GIT DIR>`

创建一个文本文件，其中包含的路径 `<git dir>` 。 该文件充当 `.git` 目录 的链接 。 如果要将 `.git` 目录 存储 在项目工作文件的不同位置或驱动器中， 这将很有用 。 一些常见的用例 `--separate-git-dir` 是：

*   要将系统配置“ dotfiles”（ `.bashrc, .vimrc` 等）保留在主目录中，同时将 `.git` 文件夹 保留在 其他位置
*   您的Git历史记录的磁盘大小已变得非常大，您需要将其移至其他位置到单独的大容量驱动器
*   您希望在可公开访问的目录中拥有一个Git项目，例如 `` `www:root` ``

您可以调用 `git init --separate-git-dir` 现有的存储库， `.git dir` 它将被移动到指定的 `<git dir>` 路径。

`--SHARED[=(FALSE|TRUE|UMASK|GROUP|ALL|WORLD|EVERYBODY|0XXX)]`

设置新存储库的访问权限。 这指定允许哪些用户和组使用Unix级别的权限推/拉到存储库。

## 例子

### 为现有代码库创建一个新的git存储库

```
cd /path/to/code \
git init \
git add . \
git commit
```

### 创建一个新的裸仓库

```
git init --bare /path/to/repo.git
```

### 创建一个git init模板并从该模板初始化一个新的git仓库

```
mkdir -p /path/to/template \
echo "Hello World" >> /absolute/path/to/template/README \
git init /new/repo/path --template=/absolute/path/to/template \
cd /new/repo/path \
cat /new/repo/path/README
```

准备学习Git吗？

试试这个交互式教程。

[现在就开始](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud)