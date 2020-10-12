---
title: Jenkins+Gogs搭建自动化部署平台
date: 2020-10-12 12:09:51
permalink: /pages/384a9a/
categories:
  - linux
  - jenkins
tags:
  - 
---
# 1、安装Gogs

> （1）、配置数据库（以mysql为例）

```csharp
  #创建gogs数据库
  create database gogs;

  #创建gogs数据库用户
  create user 'gogs'@'localhost' identified by 'your-password';
  grant all privileges on gogs.* to 'gogs'@'localhost';
  flush privileges;

```

> （2）、配置Git

```bash
#git版本需 >= 1.7.1
git version
git version 2.15.1

#创建git用户
sudo  adduser  git
#切换至git用户
su  git

```

> （3）、下载安装Gogs

*   返回根目录

```bash
cd  ~

```

*   下载安装包

```cpp
wget  https://dl.gogs.io/0.11.79/gogs_0.11.79_linux_amd64.tar.gz

```

*   解压安装包

```css
tar  -xzvf  gogs_0.11.79_linux_amd64.tar.gz

```

*   进入解压后的目录

```bash
cd  gogs

```

*   编辑配置文件

```php
vim ./scripts/init/debian/gogs

PATH=/sbin:/usr/sbin:/bin:/usr/bin
DESC="Go Git Service"
NAME=gogs
SERVICEVERBOSE=yes
PIDFILE=/var/run/$NAME.pid
SCRIPTNAME=/etc/init.d/$NAME
WORKINGDIR=/home/git/gogs #这个根据自己的目录修改
DAEMON=$WORKINGDIR/$NAME
DAEMON_ARGS="web"
USER=git  #如果运行gogs不是用的这个用户，修改对应用户

```

*   切换到root账户/复制命令/增加命令权限

```kotlin
sudo cp /home/git/gogs/scripts/init/debian/gogs /etc/init.d/

sudo chmod +x /etc/init.d/gogs

```

*   配置service命令

```undefined
cp /home/git/gogs/scripts/systemd/gogs.service /etc/systemd/system/

```

*   启动Gogs

```undefined
sudo service gogs start
或
sudo /home/git/gogs/gogs web

```

*   浏览器访问完成安装

```csharp
http://localhost:3000/install

# Gogs配置文件在 /home/git/gogs/custom/conf/app.ini
# 进入安装页后按照提示填写完成最终安装~

```

