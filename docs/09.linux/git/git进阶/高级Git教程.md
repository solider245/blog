---
title: 高级Git教程
date: 2020-10-12 12:09:51
permalink: /pages/fe030f/
categories:
  - git
  - git进阶
tags:
  - 
---
# 高级Git教程

[Atlassian的Git教程](https://www.atlassian.com/git/tutorials) 介绍了最常见的Git命令，我们的 [Git工作流程](https://www.atlassian.com/git/tutorials/comparing-workflows) 模块讨论了通常如何使用这些命令来促进协作。 仅凭这些，就足以使开发团队和Git一起运行。 但是，如果您真的想利用Git的全部功能，则可以开始阅读我们的Advanced Git文章。

每一篇文章都对Git的高级功能进行了深入的讨论。 他们没有提出新的命令和概念，而是通过解释内部发生的事情来提高您现有的Git技能。 有了这些知识，您将能够更有效地使用熟悉的Git命令。 更重要的是，您将永远不会害怕破坏Git存储库，因为您将了解它为什么损坏以及如何修复它。

## 合并与重新定基

![合并与重新定基](https://wac-cdn.atlassian.com/dam/jcr:15447956-9d33-4817-9dc6-fd6c86f24240/hero.svg?cdnVersion=1084)

Git致力于处理不同的历史。 它的 `git merge` 和 `git rebase` 命令提供了集成来自不同分支的提交的替代方法，并且这两种选择都有各自的优势。 在本文中，我们将讨论如何以及何时 `git merge` 可以用rebase替换 基本 操作。

[学到更多 ”](https://www.atlassian.com/git/tutorials/merging-vs-rebasing)

## 重置，签出和还原

![重置，签出和还原](https://wac-cdn.atlassian.com/dam/jcr:7a828d45-b8d9-49a0-9f43-8f6687110fcb/hero.svg?cdnVersion=1084)

的 `git reset` ， `git checkout` 和 `git revert` 命令都在他们撤消在你的仓库某些类型的变化相似。 但是，它们都会影响工作目录，暂存快照和提交历史记录的不同组合。 本文明确定义了这些命令的区别以及何时在标准Git工作流程中使用它们。

[学到更多 ”](https://www.atlassian.com/git/tutorials/resetting-checking-out-and-reverting)

## 高级Git日志

![高级Git日志](https://wac-cdn.atlassian.com/dam/jcr:613277ed-3b4b-4c45-8657-869f9bc3d23e/hero.svg?cdnVersion=1084)

该 `git log` 命令使您的项目历史记录有用。 没有它，您将无法访问任何提交。 但是，如果您像大多数有抱负的Git用户一样，那么您可能只是从头开始了解 `git log` 。 本文向您介绍其高级格式和过滤选项，使您能够从Git存储库中提取各种有趣的信息。

[学到更多 ”](https://www.atlassian.com/git/tutorials/git-log)

## 吉特·胡克斯

![吉特·胡克斯](https://wac-cdn.atlassian.com/dam/jcr:c5d250fd-b2ab-446a-9a5a-f7dec86abed8/hero.svg?cdnVersion=1084)

如果您希望在Git存储库中发生某个事件时执行自定义操作，则可以选择钩子。 它们使您可以标准化提交消息，自动化测试套件，通知持续集成系统等等。 在阅读完本文之后，您将了解Git挂钩可以简化工作流程的多种方式。

[学到更多 ”](https://www.atlassian.com/git/tutorials/git-hooks)

## 引用和引用日志

![引用和引用日志](https://wac-cdn.atlassian.com/dam/jcr:8d62148d-ba03-4762-bd3a-06ddc465b07f/hero.svg?cdnVersion=1084)

一个 **裁判** 是Git的内部指的是提交的方式。 您已经熟悉了许多类别的引用，包括提交哈希和分支名称。 但是，还有许多其他类型的引用，并且几乎每个Git命令都以某种形式使用它们。 您将对Git的内部运作有深入的了解，从而远离本文。

[学到更多 ”](https://www.atlassian.com/git/tutorials/refs-and-the-reflog)