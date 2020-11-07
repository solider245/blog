---
title: 使用checkinstall将源代码封装为deb或rpm安装包
date: 2020-11-06 18:54:05
permalink: /pages/e1a0ba/
sidebar: auto
categories:
  - 随笔
tags:
  - 
---
## 为什么要使用checkinstall封装？

并不是所有软件都提供了全平台安装，比如有些软件可以在ubuntu直接安装却不能在centos安装。这个时候如果这个软件提供了源码压缩包，你就可以在起`make install`时，利用`checkinstall`监视起安装过程，然后将其制作为一个rpm包，然后将其发送到你的centos系统，这个时候你就可以安装该软件了。
或者有时候一个软件在国内网络下无法下载，但是却可以在你的远程服务器下下载，这个时候你可以在远程服务器将其下载后打包成本地包，然后发送到你的国内网络上进行安装即可。

## `checkinstall`的安装

## ubuntu安装
```shell
sudo apt-get install checkinstall
```
其他平台
### 源码安装
```shell
wget http://asic-linux.com.mx/~izto/checkinstall/files/source/checkinstall-1.6.2.tar.gz #下载
tar  zxvf checkinstall-1.6.2.tar.gz #解压
cd checkinstall-1.6.2
make  && make install 
```

