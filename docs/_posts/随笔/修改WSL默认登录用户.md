---
title: "修改WSL默认登录用户"
date: 2020-07-17T08:26:39Z
lastmod: 2020-07-17T08:26:39Z
draft: true
keywords: [WSL,MS]
description: ""
tags: []
categories: []
author: ""

# You can also close(false) or open(true) something for this content.
# P.S. comment can only be closed
comment: false
toc: false
autoCollapseToc: false
postMetaInFooter: false
hiddenFromHomePage: false
# You can also define another contentCopyright. e.g. contentCopyright: "This is another copyright."
contentCopyright: false
reward: false
mathjax: false
mathjaxEnableSingleDollar: false
mathjaxEnableAutoNumber: false

# You unlisted posts you might want not want the header or footer to show
hideHeaderAndFooter: false

# You can enable or disable out-of-date content warning for individual post.
# Comment this out to use the global config.
#enableOutdatedInfoWarning: false

flowchartDiagrams:
  enable: false
  options: ""

sequenceDiagrams: 
  enable: false
  options: ""

---

<!--more-->
wsl 安装完成后默认登录是新建用户，切换root用户登录操作如下，然后重新启动wsl即可。

![](https://img-blog.csdnimg.cn/20190524161728420.png)

```shell
ubuntu config --default-user root
```
ubunt是你的系统，如果不是可以换成你用的系统
