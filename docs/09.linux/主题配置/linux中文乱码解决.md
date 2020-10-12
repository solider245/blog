---
title: linux中文乱码解决
date: 2020-10-12 12:09:51
permalink: /pages/c095e0/
categories:
  - linux
  - 主题配置
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-15 17:27:14
 * @LastEditTime: 2020-07-15 17:28:09
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\主题配置\linux中文乱码解决.md
 * @日行一善，每日一码
--> 
# locale

在RedHat/CentOS系统下，记录系统默认使用语言的文件是/etc/sysconfig/i18n,如果默认安装的是中文的系统，i18n的内容如下：

LANG="zh\_CN.UTF\-8"

SYSFONT="latarcyrheb\-sun16"
[链接](http://example)
SUPPORTED="zh\_CN.UTF\-8:zh\_CN:zh"

其中LANG变量是language的简称，稍微有英语基础的用户一看就看出来这个变量是决定系统的默认语言的，即系统的菜单、程序的工具栏语言、输入法默认语言等。SYSFONT是system font的简称，决定系统默认用哪一种字体。SUPPORTED变量决定系统支持的语言，即系统能够显示的语言。需要说明的是，由于计算机起源于英语国家，因此，不管你把这些变量设置成什么，英语总是默认支持的，而且不管用什么字体，英文字体总包含在其中。

那么如何显示中文呢？

1、系统必须安装中文语言包才行

# yum \-y groupinstall chinese\-support

2、仅仅有语言包还不行，我们得设置相应的字符集

## 临时生效
```
export LANG="zh\_CN.UTF\-8" # 设置为中文

export LANG="en\_US.UTF\-8" # 设置为英文，我比较喜欢这样 export LANG=C
```
## 永久生效， 编辑/etc/sysconfig/i18n（最好reboot一下）
```
LANG="zh\_CN.UTF\-8"
```
## 或者，编辑 /etc/profile配置文件，添加如下一行
```
export LANG="zh\_CN.UTF\-8"
```
# 重新载入
```
# . /etc/profile
```
## 查看当前的字符集
```
# echo $LANG
```
好了，经过上面的设置，在终端上应该能够显示中文了