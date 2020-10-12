---
title: Linux设置显示中文和设置字体
date: 2020-10-12 12:09:51
permalink: /pages/8d8f51/
categories:
  - linux
  - 主题配置
tags:
  - 
---
# Linux设置显示中文和设置字体

## 设置中文

#### 一、查看当前使用的系统语言

登陆linux系统打开操作终端之后，输入 **echo $LANG**可以查看当前使用的系统语言。如

```bash
echo $LANG

```

![](https://upload-images.jianshu.io/upload_images/14270006-d243829ab9ca48c9.png?imageMogr2/auto-orient/strip|imageView2/2/w/279/format/webp)

image.png

2.**查看安装的语言包**

查看是否有中文语言包可以在终端输入 **locale**命令，如有zh cn 表示已经安装了中文语言

```undefined
locale

```

![](https://upload-images.jianshu.io/upload_images/14270006-a031729a47e7dfbc.png?imageMogr2/auto-orient/strip|imageView2/2/w/270/format/webp)

image.png

3.**如果没有中文语言呢**

可以通过网上下载安装中文语言包***yum groupinstall chinese\-support***

或者sudo apt\-get install language\-pack\-zh\-han\*

```csharp
sudo apt-get install  language-pack-zh-han*

```

4.**如何修改系统语言为中文**

*   **临时更换语言**

如果只是临时更换linux系统的语言环境，可以通过输入设置 LANG=语言名称， 如中文是 zh\_CN.UTF\-8

```bash
LANG="zh_CN.UTF-8"

```

![](https://upload-images.jianshu.io/upload_images/14270006-2eb32dd83f12134b.png?imageMogr2/auto-orient/strip|imageView2/2/w/331/format/webp)

image.png

*   **修改系统默认语言**

以上方法是通过修改设置系统默认的语言配置

如***vi /etc/sysconfig/i18n***（注意改好之后重启一下系统）

```undefined
vi  /etc/sysconfig/i18n

```

![](https://upload-images.jianshu.io/upload_images/14270006-d0310c9795951f72.png?imageMogr2/auto-orient/strip|imageView2/2/w/221/format/webp)

[

image

](https://images0.cnblogs.com/blog/7833/201503/120908176676015.png)

```csharp
vi /etc/default/locale
#将原来的配置内容修改为
中文设置为：
LANG="zh_CN.UTF-8" 
LANGUAGE="zh_CN:zh" 
LANG="zh_CN.UTF-8"
LANGUAGE="zh_CN:zh"
#注销或重启后，中文的语言环境。
#英文设置为：
#LANG="en_US.UTF-8" 
#LANGUAGE="en_US:en" 
#LANG="en_US.UTF-8"
#LANGUAGE="en_US:en"
```

![](https://upload-images.jianshu.io/upload_images/14270006-d9ffcf5ec504fbb5.png?imageMogr2/auto-orient/strip|imageView2/2/w/240/format/webp)

image.png

## 设置字体

#### 一、查看系统字体

在开始安装之前，我们先查看系统中已经安装的字体。

要查看系统中已经安装的字体，我们可以使用fc\-list命令进行查看。如果系统中没有该命令的话，我们需要先安装相关的软件包。

在centos上，使用如下命令进行安装：

```undefined
yum install -y fontconfig mkfontscale

```

在ubuntu上，使用如下命令进行安装：

```csharp
sudo apt-get -y install fontconfig xfonts-utils

```

安装完毕后，我们就可以使用fc\-list命令查看系统中已经安装的字体。如下：

```undefined
cat /etc/issue

```

```bash
fc-list

```

![](https://upload-images.jianshu.io/upload_images/14270006-cc95607a16271fa1.png?imageMogr2/auto-orient/strip|imageView2/2/w/642/format/webp)

ubuntu.png

上图为ubuntu上，默认已经安装的字体。

如果要查看系统中已经安装的中文字体，我们可以使用如下命令：

```ruby
fc-list :lang=zh

```

通过命令，我们可以看到默认情况下centos6和ubuntu是没有安装中文字体的。

#### 二、安装字体

通过第一章节，我们知道目前系统中没有微软雅黑字体。我们现在需要把MSYH.TTF（微软雅黑字体文件）文件上传到linux服务器上。如下：

![](https://upload-images.jianshu.io/upload_images/14270006-5e3232c2cb97b799.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

image.png

![](https://upload-images.jianshu.io/upload_images/14270006-6c93809a27c6526b.png?imageMogr2/auto-orient/strip|imageView2/2/w/1024/format/webp)

image.png

在centos上和ubuntu上安装字体方法都是一样的，我们只需要进行相关的操作即可。

把MSYH.TTF复制到/usr/share/fonts/目录下，使用如下命令：

```bash
cd /root/

```

```undefined
cp MSYH.TTF /usr/share/fonts/

```

然后建立字体索引信息，更新字体缓存，使用如下命令：

```bash
cd /usr/share/fonts/

```

```undefined
mkfontscale

```

```undefined
mkfontdir

```

```bash
fc-cache

```

至此，字体已经安装完毕。

现在我们再来查看微软雅黑字体，是否安装成功，使用如下命令：

fc\-list :lang=zh

![](https://upload-images.jianshu.io/upload_images/14270006-61f742fcc4c59c63.png?imageMogr2/auto-orient/strip|imageView2/2/w/675/format/webp)

image.png

通过上图，我们可以很明显的看出微软雅黑字体已经成功安装。