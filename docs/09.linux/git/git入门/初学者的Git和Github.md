---
title: 初学者的Git和Github
date: 2020-10-12 12:09:51
permalink: /pages/a61786/
categories:
  - git
  - git入门
tags:
  - 
---
#### 什么是Git

Git是一个分布式版本控制系统，用于在软件开发过程中跟踪源代码的更改，旨在协调程序员之间的工作，但可用于跟踪任何文件集中的更改。

这基本上意味着：

*   这是一个记录随着时间​​变化对我们文件的更改的系统。
*   您可以随时重新调用并返回该文件的特定版本。
*   其他开发人员可以进行协作，并在自己的计算机上拥有文件的本地版本。

#### [](#why-use-git-)为什么要使用git？

*   您可以将项目的修订版本存储在一个目录中。
*   随时轻松返回您的修订。
*   使用新功能时不会弄乱原始代码库。
*   与其他开发商合作，不受地域限制。

#### [](#what-is-github)什么是Github？

Github是一项在线服务，您可以托管您的项目，共享您的代码并帮助其他开发人员下载和处理该项目。 以后，他们可以上载代码编辑并与主分支/代码库（主分支）合并。

#### [](#how-to-install-git)如何安装Git

*   转到 [Git网站](https://git-scm.com/)
*   如果您使用的是Windows，我建议使用 [Cmder](https://cmder.net/) 。 这是Windows的命令行界面。 下载安装了git随附的完整版本。 （我用过它，绝对值得）。

#### [](#how-set-your-username-amp-email)如何设置您的用户名和电子邮件

打开您的cdmer（在这篇文章中，我将使用它）

```
   git config --global user.name jane tracy

```

用于设置电子邮件

```
   git config --global user.email janetracy00@gmail.com

```

查看您注册为的用户详细信息

```
   git config user.name
   git config user.email

```

#### [](#basic-command-controls)基本命令控制

*   创建文件夹：mkdir test
*   创建文件：触摸index.html style.css app.js
*   删除文件：rm index.html
*   要查看文件夹内部：ls（Ls）/ dir
*   要向上移动文件夹：cd ..
*   删除文件夹：rmdir test

##### [](#what-is-a-git-repository-git)什么是Git存储库（.git）

这是项目内部的文件夹，git在其中跟踪所有在文件中所做的更改，并建立历史记录。 在您的项目git repository文件夹中，您将看到一个.git文件夹。
注意：git存储库应位于项目文件夹的根目录，以便跟踪整个项目的更改。

```
   git init

```

#### [](#a-work-through-the-stages-in-git)通过git的各个阶段的工作

[![项目形象](https://res.cloudinary.com/practicaldev/image/fetch/s--5O8kCP7P--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/tX6CQMR/stages.png%2522git%2520staging%2522)](https://res.cloudinary.com/practicaldev/image/fetch/s--5O8kCP7P--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/tX6CQMR/stages.png%2522git%2520staging%2522)

#### [](#1-git-status)1）git状态

运行git status将显示您当前在暂存区域中的文件。

```
   git status

```

如果列出的文件名称为红色，则表示它们不在暂存区中。 但是，如果它们是绿色的，则它们处于过渡阶段并准备提交。

#### [](#2-git-add)2）git添加

运行git add可以在暂存区中移动文件。 这有助于您在提交之前先查看更改。
添加单个文件

```
   git add index.html

```

添加多个文件

```
   git add .

```

#### [](#3-git-rm)3）git rm

这有助于取消暂存区域中任何文件的暂存。

```
    git rm --cached index.html

```

#### [](#4-git-commit)4）git提交

运行此命令将在暂存区域中提交文件。 您还可以在提交中添加描述性消息，以在将来查看项目文件夹时为您提供帮助。

```
    git commit -m "added index and styles file"

```

#### [](#5-git-log-git-log-oneline)5）git log / git log \-\-oneline

git log可以帮助您查看提交历史记录。 每个提交都有唯一的ID，作者详细信息，日期，时间和提交消息。

```
    git log/ git log --oneline

```

git log \-\-oneline显示较短的版本（登录一行）。 它包括id和提交消息。

```
    ## get commits by a specific author
    git log --author jane

    ## get commits by message
    ## get commit that contains 'index'
    git log --all --grep index

    ## get commit in the last 2 weeks
    git log --since=2.weeks

```

#### [](#undoing-things)撤消事情

[![git撤消图像](https://res.cloudinary.com/practicaldev/image/fetch/s--r25nBnZ6--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/6PBVxpH/undoing.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--r25nBnZ6--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/6PBVxpH/undoing.png)

#### [](#6-git-checkout-commit)6）git checkout提交

这可以帮助您返回上一个提交。 但是所做的任何更改都不会保存，提交历史也不会被破坏。 这是只读阶段，这就是为什么它比还原或重置更安全的原因。 如果要创建一个新分支来保留创建的提交，则可以将\-c与switch命令一起使用。

```
    git switch -c <new-branch-name>
    ## undo this by:
    git switch -

```

#### [](#7-git-revert)7）git还原

它会反转提交所引起的更改，并使用反码创建一个新的提交，这比使用git reset更安全，而且它不会永久删除提交。

#### [](#8-git-reset)8）git重置

这不会删除提交，但是该提交将没有引用来访问它们的直接路径。 它更改提交历史记录。 可以使用 [git reflog](https://www.atlassian.com/git/tutorials/rewriting-history/git-reflo) 查找并还原此提交 。

```
   git checkout 91471e4
   git revert 91471e4
   git reset 91471e4

   ## Any pending work that was hanging out in the
   Staging Index and Working Directory will be lost.
   git reset 91471e4 --hard

   ##The Staging Index is reset to the state of the specified
     commit.Any changes that have been undone from the Staging
     Index are moved to the Working Directory.
     git reset 91471e4 --mixed

  ##The ref pointers are updated and the reset stops there. The
    Staging Index and the Working Directory are left untouched.
    git reset 91471e4 --soft

```

有关 [git reset](https://www.atlassian.com/git/tutorials/undoing-changes/git-reset) 及其工作方式的 更多详细信息 。

#### [](#9-git-branch)9）git分支

[![git分支](https://res.cloudinary.com/practicaldev/image/fetch/s--rsu5dj9---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/tXFpwjh/master-branch.png%2522)](https://res.cloudinary.com/practicaldev/image/fetch/s--rsu5dj9---/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/tXFpwjh/master-branch.png%2522)
如果您有新功能要尝试而不是提交给master分支，可以创建一个新分支，该分支复制master分支中的代码状态，然后添加新的提交，最后将其合并到master分支上。结束。 如果您对新功能不满意，则可以删除分支并返回到初始代码库。

```
    ##To create a branch
    git branch feature-1

    ##To switch to a branch
    git checkout feature-1
    ## To create and switch to a branch
    git checkout -b feature-a

    ## To check the branches
    git branch -a

    ## To delete a branch
    git branch -d feature-1
    ## To forcefully delete a branch even if it's unmerged
    git branch -D feature-1

    ## To rename a current branch
    ## Rename feature-1 to feature-a
    git branch -m feature-a

```

#### [](#10-git-merge)10）git合并

它将多个提交序列组合为一个示例，您可以使用它将feature\-1组合到master分支。

```
   git merge feature-1

```

当您有冲突时，当您在另一个分支上工作时，可能是有人在master分支中更改了代码。 在解决冲突之前，您无法手动进行合并。 阅读有关 [git merge的](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts) 更多信息[](https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts)

## [](#how-to-create-a-repository-in-github)如何在Github中创建存储库

#### [](#11-git-push)11）git push

##### [](#1-method-one)1）方法一

假设您有一个正在编写的项目，并且想要将其发布在github中进行协作或托管。 您可以进入github并创建一个新的存储库，复制仓库的URL并运行：

```
   ## To push it into the master branch
   git push <url link> master

```

当您要编辑代码并将其再次推送到github时。 您可以先通过以下方式为远程仓库创建别名：

```
   git remote add origin <url>
   git remote add origin https://github.com/muchirijane/git-learning.git

   ## To push it into the master branch
   git push origin master

```

#### [](#12-git-clone)12）git克隆

##### [](#2-method-two)2）方法二

在Github中创建存储库并将其克隆到您的计算机

```
   git clone <url>
   ## you have a url repo
   git clone https://github.com/muchirijane/git-learning.git

   ## To push it up in Github to the master branch
   git push origin master

   ## To see urls of the remote repositories
   git remote -v

```

## [](#collaborating-in-github)在Github中合作

#### [](#13-git-pull)13）git pull

##### [](#1-step-1)1）步骤1

这将从远程存储库（github repo）中获取并下载代码，并更新本地存储库以使其匹配。

```
   git pull origin master

```

##### [](#2-step-2)2）步骤2

创建一个新分支，添加您的代码并进行提交

```
   git checkout -b feature-2

```

##### [](#3-step-3)3）步骤3

将分支推送到github并创建请求请求

```
   git push origin feature-2

```

## [](#conclusion)结论

如果您想在技术领域升级，Git是非常有用且非常重要的。 我没有介绍过git或github命令，但这是可以帮助您入门的基础知识。 您可以查看youtube中的教程以了解更多信息。 将来，我将使用更高级的命令制作第2部分。
如果您想知道如何创建git别名，请使用此 [网站](https://www.freecodecamp.org/news/an-intro-to-git-aliases-a-faster-way-of-working-with-git-b1eda81c7747/) 。

## [](#bonus-section)🔥奖金部分

#### [](#forking-in-github)在Github中分叉

您可以使用此方法来执行第一个开源项目。
让我们通过贡献做榜样 [第一贡献](https://github.com/firstcontributions/first-contributions) 。

##### [](#1-step-one-fork-the-github-repository)1）第一步：分叉github仓库

通过单击页面顶部的fork按钮来完成此操作。 这将在您自己的Github帐户中创建存储库的副本。
[![从github分叉图像](https://res.cloudinary.com/practicaldev/image/fetch/s--V4UoCTos--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/tKKsG5p/Screenshot-156.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--V4UoCTos--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/tKKsG5p/Screenshot-156.png)

##### [](#2-step-two-clone-the-project)2）第二步：克隆项目

[![从github分叉图像](https://res.cloudinary.com/practicaldev/image/fetch/s--N7Zbvh_a--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/nRxH5yX/Screenshot-157.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--N7Zbvh_a--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/nRxH5yX/Screenshot-157.png)
单击克隆按钮，然后单击复制到剪贴板图标。
这将创建项目文件的副本到您的计算机。
附言：您创建一个“开源”文件夹，您要在其中复制项目文件。
打开您的终端或我的cdmer并运行

```
   git clone <url>
   ## Let's get the url for contributions repo
   git clone https://github.com/muchirijane/first-contributions.git

```

##### [](#3-run-git-status)3）运行git status

在开始编码之前，请运行git status，以确保项目文件中的所有内容均使用“ origin / master分支”进行了更新

```
   git status

```

##### [](#4-create-a-new-branch)4）创建一个新的分支

在这个面向初学者的开源软件中，您的任务是添加您的姓名。
分支机构名称将包含您的姓名

```
   git checkout -b <add-your-name-in-the-branch>
   ## My name to the branch
   git checkout -b add-jane-tracy

```

##### [](#5-make-your-contribution)5）做出自己的贡献

在这种情况下，需要将名称添加到contribution.md文件
中。运行git add，git commit并推送分支后，

```
   git add .
   ## commit the changes
   git commit -m "added jane muthoni to the contributors list"
   ## Let's push our branch
   git push origin <branch-name-you-created>
   git push origin add-jane-muthoni

```

##### [](#6-compare-and-pull-request)6）比较并提取请求

不！ 您还没有完成，请再执行一步。
将代码贡献给原始存储库。
点击比较并提取请求
[![github上的开源贡献](https://res.cloudinary.com/practicaldev/image/fetch/s--a89wRdbK--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/RcQGR20/Screenshot-158.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--a89wRdbK--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/RcQGR20/Screenshot-158.png)

##### [](#7-create-a-new-pull-request)7）创建一个新的拉取请求

[![github上的开源贡献](https://res.cloudinary.com/practicaldev/image/fetch/s--OKZdei5P--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/fNVK0Tz/Screenshot-159.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--OKZdei5P--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/fNVK0Tz/Screenshot-159.png)
您可以根据需要发表评论，然后单击“创建请求请求”按钮。

## [](#congratulation-on-your-first-open-source-contribution)祝贺您的第一个开源贡献

如果您已完成上述步骤，那么您的分支将被Github存储库的原始所有者合并到master分支。
[![github上的开源贡献](https://res.cloudinary.com/practicaldev/image/fetch/s--vUTGDYin--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/6yCY4Nr/Screenshot-160.png)](https://res.cloudinary.com/practicaldev/image/fetch/s--vUTGDYin--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://i.ibb.co/6yCY4Nr/Screenshot-160.png)

我为你感到骄傲。 这只是第一步。 使用 [第一笔捐款](https://github.com/firstcontributions/first-contributions) 发出您的第一个请求请求，并签出此 [列表](https://firstcontributions.github.io/#project-list) 以查看更多项目。
让我们也连接 [我的Github](https://github.com/muchirijane) 。 