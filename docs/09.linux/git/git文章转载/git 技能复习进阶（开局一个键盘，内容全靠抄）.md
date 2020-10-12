---
title: git 技能复习进阶（开局一个键盘，内容全靠抄）
date: 2020-10-12 12:09:51
permalink: /pages/fa1d4f/
categories:
  - git
  - git文章转载
tags:
  - 
---
贴个车 [http://web.mit.edu/~mkgray/project/silk/root/afs/sipb/project/git/git\-doc/](http://web.mit.edu/~mkgray/project/silk/root/afs/sipb/project/git/git-doc/)

# 常用操作：

```
git add . 或某个文件，某些文件
git commit -m 'fix ' 提交信息
git status 查看当前版本库状态
git diff 文件 1 文件 2   对文件进行比较（也可在版本之间进行比较，后面文件均替换为版本号）
git push 推送
git pull 拉取
git merge 合并指定分支到当前分支
git checkout +文件，表示  撤销对某文件的修改; + 分支，表示切换分支
git rm 文件  删除某文件
git clone 克隆
git checkout -b +分支，表示创建新分支（非 master 分支）
git branch 查看当前分支； + -a 表示查看所有分支
git branch -d +分支 删除某分支

```

# 日志：

> 日志查询：
>
> > git log：

```
		查看某分支当前的版本号

```

> 操作日志查询：

```
		可以查看某分支自己之前执行过什么操作。

```

> > git reflog：

# 工作区及暂存区

```
	工作区就是存有.git 文件夹的父文件夹，暂存区是在.git 文件夹里的区域。
我们执行的 git add [.]就是把文件从工作区添加到了暂存区(stage)中，而 git commit 就是			把暂存区里的东西提交到当前的本地分支比如 test 分支，工作区就变干净了。

```

# 远程仓库

```
添加远程仓库 git remote add origin + 远程 git 地址 (例如 git@github.com:1900/reviewgit.git),

```

# 分支管理

```
创建一个分支就是创建一个指针，该指针指向 master 的某个节点，另外会有 head 指针来负责分支切换。具体指令在文章起始部分。

```

# 冲突解决

```
黄金准则是：有冲突解决冲突，而不要直接就回滚，因为代码库不是你一个人在用！

操作就是，打开冲突文件，搜索 >>>>>标识确定冲突部分，删除不想要的内容，删除>>>>  及 ====，然后 git add 文件，提交。

```

# bug 分支

```
并发的处理了两个问题，问题 1 需要尽快提交解决线上问题，问题 2 还没搞定，这个时候可以利用 stash 功能来暂存。git stash,接着解决问题 1，在当前分支创建一个临时分支，然后修改问题，并提交。

```

暂时先这么多吧，待续。