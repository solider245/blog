---
title: git从青铜到王者,黄金篇（分支管理）中
date: 2020-10-12 12:09:51
permalink: /pages/c3cfed/
categories:
  - git
  - git实战
tags:
  - 
---
# 序言

在git黄金篇上,我们学会了如何使用git进行分支管理。然后那个是属于比较简单的`master-feature`体系，一般来说自己一个人日常自嗨还是可以的。
但是用到生产环境就不行了，生产环境一般来说都是使用gitflow模式。
`gitflow`模式下，一共有五个分支，其中两个主分支，三个辅助分支。

- `master`
- `develop`
  - `feature`
  - `hotfix`
  - `release`


形式的话就类似上面这样。然后辅助分支里，`feature`分支又是用的最多的。
## 为什么我们需要`develop`分支
首先我们引入`develop`分支。
在引入前，我们需要知道，为什么要有`develop`分支。还是拿我们比较常见的四菜一汤模式。大多数情况下，烧菜做饭的人只是一个工具人，他们只能决定这个菜好不好吃，而不能决定这个菜该不该上。比方说，老公负责做菜，做好菜之后直接上桌即可，但是现实情况是，老公做完菜之后，还需要给老婆先尝尝，只有好吃才能出锅上桌。
所以，老婆是那个`master`，她来决定上不上桌。由于master分支已经被占用，所以老公做菜就只能在`develop`分支下操作了。同样的，老婆大人一般见不得那么多烦心的事，所以对于`feature`之前我们是从`master`直接建立的，现在也只能从`develop`上建立。我们提交到`master`的内容一般是最终的成品，只有老婆大人满意之后，才能最终合并上线。好了，在说了这么多废话之后，我们开始进入`coding`模式吧。

## 为什么我们需要`release`分支
release分支又叫发布分支，一般来说有两种情况，一种是我们把所有的功能都开发完了之后需要上线了，就以此为节点开出一个分支。这个分支上就不再进行功能上的更改，一般只进行bug的更改，当没有大的更改的时候，就切换到master分支，将该release合并。由于这个是版本合并，所以还需要打上TAG。大家比较常见的游戏版本更新就是和这样类似。
release在发布的时候，develop的分支可以继续开发别的功能，同时在release上线后将其合并回来并且删除。

用四菜一汤来打比喻。就好比老公把四菜一汤做好了，再上桌前喊老婆大人来进行品尝。由于大的部分已经搞定，所以这个时候一般就只会对菜的咸淡进行修改，确定无误，老婆大人满意之后，就会完美上桌了。

## 为什么需要`feature`分支

`feature`分支又叫功能分支，一般来说，一个功能就建立一个分支。用炒菜来做比方的话，相当于我们每做一道菜就会建立一个分支，完成之后合并再进行删除。这也是我们最常见和最常使用的分支。

## 为什么需要`hotfix`分支

`hotfix`分支就是热补丁分支，一般是在`master`分支上进行修改，或者是在`release`上进行修改，修改完之后要被合并到`master`与`develop`分支。
用炒菜来打比方的话，就相当于你菜上桌了才发现有道菜忘记放言了。这个时候就不回锅了，直接拿好盐罐子来现场加，加到咸淡适宜即可。


# 实战篇

下面我们通过一些举例来进行实战

## 引入`develop`分支

首先，我们还是先在github/gitee上建立一个远程仓库。然后使用git clong把他下载下来。然后我们输入`git status`，确保当前仓库干净并且与上游保持一致。具体如下图所示.
![20200702230020_118594a063ff4abb222ca67d1e0f18de.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200702230020_118594a063ff4abb222ca67d1e0f18de.png)

接下来我们开始建立`develop`分支，并且将其推送到服务器。
```shell
git branch develop           # 建立develop分支
git push -u origin develop   # 将develop分支推送到远程仓库
```

提示如下图，一般就建立成功了。
![20200702230425_4788efaced619172909d5f296101e67f.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200702230425_4788efaced619172909d5f296101e67f.png)
作为新手，如果你不放心，可以先上你的远程仓库看看有没有建立成功。
![20200702230345_b143b0e9addd37821508ead0ddbf41e4.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200702230345_b143b0e9addd37821508ead0ddbf41e4.png)

## 切换到`develop`分支并新增`feature`分支

```shell
git checkout develop  # 切换到develop分支
git checkout -b feature/hello # 创建并切换到功能分支feature/hello
coding
git add .                 # 提交当前变动到缓存区
git commit -am '你的摸鱼内容' #提交修改内容到本地仓库
git checkout develop          # 切换到develop分支
git merge --no-f feature/hello # 合并功能分支并且说明
git branch release/hello        # 创建发行分支
git checkout master             # 切换到Master分支
git merge release/hello         # 合并发行分支
git tag -a v1.0 -m '1.0版本来了' # 打标签
git push                         # 将本地内容推送到默认仓库
git push origin --tags           # 将本地标签推送到默认仓库
git branch -d release/hello      # 删除发行分支，注意，如果有修改，需要先合并到develop分支再进行删除
```
## `hotfix`的修复步骤
```shell
git checkout master            # 切换到master分支
git checkout -b hotfix/login   # 创建并切换到修复分支
coding                         # 工作中
git add .                      # 将修复提交到缓存
git commit -m '你修复的bug'     # 将缓存区提交到仓库
git checkout master            # 切换到master分支
git merge hotfix/login         # 合并修复的分支
git tag -a v1.3 -m '修复bug的标签' # 给修复打一个小标签
git push                        # 将修复后的内容推送到远程仓库
git push origin --tags          # 将所有标签推送到远程仓库
git checkout develop            # 切换到develop分支
git merge hotfix/login          # 将bug合并到develop分支
git branch -d hotfix/login      # 删除修复的分支
```

# 总结

- 常用就是主分支`master`与`develop`分支。
- 在`develop`分支上新建并切换到`feature`功能分支，完成后切回`develop`分支将其合并，在主要功能完成之后，想要推送就新建一个`release`分支，在测试完没有bug后就切换到`master`分支，由其合并`release`分支并且打上`tag`标签，然后先将修改`push`到远程仓库，再讲打好的标签推送到远程仓库。如果`release`分支测出了bug并且修复的话，需要切回到`develop`分支合并，如果没有的话，直接将其删除即可。其他的功能分支也可以在完成合并后删除。
- `hotfix`分支一般是直接在`master`分支上创建，然后需要被合并到`develop`分支上。
有时候如果忘记合并而直接删除的话，会导致`develop`分支反而落后`master`分支。这个时候就需要在`master`分支上创建一个临时分支一般是`tmp`，被develop合并后再删除。
  - 有时候在`release`发布之前会被测试测出bug，那么这个时候直接在这里新建`hotfix`分支即可。修复完之后再合并到`master`与`develop`分支。

- 总的来说确实是有点繁琐，但是这一套熟练了之后会好很多。

当然，在熟练了之后，可以使用`gitflow`工具来简化操作。下一章就来使用`gitflow`
