---
title: pull request
date: 2020-10-12 12:09:51
permalink: /pages/de1c00/
categories:
  - git入门
  - 拉取请求
tags:
  - 
---
# 发出拉取请求

[工作原理](#how-it-works) [示例](#example) [从这里出发](#where-to-go)

拉取请求的功能使开发人员可以更轻松地使用 [Bitbucket](http://www.bitbucket.org) 进行协作 。 它们提供了一个用户友好的Web界面，用于在将建议的更改集成到正式项目中之前对其进行讨论。

![Git工作流程：Bitbucket中的拉取请求](https://wac-cdn.atlassian.com/dam/jcr:ff6b00cc-0ca3-4d5b-8235-8d4cbcedd19e/01.svg?cdnVersion=1084)

以最简单的形式，拉取请求是开发人员通知团队成员他们已完成功能的一种机制。 开发人员的功能分支就绪后，开发人员将通过其Bitbucket帐户提出拉取请求。 这使所有相关人员都知道他们需要检查代码并将其合并到 `master` 分支中。

但是，拉取请求不仅仅是通知，它还是一个讨论提议功能的专门论坛。 如果更改有任何问题，队友可以在拉取请求中发布反馈，甚至可以通过推送后续提交来调整功能。 所有这些活动都直接在拉取请求中进行跟踪。

![Git工作流程：拉取请求中的活动](https://wac-cdn.atlassian.com/dam/jcr:dc1a0821-efd6-4852-b7e6-c3a787656c61/02.svg?cdnVersion=1084)

与其他协作模型相比，这种用于共享提交的正式解决方案使工作流程更加简化。 SVN和Git都可以使用简单的脚本自动发送通知电子邮件。 但是，在讨论更改时，开发人员通常必须依靠电子邮件线程。 这可能变得很杂乱，尤其是在涉及后续提交时。 拉取请求将所有这些功能放到Bitbucket存储库旁边的友好Web界面中。

### 提取请求的剖析

当您提交拉取请求时，您要做的就是 *请求* 另一个开发人员（例如，项目维护者） *将* 分支从您的存储库中*提取* 到其存储库中。 这意味着您需要提供4条信息来提交拉取请求：源存储库，源分支，目标存储库和目标分支。

![Git工作流程：拉取请求](https://wac-cdn.atlassian.com/dam/jcr:3a777a86-6106-4484-b75d-f2f19abc0e7f/03.svg?cdnVersion=1084)

Bitbucket将其中许多值设置为合理的默认值。 但是，根据您的协作工作流程，您的团队可能需要指定不同的值。 上图显示了一个请求，该请求请求将功能分支合并到正式的master分支中，但是还有许多其他使用请求的方式。

## 这个怎么运作

拉请求可与结合使用 [特性分支工作流](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow) ，所述 [Gitflow工作流程](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) ，或 [分岔工作流](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow) 。 但是拉取请求需要两个不同的分支或两个不同的存储库，因此它们将不适用于 [Centralized Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/centralized-workflow) 。 在这些工作流程中使用拉取请求略有不同，但是一般过程如下：

1.  开发人员在其本地仓库的专用分支中创建功能。

2.  开发人员将分支推送到公共Bitbucket存储库。

3.  开发人员通过Bitbucket提交拉取请求。

4.  团队的其余成员将检查代码，进行讨论并进行更改。

5.  项目维护人员将功能部件合并到官方存储库中，并关闭拉取请求。

本节的其余部分描述如何针对不同的协作工作流利用拉取请求。

### 具有拉取请求的功能分支工作流程

Feature Branch Workflow使用共享的Bitbucket存储库来管理协作，并且开发人员在隔离的分支中创建功能。 但是， `master` 开发人员应该 立即 打开拉取请求，以围绕功能进行讨论，然后再将其集成到主代码库中 ，而不是立即将它们合并 。

![拉取请求：功能分支工作流程](https://wac-cdn.atlassian.com/dam/jcr:8c784aa1-3393-49b7-b4c5-2b91bf3aa48a/04.svg?cdnVersion=1084)

Feature Branch工作流程中只有一个公共存储库，因此拉取请求的目标存储库和源存储库将始终相同。 通常，开发人员会将其功能分支指定为源分支，并将该 `master` 分支指定为目标分支。

收到拉取请求后，项目维护者必须决定要做什么。 如果功能准备就绪，他们可以将其合并 `master` 并关闭拉取请求。 但是，如果提议的更改存在问题，他们可以在拉取请求中发布反馈。 后续提交将显示在相关评论的旁边。

对于不完整的功能，也可以提出拉取请求。 例如，如果开发人员在执行特定要求时遇到困难，则他们可以提交包含正在进行的工作的拉取请求。 然后其他开发人员可以在拉取请求中提供建议，甚至可以通过其他提交自己解决问题。

### 带拉取请求的Gitflow工作流

Gitflow工作流程类似于Feature Branch Workflow，但定义了围绕项目发行版设计的严格分支模型。 将拉取请求添加到Gitflow工作流为开发人员提供了一个方便的地方，使他们可以在发布版本或维护分支上进行讨论。

![拉取请求：Gitflow工作流程](https://wac-cdn.atlassian.com/dam/jcr:50c76de3-6c5b-4adf-9a96-a611cc3dbebc/05.svg?cdnVersion=1084) ![拉取请求：Gitflow工作流程2](https://wac-cdn.atlassian.com/dam/jcr:a5c54fd9-09d7-4f59-90c1-8b228fec80a5/06.svg?cdnVersion=1084)

Gitflow工作流中的拉取请求的机制与上一节完全相同：当功能，发行版或修补程序分支需要复审时，开发人员只需提交拉取请求，其余团队将通过Bitbucket进行通知。 。

功能通常合并到 `develop` 分支中，而release和hotfix分支合并到 `develop` 和中 `master` 。 拉取请求可用于正式管理所有这些合并。

### 带拉取请求的派生工作流

在分叉工作流中，开发人员将已完成的功能推入 *其自己的* 公共存储库，而不是共享的存储库。 之后，他们提交拉取请求，以使项目维护者知道已准备好进行审查。

拉取请求的通知方面在此工作流程中特别有用，因为项目维护者无法知道其他开发人员何时将提交添加到其Bitbucket存储库中。

![拉取请求：分叉工作流](https://wac-cdn.atlassian.com/dam/jcr:2510a321-ba5f-4c31-82ec-f3ad062c8e6d/07.svg?cdnVersion=1084)

由于每个开发人员都有自己的公共存储库，因此拉取请求的源存储库将不同于其目标存储库。 源存储库是开发人员的公共存储库，而源分支是包含建议的更改的分支。 如果开发人员尝试将功能部件合并到主代码库中，则目标存储库为正式项目，而目标分支为 `master` 。

拉取请求还可以用于与官方项目之外的其他开发人员进行协作。 例如，如果开发人员正在与队友一起使用某项功能，则他们可以使用 *队友的* Bitbucket存储库（而非官方项目）向目的地 提出拉取请求 。 然后，他们将对源分支和目标分支使用相同的功能分支。

![拉取请求：分叉工作流](https://wac-cdn.atlassian.com/dam/jcr:0907a594-5786-47fb-87b4-05fc08e0c8dc/08.svg?cdnVersion=1084)

两位开发人员可以在pull请求中讨论和开发功能。 完成后，其中一个将提交另一个请求，要求将功能合并到正式的master分支中。 这种灵活性使派生请求成为Forking工作流中非常强大的协作工具。

## 例

下面的示例演示了如何在派生工作流中使用提取请求。 它同样适用于小型团队中的开发人员以及对开源项目做出贡献的第三方开发人员。

在示例中，Mary是开发人员，John是项目维护人员。 他们两个都有自己的公共Bitbucket存储库，而John's包含官方项目。

### 玛丽分叉官方项目

![拉取请求：分叉项目](https://wac-cdn.atlassian.com/dam/jcr:8b3d2111-5a88-4802-967c-71f51c248b03/09.svg?cdnVersion=1084)

要开始在项目中工作，Mary首先需要派生John的Bitbucket存储库。 她可以通过登录Bitbucket，导航到John的存储库并单击“ *Fork”* 按钮 来做到这一点 。

![拉取请求：Bitbucket中的分叉](https://wac-cdn.atlassian.com/dam/jcr:93d2ede4-241e-4296-b403-584d5ee24d8e/10.svg?cdnVersion=1084)

填写分叉存储库的名称和描述后，她将获得项目的服务器端副本。

### 玛丽克隆了她的Bitbucket存储库

![提取请求：克隆Bitbucket存储库](https://wac-cdn.atlassian.com/dam/jcr:4f051d96-8ce7-4aab-af74-b2de38c41443/11.svg?cdnVersion=1084)

接下来，玛丽需要克隆她刚刚创建的Bitbucket存储库。 这将为她提供本地计算机上项目的工作副本。 她可以通过运行以下命令来执行此操作：

```
git clone https://user@bitbucket.org/user/repo.git
```

请记住，它会 `git clone` 自动创建一个 `origin` 指向Mary分叉的存储库 的 远程服务器。

### 玛丽开发了一个新功能

![拉取请求：开发新功能](https://wac-cdn.atlassian.com/dam/jcr:f0979362-cf67-413d-bac1-8275e20aea58/12.svg?cdnVersion=1084)

在开始编写任何代码之前，Mary需要为该功能创建一个新分支。 她将使用此分支作为拉取请求的源分支。

```
git checkout -b some-feature
# Edit some code
git commit -a -m "Add first draft of some feature"
```

Mary可以根据需要使用任意多个提交来创建功能。 而且，如果该功能的历史记录比她想的要混乱，她可以使用 [交互式变基](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase-i) 来删除或压缩不必要的提交。 对于较大的项目，清理功能的历史记录可使项目维护人员更轻松地了解请求请求中的情况。

### 玛丽将功能推送到她的Bitbucket存储库

![提取请求：将功能推送到Bitbucket存储库](https://wac-cdn.atlassian.com/dam/jcr:d3a07e01-ad5c-4e11-929a-87c049a27a6b/13.svg?cdnVersion=1084)

完成功能后，Mary可以通过以下简单操作将功能分支推送到她自己的Bitbucket存储库（不是官方存储库） `git push` ：

```
git push origin some-branch
```

这使得她的更改可供项目维护者（或可能需要访问它们的任何协作者）使用。

### 玛丽创建拉取请求

![拉取请求：创建拉取请求](https://wac-cdn.atlassian.com/dam/jcr:36f8c233-ef70-41ce-8b91-4f21dd735817/14.svg?cdnVersion=1084)

在Bitbucket具有功能分支之后，Mary可以导航到其分叉的存储库，然后单击右上角的“ *Pull request”* 按钮，从而 通过其Bitbucket帐户创建拉取请求 。 生成的表单自动将Mary的存储库设置为源存储库，并要求她指定源分支，目标存储库和目标分支。

Mary希望将其功能合并到主代码库中，因此源分支是其功能分支，目标存储库是John的公共存储库，而目标分支是 `master` 。 她还需要为拉取请求提供标题和说明。 如果除John之外，还有其他人需要批准代码，她可以在 *Reviewers* 字段中 输入代码 。

![拉取请求：Bitbucket](https://wac-cdn.atlassian.com/dam/jcr:0aba279b-e045-4481-a9f1-cac222865612/pull-request-7.png?cdnVersion=1084)

在她创建拉取请求后，将通过其Bitbucket供稿和（可选）通过电子邮件向John发送通知。

### 约翰评论拉动请求

![提取请求：Bitbucket提取请求](https://wac-cdn.atlassian.com/dam/jcr:1b30ef44-9679-49d1-bc86-8b1a0cf5e241/pull-request-8.png?cdnVersion=1084)

John可以通过单击 其自己的Bitbucket存储库中 的“ *拉取请求”* 选项卡 来访问人们提交的所有拉取请求 。 单击Mary的请求，将向他显示请求的描述，功能的提交历史以及它包含的所有更改的差异。

如果他认为该功能已准备好合并到项目中，那么他所要做的就是单击“ *合并”* 按钮以批准拉取请求并将Mary的功能合并到他的 `master` 分支中。

但是，对于这个示例，假设约翰在玛丽的代码中发现了一个小错误，需要她在合并之前对其进行修复。他可以在整个拉取请求中发表评论，也可以在其中选择特定的提交要评论的功能的历史记录。

![拉取要求：评论](https://wac-cdn.atlassian.com/dam/jcr:6d9007c1-7b42-42e4-a1ca-f7129185c16d/pull-request-9.png?cdnVersion=1084)

### 玛丽添加了后续提交

如果Mary对反馈有任何疑问，她可以在请求请求的内部进行响应，将其作为其功能的讨论论坛。

为了更正错误，Mary向其功能分支添加了另一个提交，并将其提交到其Bitbucket存储库，就像她第一次这样做一样。 该提交将自动添加到原始请求请求中，John可以在其原始注释旁边再次查看更改。

### 约翰接受请求

最后，John接受更改，将要素分支合并到master，然后关闭拉取请求。 现在，该功能已集成到项目中，任何其他从事此功能的开发人员都可以使用标准 `git pull` 命令 将其拉入自己的本地存储库中 。

## 从这往哪儿走

现在，您应该拥有开始将拉取请求集成到现有工作流程中所需的所有工具。 请记住，拉取请求并不能替代任何 [基于Git的协作工作流程](https://www.atlassian.com/git/tutorials/comparing-workflows) ，而是对它们的便捷补充，使您的所有团队成员都可以更轻松地进行协作。

准备尝试请求请求吗？

试试这个交互式教程。

[现在就开始](https://www.atlassian.com/git/tutorials/learn-about-code-review-in-bitbucket-cloud)