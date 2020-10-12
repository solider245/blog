---
title: git从青铜到王者，白银篇(版本控制)
date: 2020-10-12 12:09:51
permalink: /pages/aaa7d0/
categories:
  - git
  - git实战
tags:
  - 
---
# 序言
通过git青铜篇的学习，大家对Git已经有了基本的了解，会安装、更新、卸载以及连接github并且从github下载文件到本地了。
接下来我们就要开始进入git白银篇——版本控制。

# 版本控制的主要内容

## 了解工作区、暂存区、本地仓库、远端仓库的概念
熟悉 git add .\git commit -m 'message'\git push\git pull等命令

要了解版本控制，先要明白三个概念.

* 工作区
* 暂存区
* 本地仓库

![20200627173416_52eaaa6763300753a3a4de9c7a0a9b08.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200627173416_52eaaa6763300753a3a4de9c7a0a9b08.png)

如上图所示。那么怎么理解工作区、暂存区、本地仓库这个概念呢，我是这样理解的。
大家都知道，Git 是Linux发明的，那么假如Git是厨师王刚发明的呢？那么工作区就会叫做锅，本地仓库就是餐桌，暂存区就是餐盘。
我们锅里炒的菜就是文件，文件在工作区翻炒，起锅之后，你不能直接丢到餐桌上，要先找个餐盘装一下，这个暂存区就是餐盘，装好盘之后就可以放到本地仓库了。

## 工作区、暂存区、本地仓库的命令提交步骤

模拟下，就是以下代码：

```shell
touch chaocai.txt # 创建一个文件/开始炒菜
git add . # 将文件提交到暂存区/炒完菜了，装盘
git commit -m '提交的内容' #将文件提交到仓库 /上菜了，顺便点评下菜
```

![20200629164956_ca02865f4170ead85162ff771b606d5d.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200629164956_ca02865f4170ead85162ff771b606d5d.png)

## `git status`的作用 

具体操作如上所示。
有时候我们一边炒菜，一边还在同时熬汤，我们想不起到底哪个菜有没有装盘，这个时候我们使用`git status`来查询.

![20200629171412_805374c3214290d54b1847a51dfa9ba9.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200629171412_805374c3214290d54b1847a51dfa9ba9.png)
(这里如果无法显示中文名文件，请改成英文名)
如上图所示。

## `git log`的作用

有时候你忘记了自己提交了太多，你可以使用`git log`来查询你的每次提交
![20200629171653_07fe1cceface50d984d75b8e60b63c94.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200629171653_07fe1cceface50d984d75b8e60b63c94.png)
如上图所示。

## 提交时遇到中文名文件乱码的处理方式
(如果文件名中文乱码，请在终端输入以下代码)
```shell
git config --global core.quotepath false
```
## 免暂存，一步提交的办法
另外，如果你只对文件修改而没有新增文件的话，那么你可以使用这个命令:

```shell
git commit -am '我只修改了文件，没增加文件'
```
这个命令可以让你少使用一步`git add .`命令，直接提交.
继续用做菜来打比方的话，类似这张图.
![20200630065215_f0448596b4356e76e137e00114848e0d.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200630065215_f0448596b4356e76e137e00114848e0d.png)
也就是说，等于盘桌一体化了。

# 本地仓库与远程仓库的交互

![20200630192812_9e9f7a791197cea192be83e4482dd8e9.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200630192812_9e9f7a791197cea192be83e4482dd8e9.png)


## 查询远程仓库链接

相信到这个时候你估计早就忘记了你的远程仓库的地址是多少了，所以，先使用以下命令，查询一下当前仓库的远程分支链接是多少。
```shell
git remote -v #查询远程仓库链接
```
如果你忘记了remote的主要作用，也可以使用`git remote -help`来获得帮助。

## 关联远程仓库地址

如果没有远程链接地址的话，这个时候就应该将本地仓库关联远程仓库.
```shell
git remote add origin https://gitee.com/solider245/myproject #关联远程仓库
```
一般来说，这个时候就应该开始推送了，不过由于经常会出现远程仓库文件内容比本地内容更新（比如你朋友/同事先更新了远程仓库）的情况，所以我们一般来说要先把远程仓库拉取到本地先合并一下.
## 更新本地仓库

```shell
git pull origin master
```
## 将本地仓库推送到远程仓库

```shell 
git push origin master
```

熟悉以上操作之后，你基本上算是可以算一个git白银选手了。当然，光会操作还不行，这个时候还有一些比较容易出现的常见问题也需要会解决，如果你是纯新手的话，即使解决不了，至少心里有个数也是很好的。

# 版本回退`git reset `,`git reset --hard`,`git revert`的用法

![20200701041452_00e1ba40e559eedb250e3a018c5fa028.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200701041452_00e1ba40e559eedb250e3a018c5fa028.png)
我们假设有五道菜，四菜一汤。
每上一道菜，我们就有一次暂存和提交。
![20200701041538_99c9970f5f204f2a68fd63a6562aefc7.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200701041538_99c9970f5f204f2a68fd63a6562aefc7.png)
如上图所示。

场景一：
假设我们发现青椒肉丝后面的菜全部都上错了，需要重新做，那这个时候我们就需要使用`git reset --hard <commit-id>`来重置到青椒肉丝这一步，后面的菜全部都会删除。
场景二：
假设我们发现，青椒肉丝后面的菜都没问题，只是上错了菜名，也即我们需要保留菜，在重新修改之后再重新提交，这个时候我们就使用：
`git reset <commit-id>`来进行重置。
场景三：
假设我们的客人只是单纯说青椒炒肉丝不好吃，那我们只是单纯需要重做青椒炒肉丝，其他菜都没问题的话，我们就使用
`git revert <commit-id>`
来重做一道青椒炒肉丝，但是桌子上还是四菜一汤，只不过之前的那盘青椒炒肉丝备份了一份。（比较常见的就是同事某个提交有问题，你`git revert`了他的那个步骤，自己再做一次提交）





# Git白银选手总结

* 了解工作区、暂存区、本地仓库、远程仓库。
* 熟悉工作区、暂存区、本地仓库的作业流程
* 能够熟练的同步本地仓库和远程仓库
* 会使用`git reset`'`git revert`来进行版本回退
* 遇到几种常见报错问题能够处理


# 常见问题以及解决办法

## `git status`不能显示中文
### 现象

status查看有改动但未提交的文件时总只显示数字串，显示不出中文文件名，非常不方便。如下图：
![](https://www.tielemao.com/wp-content/uploads/2018/08/status-dig.jpg)

### 原因
    在默认设置下，中文文件名在工作区状态输出，中文名不能正确显示，而是显示为八进制的字符编码。

### 解决办法
>将git 配置文件 `core.quotepath` 项设置为false。
>quotepath表示引用路径
>加上 `--global`表示全局配置

git bash 终端输入命令：

```shell
git config --global core.quotepath false
```

