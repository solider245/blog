---
title: git开发流程最佳实践
date: 2020-10-12 12:09:51
permalink: /pages/45f34c/
categories:
  - git
  - git文章转载
tags:
  - 
---
# [Git开发流程最佳实践](https://segmentfault.com/a/1190000017287490)

[git](https://segmentfault.com/t/git)

发布于 2018\-12\-06

# 写在前面

本文不多讲解Git命令的使用，旨在说明开发团队中如何使用git进行团队协作，release实践，如何进行hotfix等。这里推荐没用使用过Git的朋友参考廖雪峰老师的[教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)：

# GIT 工作流程概览

孔子曰：一图顶十言。下图概括了Git核心的工作流程，开发feature，修改bug，hotfix。

## 远程master分支

始终保存的是最近一次上线PROD的代码

## 远程develop分支

始终保存的是最新提交的代码

![图片描述](https://segmentfault.com/img/bVbkFLO?w=792&h=398)

## 编写feature，修改bug流程

1.  基于本地**develop**分支创建本地分支，命名规则`feature/<task-number>-short-description`，`bug/<task-number>-short-description`
2.  编写业务代码
3.  push本地分支到远程仓库
4.  创建pull request到远程分支**develop**
5.  经过code review并且approve之后，feature或bug分支被merge到远程分支develop
6.  通过QA测试
7.  远程**develop**分支会被发布到PROD环境正式上线
8.  上线后创建pull request，远程develop分支会merge到远程master分支

上述过程中，本地git操作使用的部分命令

```
git checkout -b feature/<task-number>-short-description
git checkout -b bug/<task-number>-short-description

git push origin feature/<task-number>-short-description
git push origin bug/<task-number>-short-description
```

创建pull request通常是通过git代码网站进行操作。

## hotfix流程

1.  基于本地**master**分支创建本地分支，命名规则`hotfix/<task-number>-short-description`
2.  编写业务代码
3.  push本地分支到远程仓库
4.  创建pull request到远程分支**master**
5.  经过code review并且approve之后，hotfix分支被merge到远程分支**master**
6.  通过QA测试
7.  远程**master**分支会被发布到PROD环境正式上线
8.  上线后，远程develop需要同步远程master分支的改动

# git命令拾遗

## clone远程仓库中某一个具体分支

```
git clone <url> --branch <branch name> --single-branch [folder]
```

只clone master分支到当前路径（省略了folder）：

```
git clone https://xxx.com/common.git --branch master --single-branch
```

此时使用`git branch -r`可以看到远程分支：

```
origin/HEAD -> origin/master
origin/master
```

说明我们只clone了master分支到本地仓库。

## origin

当git clone命令执行完成后，origin就存放了远程仓库地址。在命令中使用origin，就指代远程仓库。

## 查看本地分支对应的远程分支

```
git branch -vv
```

## 基于远程分支创建本地分支

通过这种方式创建的本地分支，自动把该远程分支设置为本地分支的upstream，如此一来，`git pull`，`git push`操作时不再需要指明远程分支。

```
git checkout -b <local-branch-name> --track origin/<remote-branch-name>
```

## 设置本地分支的远程upstream分支

### 方式一：\-\-set\-upstream\-to

使用`git checkout -b <branch-name>`创建的本地分支，可以显式指定其对应的远程分支。

```
git branch --set-upstream-to origin/<remote-branch-name>
```

### 方式二：git push \-u

在push本地分支到远程仓库时，顺便指定本地分支的upstream分支。

```
git push -u origin <local-branch-name>
```

branch\-name可以省略，默认为当前分支。

阅读 1.5k发布于 2018\-12\-06