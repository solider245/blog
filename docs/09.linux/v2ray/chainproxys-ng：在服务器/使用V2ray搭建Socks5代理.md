---
title: 使用V2ray搭建Socks5代理
date: 2020-10-12 12:09:51
permalink: /pages/97a8e7/
categories:
  - v2ray
  - chainproxys-ng：在服务器
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-20 09:01:49
 * @LastEditTime: 2020-07-20 09:01:57
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\v2ray\chainproxys-ng：在服务器\使用V2ray搭建Socks5代理.md
 * @日行一善，每日一码
--> 
## **服务器端**

### **1\. 安装v2ray**

*   V2Ray 提供了一个在 Linux 中的自动化安装脚本，此脚本会配置自动运行脚本，自动运行脚本会在系统重启之后，自动运行 V2Ray。

    ```
    bash <(curl -L -s https://install.direct/go.sh)
    ```

*   安装完成后，你可以使用以下命令来控制v2ray的运行：

    ```
    service v2ray start   //启动v2rayservice v2ray stop    //停止v2rayservice v2ray restart     //重新启动v2ray
    ```

### **2\. 相关配置**

*   相关的配置文件在 `/etc/v2ray/config.json`
*   以下配置仅用来搭建socks5代理，不含VMss协议部分

    ```
    {"inbounds": [    {    "protocol": "socks",    "port": 12345,    "settings": {        "auth": "password",        "accounts": [        {            "user": "test",            "pass": "password"        }        ],        "udp": false,        "ip": "127.0.0.1",        "userLevel": 0    }    }],"outbounds": [    {    "protocol": "freedom",    "settings": {}    },    {    "protocol": "blackhole",    "settings": {},    "tag": "blocked"    }],"routing": {    "rules": [    {        "type": "field",        "ip": ["geoip:private"],        "outboundTag": "blocked"    }    ]}}
    ```

**注意**

*   Socks 协议的认证方式，支持"noauth"匿名方式和"password"用户密码方式。
*   只有当 `auth` 为 `password` 时，用户名和密码才有效。
*   如果不需要用户名和密码，将 `auth` 设置为 `noauth`

## **客户端**

### **直接使用socks5**

*   Linux下可以使用 `proxychains` 代理链，编辑 `/etc/proxychains.conf`,按格式在最后一行加上

    ```
    socks5      服务器ip        端口        用户名      密码
    ```

*   测试是否配置成功。

    ```
    proxychains curl myip.ipip.net
    ```

*   若返回的为服务器ip，则配置成功。