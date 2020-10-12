---
title: Git撤销&回滚操作
date: 2020-10-12 12:09:51
permalink: /pages/b8ca14/
categories:
  - git入门
  - 撤销更改
tags:
  - 
---
开发过程中，你肯定会遇到这样的场景：

**场景一：**

> 糟了，我刚把不想要的代码，commit到本地仓库中了，但是还没有做push操作！

**场景二：**

> 彻底完了，刚线上更新的代码出现问题了，需要还原这次提交的代码！

**场景三：**

> 刚才我发现之前的某次提交太愚蠢了，现在想要干掉它！

## 撤销

上述**场景一**，在未进行`git push`前的所有操作，都是在“本地仓库”中执行的。我们暂且将“本地仓库”的代码还原操作叫做“撤销”！

**情况一：文件被修改了，但未执行`git add`操作(working tree内撤销)**

```text
$ git checkout fileName
$ git checkout .
```

**情况二：同时对多个文件执行了`git add`操作，但本次只想提交其中一部分文件**

```text
$ git add *
$ git status
# 取消暂存
$ git reset HEAD <filename>
```

**情况三：文件执行了`git add`操作，但想撤销对其的修改（index内回滚）**

```text
# 取消暂存
$ git reset HEAD fileName
# 撤销修改
$ git checkout fileName
```

**情况四：修改的文件已被`git commit`，但想再次修改不再产生新的Commit**

```text
# 修改最后一次提交
$ git add sample.txt
$ git commit --amend -m"说明"
```

**情况五：已在本地进行了多次`git commit`操作，现在想撤销到其中某次Commit**

```text
$ git reset [--hard|soft|mixed|merge|keep] [commit|HEAD]
```

具体参数和使用说明，请查看：[Git Pro深入浅出（二）中的重置揭秘部分](https://link.zhihu.com/?target=http%3A//blog.csdn.net/ligang2585116/article/details/51816372%23t7)

## 回滚

上述**场景二**，已进行`git push`，即已推送到“远程仓库”中。我们将已被提交到“远程仓库”的代码还原操作叫做“回滚”！**注意：对远程仓库做回滚操作是有风险的，需提前做好备份和通知其他团队成员！**

*如果你每次更新线上，都会打[tag](https://link.zhihu.com/?target=http%3A//blog.csdn.net/ligang2585116/article/details/46468709)，那恭喜你，你可以很快的处理上述**情景二**的情况*

```text
$ git checkout <tag>
```

*如果你回到当前HEAD指向*

```text
$ git checkout <branch_name>
```

**情况一：撤销指定文件到指定版本**

```text
# 查看指定文件的历史版本
$ git log <filename>
# 回滚到指定commitID
$ git checkout <commitID> <filename>
```

**情况二：删除最后一次远程提交**

*方式一：使用revert*

```text
$ git revert HEAD
$ git push origin master
```

*方式二：使用reset*

```text
$ git reset --hard HEAD^
$ git push origin master -f
```

*二者区别：*

*   **revert**是放弃指定提交的修改，但是会生成一次新的提交，需要填写提交注释，以前的历史记录都在；
*   **reset**是指将HEAD指针指到指定提交，历史记录中不会出现放弃的提交记录。

**情况三：回滚某次提交**

```text
# 找到要回滚的commitID
$ git log
$ git revert commitID
```

## 删除某次提交

```text
$ git log --oneline -n5
```

![](https://pic1.zhimg.com/v2-127fb8e0d9403055d38e66809fc1d908_b.jpg)

![](https://pic1.zhimg.com/80/v2-127fb8e0d9403055d38e66809fc1d908_720w.jpg)

Git撤销&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;回滚操作\-log.png

```text
$ git rebase -i "commit id"^
```

**注意：**需要注意最后的*^*号，意思是commit id的前一次提交

```text
$ git rebase -i "5b3ba7a"^
```

![](https://pic1.zhimg.com/v2-d20ffea4c5e2d887e0947f302b635e18_b.jpg)

![](https://pic1.zhimg.com/80/v2-d20ffea4c5e2d887e0947f302b635e18_720w.jpg)

Git撤销&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;回滚操作\-rebase.png

在编辑框中删除相关commit，如`pick 5b3ba7a test2`，然后保存退出（如果遇到冲突需要先解决冲突）！

```text
$ git push origin master -f
```

**通过上述操作，如果你想对历史多个commit进行处理或者，可以选择`git rebase -i`，只需删除对应的记录就好。rebase还可对 commit 消息进行编辑，以及合并多个commit。**

> 欢迎关注 「 **Super 前端** 」微信公众号

![](https://pic4.zhimg.com/v2-dc217c293c9b2a788556656554f0c763_b.jpg)

![](https://pic4.zhimg.com/80/v2-dc217c293c9b2a788556656554f0c763_720w.jpg)