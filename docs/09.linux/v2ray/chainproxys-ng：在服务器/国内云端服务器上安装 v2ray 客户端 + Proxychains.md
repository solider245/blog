---
title: 国内云端服务器上安装 v2ray 客户端 + Proxychains
date: 2020-10-12 12:09:51
permalink: /pages/05c9ff/
categories:
  - v2ray
  - chainproxys-ng：在服务器
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-20 05:51:50
 * @LastEditTime: 2020-07-20 05:51:50
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\v2ray\chainproxys-ng：在服务器\国内云端服务器上安装 v2ray 客户端 + Proxychains.md
 * @日行一善，每日一码
--> 
你懂的， 这是为了服务器上下载一些软件，绕过 GFW。
CentOS 7 没有找到 proxychains 的 yum repo，直接 rpm 了：

\# rpm \-ivh http://download\-ib01.fedoraproject.org/pub/fedora/linux/releases/30/Everything/x86\_64/os/Packages/p/proxychains\-ng\-4.13\-3.fc30.x86\_64.rpm

然后 V2ray 的安装就是一句话：
\# bash <(curl \-L \-s [https://install.direct/go.sh)](https://install.direct/go.sh))

拷贝一个之前配置过的客户端的 配置：/etc/v2ray/config.json

![](data:image/svg+xml;charset=utf-8,<svg height="836" width="971" xmlns="http://www.w3.org/2000/svg" version="1.1"/>)

![](https://tech.yj777.cn/wp-content/uploads/2019/12/image-3.png)

![](https://tech.yj777.cn/wp-content/uploads/2019/12/image-3.png)

systemctl restart v2ray， 然后用
\# proxychains curl \-kIsS https://www.google.com/
测试，如果有正常的 http 头显示，那就对了！

当然要先去修改 /etc/proxychains.conf 文件把最后一句修改为：
socks5 127.0.0.1 1080
另外修改：
proxy\_dns 8.8.8.8

然后你就可以用
\# proxychains wget 下载东西，
\# proxychains yum install 直接安装东西了，速度飞快！

后来发现，云端上也要做 dns 加密：
Ununtu 1804 之前的机器安装 dnscrypt\-proxy:
`sudo add-apt-repository ppa:shevchuk/dnscrypt-proxy`