---
title: git别名
date: 2020-10-12 12:09:51
permalink: /pages/8342bc/
categories:
  - git
  - git入门
tags:
  - 
---
# Git Alias

本节将重点介绍Git别名。 为了更好地理解Git别名的值，我们必须首先讨论什么是别名。 术语别名是快捷方式的同义词。 别名创建是在其他流行的实用程序（如bash shell）中发现的常见模式。 别名用于创建映射到较长命令的较短命令。 别名通过减少执行命令所需的击键次数，使工作流程更高效。 作为一个简短的示例，请考虑该 `git checkout` 命令。 checkout命令是一个常用的git命令，随着时间的推移，它会累积累积的击键次数。 可以创建一个映射 `git co` 到 的别名 `git checkout` ，该 别名 `git co` 通过键入 较短的击键形式 来代替 ，从而节省了宝贵的人工指尖力量 。

## Git Alias概述

重要的是要注意，没有直接 `git alias` 命令。 通过使用 `[git config](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config)`  命令和Git配置文件 来创建别名 。 与其他配置值一样，可以在本地或全局范围内创建别名。

为了更好地理解Git别名，让我们创建一些示例。

```
$ git config --global alias.co checkout$ git config --global alias.br branch$ git config --global alias.ci commit$ git config --global alias.st status
```

前面的代码示例为通用git命令创建全局存储的快捷方式。 创建别名不会修改源命令。 因此， `git checkout` 即使我们现在有了 `git co` 别名，它 仍然可用 。 这些别名是用 `--global` 标志 创建的， 这意味着它们将存储在Git的全局操作系统级别的配置文件中。 在linux系统上，全局配置文件位于用户主目录下的 `/.gitconfig` 。

```
    [alias]        co = checkout            br = branch            ci = commit            st = status
```

这说明别名现在等同于源命令。

## 用法

通过使用启用Git别名 `git config` ，有关命令行选项和用法示例，请查阅 `[git config](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config) ` 文档。

## 例子

### 使用别名创建新的Git命令

常见的Git模式是从登台区域删除最近添加的文件。 这是通过利用 `git reset` 命令的 选项来实现的 。 可以创建一个新的别名来封装此行为，并创建一个易于记忆的新的alias\-command\-keyword：

```
git config --global alias.unstage 'reset HEAD --'
```

前面的代码示例创建一个新别名 `unstage` 。 现在， `git unstage. git unstage` 这将 启用该调用， 该 调用 将在登台区域上执行重置。 这使得以下两个命令等效。

```
git unstage fileA$ git reset HEAD -- fileA
```

## 讨论区

### 如何创建Git别名？

别名可以通过两种主要方法创建：

#### 直接编辑Git配置文件

可以手动编辑全局或本地配置文件并保存以创建别名。 全局配置文件位于 `$HOME/.gitconfig` 文件路径中。 本地路径位于活动git储存库中 `/.git/config`

，配置文件将遵循以下 `[alias]` 部分：

```
[alias] co = checkout
```

这意味着这 `co` 是 `checkout`

#### 使用git config创建别名

如前所述，该 `git config` 命令是快速创建别名的便捷实用程序。 该 `git config` 命令实际上是用于写入全局和本地Git配置文件的帮助程序实用程序。

```
git config --global alias.co checkout
```

调用该命令将更新基础的全局配置文件，就像在前面的示例中进行了编辑一样。

## Git Alias摘要

Git别名是功能强大的工作流工具，可创建常用Git命令的快捷方式。 使用Git别名将使您成为一个更快，更高效的开发人员。 别名可用于将一系列Git命令包装到新的伪Git命令中。 Git别名是通过使用 git config命令，从本质上修改本地或全局Git配置文件。 在 `[git config](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config)` 页面 上了解更多 。