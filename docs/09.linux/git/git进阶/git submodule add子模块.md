---
title: git submodule add子模块
date: 2020-10-12 12:09:51
permalink: /pages/ccd6d8/
categories:
  - git
  - git进阶
tags:
  - 
---
# Git子模块

[返回目录](https://www.atlassian.com/git/articles)

Git子模块允许您将git存储库保留为另一个git存储库的子目录。 Git子模块只是在特定时间快照上对另一个存储库的引用。 Git子模块使Git存储库能够合并和跟踪外部代码的版本历史。

## 什么是git子模块？

 通常，代码存储库将取决于外部代码。 可以通过几种不同的方式合并此外部代码。 外部代码可以直接复制并粘贴到主存储库中。 这种方法的缺点是丢失了对外部存储库的任何上游更改。 合并外部代码的另一种方法是使用诸如Ruby Gems或NPM之类的语言的程序包管理系统。 这种方法的缺点是需要在所有部署原始代码的地方进行安装和版本管理。 这两种建议的合并方法均无法跟踪外部存储库的编辑和更改。

git子模块是主机git储存库中的一条记录，指向另一个外部储存库中的特定提交。 子模块非常静态，仅跟踪特定的提交。 子模块不跟踪git ref或分支，并且在更新主机存储库时不会自动更新。 将子模块添加到存储库时，将创建一个新的.gitmodules文件。 .gitmodules文件包含有关子模块项目的URL与本地目录之间的映射的元数据。 如果主机存储库具有多个子模块，则.gitmodules文件将为每个子模块都有一个条目。

## 什么时候应该使用git子模块？

如果需要对外部依赖项进行严格的版本管理，则可以使用git子模块。 以下是git子模块的一些最佳用例。

*    当外部组件或子项目的更改速度太快或即将发生的更改将破坏API时，出于安全考虑，您可以将代码锁定为特定的提交。
*    当您有一个不经常更新的组件并且想要将其作为供应商依赖项进行跟踪时。
*    当您将项目的一部分委派给第三方，并且想要在特定时间或发布时集成他们的工作。 同样，当更新不是太频繁时，这种方法也适用。

## git子模块的常用命令

### 添加git子模块

将 `git submodule add` 用于一个新的子模块添加到现有的存储库。 以下是创建一个空仓库和浏览git子模块的示例。

```
$ mkdir git-submodule-demo$ cd git-submodule-demo/$ git initInitialized empty Git repository in /Users/atlassian/git-submodule-demo/.git/
```

此命令序列将创建一个新目录 `git-submodule-demo` ，输入该目录，并将其初始化为新的存储库。 接下来，我们将为这个新的新仓库添加一个子模块。

```
$ git submodule add https://bitbucket.org/jaredw/awesomelibraryCloning into '/Users/atlassian/git-submodule-demo/awesomelibrary'...remote: Counting objects: 8, done.remote: Compressing objects: 100% (6/6), done.remote: Total 8 (delta 1), reused 0 (delta 0)Unpacking objects: 100% (8/8), done.
```

该 `git submodule add` 命令采用指向git存储库的URL参数。 在这里，我们添加了 `awesomelibrary` 作为子模块。 Git将立即克隆子模块。 现在，我们可以使用 `git status` ... 查看存储库的当前状态 。

```
$ git statusOn branch masterNo commits yetChanges to be committed:  (use "git rm --cached <file>..." to unstage) new file:   .gitmodules new file:   awesomelibrary
```

现在，存储库 `.gitmodules` 和 `awesomelibrary` 目录中 有两个新文件 。 查看内容 `.gitmodules` 显示新的子模块映射

```
[submodule "awesomelibrary"] path = awesomelibrary url = https://bitbucket.org/jaredw/awesomelibrary
```

现在可以使用 [git add](https://www.atlassian.com/git/tutorials/saving-changes) 和 [git commit](https://www.atlassian.com/git/tutorials/saving-changes/git-commit) [将](https://www.atlassian.com/git/tutorials/saving-changes) 这些文件提交到原始存储库 。

```
$ git add .gitmodules awesomelibrary/$ git commit -m "added submodule"[master (root-commit) d5002d0] added submodule 2 files changed, 4 insertions(+) create mode 100644 .gitmodules create mode 160000 awesomelibrary
```

### 克隆git子模块

当使用 [git clone克隆](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone) 具有子模块的项目时 ，它将创建包含子模块但其中没有文件的目录。 在运行另外两个命令之前，不会创建子模块文件。 `git submodule init` 将 `.git/config` 使用 `.gitmodules` 文件中 的映射 更新本地 。 `git submodule update` 然后将从子模块项目中获取所有数据，并在父项目中检出映射的提交。

有一个 `-recursive` 选项可以传递给 `git clone` 此参数，该参数将告诉git clone也可以初始化和更新任何子模块。 使用\-recursive选项等效于执行：

```
git clone /url/to/repo/with/submodulesgit submodule initgit submodule update
```

### Git子模块Init

的默认行为 `git submodule init` 是将映射从 `.gitmodules` 文件 复制 到本地 `./.git/config` 文件。 这似乎是多余的，并导致质疑的 `git submodule init` 用处。 `git submodule init` 具有扩展行为，其中它接受显式模块名称的列表。 这使工作流仅激活在存储库上工作所需的特定子模块。 如果存储库中有许多子模块，但是不需要将其全部拿来进行工作，这将很有帮助。

### 子模块工作流程

子模块在父存储库中正确初始化和更新后，就可以像独立存储库一样使用它们。 这意味着子模块具有自己的分支和历史记录。 对子模块进行更改时，重要的是发布子模块更改，然后更新对子模块的父存储库引用。 让我们继续该 `awesomelibrary` 示例并进行一些更改：

```
$ cd awesomelibrary/$ git checkout -b new_awesomeSwitched to a new branch 'new_awesome'$ echo "new awesome file" > new_awesome.txt$ git statusOn branch new_awesomeUntracked files:  (use "git add <file>..." to include in what will be committed) new_awesome.txtnothing added to commit but untracked files present (use "git add" to track)$ git add new_awesome.txt$ git commit -m "added new awesome textfile"[new_awesome 0567ce8] added new awesome textfile 1 file changed, 1 insertion(+) create mode 100644 new_awesome.txt$ git branch  master* new_awesome
```

在这里，我们将目录更改为awesomelibrary子模块。 我们创建了一个 `new_awesome.txt` 包含一些内容 的新文本文件 ，并将此新文件添加并提交到了子模块。 现在，让我们将目录更改回父存储库，并查看父存储库的当前状态。

```
$ cd ..$ git statusOn branch masterChanges not staged for commit:  (use "git add <file>..." to update what will be committed)  (use "git checkout -- <file>..." to discard changes in working directory) modified:   awesomelibrary (new commits)no changes added to commit (use "git add" and/or "git commit -a")
```

执行 `git status` 表明我们父存储库知道对子 `awesomelibrary` 模块 的新提交 。 它没有详细介绍特定的更新，因为这是子模块存储库的职责。 父存储库仅与将子模块固定到提交有关。 现在，我们可以通过 在子模块上 执行 `git add` 和 `git commit` 来 再次更新父存储库 。 这将使所有内容都与本地内容保持良好状态。 如果您在团队环境中工作，则必须先 `git push` 更新子模块， 然后再 更新父存储库， 这一点至关重要 。

使用子模块时，常见的混乱和错误模式是忘记为远程用户推送更新。 如果我们重新审视 `awesomelibrary` 我们所做的工作，我们仅将更新推送到父存储库。 另一位开发人员将去拉最新的父存储库，这将指向 `awesomelibrary` 他们无法拉出 的提交， 因为我们忘记了推子模块。 这将破坏远程开发人员的本地存储库。 为了避免这种故障情况，请确保始终提交并推送子模块和父存储库。

## 结论

Git子模块是将git用作外部依赖项管理工具的强大方法。 在使用git子模块之前，请权衡其优缺点，因为它们是高级功能，可能需要学习曲线才能供团队成员采用。