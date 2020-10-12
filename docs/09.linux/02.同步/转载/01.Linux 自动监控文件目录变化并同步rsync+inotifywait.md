---
title: Linux 自动监控文件目录变化并同步rsync+inotifywait
date: 2020-10-12 12:09:51
permalink: /pages/aef25e/
categories:
  - 同步
  - 转载
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-28 22:54:15
 * @LastEditTime: 2020-07-28 22:54:28
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\同步\转载\Linux 自动监控文件目录变化并同步rsync+inotifywait.md
 * @日行一善，每日一码
--> 
# 介绍

有时候我们常需要当文件变化的时候便触发某些脚本操作，比如说有文件更新了就同步文件到远程机器。在实现这个操作上，主要用到两个工具，一个是rsync，一个是inotifywait 。inotifywait的作用是监控文件夹变化，rsync是用来同步，可同步到本机的其他目录或者远程服务器上。

# 安装rsync

```bash
wget http://rsync.samba.org/ftp/rsync/src/rsync-3.1.1.tar.gz
tar zxvf rsync-3.1.1.tar.gz
./configure –prefix=/usr/local/rsync-3.1.1
make
make install

```

# 安装inotifywait

```bash
wget http://github.com/downloads/rvoicilas/inotify-tools/inotify-tools-3.14.tar.gz
tar zxvf inotify-tools-3.14.tar.gz
cd inotify-tools-3.14
./configure
make
make install

```

# 创建并运行脚本

新建脚本inotifywait.sh 并输入以下内容

```bash
#!/bin/bash
export CNROMS_SRC=/home/ftpuser/gri/   # 同步的路径，请根据实际情况修改
inotifywait --exclude '\.(part|swp)' -r -mq -e  modify,move_self,create,delete,move,close_write $CNROMS_SRC |
  while read event;
    do
    rsync -vazu --progress  --password-file=/etc/rsyncd_rsync.secret  /home/ftpuser/gri/sla  rsync@10.208.1.1::gri ##这里执行同步的命令，可以改为其他的命令

  done

```

然后执行下面命令，会在后台执行监控：

```bash
nohup sh inotifywait.sh > /dev/null 2>&1

```

然后就可以关闭命令行窗口了。