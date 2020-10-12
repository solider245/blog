---
title: jenkins与gogs整合
date: 2020-10-12 12:09:51
permalink: /pages/5b4184/
categories:
  - linux
  - jenkins
tags:
  - 
---
# 前言

我们在前面使用Jenkins集合Gogs来进行持续集成的时候，选择的是Jenkins定时检测git仓库是否有更新来决定是否构建。也就是说，我们提交了代码Jenkins并不会马上知道，那么我们可以通过webhook来解决。Jenkins的插件中心已经有对gogs的支持，真的是非常赞。

> [plugins.jenkins.io/gogs\-webhoo…](https://plugins.jenkins.io/gogs-webhook)

# 安装Gogs webhook 插件

打开 系统管理 \-> 管理插件 \-> 可选插件 ，在右上角的输入框中输入“gogs”来筛选插件：

![](https://user-gold-cdn.xitu.io/2019/3/12/1697047fdc5548f6?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

# 在gogs中配置

1.  进入我们的仓库，点击仓库设置

![](https://user-gold-cdn.xitu.io/2019/3/12/169704801fb82d37?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

2.添加webhook

点击 管理Web钩子 \-> 添加Web钩子 \->选择Gogs

![](https://user-gold-cdn.xitu.io/2019/3/12/1697047fddab8eb8?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

添加如下配置：

![](https://user-gold-cdn.xitu.io/2019/3/12/1697047fdde8c47b?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

推送地址的格式为：`http(s)://<你的Jenkins地址>/gogs-webhook/?job=<你的Jenkins任务名>`

3.配置Jenkins

进入主面板，点击我们的任务：

![](https://user-gold-cdn.xitu.io/2019/3/12/1697047fde8c77fb?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

选择配置：

![](https://user-gold-cdn.xitu.io/2019/3/12/169704801f3c46b2?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

选择Gogs Webhook 根据自己的需要进行配置，如果没有设置密钥那么什么都不用动。

![](https://user-gold-cdn.xitu.io/2019/3/12/1697047fe82ff064?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

# 测试

我们回到gogs，点击 推送测试 ，推送成功之后会看到一条推送记录

![](https://user-gold-cdn.xitu.io/2019/3/12/1697047fea789a34?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

回到我们的Jenkins可以看到已经成功进行了一次构建：

![](https://user-gold-cdn.xitu.io/2019/3/12/169704801972d167?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

转载自https://www.cnblogs.com/stulzq/p/8629720.html