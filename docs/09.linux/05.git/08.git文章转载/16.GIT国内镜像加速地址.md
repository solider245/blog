---
title: GIT国内镜像加速地址
date: 2020-10-12 12:09:51
permalink: /pages/3cf846/
categories:
  - git
  - git文章转载
tags:
  - 
---
# 使用国内镜像网站解决github clone速度慢问题

![](https://csdnimg.cn/release/phoenix/template/new_img/original.png)

[知用改创](https://me.csdn.net/u014630636) 2020\-05\-17 23:43:18 ![](https://csdnimg.cn/release/phoenix/template/new_img/articleReadEyes.png) 626 ![](https://csdnimg.cn/release/phoenix/template/new_img/tobarCollect.png) ![](https://csdnimg.cn/release/phoenix/template/new_img/tobarCollectionActive.png) 收藏  3

最后发布:2020\-05\-17 23:43:18首发:2020\-05\-17 23:43:18

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY\-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：[https://blog.csdn.net/u014630636/article/details/106181159](https://blog.csdn.net/u014630636/article/details/106181159)

版权

## 问题描述

我从github clone一些项目的时候速度极慢，有时候clone到一半还会失败，简直令人抓狂。

## 解决步骤

### 1\. 使用国内镜像网站

目前已知Github国内镜像网站有[github.com.cnpmjs.org](https://github.com.cnpmjs.org/)（亲测这个访问速度较快）和[git.sdut.me/](https://git.sdut.me/)。你可以根据你对这两个网站的访问速度快慢，选择其中一个即可。接下来只需要在clone某个项目的时候将github.com替换为github.com.cnpmjs.org即可。如下例：

```bash
git clone https://github.com/Hackergeek/architecture-samples

```

替换为

```bash
git clone https://github.com.cnpmjs.org/Hackergeek/architecture-samples

```

或者

```bash
git clone https://git.sdut.me/Hackergeek/architecture-samples

```

如果你仅仅只是想clone项目，不需要对clone下来的项目进行modify和push，那下面那个步骤就不需要看了。下面的步骤是为了解决使用镜像网站clone下来的项目无法进行push的问题的，因为国内的镜像网站是无法登录的，如果你尝试登录，结果如下图。
![Github国内镜像网站登录](https://img-blog.csdnimg.cn/20200517225636888.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTQ2MzA2MzY=,size_16,color_FFFFFF,t_70)

### 2\. 修改仓库push url

为了解决使用国内镜像网站clone下来的项目无法push的问题，我们需要将clone下来的仓库push url修改为github.com。如下例：
使用国内镜像网站clone下来的项目远程仓库地址如下图： ![远程仓库地址](https://img-blog.csdnimg.cn/20200517230350701.png)
使用如下命令修改仓库的push url：

```bash
git remote set-url --push origin  https://github.com/Hackergeek/architecture-samples

```

过程如下图：
![修改仓库push url](https://img-blog.csdnimg.cn/20200517234111570.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTQ2MzA2MzY=,size_16,color_FFFFFF,t_70)

## 参考资料

1.  [Openpilot 国内镜像](https://doc.sdut.me/mirror.html)
2.  [git clone一个github上的仓库，太慢，经常连接失败，但是github官网流畅访问，为什么？](https://www.zhihu.com/question/27159393)