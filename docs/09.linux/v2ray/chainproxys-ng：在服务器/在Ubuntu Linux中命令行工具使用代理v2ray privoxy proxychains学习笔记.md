---
title: 在Ubuntu Linux中命令行工具使用代理v2ray privoxy proxychains学习笔记
date: 2020-10-12 12:09:51
permalink: /pages/efd2d3/
categories:
  - v2ray
  - chainproxys-ng：在服务器
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-20 05:45:36
 * @LastEditTime: 2020-07-20 05:45:37
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\v2ray\在Ubuntu Linux中命令行工具使用代理v2ray privoxy proxychains学习笔记.md
 * @日行一善，每日一码
--> 
## 在Ubuntu Linux中命令行工具使用代理的必要性:

在Ubuntu Linux中很多命令行工具, 如apt\-get pip git wget curl等, 需要访问外网服务器(主要是github). 但是由于github没有国内的服务器以及其他特殊的原因, 网络链接经常失败, 这时只能求助于代理.

## Step 1: 配置V2ray socks5

当前最好的方法是租v2ray的服务器, 并在ubuntu配置客户端.

首先下载脚本:

wget https://install.direct/go.sh

然后执行脚本安装 V2Ray:

sudo bash go.sh

go.sh 会下载[github上的v2ray\-linux\-64.zip文件](https://github.com/v2ray/v2ray-core/releases), 在国内经常出现网络连接失败的情况, 因此需要修改go.sh内容, 并把外网下载的v2ray\-linux\-64.zip复制到/tmp/v2ray/v2ray.zip .

复制配置文件config.json到/etc/v2ray. config.json可以直接从[windows的v2rayN客户端](https://github.com/2dust/v2rayN/releases)夹中直接复制过来.

启动v2ray服务

systemctl restart v2ray

socks5代理已经启动, 默认端口是10808, (socks5://127.0.0.1:10808).

## Step 2: 配置http代理 privoxy

有些命令行工具只能使用http代理, 不能使用socks5代理, 因此需要用privoxy把socks5代理转换为http代理.

安装privoxy

sudo apt install \-y privoxy

修改配置文件/etc/privoxy/config

listen\-address  :10809

forward\-socks5    /    127.0.0.1:10808  .

启动privoxy服务

systemctl restart privoxy

http代理已经启动, 默认端口是10809, (http://127.0.0.1:10809).

## Step 3: 配置proxychains

有些linux命令行工具没有配置代理的方法, 可以用proxychains强制应用使用代理网络.

安装proxychains

sudo apt install \-y proxychains

修改配置文件/etc/proxychains.conf最后一行

socks5  127.0.0.1 10808

使用proxychains方法, 在命令前加上proxychains, 如:

proxychains apt update

## python pip使用http代理加速

方法1:

pip3 install \-r requirement.txt \-\-proxy http://127.0.0.1:10809

方法2:

proxychains pip3 install \-r requirement.txt

## git使用http代理加速

方法1:

git config \-\-global http.proxy http://127.0.0.1:10809
git config \-\-global https.proxy http://127.0.0.1:10809

取消设置

git config \-\-global \-\-unset http.proxy

方法2:

proxychains git clone https://github.com/opencv/opencv.git

## docker使用http代理加速

\# mkdir /etc/systemd/system/docker.service.d
/etc/systemd/system/docker.service.d/http\-proxy.conf
\-\-\-\-\-\-
\[Service\]
Environment="HTTP\_PROXY=http://127.0.0.1:10809/"
\-\-\-\-\-\-
# systemctl daemon\-reload
# systemctl restart docker