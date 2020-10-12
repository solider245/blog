---
title: vim粘贴出现乱码
date: 2020-10-12 12:09:51
permalink: /pages/e71465/
categories:
  - linux
  - vim
tags:
  - 
---
# 解决vim粘贴代码格式混乱的方法

![](https://csdnimg.cn/release/phoenix/template/new_img/reprint.png)

[weixin\_33937778](https://me.csdn.net/weixin_33937778) 2013\-03\-29 18:01:15 ![](https://csdnimg.cn/release/phoenix/template/new_img/articleReadEyes.png) 133 ![](https://csdnimg.cn/release/phoenix/template/new_img/tobarCollect.png) ![](https://csdnimg.cn/release/phoenix/template/new_img/tobarCollectionActive.png) 收藏

最后发布:2013\-03\-29 18:01:15首发:2013\-03\-29 18:01:15

原文链接：[http://blog.51cto.com/fei007/1166808](http://blog.51cto.com/fei007/1166808)

版权

在vim粘贴代码的时候，粘贴的代码（shift+insert）会自动缩进，导致格式非常混乱。

**下面介绍两种方法：**

（1）在vim中，进入命令模式输入：set paste，在进行粘贴，就不会乱码了。但是这样存在一个问题，就是不会自动产生缩进了，因此需要在粘贴完成之后命了输入：set nopaste，恢复缩进模式。

（2）在vimrc文件中添加set pastetoggle=<F9>，这样<F9>就成了改变paste模式的快捷键，日后再粘贴时，就可以使用<F9>进行切换了。是不是方便了很多。