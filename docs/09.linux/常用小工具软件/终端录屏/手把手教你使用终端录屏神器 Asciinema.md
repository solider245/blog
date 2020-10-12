---
title: 手把手教你使用终端录屏神器 Asciinema
date: 2020-10-12 12:09:51
permalink: /pages/d8765f/
categories:
  - 常用小工具软件
  - 终端录屏
tags:
  - 
---
Asciinema 是一个终端下非常棒的录屏和回放软件。Asciinema 对终端输入输出进行捕捉，然后以文本的形式来记录和回放。

基于 Asciinema 用文本来记录的特性，使其拥有了非常炫酷的特性。你可以在播放过程中随时暂停，然后对播放器中的文本进行复制或者其它操作。

Asciinema 同时支持多个操作系统（除 Windows 之外）。

## **Asciinema 工作原理**

将终端的操作和时间戳记录成 JSON 格式，然后使用 JavaScript 解析并配合 CSS 展示，看起来就像是在视频播放器中播放。

相比 GIF 和视频文件，Asciinema 录屏的体积非常之小（时长 2 分 50 秒的录屏只有 325 KB），无需缓冲就可播放。也可以方便的分享给别人或嵌入到网页中。

## **Asciinema ****安装**

*   Pip 安装

通过 Pip 安装需要 Python 3 版本支持 :

```
$ sudo pip3 install asciinema
```

这是适用于所有操作系统的通用安装方法，它始终提供最新版本。

*   ## macOS

```
$ brew install asciinema
```

*   Ubuntu

```
$ apt-add-repository ppa:zanchey/asciinema$ apt-get update$ apt-get install asciinema
```

*   ### Debian

```
$ sudo apt-get install asciinema
```

*   ### Arch Linux

```
$ pacman -S asciinema
```

*   ### Fedora

For Fedora < 22:

```
$ sudo yum install asciinema
```

For Fedora >= 22:

```
$ sudo dnf install asciinema
```

*   ### openSUSE

```
$ zypper in asciinema
```

这里我们介绍了几种常用的安装方式，更多安装方式可参考官方文档：https://asciinema.org/docs/installation

## **Asciinema 使用**

*   录制终端

安装完成后，我们来尝试录制一个试试？在你的终端输入 asciinema rec 回车后你会看到下面两行输出：

```
$ Asciicast recording started.$ Hit Ctrl-D or type "exit" to finish.
```

这表示录制已经开始，你可以按 Ctrl+D 或输入 exit 进行退出。退出后终端会输出：

```
$ Asciicast recording finished.
                        $ Press <Enter> to upload, <Ctrl-C> to cancel.
                        https://asciinema.org/a/113463

```

按下回车后就会将你的录制结果上传到 asciinema.org 上，按下 Ctrl+C 就退出并不上传录制结果，本次操作记录会保存在本地。

下面用官方录制的一个安装 Asciinema 的例子来演示下具体效果：

![](https://user-gold-cdn.xitu.io/2019/3/11/1696c38607d20efe?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

由于微信公众号不能加外链，你可以访问 https://asciinema.org/a/113463 查看。

*   回放录制

我们前面进行了一个录制终端操作，这里就可以使用 asciinema play 命令在本地回放刚才的录制操作。

```
回放托管在 asciinema.org 上的终端操作
```

```
$ asciinema play https://asciinema.org/a/113463
```

回放存在本地的终端操作文件

```
$ asciinema play /path/113463.json
```

*   在网页中嵌入播放器

a). 直接嵌入播放器

> <script id="asciicast\-113463" src="https://asciinema.org/a/113463.js" async></script>

b). 以图片方式嵌入播放器

    Markdown 方式

