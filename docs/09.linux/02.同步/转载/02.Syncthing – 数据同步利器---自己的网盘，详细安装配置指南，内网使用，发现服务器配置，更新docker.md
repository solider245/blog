---
title: Syncthing – 数据同步利器---自己的网盘，详细安装配置指南，内网使用，发现服务器配置，更新docker
date: 2020-10-12 12:09:51
permalink: /pages/98fa58/
categories:
  - 同步
  - 转载
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-28 22:52:21
 * @LastEditTime: 2020-07-28 22:52:29
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\同步\转载\Syncthing – 数据同步利器---自己的网盘，详细安装配置指南，内网使用，发现服务器配置，更新docker.md
 * @日行一善，每日一码
--> 
**目录**

*   [简介：](#_label0)
*   [一：官网及下载](#_label1)
*   [二：在linux下进行安装](#_label2)
    *   [1.下载](#_label2_0)
    *   [2.配置](#_label2_1)
    *   [3.运行](#_label2_2)
    *   [4.测试](#_label2_3)
*   [二：在Docker中安装](#_label3)
    *   [1.下载](#_label3_0)
    *   [2.运行](#_label3_1)
    *   [3.测试](#_label3_2)
*   [三：在windows中安装](#_label4)
    *   [1.下载](#_label4_0)
    *   [2.运行](#_label4_1)
    *   [3.配置](#_label4_2)
*   [四：基本配置](#_label5)
    *   [1.配置简介](#_label5_0)
    *   [2.配置中文.](#_label5_1)
    *   [3.配置WEB安全](#_label5_2)
    *   [4.配置设备名称](#_label5_3)
*   [五：添加远程设备](#_label6)
    *   [1.获取远程设备ID](#_label6_0)
    *   [2.本地设备添加远程设备](#_label6_1)
    *   [3.等待](#_label6_2)
*   [六：添加同步文件夹](#_label7)
    *   [1.删除默认文件夹](#_label7_0)
    *   [2.本地设备添加文件夹](#_label7_1)
*   [七：给远程设备添加同步文件夹](#_label8)
    *   [1.还是等待，我们使用的是全球发现服务器](#_label8_0)
    *   [2.配置远程设备共享文件夹路径](#_label8_1)
    *   [3.配置文件夹 ID](#_label8_2)
    *   [4.查看同步状态](#_label8_3)
*   [八:内部网络使用（固定IP），无法连接全球发现服务器](#_label9)
    *   [1.简介](#_label9_0)
    *   [2.配置](#_label9_1)
    *   [3.验证连通](#_label9_2)
*   [九:内部网络使用（动态IP），无法连接全球发现服务器](#_label10)
    *   [1.简介](#_label10_0)
    *   [2.命令参考](#_label10_1)
    *   [3.运行](#_label10_2)
    *   [4.生成节点配置URL](#_label10_3)
    *   [4.给节点配置URL](#_label10_4)
    *   [5.关闭手动指定的远程设备地址](#_label10_5)
    *   [6.测试](#_label10_6)
*   [结语：](#_label11)
*   [更新docker\-compose](#_label12)

---

[回到顶部](#_labelTop)

## 简介：

无论办公、文件共享、团队协作还是家庭照片、视频、音乐、高清电影的存储，我们常常都有文件同步和存储的需求。但随着国内各大网盘的花式阵亡或限速，早已没什么好选择了。好吧，我已经转战使用onedriver了，但是在单位里面，没有互联网，找开源的软件试试自己搭建吧。

自建网盘云储存同步服务的软件有很多， Seafile、NextCloud、ownCloud、BT Sync (Resilio Sync) 等。

而 Syncthing 则有着自己非常特别的优点，受到众多高手们的推荐，被誉为是 Resilio Sync / BT Sync 和 Dropbox 的最佳开源替代品。

Syncthing 最大的特色是采用了与 Resilio Sync (BitTorrent Sync) 类似的 P2P 分布式技术，无需中心服务器，即可让多台设备互相实时同步文件。

Syncthing 官方支持 Linux、Windows、OS X、FreeBSD、Solaris 等系统，并且有第三方的 iOS、Android 应用。

我选择它还有一个原因就是，它只需要一个文件就可以了。在linux下只有一个文件，在windows下也可以只有一个文件，当然还有一个GUI桌面程序。

[回到顶部](#_labelTop)

## 一：官网及下载

官网地址：[https://syncthing.net/](https://syncthing.net/)

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180314172937350-1039936169.png)

linux64位就是我主力使用的，放在一个fedora服务器上，不过是跑在docker里面。

SyncTrayzor是官方提供的GUIwindows客户端，方便设置开机启动进行自动同步。可以缩小到任务栏。实在是方便部署到客户端，让它自动上传啊。

SyncTrayzor维护在github。[https://github.com/canton7/SyncTrayzor/releases](https://github.com/canton7/SyncTrayzor/releases)

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180314173504678-794314394.png)

Portable是免安装版本。

Setup就是安装版本。

X64 X86,根据你的系统，随便下载吧。

[回到顶部](#_labelTop)

## 二：在linux下进行安装

### 1.下载

随你喜欢wget curl winscp了。解压后只需要一个文件：

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180314173836597-39216564.png)

### 2.配置

#### 2.1复制文件

cp syncthing /usr/bin/syncthing

只需要复制这一个文件，其他的可以删了。

#### 2.2修改权限

chmod +x /usr/bin/syncthing

加上可执行权限

#### 2.3运行

./usr/bin/syncthing

就这一个文件，直接执行。

它会自动生成配置文件，还不能先改，只好运行一遍，等它出现

\[CKEAY\] 17:44:53 INFO: Detected 1 NAT service
\[CKEAY\] 17:45:39 INFO: Joined relay relay://36.229.223.123:22067
大概就是已经生成配置文件，并运行起来了。

ctrl+c 停止这个进程。

#### 2.4修改配置文件

sed 's/127.0.0.1/0.0.0.0/g' /root/.config/syncthing/config.xml

默认配置文件在/root/.config/syncthing/config.xml，默认监听网络是127.0.0.1，远程不能访问，所以用sed命令修改为0.0.0.0

### 3.运行

./usr/bin/syncthing

再次运行起来。

### 4.测试

http://youip:8384/     或者  http://hostname:8384/ 都可以访问，记得改你的ip，或者网络名。复制不能用。

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180314175342597-1043908804.png)

只要没出乱七八糟的错误，就算安装成功了。

[回到顶部](#_labelTop)

## 二：在Docker中安装

### 1.下载

docker pull syncthing/syncthing

### 2.运行

docker run \-it  \-p 8384:8384 \-p 22000:22000 \\
    \-v /storage/conf/syncthing:/var/syncthing/config \\
    \-v /storage/data/syncthing:/var/syncthing \\
    syncthing/syncthing:latest

官方给的运行参数就是这样了。

/storage/conf/syncthing，配置文件存储位置。

/storage/data/syncthing，数据存储主目录。

两个目录根据自己的情况替换。

8384  22000，两个端口一般不占用，直接运行。

### 3.测试

和linux测试一样。

http://youip:8384/     或者  http://hostname:8384/ 都可以访问，记得改你的ip，或者网络名。复制不能用。

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180314175342597-1043908804.png)

只要没出乱七八糟的错误，就算安装成功了。

[回到顶部](#_labelTop)

## 三：在windows中安装

### 1.下载

windows下我们就不使用linux那样的单文件版了。

[https://github.com/canton7/SyncTrayzor/releases/download/v1.1.21/SyncTrayzorPortable\-x64.zip](https://github.com/canton7/SyncTrayzor/releases/download/v1.1.21/SyncTrayzorPortable-x64.zip)

目前最新的应该是这个版本。如果你是32位的系统，请下载[x86版](https://github.com/canton7/SyncTrayzor/releases/download/v1.1.21/SyncTrayzorPortable-x86.zip)。

### 2.运行

解压后找到SyncTrayzor.exe，双击运行即可

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180314175929740-856155834.png)

### 3.配置

还是老问题，默认只有127.0.0.1，localhost可以访问，没有远程访问权限。

照下图，右边的设置，用来修改图形界面监听地址，并且可以设置随开机自动启动

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180314180140731-2017142262.png)

 ![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180314180345124-659456150.png)

[回到顶部](#_labelTop)

## 四：基本配置

### 1.配置简介

我们要配置自动同步，那么就要有2台电脑运行syncthing，相互要能连通，并配置相同ID的共享文件夹。

每台电脑，第一次运行syncthing时，会自动生成随机ID，并注册ID,网络地址到全球发现服务器。添加远程设备时，去全球发现服务器，来查ID，取得远程设备的网络地址。

所以，在windows不要复制解压运行过的[SyncTrayzorPortable\-x64.zip](https://github.com/canton7/SyncTrayzor/releases/download/v1.1.21/SyncTrayzorPortable-x64.zip)，只复制压缩包，解压，重新生成新的ID。

后面的例子以2台设备同步一个文件夹为例讲解。设备1：WORKER（操作机，本地设备），设备2： NUC（家庭服务器，放在路由器边上，没键盘，没鼠标，只接了HDMI到电视，远程设备） 同步一个文件夹，WORKER路径：D:\\PythonTest\\flasktest ，nuc路径：/var/syncthing/temp/app。WORKER操作系统windows，NUC操作系统fedora，syncthing运行在docker中，映射容器路径 /var/syncthing到物理路径/storage,那么最后的共享文件夹，即NUC物理机的/storage/temp/app。对这些不理解的，自己慢慢补docker的知识。忽略NUC运行的DOCKER。

### 2.配置中文.

如下图，先点English，在弹出的下拉框，点击Chinese（china），就变成中文了。

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317024801061-1388212297.png)

### 3.配置WEB安全

我们输入地址：8384，默认设置，syncthing只允许localhost本地登录，但是我们为了方便配置，已经给它改了监听0.0.0.0，任意地址都可以访问，貌似不安全啊。

那么我们就配置一下web登录密码：

访问web页面后在右上角 ，操作\-\-设置\-\-图形用户界面

图形管理界面用户名

图形管理界面密码

这两项就可以设置图形界面登录账户密码了。

使用加密连接到图形管理页面

如果你怕被监听到，开启加密也可以。

每个运行syncthing的机器（WORKER NUC）都要单独设置。

### 4.配置设备名称

访问web页面后在右上角 ，操作\-\-设置\-\-常规\-\-设备名

为了方便使用，还是设个设备名吧，不然貌似是使用ID前几位的随机字符串做设备名，机器多了，可真不方便。

还是每个设备设置。

[回到顶部](#_labelTop)

## 五：添加远程设备

### 1.获取远程设备ID

在WORKER上添加NUC。

你时去NUC抄，还是远程登录看？当然时远程登录看了，安装的时候，我都设置了任意IP监听登录。

访问NUCweb页面后在右上角 ，操作\-\-显示ID，

BTQMGH2\-JBPTQGX\-HQWBLLW\-EBEQJUC\-NMZOUMQ\-3TLYVSV\-\*\*\*\*\-\*\*\*\*

这一长串就是远程设备的ID。下面的二维码时方便android手机端使用的扫码添加。

### 2.本地设备添加远程设备

访问WORKERweb页面（或SyncTrayzor窗口）后在右下角 ，添加远程设备

在设备ID，填上刚复制过来的远程设备ID。

下面有两个选项介绍一下：

作为中介，syncthing使用了P2P技术来实现文件同步，现在我们实验的时候时2台设备，同步一个文件夹，如果加入新设备，是要分别给这两台设备配置一个新的远程设备。如果开启作为中介，那么，WORKER，会自动添加，或称为同步NUC的远程设备（新设备）。

自动接受，如果在NUC创建了一个共享文件夹，并共享给WORKER，无需WORKER选择接受，即在默认目录，创建共享文件夹，并同步。

根据自己的需要来选择开启吧。我都没开启，因为我实验2台设备，部署也就3\-4个设备。

### 3.等待

因为默认使用全球发现服务器，受网速影响，还是要等等的。

注意NUC的web界面。出现新设备，就是已经连上了，选择添加设备，就会自动把WORKER，作为远程设备，连接到NUC。

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317032126584-1197560648.png)

此时两台设备web页面，右下角部分，都会出现远程设备（即对方）

[回到顶部](#_labelTop)

## 六：添加同步文件夹

### 1.删除默认文件夹

貌似新装，管理页左边都会出现 default \*\*\*

点击 文件夹名\-\-下拉框右下部分\-\-选项\-\-移除\-\-确认

删除是因为路径问题，它们分别生成在每台设备的默认共享目录下，基本不是我们需要的路径。

### 2.本地设备添加文件夹

管理页中间部分，添加文件夹。

文件夹路径，估计要你自己写一下了（D:\\PythonTest\\flasktest ），到资源管理器去复制也可以的。

关键设置文件夹ID（app） ，说明在所有从设备上必须一致，也就是在我们这多个设备同步时，都用这个ID，来同步这个文件夹。下面还有共享给远程设备（NUC），勾选远程设备的名字就好了。

其中的高级设置，看一下也能明白。最后保存即可。

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317033022532-1492996890.png)

[回到顶部](#_labelTop)

## 七：给远程设备添加同步文件夹

### 1.还是等待，我们使用的是全球发现服务器

直到这个在NUC的管理页面出现，点击添加即可。

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317033452512-1499026286.png)

### 2.配置远程设备共享文件夹路径

/var/syncthing/temp/app

这个应该时前期就决定好的，这时填一下就可以了，记得勾选下面的共享给WORKER。不勾选的时候是单向同步？

### 3.配置文件夹 ID

app

这个也是在本地设备配置文件夹时给定的ID

### 4.查看同步状态

看下面两个图，区别是远程设备是否显示同步完成，因为使用P2P 分布式技术，所以没有中心服务器，那么每台设备，都即是客户端，又是服务器。

文件夹上的同步完成，仅代表本地客户端已经和本地服务器同步了。（两台设备没完成完全同步）

远程设备上的同步完成，代表本地客户端和这个远程服务器同步了。（两台设备完成完全同步）

有的时候那个同步完成，会显示同步中。

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317100243336-1150981568.png)![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317100448172-1224734178.png)

[回到顶部](#_labelTop)

## 八:内部网络使用（固定IP），无法连接全球发现服务器

### 1.简介

当我们在内部网络使用syncthing时，因为没有办法连接全球发现服务器，那么我们该如何配置呢？这章节说明一下在固定IP的情况下，我们可以使用IP地址来配置互相发现。只要能互相ping通，跨网段也没关系的。

我们在官方的DOCKER运行命令中可以看出映射两个端口出来，8384和22000，8384是我们用来web控制的，那么22000就是syncthing的监听端口了。

### 2.配置

看下面两图，这时编辑已经建立连接的远程设备，新建设备时也一样，我在地址列表中填入了远程设备的协议,IP,端口。看说明，host计算机名字也可以，域名应该也可以。

dynamic，就是自动发现，也是默认值，难道时自动扫描么？删除也可以。

 ![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317101850077-266944207.png)

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317101911126-66131779.png)

### 3.验证连通

下面两图，都是连接断开的状态，不过，我这两台设备，都能连接互联网，估计获取了发现服务器记录的地址。但这并不影响我们做测试。

第二张图看出地址多了一行我们配置的tcp://192.168.1.4:22000

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317102401709-1356112089.png)

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317102330278-489327615.png)

下面两图是使用dynamic时的连通状态，真不知道时什么IP地址。

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317102825274-857643138.png)

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317102838073-1004480991.png)

下面两图就是都配置对方地址后的连通状态了。使用对方的网络地址连接。

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317103053281-442929493.png)

 ![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317103104449-372361120.png)

[回到顶部](#_labelTop)

## 九:内部网络使用（动态IP），无法连接全球发现服务器

### 1.简介

上一章节我们使用固定ip，可以通过填写对方的网络连接参数来配置远程设备。如果同网段动态IP，应该也可以用host计算机名来配置远程设备。

那么另一个麻烦又跳出来了，如果是不同网段，又是动态IP，怎么办？连接参数中IP是变动的，计算机名时无法广播解析的。或许可以建个DNS服务器来实现。

太扯了。又可能影响原来的DNS解析。

Syncthing Discovery Server\-\-\-syncting发现服务器来解救你，你这么复杂的运行环境，相信会有一个小型服务器的，只要有一个固定IP，就可以了。几十台设备，几百台设备，都可以注册到这个发现服务器，替代全球发现服务器。

发现服务介绍https://docs.syncthing.net/users/stdiscosrv.html        发现服务源码 https://github.com/syncthing/discosrv   发现服务下载：https://github.com/syncthing/discosrv/releases

### 2.命令参考

stdiscosrv \[\-cert\=<file\>\] \[\-db\-dir\=<string\>\] \[\-debug\] \[\-http\] \[\-key\=<string\>\] \[\-listen\=<address\>\] \[\-metrics\-listen\=<address\>\] \[\-replicate\=<peers\>\] \[\-replication\-listen\=<address\>\]

\-cert=<file>
    证书文件(default “./cert.pem”).

\-db\-dir=<string>
   数据存储目录 (default “./discovery.db”).

\-debug
    debug模式输出

\-http
    使用http协议还要求在https代理后面 (behind an HTTPS proxy).

\-key=<file>
    key文件 (default “./key.pem”).

\-listen=<address>
    监听端口 (default “:8443”).

\-metrics\-listen=<address>
    不知道是什么意思 (default disabled).

\-replicate=<peers>
    复制另一台发现服务器？

\-replication\-listen=<address>
    另一台发现服务器监听端口？

### 3.运行

syncthing真是良心，也不用复杂的安装，linux下也不用编译，不论linux还是windows，都是一个文件，直接运行。而且这个发现服务器，看着挺多的运行参数，其实一个也不用写。它和单文件的客户端一样，直接运行就可以了，自动生成各个目录和文件。

windows下是这样

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317114459863-872821546.png)

linux下是这样

![](https://images2018.cnblogs.com/blog/1241143/201803/1241143-20180317114942482-1882634831.png)

如果你有自己的证书，那么可以这样运行，把证书路径作为参数，启动发现服务器。

stdiscosrv \-cert=/path/to/cert.pem \-key=/path/to/key.pem

### 4.生成节点配置URL

如果您使用的是非CA签名证书，则必须将该设备ID（指纹）交给使用发现服务器URL的客户机。

这个客户机的意思时对发现服务器，所有运行syncthing的节点都是发现服务器的客户机。

非CA签名的证书，自动生成的一定时非CA签名证书。

官方给的示例是这样的

https://disco.example.com:8443/?id=7DDRT7J\-UICR4PM\-PBIZYL3\-MZOJ7X7\-EX56JP6\-IK6HHMW\-S7EK32W\-G3EUPQA

看到那串像序列号的东西，就是设备ID，启动发现服务器的时候，它也显示出来了。记下来，用来组合我们自己的发现服务器地址。

本来就内网了，域名就算了，可以使用IP地址。

对应上面启动的两个发现服务器。

windows：IP    192.168.1.4

URL      https://192.168.1.4:8443/?id=ZRXXI2M\-XEARVGA\-SSYYEWO\-6QGNNIZ\-HPBVH3K\-PIR6DCY\-HJERGZE\-PXF7NAL

linux: IP 192.168.1.3

URL    http://192.168.1.3:8443/?id=5OJDGM7\-BZ6EJT2\-M2BEAIX\-MK2SBMY\-N4STHNI\-MEP3VKO\-RI6H27D\-PYXTPAB

如果你有CA签名的证书，那么URL就不需要ID参数了。

https://disco.example.com:8443/      https://disco\_server\_ip:8443/

### 4.给节点配置URL

管理界面，右上角  操作\-\-设置\-\-连接

全球发现服务器，删除原来的default，填上我们生成的节点配置URL。

提示重启syncthing，重启一下就可以了。

### 5.关闭手动指定的远程设备地址

远程设备\-\-选项\-\-地址列表

原来的：tcp://192.168.1.4:22000,dynamic

改为：dynamic

### 6.测试

其实就是看远程设备的地址，原来我们使用defalut全球发现服务器的时候，远程设备地址，反正是我不认识的地址。

当我们配置了远程设备IP地址之后，远程设备地址，是我们配置的远程设备地址。

现在我们取消了远程设备地址，使用了我们自己的发现服务器地址。

也就是syncthing，把自己注册到我们自己的发现服务器上，并根据ID从我们自己的发现服务器地址，查找远程设备地址。

如果远程设备地址，是我们的内部网IP地址，并可以显示同步完成。

那就一切OK了。

[回到顶部](#_labelTop)

## 结语：

syncthing，使用方便，配置方便，在各大网盘纷纷关停，收费，限速………………因素下。

自己搭建一个，也挺好。或者百度搜索5T onedriver已失效。

我的用途呢，其实是在进行软件开发的时候。worker编写了源代码，server生成docker，以前用ftp，sftp上传，然后docker build。

文件少的时候还好，文件多的时候，又覆盖，那是一个慢啊。都在一个局域网，又没必要使用github的自动构建，用自动构建，还要等docker hub 服务器空暇。

现在是把woker的源码文件夹，同步到server的docker build目录。docker build的时候把源码copy进镜像。编译前还可以到web管理界面扫描同步一下。

尤其时源码只改几个文件的时候，同步很快。方便了我这个伪全栈的开发过程。

个人现在比较喜欢在服务器上使用docker作为服务。官方提供了linux\_syncthing的dockre镜像。

我还需要一个linux\_stdiscosrv的镜像。这几天写好了，把地址给大家。

写着也挺快，但这篇教程，又臭又长，让我休息一下吧。

[回到顶部](#_labelTop)

## 更新docker\-compose

更新一个docker\-compose文件，用来使用docker\-compose启动。同时包含syncthing 和 discosrv。

不需要discosrv的可以删掉。

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")

version: '2' services:
    syncthing:
        image: syncthing/syncthing
        container\_name: syncthing
        volumes: \- syncthing\_con=/var/syncthing/config \- /opt/data=/var/syncthing"\]
 ports : \- "8384:8384"
            \- "22000:22000"
            \- "21027:21027/udp" networks: \- sync\_net
        restart: always
    discosrv:
        image: syncthing/discosrv
        container\_name: discosrv
        volumes: \- discosrv\_con=/var/stdiscosrv
        ports : \- "19200:19200"
            \- "8443:8443" networks: \- sync\_net
        restart: always

networks:
    sync\_net:
volumes:
    syncthing\_con:
    discosrv\_con:

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0); "复制代码")