![](https://upload-images.jianshu.io/upload_images/1774338-38ce2d2346ae2045.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

Gogs

# 2、安装jenkins

> （1）、安装JDK

```undefined
yum install -y java

```

> （2）、安装jenkins

**添加Jenkins库到yum库，Jenkins将从这里下载安装**

```swift
wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo

rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key

yum install -y jenkins

```

**如果不能安装就到官网下载jenkis的rmp包，官网地址（[http://pkg.jenkins\-ci.org/redhat\-stable/](http://pkg.jenkins-ci.org/redhat-stable/)）**

```cpp
wget http://pkg.jenkins-ci.org/redhat-stable/jenkins-2.7.3-1.1.noarch.rpm

rpm -ivh jenkins-2.7.3-1.1.noarch.rpm

```

**配置jenkins端口号**

```bash
 vi /etc/sysconfig/jenkins

# 找到修改端口号：
JENKINS_PORT="8088"  此端口不冲突可以不修改

```

> （3）、启动jenkins

```undefined
service jenkins start/stop/restart

```

*   安装成功后Jenkins将作为一个守护进程随系统启动
*   系统会创建一个“jenkins”用户来允许这个服务，如果改变服务所有者，同时\-
    需要修改/var/log/jenkins, /var/lib/jenkins, 和/var/cache/jenkins的所有者
*   启动的时候将从/etc/sysconfig/jenkins获取配置参数
    默认情况下，Jenkins运行在8080端口，在浏览器中直接访问该端进行服务配置
*   Jenkins的RPM仓库配置被加到/etc/yum.repos.d/jenkins.repo

> （4）、打开jenkins

```csharp
在浏览器中访问 http://IP:端口
首次进入会要求输入初始密码如下图，
初始密码在：/var/lib/jenkins/secrets/initialAdminPassword

```

![](https://upload-images.jianshu.io/upload_images/1774338-26bd26abe727d838.png?imageMogr2/auto-orient/strip|imageView2/2/w/558/format/webp)

**选择“Install suggested plugins”安装默认的插件，下面Jenkins就会自己去下载相关的插件进行安装**

![](https://upload-images.jianshu.io/upload_images/1774338-e90832364d5a08d6.png?imageMogr2/auto-orient/strip|imageView2/2/w/558/format/webp)

![](https://upload-images.jianshu.io/upload_images/1774338-41ed02f96230268e.png?imageMogr2/auto-orient/strip|imageView2/2/w/558/format/webp)

**创建超级管理员账号**

![](https://upload-images.jianshu.io/upload_images/1774338-56ada88d9ffde0b1.png?imageMogr2/auto-orient/strip|imageView2/2/w/558/format/webp)

![](https://upload-images.jianshu.io/upload_images/1774338-7c7966a96132d401.png?imageMogr2/auto-orient/strip|imageView2/2/w/558/format/webp)

> （5）、创建项目

![](https://upload-images.jianshu.io/upload_images/1774338-4b91e5c5f7984961.png?imageMogr2/auto-orient/strip|imageView2/2/w/1132/format/webp)

**其它配置项先默认即可**

# 3、Jenkins配置Gogs webhook插件

> （1）、进入jenkins平台打开 系统管理 \-> 管理插件 \-> 可选插件，在右上角输入框中输入"gogs"来筛选插件：

![](https://upload-images.jianshu.io/upload_images/1774338-c31234611c96d3f8.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

> （2）、gogs中仓库配置

*   1、进入对应的仓库，点击仓库设置

![](https://upload-images.jianshu.io/upload_images/1774338-20def0c434ca2d1e.png?imageMogr2/auto-orient/strip|imageView2/2/w/1123/format/webp)

*   2、添加webhook

**点击 管理Web钩子 \-> 添加Web钩子 \-> 选择Gogs**

![](https://upload-images.jianshu.io/upload_images/1774338-3307b869943b91a2.png?imageMogr2/auto-orient/strip|imageView2/2/w/1078/format/webp)

*   3、添加如下配置：

![](https://upload-images.jianshu.io/upload_images/1774338-8b12403b6ed0ca49.png?imageMogr2/auto-orient/strip|imageView2/2/w/1005/format/webp)

**推送地址的格式为：**

```ruby
http(s)://<你的Jenkins地址>/gogs-webhook/?job=<你的Jenkins任务名>

```

*   4、点击 推送测试，如 成功 会看到下推送记录

![](https://upload-images.jianshu.io/upload_images/1774338-a4bb30884ad26863.png?imageMogr2/auto-orient/strip|imageView2/2/w/792/format/webp)

# 4、Jenkins配置构建远程服务器

> （1）、进入jenkins平台 \-> 安装插件 \-> 搜索 Publish Over SSH 并安装

![](https://upload-images.jianshu.io/upload_images/1774338-8cdfe48a1befb97e.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

> （2）、重启Jenkins服务

```undefined
service jenkins restart

```

> （3）、配置服务器密钥认证
> 注：
> A服务器：jenkins所在服务器 (192.168.100.101)
> B服务器：目标线上服务器 (192.168.100.100)

*   1、服务器A上生成密钥

```undefined
ssh-keygen -f jenkins

```

*   2、查看生成的公钥

```jsx
cat ~/.ssh/jenkins.pub

```

*   3、登录服务器B将服务器A生成的公钥加入authorized\_keys

```jsx
vim  ~/.ssh/authorized_keys

```

*   4、jenkins配置 Publish Over SSH

**进入Jenkins平台，点击 系统管理 \-> 系统设置 \-> 找到 Publish Over SSH 配置项**

```ruby
# 查看并拷贝服务器A的私钥

cat ~/.ssh/jenkins

```

![](https://upload-images.jianshu.io/upload_images/1774338-aba1b6f70f5e3f36.png?imageMogr2/auto-orient/strip|imageView2/2/w/1066/format/webp)

**注：Jenkins SSH Key 这一栏默认会使用Jenkins管理员admin账户的密码，可以不填则设置为空密码**

*   5、项目Git项相关配置

**打开项目（test）配置页**

![](https://upload-images.jianshu.io/upload_images/1774338-a519c5abb2296f9a.png?imageMogr2/auto-orient/strip|imageView2/2/w/985/format/webp)

*   6、建构触发器配置

**构建触发器，以及构建环境都不需要配置，因为我们发布的是php代码！**

![](https://upload-images.jianshu.io/upload_images/1774338-5a101b6ffba5e0b7.png?imageMogr2/auto-orient/strip|imageView2/2/w/1126/format/webp)

*   7、构建项配置

**最核心的一步，选择"Send files or execute commands over SSH"**

![](https://upload-images.jianshu.io/upload_images/1774338-0dd619f111284136.png?imageMogr2/auto-orient/strip|imageView2/2/w/1162/format/webp)

**简单说明**

*   SSH Server，Name 选择对应的服务器，
*   Transfers, Source files填写**/**，表示全部文件
*   Remove prefix可以指定截掉的前缀目录，这里留空即可，
*   Remote directory指定远程服务器上代码存放路径，比如/data/wwwroot/[www.aaa.com](http://www.aaa.com)
*   Exec command为文件传输完成后要执行的命令，比如可以是更改文件权限的命令，设置完成后点击 “Add Transfer Set”，如果还有另外的机器，可以点击 “Add Server”重复以上操作

# 5、推送自动构建测试

**Gogs上关联的仓库（test）master分支下push一条修改记录后，会发现jenkins上自动完成本地push的远程构建**

![](https://upload-images.jianshu.io/upload_images/1774338-1b6766bf6f9cb9dc.png?imageMogr2/auto-orient/strip|imageView2/2/w/1156/format/webp)

![](https://upload-images.jianshu.io/upload_images/1774338-45742be5bb1e5757.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

**查看远程服务器（B）目录情况**

![](https://upload-images.jianshu.io/upload_images/1774338-c44d105c61e75fbe.png?imageMogr2/auto-orient/strip|imageView2/2/w/466/format/webp)

线上服务器B

---

**OK~~ 整个Jenkins+Gogs自动化部署平台完成 ~~**

---

**注：**

*   1、私有库项目Jenkins中Git项授权配置

![](https://upload-images.jianshu.io/upload_images/1774338-962bf0ba63963e38.png?imageMogr2/auto-orient/strip|imageView2/2/w/1000/format/webp)

添加授权凭证

![](https://upload-images.jianshu.io/upload_images/1774338-661bed2ef2f47c16.png?imageMogr2/auto-orient/strip|imageView2/2/w/1055/format/webp)

添加授权凭证

![](https://upload-images.jianshu.io/upload_images/1774338-c969fb173b981d35.png?imageMogr2/auto-orient/strip|imageView2/2/w/976/format/webp)

授权成功

4人点赞

[学习笔记](https://www.jianshu.com/nb/7425433)