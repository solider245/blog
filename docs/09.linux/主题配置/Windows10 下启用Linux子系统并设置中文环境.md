---
title: Windows10 下启用Linux子系统并设置中文环境
date: 2020-10-12 12:09:51
permalink: /pages/245757/
categories:
  - linux
  - 主题配置
tags:
  - 
---
1、启用开发者模式
设置\-更新和安全\-针对开发人员\-开发人员模式\-等待完成
![这里写图片描述](https://img-blog.csdn.net/20180703203332407?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMDczNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
2、设置\-程序和功能\-启用或关闭windows功能\-适用于Linux的Windows子系统\-确定\-等待安装完成并重启PC

![这里写图片描述](https://img-blog.csdn.net/20180703203535530?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMDczNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
3、安装Linux
打开windows10的应用商店，搜索Linux，选择需要的版本点击\-获取
![这里写图片描述](https://img-blog.csdn.net/20180703203857631?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMDczNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
![这里写图片描述](https://img-blog.csdn.net/20180703203933957?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMDczNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
我这里选择的是ubuntu18.04，点击获取后等待安装完成
4、启动
在开始菜单中找到安装的ubuntu点击启动，第一次启动需要设置用户和密码按照提示设置即可。
![这里写图片描述](https://img-blog.csdn.net/20180703204115533?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMDczNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
5、设置中文环境
a、因为是刚刚安装的需要更新下软件源和软件包：
```shell
sudo apt update &&sudo apt upgrade
```
b、安装中文语言包
```shell
sudo apt install \-y language\-pack\-zh\-hans language\-pack\-zh\-hans\-base
```
![这里写图片描述](https://img-blog.csdn.net/20180703204444395?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMDczNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
c、设置中文环境变量

```
vi ~/.profile
```
在末尾新增一行:LANG=zh\_CN.UTF\-8
![这里写图片描述](https://img-blog.csdn.net/20180703205120465?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMDczNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
设置完毕重新打开ubuntu即可，部分软件及命令不支持汉化以ls命令为例： ![这里写图片描述](https://img-blog.csdn.net/20180703205416889?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2xiMDczNw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
也可以输入
```
source ~/.profile
```
令其生效。