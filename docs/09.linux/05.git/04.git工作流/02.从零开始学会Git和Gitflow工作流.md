---
title: 从零开始学会Git和Gitflow工作流
date: 2020-10-12 12:09:51
permalink: /pages/7b4af1/
categories:
  - git
  - git工作流
tags:
  - 
---
# 从零开始，学会Git和Gitflow工作流

阅读 2064

收藏 144

2017\-12\-04

原文链接：[www.jianshu.com](http://www.jianshu.com/p/84dd2da33c82)

## 前言

大家好！在下游回来了！不啰嗦快进正题！ 本篇文章是面对刚开始接触Git的新手，所讲命令并不全，在文章结束会放入各路大手的比较全面的文章，有兴趣继续学习的同学可以看下。

工作时大家可能有这种感受，部门里的开发越来越多，并行开发的需求也越来越多，代码版本的管理就越来越复杂，冲突会越来越多。所以急需一个成熟的代码管理工具来管理，现在市面上主要使用的是Git、SVN。

**本篇文章将以操作步骤的方式，带大家一步步的学会Git。学会了如何提交仓库，再学习下Gitflow，进一步规范代码管理！**

**强烈推荐初学者手敲Git指令，知道自己在做什么。**

![](https://user-gold-cdn.xitu.io/2017/11/30/1600b046a29b94df?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

## 目录

1.  概念
2.  提交代码
    2.1 小提示
    2.2 创建工作区（Workspace）代码
    ~ 2.2.1 从远程仓库（Remote）拉取
    ~ 2.2.2 上传本地代码并连接远程仓库
    2.3 修改代码后，将代码提交到暂存区（Index）
    2.4 将暂存区文件提交到本地仓库（Repository）
    2.5 将本地仓库提交到远程仓库（Remote）
3.  关于协作
    3.1 拉取远程仓库（Remote）代码到本地仓库（Repository）
    3.2 分支（branch）
    3.3 合并分支代码（merge）
4.  其他操作
    4.1 Git常用命令速查表
    4.2 大手的入门文章
5.  Gitflow工作流
    5.1 Gitflow概念
    5.2 Gitflow图解
    5.3 Gitflow的主分支
    ~ 5.3.1 master分支
    ~ 5.3.2 develop分支
    5.4 Gitflow的辅助分支
    ~ 5.4.1 feature分支
    ~ 5.4.2 release分支
    ~ 5.4.3 hotfix分支
    5.5 Gitflow小结
6.  结语

没研究出简书怎么页内跳转，大家先搜索下。

## 1.概念

学习具体操作步骤之前，先要理解四个概念，下面看一张图（从大神那拿的，下面放大神文章的链接）。

![](https://user-gold-cdn.xitu.io/2017/11/30/1600b046a716c223?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

咱们先不看上面的线，先理解一下这4个大色块的名词：

*   **Workspace**：工作区，平时我们写代码的地方。
*   **Index**：暂存区，写完代码后让它变成的待提交的状态。
*   **Repository**：本地仓库，提交暂存区的代码到这里，记录进入代码本地管理。
*   **Remote**：远程仓库，将本地仓库的修改的代码提交到远程，可以供远程协作的人下载。

以上四个名词是Git中最重要的概念，记好咯，在下一节非常重要。接下来开始介绍Git的操作步骤！

## 2.提交代码

#### 2.1 小提示：

1.  该节会从项目创建（或从远程仓库下载）开始，直到代码提交到远程仓库所有的步骤，建议读者跟着敲一下，熟能生巧。

2.  读者需要安装好Git，给大家一份安装指南，包括各个系统。
    [《Git学习笔记二 Git安装》](https://www.jianshu.com/p/1d17fff250ed)

#### 2.2 创建工作区（Workspace）代码

想开始Git操作必须本地有一份代码是跟远程仓库（Remote）相连。这部分代码有两种获取方式。

*   **2.2.1 从远程仓库（Remote）拉取：**（公司项目比较常见）
    *   建立自己项目的文件夹，比如：D:\\test。
    *   在该文件夹中点击鼠标右键，选择Git Bash Here（打开Git的命令行界面）。 ![](https://user-gold-cdn.xitu.io/2017/11/30/1600b046a2611fa5?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)
    *   在命令行输入： **git clone <url>**，将远程git仓库的地址填入，成功后完成。

> **git clone <url>** ：克隆远程仓库的版本到本地，成功后本地就有了和远程仓库相同的代码。并且已经和远程仓库连接成功。

*   **2.2.2 上传本地代码并连接远程仓库：**（自己使用Github的时候，使用比较多）
    *   打开本地项目的文件夹，比如：D:\\test\\MyApplicationTest（要在项目的根目录里）
    *   在该文件夹中点击鼠标右键，选择Git Bash Here
    *   执行以下步骤（命令具体作用下文说）：
        git init
        git add .
        git commit \-m "first commit"
        git remote add origin 远程仓库地址
        git push \-u origin master
    *   完成

**小结：前者适用于代码存在于远程仓库（Remote）的情况。后者适用于本地仓库（Repository）初次上传到远程仓库的情况。**

#### 2.3 修改代码后，将代码提交到暂存区（Index）

**代码提交到远程仓库的第一步。**写完代码后感觉可以提交了，将代码提交到暂存区（Index），成为待提交状态，被Git管理。

> **git add .** ：添加**当前目录**所有的文件都进入暂存区。
> **git add <dir>**：添加**指定目录**所有的文件都进入暂存区。
> **git add <file1>**：添加**指定文件**进入暂存区。

以上三种方式，具体看需要提交多少文件，通常第一种比较常用。

![](https://user-gold-cdn.xitu.io/2017/11/30/1600b046a2734d74?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)
如图执行git add . 之后没有任何提示，**想看一下是否已经加入暂存区的话怎么办呢？**

> **git status** ：查看所有文件是否有修改，是否进入暂存区，已提交到本地仓库的不会展示。

![](https://user-gold-cdn.xitu.io/2017/11/30/1600b046c4bd462e?imageView2/0/w/1280/h/960/format/webp/ignore-error/1) *未进入暂存区* ![](https://user-gold-cdn.xitu.io/2017/11/30/1600b046c8ab61ad?imageView2/0/w/1280/h/960/format/webp/ignore-error/1) *已进入暂存区*

#### 2.4 将暂存区文件提交到本地仓库（Repository）

**代码提交到远程仓库的第二步。**将已进入暂存区管理的文件上传到本地仓库，这是一个离线操作。

> **git commit \-m <message>**：将暂存区的文件上传到本地仓库，<message>的位置填写本次提交修改的内容和一些注释。

![](https://user-gold-cdn.xitu.io/2017/11/30/1600b046ca64a71d?imageView2/0/w/1280/h/960/format/webp/ignore-error/1) *提交本地仓库*

#### 2.5 将本地仓库提交到远程仓库（Remote）

**代码提交到远程仓库的最后一步！**将本地仓库新的记录，提交到远程仓库，这样小伙伴就可以下载到已提交的代码了。

> **git push <remote><branch>**：将本地仓库新记录提交到远程仓库，<remote>位置填写远程仓库名称，<branch>填写远程仓库需要提交的分支。

![](https://user-gold-cdn.xitu.io/2017/11/30/1600b046cd4047cd?imageView2/0/w/1280/h/960/format/webp/ignore-error/1) *推送到远程origin仓库的master分支*

走完了以上四步，大家基本上就学会提交代码了。

## 3.关于协作

在公司工作不可能不涉及到协作，许多人操纵同一份代码只提交代码并不能解决全部问题。之前明白了如何提交代码，现在讲解下有关协作的重要的命令。

#### 3.1 拉取远程仓库（Remote）代码到本地仓库（Repository）

在协作中小伙伴写了代码上传到远程仓库，需要我们手动去拉取代码。

> **git pull <remote><branch>**：从远程仓库拉取代码到本地仓库，<remote>位置填写远程仓库名称，<branch>填写拉取远程仓库的分支。

![](https://user-gold-cdn.xitu.io/2017/11/30/1600b046ece0dd46?imageView2/0/w/1280/h/960/format/webp/ignore-error/1) *拉取远程origin仓库的master分支到本地仓库*

将代码提交到远程仓库之前，最好先拉取一下远程代码，小伙伴们的最新代码，以免产生冲突。

#### 3.2 分支（branch）

分支是一个很重要的概念，在合作中有可能会有并行开发的需求，但可能不会同时上线，不能把没有开发完成的分支上线，所以就出现了分支（branch）。

**分支的功能：从同一份稳定代码拉出有相同代码的分支，每个人在自己的分支上开发提交代码，不会互相打扰，完成后再进行代码的合并。**

> **git branch**：列出所有本地分支
> **git branch \-r**：列出所有远程分支
> **git branch \-a**：列出所有本地分支和远程分支

**git branch <branch\-name>**：新建一个分支，但依然停留在当前分支，<branch\-name>为新建的分支名
**git checkout \-b <branch\-name>**：新建一个分支，并切换到该分支，<branch\-name>为新建的分支名
**git checkout <branch\-name>**：切换到指定分支，并更新工作区，<branch\-name>为指定的分支名
**git branch \-d <branch\-name>**：删除分支，<branch\-name>为指定的分支名
**git push origin \-\-delete <branch\-name>**：删除远程分支，<branch\-name>为指定的分支名
**git push origin <branch\-name>**：将当前分支上传到远程仓库，<branch\-name>为新建的远程分支名

![](https://user-gold-cdn.xitu.io/2017/11/30/1600b046ecd95855?imageView2/0/w/1280/h/960/format/webp/ignore-error/1) *分支操作*

分支的命令看起来很多，但其实都不复杂，可以敲着玩一下。

#### 3.3 合并分支代码（merge）

如果完成了开发需要合并，那就轮到merge出场了！合并之前确保要合并的两个分支都是当前分支的最新代码（pull一下）。然后切换到要保存合并代码的分支。

> **git merge <branch\-name>**：合并指定分支到当前分支，<branch\-name>是指定分支，将该分支代码合并到当前分支。
>
> ![](https://user-gold-cdn.xitu.io/2017/11/30/1600b046eac89818?imageView2/0/w/1280/h/960/format/webp/ignore-error/1) *将master分支代码合并到develop上*

合并完成后可能会出现冲突，分支会变成 **xxxx|MERGING** 状态，可能两个分支都修改了同一个文件的某一段代码，就需要我们人力处理他们了。

![](https://user-gold-cdn.xitu.io/2017/11/30/1600b046ee704644?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)*删除错误代码，保留正确的代码，记得把 "<<<<< HEAD，======" 删除*

处理完成后重新commit一下，就会恢复到正常状态。

## 4.其他操作

#### 4.1 Git常用命令速查表

![](https://user-gold-cdn.xitu.io/2017/11/30/1600b0470bd30d66?imageView2/0/w/1280/h/960/format/webp/ignore-error/1) *git常用命令.jpg*
这是刚开始学习使用Git就保留的图，分享给大家。**建议大家先不要使用GUI去操作，先敲命令行才会明白自己在做的是什么，更容易掌握Git。**

#### 4.2 大手的入门文章

[《一篇文章，教你学会Git》](https://www.jianshu.com/p/072587b47515)
分享给大家，写的比较全面，看完会更加深入理解。

## 5.Gitflow工作流

首先为什么要学习Gitflow，之前咱们学会了各种分支提交合并等等还不行吗？答案是：对！还不行！！因为一旦项目人数变多，并行开发的功能多了，免不了各种合并问题和冲突，各种不规范的合并就像破窗户越破越大，最后变得无可救药。

#### 5.1 Gitflow概念

Git Flow是构建在Git之上的一个组织软件开发活动的模型，是在Git之上构建的一项软件开发最佳实践。Git Flow是一套使用Git进行源代码管理时的一套行为规范和简化部分Git操作的工具。Git Flow重点解决的是由于源代码在开发过程中的各种冲突导致开发活动混乱的问题。因此，Git flow可以很好的于各种现有开发模型相结合使用。

#### 5.2 Gitflow图解

![](https://user-gold-cdn.xitu.io/2017/11/30/1600b0470ec80e2a?imageView2/0/w/1280/h/960/format/webp/ignore-error/1) *Gitflow模型全貌*

看起来发懵？没事，咱们来缕一缕。

Git Flow模型中定义了主分支和辅助分支两类分支。其中主分支用于组织与软件开发、部署相关的活动；辅助分支组织为了解决特定的问题而进行的各种开发活动。

#### 5.3 Gitflow的主分支

主分支是所有开发活动的核心分支。所有的开发活动产生的输出物最终都会反映到主分支的代码中。主分支分为master分支和development分支。

*   **5.3.1 master分支**
    **只存线上的代码，只有确定可以上线时的才合并到master上，并且在master的基础上打Tag。**
    比如，上线了1.0版本，那就将代码提交到master上，并打Tag命名为1.0。

    ![](https://user-gold-cdn.xitu.io/2017/11/30/1600b0471aa58614?imageView2/0/w/1280/h/960/format/webp/ignore-error/1) *master分支*
*   **5.3.2 develop分支**
    初次创建develop时，需要从master分支拉取，保持开发时代码和线上最新的代码相同。**develop分支是在开发时的最终分支，具有所有当前版本需要上线的所有功能。**
    比如：当我们和小伙伴在自己创建的feature分支（开发功能分支，后面讲）开发完不同的需求，需要合并测试，那这时就需要将所有的feature分支合并到develop上。然后再提交测试，一起在develop上修改Bug。

    ![](https://user-gold-cdn.xitu.io/2017/11/30/1600b04711c8ea91?imageView2/0/w/1280/h/960/format/webp/ignore-error/1) *feature合并到develop分支*

#### 5.4 Gitflow的辅助分支

辅助分支是用于组织解决特定问题的各种软件开发活动的分支。辅助分支主要用于组织软件新功能的并行开发、简化新功能开发代码的跟踪、辅助完成版本发布工作以及对生产代码的缺陷进行紧急修复工作。这些分支与主分支不同，通常只会在有限的时间范围内存在。

辅助分支包括：
1.用于开发新功能时所使用的feature分支；
2.用于辅助版本发布的release分支；
3.用于修正生产代码中的缺陷的hotfix分支。

*   **5.4.1 feature分支**
    *   **用于开发功能的分支，必须从最新的develop分支代码拉取。分支命名基本上是feature/xxxxx（和功能相关的名字）。**
    *   不强制提交到远程仓库，可以本地创建。
    *   比如，我要开发登录功能，我从develop分支的最新代码创建新分支命名为feature/login，然后切换到这个新分支开始开发。开发完成后，测试差不多完成，合并到develop分支。

![](https://user-gold-cdn.xitu.io/2017/11/30/1600b0472c098c49?imageView2/0/w/1280/h/960/format/webp/ignore-error/1) *创建feature/login流程*

*   **5.4.2 release分支**
    *   **当develop分支已经有了本次上线的所有代码的时候，并且以通过全部测试的时候，可以从develop分支创建release分支了，release分支是为发布新的产品版本而设计的。**
    *   通过在release分支上进行这些工作可以让develop分支空闲出来以接受新的feature分支上的代码提交，进入新的软件开发迭代周期。
    *   在这个分支上的代码允许做小的缺陷修正、准备发布版本所需的各项说明信息（版本号、发布时间、编译时间等等）。
    *   比如，此次1.0版本所有的功能版本都已经合并到了develop上，并且所有测试都已经通过了测试，那我就创建新的release分支release/v1.0。切换到新分支，修改最新的版本号等，不允许大的更改。

![](https://user-gold-cdn.xitu.io/2017/11/30/1600b047326e8d1f?imageView2/0/w/1280/h/960/format/webp/ignore-error/1) *release操作步骤*

*   **5.4.3 hotfix分支**
    *   **当线上出现bug需要紧急修复时，从当前master分支派生hotfix分支。**
    *   修改线上bug，修改完成后合并回develop和master分钟。
    *   比如，在线上v1.0登录功能出现问题，我从master拉取代码创建新的分支hotfix/v1.0\_login，修改完成后合并到master和develop上。

![](https://user-gold-cdn.xitu.io/2017/11/30/1600b04739042c74?imageView2/0/w/1280/h/960/format/webp/ignore-error/1) *hotfix分支操作*

#### 5.5 Gitflow小结

Git Flow开发模型从源代码管理角度对通常意义上的软件开发活动进行了约束。应该说，为我们的软件开发提供了一个可供参考的管理模型。Git Flow开发模型让nvie的开发代码仓库保持整洁，让小组各个成员之间的开发相互隔离，能够有效避免处于开发状态中的代码相互影响而导致的效率低下和混乱。

所谓模型，在不同的开发团队，不同的文化，不同的项目背景情况下都有可能需要进行适当的裁剪或扩充。祝各位好运！ ![](https://user-gold-cdn.xitu.io/2017/11/30/1600b0473db2e108?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

## 6.结语

浩浩荡荡的文章终于结束了，相信大家都想打我了，希望大家能从这篇文章中学会Git的基础，也能学会如何去管理自己和公司的代码。在代码合并上出现的惨不忍睹的现场真的太多了。在下不才，只想把这些分享给大家和后来的人。

希望我的文章能给大家带来一点点的福利，那在下就足够开心了。 下次再见！