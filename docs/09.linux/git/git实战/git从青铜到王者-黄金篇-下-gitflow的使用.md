---
title: git从青铜到王者-黄金篇-下-gitflow的使用
date: 2020-10-12 12:09:51
permalink: /pages/cfe995/
categories:
  - git
  - git实战
tags:
  - 
---
# 序言

在git黄金篇中我们知道了gitflow模式。但是大家使用当中发现，这个确实是有点繁琐的。所以就有达人开发了git-flow命令行工具来简化大家的操作。接下来就来和大家说说这个git-flow工具的使用。

# git-flow的安装
## macOS

Homebrew

> $ brew install git\-flow\-avh

Macports

> $ port install git\-flow\-avh

## Linux
### Ubuntu
> $ apt\-get install git\-flow
### centos
>$ yum install gitflow
### 其他linux脚本安装方法
```shell
$ curl -OL https://raw.github.com/nvie/gitflow/develop/contrib/gitflow-installer.sh
$ chmod +x gitflow-installer.sh
$ sudo ./gitflow-installer.sh
```

## Windows (Cygwin)

> $ wget \-q \-O \- \-\-no\-check\-certificate https://raw.github.com/petervanderdoes/gitflow\-avh/develop/contrib/gitflow\-installer.sh install stable | bash

安装 git\-flow, 你需要 wget 和 util\-linux。

# git-flow常用命令

## 起手式`git flow init`
```shell
git flow init -d  # -d是参数表示使用默认配置
git flow init     # 新手第一次使用请用这个命令，可以知道git-flow是怎么设置的
```
效果等同于`git init`也即对仓库初始化，不过`git flow init`还初始化了你的功能参数

![20200705161441_2ede1867247bd26eb4ac4a934713efbf.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200705161441_2ede1867247bd26eb4ac4a934713efbf.png)
如上图所示。这个是`git flow`的起手式。

输入上面的命令后，`git flow`会对以下命令进行默认
- 默认生产模式分支`master`
- 默认开发模式分支`develop`
- 默认功能分支名称`feature`
- 默认bug修复分支`bugfix`
- 默认发布分支`release`
- 默认支撑分支`support`

除了`support`分支外，其他分支大家都比较常见了。
如果你没有建立`develop`分支的话，这个命令会自动帮你建立。

## 功能分支feature的使用
功能分支常用命令是：
```shell
git flow feature                       # 查看功能分支
git flow feature start <name> [<base>] # 开始一个功能分支，默认从`develop`分出
git flow feature finish <name>         # 完成一个功能分支
git flow feature delete <name>         # 删除一个功能分支
```
### 实战模拟
通常我们要开始一个分支，则使用：
```shell
git flow feature start login # 开始一个登陆分支
```
上面的命令等同于：
```shell
git checkout develop   #切换到开发分支
git checkout feature/login #新建一个feature/login分支
```
我还省略了一步，也就是说，`git flow`等于让你实行了3个命令，同时还使用了一个自动命名规范，给你的分支功能加上了`feature`的前缀。

![20200705164853_0063ea99269ebcfa0fee9d62b5ffbc39.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200705164853_0063ea99269ebcfa0fee9d62b5ffbc39.png)
如下图所示。

当我们工作完成，需要合并分支时，我们使用：
```shell
git flow feature finish login # 结束login分支
```
![20200705165544_41f543a1fc3d3ebb68180a596709bd97.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200705165544_41f543a1fc3d3ebb68180a596709bd97.png)
如上图所示，上面的命令等同于：
```shell
git checkout develop        # 切换到开发分支
git merge feature/login     # 合并feature/login分支
git branch -d feature/login # 删除feature/login分支
```
还是那句话，一行命令等于我们的三行命令。

`start` `finish`这两个命令是用的是最多的，然后就是查询，和删除。
*   要将功能分支推/拉到远程存储库，请使用：

```shell
git flow feature publish <name>
git flow feature track <name>
```

## 发行分支`release`的使用


*   要列出/开始/完成/删除发行分支，请使用：

```shell
git flow release                           # 查询
git flow release start <release> [<base>]  # 开始，默认是develop分支
git flow release finish <release>          # 结束
git flow release delete <release>          # 删除
```
![20200705170739_d8d6245f3d883e6b5b1f40aee5badf7b.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200705170739_d8d6245f3d883e6b5b1f40aee5badf7b.png)
如上图所示，要发布新的分支，可以使用以下命令：
```shell
git flow release start v1.3.4             # v1.3.4是版本号，开开眼自行修改，也用中文，类似玄雍，白虎，朱雀等等。
```
以上命令等同于：
```shell
git checkout develop
git checkout -b release/v1.3.4
```
要开始推送到远程仓库，使用以下命令
```shell
git flow release finish 'v1.3.4' # 后面的版本要和你的版本相对应
```
![20200705171446_58694ad088afa6528b90e61b31478585.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200705171446_58694ad088afa6528b90e61b31478585.png)
如上图所示，以上命令等同于：
```shell
git checkout master                   # 切换到master分支
git merge release/v1.3.4              # 合并发行分支
git tag -a v1.3.4 -m '你提交的标签信息' # 给这次提交打上标签
git push origin master                 # 推送到远程分支
git checkout develop                  # 切换到develop分支
git merge release/v1.3.4              # 合并发行分支
git branch -d release/v1.3.4          # 删除分支版本
```
怎么样？算下来是不是简化了很多操作？看上去确实很繁琐，然而实际上你现在稍微繁琐一些，以后版本控制起来就香了。

补充工作：
`git-flow`不会推送标签，所以你需要追加标签推送命令。
```shell
git push --tags # 推送所有标签到远程仓库
```
`git-flow`不会推送你的开发分支到远程仓库，所以有时候你还需要切换到develop分支，将其推送到远程仓库。当然不推送也行。

## 修复分支`hotfix`的使用
*   要列出/开始/完成/删除修补程序分支，请使用：

```shell
git flow hotfix                          #查询
git flow hotfix start <release> [<base>] #新建
git flow hotfix finish <release>         #完成
git flow hotfix delete <release>         #删除
```

`hotfix`命令的话，默认从你当前`master`创建一个分支。
```shell
git tag                        #查询你的标签
git flow hotfix start 登录修复  # 创建一个登录修复的分支
```
![20200705181703_2f82ec0fb944ea38bdcb097a0c3e1083.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200705181703_2f82ec0fb944ea38bdcb097a0c3e1083.png)

```shell
git checkout master               # 切换到master分支
git checkout -b hotfix/登录修复    # 创建并切换到hotfix/登录修复分支
```
![20200705182037_135ea38fc424a558b421fba90b6e40e0.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200705182037_135ea38fc424a558b421fba90b6e40e0.png)
如上图所示，这个命令等同于：
```shell
git checkout master 
git merge hotfix/登录修复
git tag -a 登录修复 -m '修复了登录bug'
git checkout develop
git merge hotfix/登录修复
git branch -d hotfix/登录修复
git checkout develop
```

当然修复只是本地修复，我们还需要推送到远程仓库：
```shell
git push origin master
git push --tags
git checkout develop
git push
```
看到没，git flow极大的精简了我们的操作。

# git-flow命令总结
![20200705182849_2a81c25b69ce28a2ddeb888c330b9d59.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200705182849_2a81c25b69ce28a2ddeb888c330b9d59.png)
上面就是gitflow的常用命令总结，建议保存，想不起来的时候可以多看看。

