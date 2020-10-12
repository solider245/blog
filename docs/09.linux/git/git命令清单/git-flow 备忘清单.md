---
title: git-flow 备忘清单
date: 2020-10-12 12:09:51
permalink: /pages/479da8/
categories:
  - git
  - git命令清单
tags:
  - 
---
## 关于

git\-flow 是一个 git 扩展集，按 Vincent Driessen 的分支模型提供高层次的库操作。 [查看详情](http://nvie.com/posts/a-successful-git-branching-model/)

★ ★ ★

这个备忘清单展示了 git\-flow 的基本操作和效果。

★ ★ ★

## 基础建议

*   Git flow 提供了极出色的命令帮忙以及输出提示。请仔细阅读并观察发生了什么事情...
*   macOS 程序 [Sourcetree](http://www.sourcetreeapp.com/) 是一个极出色的 git 界面客户端，已经提供了 git\-flow 的支持。
*   \- Git\-flow 是一个基于归并的解决方案，它并没有提供重置(rebase)特性分支的能力。

★ ★ ★

## [安装](#setup)

*   你需要有一个可以工作的 git 作为前提。
*   Git flow 可以工作在 macOS, Linux 和 Windows之下

★ ★ ★

### macOS

Homebrew

> $ brew install git\-flow\-avh

Macports

> $ port install git\-flow\-avh

### Linux

> $ apt\-get install git\-flow

### Windows (Cygwin)

> $ wget \-q \-O \- \-\-no\-check\-certificate https://raw.github.com/petervanderdoes/gitflow\-avh/develop/contrib/gitflow\-installer.sh install stable | bash

安装 git\-flow, 你需要 wget 和 util\-linux。

更多的 git flow 安装指引，请阅读 [git flow wiki](https://github.com/petervanderdoes/gitflow-avh/wiki/Installation).

![install git-flow](http://danielkummer.github.io/git-flow-cheatsheet/img/download.png)

## [开始](#getting_started)

为了自定义你的项目，Git flow 需要初始化过程。

★ ★ ★

### 初始化

使用 git\-flow，从初始化一个现有的 git 库内开始:

> git flow init

你必须回答几个关于分支的命名约定的问题。
建议使用默认值。

## [特性](#features)

*   为即将发布的版本开发新功能特性。
*   这通常只存在开发者的库中。

★ ★ ★

### 增加新特性

新特性的开发是基于 'develop' 分支的。

通过下面的命令开始开发新特性：

> git flow feature start MYFEATURE

这个操作创建了一个基于'develop'的特性分支，并切换到这个分支之下。

### 完成新特性

完成开发新特性。这个动作执行下面的操作.

*   合并 MYFEATURE 分支到 'develop'
*   删除这个新特性分支
*   切换回 'develop' 分支

> git flow feature finish MYFEATURE

### 发布新特性

你是否合作开发一项新特性？
发布新特性分支到远程服务器，所以，其它用户也可以使用这分支。

> git flow feature publish MYFEATURE

### 取得一个发布的新特性分支

取得其它用户发布的新特性分支，并签出远程的变更。

> git flow feature pull origin MYFEATURE

你可以使用 `git flow feature track MYFEATURE` 跟踪在origin上的特性分支。

## [作一个release版本](#release)

*   支持一个新的用于生产环境的发布版本。
*   允许修正小问题，并为发布版本准备元数据。

★ ★ ★

### 开始准备release版本

开始准备release版本，使用 git flow release 命令.

它从 'develop' 分支开始创建一个 release 分支。

> git flow release start RELEASE \[BASE\]

你可以选择提供一个 `[BASE]`参数，即提交记录的 sha\-1 hash 值，来开启动 release 分支. 这个提交记录的 sha\-1 hash 值必须是'develop' 分支下的。

★ ★ ★

创建 release 分支之后立即发布允许其它用户向这个 release 分支提交内容是个明智的做法。命令十分类似发布新特性：

> git flow release publish RELEASE

(你可以通过
`git flow release track RELEASE` 命令签出 release 版本的远程变更)

### 完成 release 版本

完成 release 版本是一个大 git 分支操作。它执行下面几个动作：

*   归并 release 分支到 'master' 分支
*   用 release 分支名打 Tag
*   归并 release 分支到 'develop'
*   移除 release 分支

> git flow release finish RELEASE

## [紧急修复](#hotfixes)

*   紧急修复来自这样的需求：生产环境的版本处于一个不预期状态，需要立即修正。
*   有可能是需要修正 master 分支上某个 TAG 标记的生产版本。

★ ★ ★

### 开始 git flow 紧急修复

像其它 git flow 命令一样, 紧急修复分支开始自：

> git flow hotfix start VERSION \[BASENAME\]

VERSION 参数标记着修正版本。你可以从 \[BASENAME\]开始，`[BASENAME]`为finish release时填写的版本号

### 完成紧急修复

当完成紧急修复分支，代码归并回 develop 和 master 分支。相应地，master 分支打上修正版本的 TAG。

> git flow hotfix finish VERSION

## [命令](#commands)

![git-flow commands](http://danielkummer.github.io/git-flow-cheatsheet/img/git-flow-commands.png)

## Backlog

★ ★ ★

*   并非所有可用的命令都涵盖在这里，这里包含有最重要的部分命令。
*   你依旧可以继续使用你所知道和了解的 git 命令， git flow 只是一个工具集合。
*   'support' 功能只是测试版本, 不建议使用
*   如果你乐意提供翻译，我很乐意整合它。