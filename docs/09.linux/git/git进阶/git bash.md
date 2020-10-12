---
title: git bash
date: 2020-10-12 12:09:51
permalink: /pages/a3e9a7/
categories:
  - git
  - git进阶
tags:
  - 
---
# 吉特·巴什（Git Bash）

Git的核心是一组命令行实用程序，旨在在Unix风格的命令行环境中执行。 像Linux和macOS这样的现代操作系统都包含内置的Unix命令行终端。 使用Git时，这使Linux和macOS成为互补的操作系统。 相反，Microsoft Windows使用Windows命令提示符（非Unix终端环境）。

在Windows环境中，Git通常打包为高级GUI应用程序的一部分。 Git的GUI可能会尝试抽象和隐藏底层的版本控制系统原语。 这可以为Git初学者快速为项目做出贡献提供很大的帮助。 一旦项目的协作需求与其他团队成员一起增长，了解实际的原始Git方法如何工作就变得至关重要。 这是为命令行工具删除GUI版本的好处。 提供Git Bash来提供终端Git体验。

## 什么是Git Bash？

Git Bash是用于Microsoft Windows环境的应用程序，它为Git命令行体验提供了一个仿真层。 Bash是Bourne Again Shell的首字母缩写。 Shell是用于通过书面命令与操作系统进行交互的终端应用程序。 Bash是Linux和macOS上流行的默认Shell。 Git Bash是一个软件包，可以在Windows操作系统上安装Bash，一些常见的bash实用程序和Git。

## 如何安装Git Bash

Git Bash包含在 [Git For Windows](https://gitforwindows.org/) 软件包中。 与其他Windows应用程序一样，下载并安装Windows版Git。 下载完成后，找到包含的 `.exe` 文件并打开以执行Git Bash。

## 如何使用Git Bash

Git Bash具有与标准Bash体验相同的操作。 回顾基本的Bash使用情况将很有帮助。 Bash的高级用法超出了本Git重点文档的范围。

## 如何浏览文件夹

Bash命令 `pwd` 用于打印“当前工作目录”。 `pwd` 等效于  在DOS（Windows控制台主机）终端上 执行 cd 。 这是当前Bash会话所在的文件夹或路径。

Bash命令 `ls` 用于“列出”当前工作目录的内容。 `ls` 等效 `DIR` 于Windows控制台主机终端上的。

Bash和Windows控制台主机都具有 cd 命令。 cd 是“更改目录”的首字母缩写。  使用附加的目录名调用 cd 。 执行 cd  会将终端会话的当前工作目录更改为传递的目录参数。

## Git Bash命令

Git Bash与其他命令打包在一起，这些命令可以 `/usr/bin` 在Git Bash仿真 的 目录中 找到 。 实际上，Git Bash可以在Windows上提供相当强大的Shell体验。 GIT中击来包装的作为本文件的范围之内的下列外壳命令： `[Ssh](https://man.openbsd.org/ssh.1)` ， `[scp](https://linux.die.net/man/1/scp)` ， `[cat](http://man7.org/linux/man-pages/man1/cat.1.html)` ， `[find](https://linux.die.net/man/1/find)` 。

除了前面讨论的Bash命令集之外，Git Bash还包括整个站点讨论的整套Git核心命令。 有关更多信息，请参见相应的文档页面 。 ```[git clone](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone)``, `[git commit](https://www.atlassian.com/git/tutorials/saving-changes/git-commit)`, `[git checkout](https://www.atlassian.com/git/tutorials/using-branches/git-checkout)`, `[git push](https://www.atlassian.com/git/tutorials/syncing/git-push)`,`` ```