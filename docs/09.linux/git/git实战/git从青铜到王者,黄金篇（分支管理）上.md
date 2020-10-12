---
title: git从青铜到王者,黄金篇（分支管理）上
date: 2020-10-12 12:09:51
permalink: /pages/5b94c9/
categories:
  - git
  - git实战
tags:
  - 
---
# 序言
git白银篇里，我们熟悉并掌握了git的版本控制方法。

接下来我们还要开始了解git最重要的分支管理办法。
其中分支管理分为三种类型，即初级、中级、高级管理。

初级管理比较适合新手，因为他只有`master-feature`也即主分支和功能分支。他比较适合新手使用。

![20200701173728_6e5db6f44d13b832585904dbc1122c63.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200701173728_6e5db6f44d13b832585904dbc1122c63.png)

用图来表示的话，就是一个非常简单的主副分支图。
一般来说，每一个分支就是一个功能，一个功能完成后，再切换到主分支将其合并，即可完成。
下面，我们结合实践来展示。

# 本地仓库分支管理

## 建立`master`分支的初始化仓库
```shell
mkdir gittest # 创建gittest文件夹
cd gitttest   # 切换到gittest文件夹
git init      # 初始化当前仓库
ls -a         # 查看当前所有文件，有.git文件表示成功
vim README.md # 创建READEME.md文件
git add README.md # 将README.md文件提交到暂存区，也可以使用git add .
git commit -m '第一次提交，创建了README.md文件' # 将暂存区文件提交到本地仓库
git checkout master # 切换到master分支
```
上面是精简代码，下面是原始代码.大家可以查看一下。

![20200702004905_2134ca281c8c61543ca408158305e009.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200702004905_2134ca281c8c61543ca408158305e009.png)

通过以上代码，我们在本地建立了一个分支为`master`的初始化仓库，接下来，我们开始建立分支.为了便于大家理解，我将会以为做一道"四菜一汤"为例子，来方便大家更好的理解。

首先，我们在`master`分支下创建四菜一汤五个文件。
```shell
➜  gittest git:(master) touch 番茄炒蛋.md 肉末茄子.md 叫花鸡.md 青椒炒肉.md 莲藕汤.md
➜  gittest git:(master) ✗ ls
番茄炒蛋.md  叫花鸡.md  莲藕汤.md  青椒炒肉.md  肉末茄子.md  README.md
➜  gittest git:(master) ✗ git add .
➜  gittest git:(master) ✗ git commit -m '创建了四菜一汤五个文件'
[master dd9fbb1] 创建了四菜一汤五个文件
 5 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 叫花鸡.md
 create mode 100644 番茄炒蛋.md
 create mode 100644 肉末茄子.md
 create mode 100644 莲藕汤.md
 create mode 100644 青椒炒肉.md
```

在经过暂存和提交之后，接下来我们为四菜一汤中的每一道菜分别创建一个对应的分支。


```shell
git branch 叫花鸡 && git branch 番茄炒蛋 && git branch 肉末茄子 &&git branch 莲藕汤 && git branch 青椒炒肉
```
这里批量创建四菜一汤五个分支。
然后输入`git branch`来确定你当前文件夹下的的分支。
![20200702014508_eb21868c113181c9738ab9dd84268b91.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200702014508_eb21868c113181c9738ab9dd84268b91.png)
如上图所示，我一次性创建了五个分支。
在有了五个文件和五个分支之后，接下来我们会在对应的分支修改对应的文件。
下面我们来模拟一下实战。

比如做五个菜，我们草拟下顺序，知道叫花鸡和莲藕汤需要的时间最久，肉末茄子需要的时间其次，青椒炒肉和番茄炒蛋则属于可以快速上菜的。因此我们统筹一下时间，四道菜的顺序依次是：
叫花鸡→莲藕汤→肉末茄子→青椒炒肉→番茄炒蛋
确定了顺序之后，我们开始切换到对应的分支。
```shell
git checkout 叫花鸡      # 切换到叫花鸡分支
cat 叫花鸡.md            # 查看当前分支下叫花鸡的内容
vim 叫花鸡.md            # 修改叫花鸡
git commit -am '提交叫花鸡' # 修改文件
git checkout master     # 修改完文件后，切换回master分支
git merge 叫花鸡         # 合并叫花鸡分支
cat 叫花鸡.md            # 查看叫花鸡文件，看看内容是否增加了
git branch -d 叫花鸡      # 删除叫花鸡分支
git branch               # 查看当前分支
```
经过以上步骤之后，我们对叫花鸡这个步骤完成了。接下来，我们继续做莲藕汤.
```shell
git checkout 莲藕汤          # 切换到莲藕汤分支
cat 叫花鸡.md                # 查看叫花鸡文件，发现什么都没有，就对了
vim 莲藕汤.md                # 编辑莲藕汤文件
git commit -am '莲藕汤做好了' #免暂存提交
git checkout master          # 切换回master为你教案
git merge 莲藕汤              # 合并莲藕汤分支
cat 莲藕汤.md                 # 查看莲藕汤文件，发现有内容
git branch -d 莲藕汤          # 删除莲藕汤分支
git branch                   # 查看分支，发现莲藕汤分支已经被删除
```

以上，另外三个分支和文件同理。你也可以在左右分支全部做好所有工作之后，
但是有些时候我们要删除很多分支，比如除了master外的所有分支，那么我们可以这么做：

```shell
git checkout master
git branch | grep -v 'master' | xargs git branch -D
```

具体执行步骤是：

1.  切换到master分支
2.  将git branch的结果进行筛选，除去master
3.  将处理后的结果作为git branch \-D的参数来进行删除分支

## 打标签
全部写完之后，算是大功告成，这个时候就可以发布了。发布的时候记得打一个标签
```shell
git tag -a v1.0 -m "四菜一汤第一版"
```
上面的命令会创建一个v1.0的标签，同时附加一个标签说明。大家比较常见的游戏更新一般就是使用这种模式。
以后大家熟悉了的话，可以每一小步就打一个小标签，方便记忆。

## 将本地仓库推送到远程仓库
```shell
git pull origin master # 拉取远程文件到本地并且合并
git push origin master # 推送本地文件到远程仓库
git push origin --tags # 推送标签
```

# 技术总结

初级版本管理的主要内容
* 会创建分支
* 会查询分支
* 会切换分支
* 会合并分支
* 会删除分支
* 会打标签
* 会将本地仓库更新推送到远程仓库

# 常见问题

## 无法切换到master分支
因为master分支下没有文件，所以无法进行版本控制，所以一般需要先建一个文件才行。这也是为什么第一个文件总是README.md的原因。
## 将标签推送到远程服务器
通常的`git push`不会将标签对象提交到git服务器，我们需要进行显式的操作：
```shell
# 将v0.1.2标签提交到git服务器
$ git push origin v0.1.2

# 将本地所有标签一次性提交到git服务器
$ git push origin –tags
```
## 当 git pull 碰到拒绝合并无关历史

在拉取时使用以下命令：

```shell
git pull origin master --allow-unrelated-histories
```
git 默认拒绝合并没有共同祖先历史的两个项目