> \[!\[asciicast\](https://asciinema.org/a/113463.svg)\](https://asciinema.org/a/113463)

    HTML 方式

> <a href="https://asciinema.org/a/113463" target="\_blank"><img src="https://asciinema.org/a/113463.svg" /></a>

*   自由拷贝

在播放记录时，你可以自由地拷贝正在播放的记录中的命令，这一点上 ttyrec 和 screen 是无法相比的。

*   ### 管理 Asciinema.org 中的录制片段

如果想在 Asciinema 的网站上管理你所有录制的终端操作视频，首先你需要用自己的邮箱注册一个账号并进行登录。

其次使用 asciinema auth 命令产生的链接和 asciinema.org 中已登录的账户关联起来。

`$ asciinema auth`

Open the following URL in a web browser to link your install ID with your asciinema.org user account:

https://asciinema.org/connect/10cd4f24\-45b6\-4f64\-b737\-ae0e5d12baf8

This will associate all recordings uploaded from this machine (past and future ones) to your account, and allow you to manage them (change title/theme, delete) at asciinema.org.

> 在已登陆 asciinema.org 帐号的浏览器中访问上面  asciinema auth 生成的链接就可自动完成关联。

*   删除录制

如果不小心录制了一些隐私信息并上传到  asciinema.org。不要担心，你可以在类似 asciinema.org/a/1113463  链接中登录进去并删除它。

*   配置文件

您也可以通过创建配置文件来配置 Asciinema，其默认配置文件在 $HOME/.config/asciinema/config。

Asciinema 配置文件类似下面这个样子

```
[api]url = https://asciinema.example.com[record]command = /bin/bash -lyes = truequiet = true[play]speed = 2
```

\[api\] 中的选项与 API 位置和身份验证有关。如果要让 Asciinema 使用您自己的 Asciinema 站点而不是默认的 asciinema.org，可以设置 url 选项。url 也可以通过 ASCIINEMA\_API\_URL 环境变量来进行传递。

\[record\] 和 \[play\] 部分中的选项主要配合 asciinema rec/asciinema play 命令使用。

*   ## 其它技巧

```
将终端录屏记录保存到本地文件$ asciinema rec /path/demo录制终端操作并指定标题后将其上传到 asciinema.org$ asciinema rec -t "my first app"将终端录屏记录到本地文件，并限制空闲时间最大为 2.5 秒$ asciinema rec -i 2.5 /path/demo以两倍速来回放录制的终端会话$ asciinema play -s 2 /path/demo打印终端录屏记录的全部输出$ asciinema cat /path/demo分享本地已经录制的会话到 asciinema.org$ asciinema upload /path/demo
```

**参考文档**

http://www.google.com

http://t.cn/EI6Od9m

http://t.cn/EcXoV2Y

http://t.cn/EIX5fPS

![](https://user-gold-cdn.xitu.io/2019/3/11/1696c34640e678d2?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

**今日思想**

我们已经走得太远，以致于忘了当初为什么出发。

—— 纪伯伦

![](https://user-gold-cdn.xitu.io/2019/3/11/1696c34640d5fc4f?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

**推荐阅读**

*   [图解 Docker 架构](http://mp.weixin.qq.com/s?__biz=MzI3MTI2NzkxMA==&mid=2247486100&idx=1&sn=5f3384791ca3ebd3ee598cfb39cbe703&chksm=eac52bbdddb2a2ab861261a5bf303fd737a28d646e0e55adfaf31cebb626d6dd6d5d8699869f&scene=21#wechat_redirect)

*   [图解 Kubernetes 架构](http://mp.weixin.qq.com/s?__biz=MzI3MTI2NzkxMA==&mid=2247486123&idx=1&sn=0ea4f81c9cf2991eadca1ed454cd48ba&chksm=eac52b82ddb2a29452d5115f91d947bacdfd673d946df90bafd7901edb4dd44b9ddb8fa76c8e&scene=21#wechat_redirect)

*   [Docker 配置与实践清单](http://mp.weixin.qq.com/s?__biz=MzI3MTI2NzkxMA==&mid=2247486277&idx=1&sn=b9bebbb0e8a117dc9894e6c49fe3a312&chksm=eac52a6cddb2a37af125a3ea644950fb5e9f7639987ed0e8df24cbb9f4514b8d9b6891d17f1a&scene=21#wechat_redirect)

*   [使用 TC 和 Netem 模拟网络异常](http://mp.weixin.qq.com/s?__biz=MzI3MTI2NzkxMA==&mid=2247486252&idx=1&sn=f7e1021249fba8a4d3e83b214c3b6337&chksm=eac52a05ddb2a313bd42037f1d31c3b5b8731280909a62c47ced678789e87852b81c66a89816&scene=21#wechat_redirect)

*   [利用ngx\_http\_mirror\_module实现流量镜像](http://mp.weixin.qq.com/s?__biz=MzI3MTI2NzkxMA==&mid=2247485466&idx=1&sn=acd2b1d40414d3af8911b4550eefa3fb&chksm=eac52933ddb2a02533091c8bbb919fc97c75a86d6338e7c89c6d308529dd27db60803081ec1f&scene=21#wechat_redirect)