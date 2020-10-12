---
title: Linux Shell脚本攻略
date: 2020-10-12 12:09:51
permalink: /pages/b54df2/
categories:
  - linux
  - Linux Shell脚本攻略
tags:
  - 
---
# Linux Shell脚本攻略

**Shell** 是系统的用户界面，提供了用户与内核进行交互操作的一种接口。它接收用户输入的命令并把它送入内核去执行。本页会汇总我学习Shell（Bash）中记录的所有笔记。

Bash （GNU Bourne\-Again Shell） 是许多Linux发行版的默认Shell。事实上，还有许多传统UNIX上用的Shell，例如tcsh、csh、ash、bsh、ksh等等，Shell Script大致都类同，当您学会一种Shell以后，其它的Shell会很快就上手，大多数的时候，一个Shell Script通常可以在很多种Shell上使用。

## 目录列表

*   [终端打印、算术运算、常用变量](http://man.linuxde.net/shell-script/shell-1)
*   从键盘或文件中获取标准输入：**[read命令](http://man.linuxde.net/read)**
*   [文件的描述符和重定向](http://man.linuxde.net/shell-script/shell-2)
*   [数组、关联数组和别名的使用](http://man.linuxde.net/shell-script/shell-3)
*   [函数的定义、执行、传参和递归函数](http://man.linuxde.net/shell-script/shell-4)
*   [条件测试操作与流程控制语句](http://man.linuxde.net/shell-script/shell-5)
*   获取时间日期格式和延时：**[date命令](http://man.linuxde.net/date)**、**[sleep命令](http://man.linuxde.net/sleep)**
*   [内部字段分隔符IFS和脚本的调试DEBUG](http://man.linuxde.net/shell-script/shell-6)
*   显示、读取或拼接文件内容：**[cat命令](http://man.linuxde.net/cat)**
*   文件查找与打印文件列表：**[find命令](http://man.linuxde.net/find)**
*   命令传参过滤器、命令组合工具：**[xargs命令](http://man.linuxde.net/xargs)**
*   字符转换、删除及压缩工具：**[tr命令](http://man.linuxde.net/tr)**
*   对文本进行排序、单一和重复操作：**[sort命令](http://man.linuxde.net/sort)**、**[uniq命令](http://man.linuxde.net/uniq)**
*   [切分文件名提取文件扩展名或提取文件名：**%、%%** 和 **#、##**](http://man.linuxde.net/shell-script/shell-7)
*   [Shell的正则表达式](http://man.linuxde.net/docs/shell_regex.html)
*   在文件中搜索文本工具：**[grep命令](http://man.linuxde.net/grep)**
*   按列切分文件字段工具：**[cut命令](http://man.linuxde.net/cut)**
*   文本处理流编辑器：**[sed命令](http://man.linuxde.net/sed)**
*   对文本和数据进行处理：**[awk编程](http://man.linuxde.net/awk)**
*   临时文件的命名方法与随机数：**[tempfile命令](http://man.linuxde.net/tempfile)**
*   创建任意大小的文件和分割任意大小的文件：**[dd命令](http://man.linuxde.net/dd)**、**[split命令](http://man.linuxde.net/split)**、**[csplit命令](http://man.linuxde.net/csplit)**
*   Linux文件比较，文本文件的交集、差集与求差：**[comm命令](http://man.linuxde.net/comm)**
*   使用命令下载网站文件或网页：**[wget命令](http://man.linuxde.net/wget)**、**[lynx命令](http://man.linuxde.net/lynx)**
*   命令行下的高级网络工具：**[curl命令](http://man.linuxde.net/curl)**
*   监视文件及目录访问信息并记录：**[inotifywait命令](http://man.linuxde.net/inotifywait)**
*   Linux系统日志的相关命令、文件和管理工具：**[logrotate命令](http://man.linuxde.net/logrotate)**、**[logger命令](http://man.linuxde.net/syslog)**
*   当前登录用户、启动日志及启动故障相关信息：[who命令](http://man.linuxde.net/who)、[w命令](http://man.linuxde.net/w)、[users命令](http://man.linuxde.net/users)、[uptime命令](http://man.linuxde.net/uptime)、[last命令](http://man.linuxde.net/last)、[lastb命令](http://man.linuxde.net/lastb)
*   计算命令执行花费的时间信息：[time命令](http://man.linuxde.net/time)
*   数据归档和解压缩：[tar命令](http://man.linuxde.net/tar)、[cpio命令](http://man.linuxde.net/cpio)、[gzip命令](http://man.linuxde.net/gzip)、[bzip2命令](http://man.linuxde.net/bzip2)、[zip命令](http://man.linuxde.net/zip)