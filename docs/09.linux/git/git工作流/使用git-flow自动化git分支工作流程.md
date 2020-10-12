---
title: 使用git-flow自动化git分支工作流程
date: 2020-10-12 12:09:51
permalink: /pages/481e1c/
categories:
  - git
  - git工作流
tags:
  - 
---
[Vincent Driessen的“ git flow”分支模型](http://nvie.com/posts/a-successful-git-branching-model/) 是git分支和发行版管理工作流，可帮助开发人员跟踪大型软件项目中的功能，修补程序和发行版。 这个工作流程有很多命令可以键入和记住，因此还有 [git子命令](https://github.com/nvie/gitflow) 的 [git\-flow库，](https://github.com/nvie/gitflow) 可以帮助自动化流程的某些部分，从而使流程更容易使用。

![“ git flow”分支模型](https://jeffkreeftmeijer.com/git-flow/git-flow.png)

之后 [安装的git流](https://github.com/nvie/gitflow/wiki/Installation) （ `brew install git-flow` ），你就可以开始使用存储库中的混帐流通过使用它的 `init` 命令。 您可以在现有项目中使用它，但让我们开始一个新的存储库：

$ git flow init
Initialized empty Git repository in ~/project/.git/
No branches exist yet. Base branches must be created now.
Branch name for production releases: \[master\]
Branch name for "next release" development: \[develop\]

How to name your supporting branch prefixes?
Feature branches? \[feature/\]
Release branches? \[release/\]
Hotfix branches? \[hotfix/\]
Support branches? \[support/\]
Version tag prefix? \[\]

git\-flow是现有git命令的包装，因此该 `init` 命令除了为您创建分支外，不会更改存储库中的任何内容。 如果您不想再使用git\-flow，则无需更改或删除任何内容，只需停止使用git\-flow命令即可。

如果您 `git branch` 在设置后 运行 ，则会注意到您已从master分支切换到名为的新分支 `develop` 。

$ git branch
\* develop
  master

该 `develop` 分支是将执行大部分工作的默认分支，并且该 `master` 分支跟踪生产就绪代码。

## 功能分支

git\-flow通过使用功能分支，可以轻松地同时处理多个功能。 首先，使用 `feature start` 新功能的名称（在本例中为“身份验证”）：

$ git flow feature start authentication
Switched to a new branch 'feature/authentication'

Summary of actions:
\- A new branch 'feature/authentication' was created, based on 'develop'
\- You are now on branch 'feature/authentication'

Now, start committing on your feature. When done, use:

     git flow feature finish authentication

已创建功能分支，您将自动切换到该分支。 像往常一样使用git时，在此分支中实现功能。 完成后，请使用 `feature finish` ：

$ git flow feature finish authentication
Switched to branch 'develop'
Updating 9060376..00bafe4
Fast\-forward
 authentication.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 authentication.txt
Deleted branch feature/authentication (was 00bafe4).

Summary of actions:
\- The feature branch 'feature/authentication' was merged into 'develop'
\- Feature branch 'feature/authentication' has been removed
\- You are now on branch 'develop'

您的功能分支将被合并，您将被带回到 `develop` 分支。 在内部，git\-flow用于 `git merge --no-ff feature/authentication` 确保您在删除功能分支之前不会丢失任何历史信息。

## 版本发布

如果需要标记和版本控制的发行版，可以在准备将新版本部署到生产环境时使用git\-flow的发行版分支来启动新分支。

像git\-flow中的其他所有内容一样，如果您不想使用发布分支，则不必使用。 宁愿手动 `git merge --no-ff develop` 进入母版而不进行标记？ 没问题。 但是，如果您使用的是版本化的API或库，则发行分支可能真的很有用，它们的工作方式完全符合您的期望：

$ git flow release start 0.1.0
Switched to a new branch 'release/0.1.0'

Summary of actions:
\- A new branch 'release/0.1.0' was created, based on 'develop'
\- You are now on branch 'release/0.1.0'

Follow\-up actions:
\- Bump the version number now!
\- Start committing last\-minute fixes in preparing your release
\- When done, run:

     git flow release finish '0.1.0'

突出版本号，并在release分支中执行发布项目所需的一切。 我个人不会在最后一刻进行任何修复，但是如果您这样做，git\-flow将确保所有内容都正确地合并到 `master` 和中 `develop` 。 然后，完成发行：

$ git flow release finish 0.1.0
Switched to branch 'master'
Merge made by the 'recursive' strategy.
 authentication.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 authentication.txt
Deleted branch release/0.1.0 (was 1b26f7c).

Summary of actions:
\- Latest objects have been fetched from 'origin'
\- Release branch has been merged into 'master'
\- The release was tagged '0.1.0'
\- Release branch has been back\-merged into 'develop'
\- Release branch 'release/0.1.0' has been deleted

繁荣。 git\-flow从源中拉出，将release分支合并到master，标记发布，然后在删除release分支之前将所有内容重新合并回develop。

您仍然是master上的人，因此您可以在返回 `develop` 分支 之前进行部署 ，git\-flow确保确保随着中的发行版更新而更新 `master` 。

## 修补生产代码

因为您可以使 `master` 分支始终与生产环境中的代码 保持 同步，所以您可以快速解决生产环境中的所有问题。

例如，如果您的资产未在生产中加载，则将回滚部署并启动修补程序分支：

$ git flow hotfix start assets
Switched to a new branch 'hotfix/assets'

Summary of actions:
\- A new branch 'hotfix/assets' was created, based on 'master'
\- You are now on branch 'hotfix/assets'

Follow\-up actions:
\- Bump the version number now!
\- Start committing your hot fixes
\- When done, run:

     git flow hotfix finish 'assets'

修补程序分支与发行分支很像，只是它们基于master而不是develop。 您将自动切换到新的修补程序分支，以便可以开始解决问题并提高次要版本号。 完成后， `hotfix finish` ：

$ git flow hotfix finish assets
Switched to branch 'master'
Merge made by the 'recursive' strategy.
 assets.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 assets.txt
Switched to branch 'develop'
Merge made by the 'recursive' strategy.
 assets.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 assets.txt
Deleted branch hotfix/assets (was 08edb94).

Summary of actions:
\- Latest objects have been fetched from 'origin'
\- Hotfix branch has been merged into 'master'
\- The hotfix was tagged '0.1.1'
\- Hotfix branch has been back\-merged into 'develop'
\- Hotfix branch 'hotfix/assets' has been deleted

就像完成发行分支一样，修补程序分支也合并到 `master` 和中 `develop` 。 该版本已标记，并且修复程序分支已删除。

## 为什么不使用git\-flow？

如果您 [不执行版本发布](http://scottchacon.com/2011/08/31/github-flow.html) ，则Vincent的git工作流程和git\-flow库可能不适合您。 但是，如果您处理的是 [语义版本化](http://semver.org) 的项目 （例如Rubygem或版本化的API），则git\-flow将为您提供几个简单的命令，这些命令将在幕后进行大量工作，使功能得以实现，并发布新版本和修复错误要容易得多。 好吧，至少在git方面。