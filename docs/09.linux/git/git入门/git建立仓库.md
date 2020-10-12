---
title: git建立仓库
date: 2020-10-12 12:09:51
permalink: /pages/6d1786/
categories:
  - git
  - git入门
tags:
  - 
---
# 建立资料库

[git init](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-init) [git clone](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone) [git配置](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config)

本教程概述了如何在Git版本控制下设置存储库（repo）。 该资源将引导您为新项目或现有项目初始化Git存储库。 下面包括本地创建和从远程存储库克隆的存储库的工作流示例。 本指南假定您基本熟悉命令行界面。

本指南涵盖的主要内容是：

*   初始化一个新的Git仓库
*   克隆现有的Git存储库
*   将文件的修改版本提交到仓库
*   配置Git仓库进行远程协作
*   通用Git版本控制命令

在本模块结束之前，您应该能够创建Git存储库，使用常见的Git命令，提交修改的文件，查看项目的历史记录以及配置与Git托管服务（Bitbucket）的连接。

## 什么是Git存储库？

一个 [Git仓库](http://bitbucket.org/code-repository) 是项目的一个虚拟存储。 它允许您保存代码的版本，您可以在需要时访问它们。

## 初始化一个新的仓库：git init

要创建一个新的仓库，您将使用 `git init` 命令。 `git init` 是您在新存储库的初始设置期间使用的一次性命令。 执行此命令将 `.git` 在当前工作目录中 创建一个新的 子目录。 这还将创建一个新的master分支。

### 使用新的git存储库对现有项目进行版本控制

本示例假定您已经具有要在其中创建存储库的现有项目文件夹。 您将首先 `cd` 进入根项目文件夹，然后执行 `git init` 命令。

```
cd /path/to/your/existing/code
git init
```

指向 `git init` 现有项目目录将执行与上述相同的初始化设置，但范围仅限于该项目目录。

```
git init <project directory>
```

访问 [git init](http://www.atlassian.com/git/tutorials/setting-up-a-repository/git-init) 页面以获取有关的更详细的资源 `git init` 。

## 克隆现有存储库：git clone

如果已经在中央存储库中设置了项目，则clone命令是用户获取本地开发克隆的最常用方法。 像一样 `git init` ，克隆通常是一次性操作。 开发人员获得工作副本后，所有 [版本控制](http://bitbucket.org/version-control-software) 操作都将通过其本地存储库进行管理。

```
git clone <repo url>
```

`git clone` 用于创建远程存储库的副本或克隆。 您传递 `git clone` 一个存储库URL。 Git支持一些不同的网络协议和相应的URL格式。 在此示例中，我们将使用Git SSH协议。 Git SSH URL遵循以下模板： `git@HOSTNAME:USERNAME/REPONAME.git`

一个Git SSH URL示例是： `git@bitbucket.org:rhyolight/javascript-data-store.git` 模板值匹配：

*   `` `HOSTNAME: bitbucket.org` ``
*   `` `USERNAME: rhyolight` ``
*   `` `REPONAME: javascript-data-store` ``

执行后，master分支上的远程回购文件的最新版本将被下拉并添加到新文件夹中。 在这种情况下，新文件夹将以REPONAME命名 `javascript-data-store` 。 该文件夹将包含远程存储库的完整历史记录和一个新创建的master分支。

有关 `git clone` 用法和受支持的Git URL格式的 更多文档 ，请访问 [git clone Page](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone) 。

## 将更改保存到存储库：git add和git commit

现在，您已克隆或初始化了存储库，您可以提交文件版本更改。 以下示例假定您已在处建立了一个项目 `/path/to/project` 。 本示例中采取的步骤是：

*   将目录更改为 `/path/to/project`
*   创建一个 `CommitTest.txt` 包含内容 的新文件 〜“ git教程的测试内容”〜
*   git添加 `CommitTest.txt` 到存储库暂存区
*   创建一个新的提交，并带有一条消息，描述该提交中已完成的工作

```
cd /path/to/project
echo "test content for git tutorial" >> CommitTest.txt
git add CommitTest.txt
git commit -m "added CommitTest.txt to the repo"
```

执行 `CommitTest.txt` 完 此示例后，您的存储库现在将已 添加到历史记录中，并将跟踪对该文件的将来更新。

此示例引入了两个附加的git命令： `add` 和 `commit` 。 这是一个非常有限的示例，但是在 [git add](https://www.atlassian.com/git/tutorials/saving-changes) 和 [git commit](https://www.atlassian.com/git/tutorials/saving-changes#git-commit) 页面 上都更深入地介绍了这两个命令 。 `git add` 该 `--all` 选项的 另一个常见用例 是 。 执行 `git add --all` 将获取回购中任何已更改和未跟踪的文件，并将它们添加到回购中并更新回购的工作树。

## 仓库到仓库协作：git push

重要的是要了解，Git的“工作副本”概念与通过从SVN存储库中签出源代码而获得的工作副本有很大不同。 与SVN不同，Git在工作副本和中央存储库之间没有区别，它们都是成熟的 [Git存储库](http://bitbucket.org/code-repository) 。

这使得与Git的协作与SVN的协作从根本上不同。 SVN取决于中央存储库和工作副本之间的关系，而Git的协作模型则基于存储库到存储库的交互。 您无需将工作副本检入SVN的中央存储库中，而是将提交从一个存储库推入或拉入另一个存储库。

当然，没有什么可以阻止您赋予某些Git仓库特殊的意义。 例如，只需将一个Git存储库指定为“中央”存储库，就可以使用Git复制集中式工作流程。 这是通过约定完成的，而不是硬连接到VCS本身。

### 裸仓库与克隆仓库

如果您 `git clone` 在前面的“初始化新存储库”部分中使用过来设置本地存储库，则您的存储库已配置为进行远程协作。 `git clone` 会自动使用指向您克隆它的Git URL的远程配置您的仓库。 这意味着，一旦您对文件进行了更改并将其提交，就可以 `git push` 对远程存储库 进行 这些更改。

如果您 `git init` 以前进行新的存储库，则没有远程存储库可将更改推送到。 初始化新存储库时，常见的模式是转到托管的Git服务（如Bitbucket）并在那里创建存储库。 该服务将提供一个Git URL，您可以将该URL添加到本地Git存储库和 `git push` 托管 仓库中 。 使用所选服务创建远程仓库后，您将需要使用映射更新本地仓库。 我们将在下面的“配置和设置”指南中讨论此过程。

如果您希望托管自己的远程存储库，则需要设置“裸存储库”。 无论 `git init` 和 `git clone` 接受 `--bare` 的说法。 裸仓库最常见的用例是创建一个远程中央Git存储库

## 配置和设置：git config

设置远程存储库后，您需要将远程存储库URL添加到local `git config` ，并为本地分支机构设置上游分支。 该 `git remote` 命令提供了这样的实用程序。

```
git remote add <remote_name> <remote_repo_url>
```

此命令会将远程存储库映射 `<remote_repo_url>` 到的本地 仓库中 的ref `<remote_name>` 。 映射远程仓库后，可以将本地分支推送到该仓库。

```
git push -u <remote_name> <local_branch_name>
```

此命令会将本地存储库分支推 `<local_branc_name>` 送到位于的远程存储库下 `<remote_name>` 。

有关更多详细信息 `git remote` ，请参阅 [`Git remote page`](https://www.atlassian.com/git/tutorials/syncing#git-remote) 。

除了配置远程回购URL，您可能还需要设置全局Git配置选项，例如用户名或电子邮件。 该 `git config` 命令使您可以从命令行配置Git安装（或单个存储库）。 该命令可以定义从用户信息到首选项，再到存储库行为的所有内容。 下面列出了几个常见的配置选项。

Git将配置选项存储在三个单独的文件中，这使您可以将选项的作用域限定为单个存储库（本地），用户（全局）或整个系统（系统）：

*   本地： `<repo>/.git/config` –特定于存储库的设置。
*   全局： `/.gitconfig` –用户特定的设置。 这是使用\-\-global标志设置的选项的存储位置。
*   系统： `$(prefix)/etc/gitconfig` –系统范围的设置。

定义要用于当前存储库中所有提交的作者名称。 通常，您将需要使用该 `--global` 标志来为当前用户设置配置选项。

```
git config --global user.name <name>
```

定义当前用户用于所有提交的作者姓名。

添加 `--local` 选项或根本不通过配置级别的选项，将为 `user.name` 当前本地存储库设置。

```
git config --local user.email <email>
```

定义要用于当前用户所有提交的作者电子邮件。

```
git config --global alias.<alias-name> <git-command>
```

为Git命令创建快捷方式。 这是一个强大的实用程序，可为常用的git命令创建自定义快捷方式。 一个简单的例子是：

```
git config --global alias.ci commit
```

这将创建一个 `ci` 命令，您可以将其作为的快捷方式执行 `git commit` 。 要了解有关git别名的更多信息，请访问 [`git config`页面](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config) 。

```
git config --system core.editor <editor>
```

定义命令所使用的文本编辑器，例如 `git commit` 当前计算机上的所有用户。 该 `<editor>` 参数应该是命令，该命令发射所需的编辑器（例如，六）。 本示例介绍了该 `--system` 选项。 该 `--system` 选项将设置整个系统的配置，即机器上的所有用户和存储库。 有关配置级别的更多详细信息，请访问 [git config页面](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config) 。

```
git config --global --edit
```

在文本编辑器中打开全局配置文件以进行手动编辑。 可以在 [Git config页面](http://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config) 上找到有关如何配置文本编辑器以供git使用的深入指南 。

### 讨论区

所有配置选项都存储在纯文本文件中，因此该 `git config` 命令实际上只是一个方便的命令行界面。 通常，您只需要在首次开始在新的开发机器上工作时配置Git安装，并且在几乎所有情况下，都需要使用该 `--global` 标志。 一个重要的例外是覆盖作者的电子邮件地址。 您可能希望为个人和开放源存储库设置个人电子邮件地址，为与工作相关的存储库设置专业电子邮件地址。

Git将配置选项存储在三个单独的文件中，这使您可以将选项的作用域限定于单个存储库，用户或整个系统：

*   `<repo>/.git/config` –特定于存储库的设置。
*   `~/.gitconfig` –用户特定的设置。 这是使用\-\-global标志设置的选项的存储位置。
*   `$(prefix)/etc/gitconfig` –系统范围的设置。

当这些文件中的选项发生冲突时，本地设置将覆盖用户设置，而用户设置将覆盖系统范围内的用户设置。 如果打开这些文件中的任何一个，将会看到类似以下的内容：

```
[user] name = John Smith email = john@example.com [alias] st = status co = checkout br = branch up = rebase ci = commit [core] editor = vim
```

您可以手动编辑这些值，使其效果与完全相同 `git config` 。

### 例

安装Git之后，您要做的第一件事就是告诉它您的名字/电子邮件并自定义一些默认设置。 典型的初始配置可能类似于以下内容：

告诉吉特你是谁 `git config`

```
git --global user.name "John Smith" git config --global user.email john@example.com
```

选择您喜欢的文本编辑器

```
git config --global core.editor vim
```

添加一些类似于SVN的别名

```
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.up rebase
git config --global alias.ci commit
```

这将产生上一部分的 `~ /.gitconfig` 文件。 在 [git config页面](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config) 上更深入地了解 [git config](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config) 。

## 摘要

在这里，我们演示了如何使用两种方法创建git存储库： [git init](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-init) 和 [git clone](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone) 。 本指南可用于管理软件源代码或其他需要版本控制的内容。 还介绍了 [Git add](https://www.atlassian.com/git/tutorials/saving-changes) ， [git commit](https://www.atlassian.com/git/tutorials/saving-changes#git-commit) ， [git push](https://www.atlassian.com/git/tutorials/syncing#git-push) 和 [git remote](https://www.atlassian.com/git/tutorials/syncing#git-remote) 并在较高级别上加以利用。

阅读我们的 [指南，了解哪种代码存储库系统适合您的团队](http://bitbucket.org/code-repository) ！

准备学习Git吗？

试试这个交互式教程。

[现在就开始](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud)