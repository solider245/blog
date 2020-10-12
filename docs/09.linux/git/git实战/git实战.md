---
title: git实战
date: 2020-10-12 12:09:51
permalink: /pages/c2b755/
categories:
  - git
  - git实战
tags:
  - 
---
# Git实战

## 主要目标

+ GitHub建立远程仓库——dotfiles
+ 本地拉取远程仓库
+ 本地建立Dev分支
+ 创建zshrc/vimrc/tmux.conf三个文件夹并且写入配置
+ 本地提交
+ 推送到远程仓库

## 任务

+ 熟习git的一般提交与推送
+ 掌握Git的版本管理与分支合并技巧



## 一.GitHub建立远程仓库

首先来到 www.github.com 网站创建帐号与仓库。无法上GitHub的同学可以去国内的www.gitee.com也就是大家所说的码云。

![image-20200620205514006](https://images-1255533533.cos.ap-shanghai.myqcloud.com/img/image-20200620205514006.png)

## git clone 下载远程仓库到本地

```shell
cd #切换到根目录
git clone https://github.91chifun.workers.dev//https://github.com/solider245/dotfiles.git #下载远程文件（我这里用的是加速地址，所以你看起来会有点奇怪）
cd dotfiles #切换到目标目录
ls # 查看本地文件

```

![image-20200620213441721](https://images-1255533533.cos.ap-shanghai.myqcloud.com/img/image-20200620213441721.png)

如上图所示，成功仓GitHub仓库获取到了文件并且下载到了本地。



