---
title: v2ray客户端与服务端配置指南
date: 2020-10-12 12:09:51
permalink: /pages/fafae6/
categories:
  - linux
  - v2ray
tags:
  - 
---
# 序言

配置v2ray客户端与服务端的时候踩了不少坑，主要的坑还是在v2ray命令行上面踩的，这里写一篇内容，防止以后再踩坑。



# 下载地址

## GitHub下载地址

https://github.com/v2ray/v2ray-core/releases

## GitHub镜像加速下载地址（适合国内用户）

https://github.com.cnpmjs.org/v2ray/v2ray-core/releases



## v2ray客户端与服务端配置地址

https://intmainreturn0.com/v2ray-config-gen/



主要用于给新手使用。左边是服务端地址，右边是客户端地址。



## v2ray Linux安装脚本地址

```shell
bash <(curl -L -s https://install.direct/go.sh)

```

此脚本会自动安装以下文件：

*   `/usr/bin/v2ray/v2ray`：V2Ray 程序；
*   `/usr/bin/v2ray/v2ctl`：V2Ray 工具；
*   `/etc/v2ray/config.json`：配置文件；
*   `/usr/bin/v2ray/geoip.dat`：IP 数据文件
*   `/usr/bin/v2ray/geosite.dat`：域名数据文件

### 安装包无法下载解决办法

主要原因在于脚本默认的下载地址是github，而那个地址如果你本身没有代理的话是无法下载的，解决办法是更换镜像加速地址即可。

#### 1.使用curl 软件下载安装脚本到本地

```shell
curl -O https://install.direct/go.sh
```

#### 2.使用vim定位链接地址并修改

然后输入

```shell
sudo vim go.sh
```

打开脚本，然后输入/LINK,定位到下载链接地址，替换为加速地址即可。



![image-20200619154043440](../../../../AppData/Roaming/Typora/typora-user-images/image-20200619154043440.png)

```shell
https://github.91chifun.workers.dev//https://github.com/v2ray/v2ray-core/releases/download/v4.24.2/v2ray-linux-64.zip
```

#### 3.重新开始安装

然后，再输入

```shell
bash <(curl -L -s https://install.direct/go.sh)
```

即可开始自动安装。

#### 4.配置并且启动与控制v2ray



*   编辑 /etc/v2ray/config.json 文件来配置你需要的代理方式；
*   运行 service v2ray start 来启动 V2Ray 进程；
*   之后可以使用 service v2ray start|stop|status|reload|restart|force\-reload 控制 V2Ray 的运行。



#### 5.go.sh 参数的一些参数配置与用法

go.sh 支持如下参数，可在手动安装时根据实际情况调整：

*   `-p` 或 `--proxy`: 使用代理服务器来下载 V2Ray 的文件，格式与 curl 接受的参数一致，比如 `"socks5://127.0.0.1:1080"` 或 `"http://127.0.0.1:3128"`。
*   `-f` 或 `--force`: 强制安装。在默认情况下，如果当前系统中已有最新版本的 V2Ray，go.sh 会在检测之后就退出。如果需要强制重装一遍，则需要指定该参数。
*   `--version`: 指定需要安装的版本，比如 `"v1.13"`。默认值为最新版本。
*   `--local`: 使用一个本地文件进行安装。如果你已经下载了某个版本的 V2Ray，则可通过这个参数指定一个文件路径来进行安装。

# v2ray客户端与服务端常见配置方法

## 一.客户端配置

在你的 PC （或手机）中，你需要运行 V2Ray 并使用下面的配置：

```shell
{
  "inbounds": [{
    "port": 1080,  // SOCKS 代理端口，在浏览器中需配置代理并指向这个端口1080换成你的代理软件监视端口
    "listen": "127.0.0.1",
    "protocol": "socks",
    "settings": {
      "udp": true
    }
  }],
  "outbounds": [{
    "protocol": "vmess",
    "settings": {
      "vnext": [{
        "address": "server", // 服务器地址，请修改为你自己的服务器 ip 或域名例如192.168.1.1
        "port": 10086,  // 服务器端口，防火墙记得放心该端口
        "users": [{ "id": "b831381d-6324-4d53-ad4f-8cda48b30811" }] //id 可以在服务端配置地址生成
      }]
    }
  },{
    "protocol": "freedom",
    "tag": "direct",
    "settings": {}
  }],
  "routing": {
    "domainStrategy": "IPOnDemand",
    "rules": [{
      "type": "field",
      "ip": ["geoip:private"],
      "outboundTag": "direct"
    }]
  }
}
```

## 服务器

然后你需要一台防火墙外的服务器，来运行服务器端的 V2Ray。配置如下：

```shell
{
  "inbounds": [{
    "port": 10086, // 服务器监听端口，必须和上面的一样
    "protocol": "vmess",
    "settings": {
      "clients": [{ "id": "b831381d-6324-4d53-ad4f-8cda48b30811" }]
    }
  }],
  "outbounds": [{
    "protocol": "freedom",
    "settings": {}
  }]
}

```

服务器的配置中需要确保 `id` 和端口与客户端一致，就可以正常连接了。



## 运行

* 在 Windows 和 macOS 中，配置文件通常是 V2Ray 同目录下的 `config.json` 文件。直接运行 `v2ray` 或 `v2ray.exe` 即可。

* 在 Linux 中，配置文件通常位于 `/etc/v2ray/config.json` 文件。运行 `v2ray --config=/etc/v2ray/config.json`，或使用 systemd 等工具把 V2Ray 作为服务在后台运行。

* service v2ray start|stop|status|reload|restart|force\-reload #常用命令

* ```shell
  sudo systemctl start v2ray # systemctl启动的办法
  ```

# v2ray图形界面（GUI）客户端主要下载地址

**V2Ray**是近几年兴起的科学上网技术，采用新的协议，因功能强大、能有效抵抗墙的干扰而广受好评。**V2Ray官网**是 [https://v2ray.com](https://v2ray.com)，目前已无法直接打开。V2Ray安装部署及流量伪装请参考：[V2Ray教程](https://tlanyan.me/v2ray-tutorial) 和 [V2Ray高级技巧：流量伪装](https://tlanyan.me/v2ray-traffic-mask/)。

本站提供最新版v2ray Windows客户端、v2ray安卓客户端、v2ray mac客户端、v2ray苹果客户端和v2ray Linux客户端下载，并给出各v2ray客户端配置教程。

推荐猎豹加速器，下载地址：[https://lbjsq.net/e8nf](https://lbjsq.net/e8nf)

---

## V2ray Windows客户端：

| V2rayN | [v2rayN\-v3.19.zip](https://tlanyan.me/download.php?filename=/v2/windows/v2rayN-v3.19.zip) | [官网下载](https://github.com/2dust/v2rayN/releases) | [配置教程](https://www.hijk.pw/v2rayn-config-tutorial/) |
| V2rayW | [v2rayW\-v1.0.0\-beta2.zip](https://tlanyan.me/download.php?filename=/v2/windows/v2rayW-v1.0.0-beta2.zip) | [官网下载](https://github.com/Cenmrev/V2RayW/releases) | [配置教程](https://www.hijk.pw/v2rayw-config-tutorial/) |
| Clash | [Clash.for.windows\-0.9.11.7z](https://tlanyan.me/download.php?filename=/v2/windows/Clash.for.Windows-0.9.11-win.7z) | [官网下载](https://github.com/Fndroid/clash_for_windows_pkg/releases) | [配置教程](https://www.hijk.pw/clash-for-windows-v2ray-tutorial/) |
| V2rayS | [v2rayS\-v1.0.0.3.zip](https://tlanyan.me/download.php?filename=/v2/windows/v2rayS-v1.0.0.3.zip) | [官网下载](https://github.com/Shinlor/V2RayS/releases) | [配置教程](https://www.hijk.pw/v2rays-config-tutorial/) |
| Mellow | [Mellow.Setup.0.1.17.exe](https://tlanyan.me/download.php?filename=/v2/windows/Mellow.Setup.0.1.17.exe) | [官网下载](https://github.com/mellow-io/mellow/releases) |  |
| Qv2ray | [Qv2ray.v2.5.0.Windows.7z](https://tlanyan.me/download.php?filename=/v2/windows/Qv2ray.v2.5.0.Windows-x86.7z) | [官网下载](https://github.com/Qv2ray/Qv2ray/releases) |  |

**Windows系统建议使用V2rayN**，界面简洁大气且支持Vmess和Shadowsocks。**本站提供的V2rayN即官网的V2rayN\-Core.zip**，不需要单独下载V2ray\-Core。(**更新**：最新版v2rayN已修复v2ray安全漏洞，建议使用)

## V2ray安卓客户端：

| V2rayNG | [v2rayNG\-v1.2.10.apk](https://tlanyan.me/download.php?filename=/v2/android/v2rayNG-v1.2.10.apk) | [官网下载](https://github.com/2dust/v2rayNG/releases) | [配置教程](https://www.hijk.pw/v2rayng-config-tutorial/) |
| BifrostV | [bifrostV\-v0.6.8.apk](https://tlanyan.me/download.php?filename=/v2/android/bifrostV-v0.6.8.apk) | [上游下载](https://apkpure.com/bifrostv/com.github.dawndiy.bifrostv) | [配置教程](https://www.hijk.pw/bifrostv-config-tutorial/) |
| Clash | [ClashForAndroid\-v1.2.15.apk](https://tlanyan.me/download.php?filename=/v2/android/ClashForAndroid-v1.2.15.apk) | [官网下载](https://github.com/Kr328/ClashForAndroid/releases) | [配置教程](https://www.hijk.pw/clash-for-android-config-v2ray-tutorial/) |
| Kitsunebi | [Kitsunebi\_v1.8.0.apk](https://tlanyan.me/download.php?filename=/v2/android/Kitsunebi_v1.8.0.apk) | [上游下载](https://apkpure.com/kitsunebi/fun.kitsunebi.kitsunebi4android) | [配置教程](https://www.hijk.pw/kitsunebi-android-config-tutorial/) |

如果V2rayNG用起来网速慢，可以试试BifrostV或者Clash for Android。

## V2ray苹果客户端：

*   目前没有发现免费v2ray iOS客户端，付费v2ray iOS客户端有：Shadowrocket、pepi、i2Ray、Kitsunebi和Quantumult。无法搜索到这些app请参考 [获取ios科学上网客户端](https://tlanyan.me/get-proxy-clients/)。

**V2ray Mac客户端**：

| V2rayU | [v2rayU\-v2.1.0.dmg](https://tlanyan.me/download.php?filename=/v2/macos/v2rayU-v2.1.0.dmg) | [官网下载](https://github.com/yanue/V2rayU/releases) | [配置教程](https://www.hijk.pw/v2rayu-config-tutorial/) |
| V2rayX | [v2rayX\-v1.5.1.zip](https://tlanyan.me/download.php?filename=/v2/macos/v2rayX-v1.5.1.zip) | [官网下载](https://github.com/Cenmrev/V2RayX/releases) | [配置教程](https://www.hijk.pw/v2rayx-config-tutorial/) |
| ClashX | [clashX\-v1.20.4.dmg](https://tlanyan.me/download.php?filename=/v2/macos/clashX-v1.20.4.dmg) | [官网下载](https://github.com/yichengchen/clashX/releases) | [配置教程](https://www.hijk.pw/clashx-config-v2ray-tutorial/) |

V2rayU有中文界面，如果英文较好，V2RayX是更好的选择。ClashX界面美观，非常适合订阅地址用。

## V2ray Linux客户端：

| Qv2ray | [Qv2ray.v2.5.0.AppImage](https://tlanyan.me/download.php?filename=/v2/linux/Qv2ray.v2.5.0.linux-x64.AppImage) | [官网下载](https://github.com/Qv2ray/Qv2ray/releases) |
| Mellow | [Mellow\-0.1.17.AppImage](https://tlanyan.me/download.php?filename=/v2/linux/Mellow-0.1.17.AppImage) | [官网下载](https://github.com/mellow-io/mellow/releases) |
| V2rayL | [官方安装文档](https://github.com/jiangxufeng/v2rayL) |  |

**注意：** 客户端需要添加 **v2ray节点** 才能上外网， v2ray服务端部署请参考：[V2Ray一键脚本](https://www.hijk.pw/centos-one-click-install-v2ray/)，购买服务可考虑 [搬瓦工官方代理Just My Socks](https://www.hijk.pw/just-my-socks-buy-and-use-tutorial/)

---

## 其他客户端下载：

*   [Shadowsocks/SS客户端](https://tlanyan.me/shadowsock-clients/)
*   [ShadowsocksR/SSR客户端](https://tlanyan.me/shadowsockr-shadowsocksr-shadowsocksrr-clients/)
*   [trojan客户端](https://tlanyan.me/trojan-clients-download/)
*   [WireGuard客户端](https://tlanyan.me/wireguard-clients/)

突然无法科学上网或者服务器被墙？请参考：[拯救被墙的服务器

## Linux命令行客户端proxychains 使用指北

### 序言

在经历了无数想象不到的折腾之后，我能找到的最优解就是在命令行界面使用proxychains来进行代理转发，使用起来十分的惬意。



### proxychains的安装



#### proxychains与proxychains-ng的区别

简单来说，前面安装的是3.1版本，proxychains-ng的使用命令是proxychains4，也就是4.0版本，更新了一些东西，但是除了使用命令上有区别外，对于我个人来说还没有碰到有很大区别的地方。



#### MAC 下brew安装

```shell
brew install proxychains-ng #这里安装的是4.0版本
```

#### Ubuntu下APT安装

```shell
 apt-get install proxychains # 这里安装的是3.1的旧版本
```

源码编译安装:

```shell
git clone https://github.com/rofl0r/proxychains-ng.git # 国内用户用加速链接更换成这个镜像地址https://github.91chifun.workers.dev//https://github.com/rofl0r/proxychains-ng.git
cd proxychains-ng # 切换目录
./configure
make && make install
cp ./src/proxychains.conf /etc/proxychains.conf
cd .. && rm -rf proxychains-ng
```

这里安装的是最新版的，国内用户请将第一条github地址更换成镜像加速地址，否则无法使用。

#### /etc/proxychains.conf配置修改

proxychains 与proxychains-ng 的配置文件都是/etc/proxychains.conf。

`/etc/proxychains.conf` 文件把最后一句修改为：

`socks5 127.0.0.1 1080` （这个1080是你的代理软件监控的端口，如果你监控的是25575，那就改成`127.0.0.1 25575`）
另外修改：
`proxy_dns 8.8.8.8` (我不改也能用，如果你不能用就改一下)

![image-20200619183505842](../../../../AppData/Roaming/Typora/typora-user-images/image-20200619183505842.png)

#### 命令测试

在命令前面加proxychains 即可，如上图所示。

如果你下载的是proxychains4，则使用proxychains4替代即可。





