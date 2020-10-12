---
title: 命令行备忘录 navi 使用教程
date: 2020-10-12 12:09:51
permalink: /pages/d77338/
categories:
  - 常用小工具软件
  - 命令行备忘录
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-22 22:00:18
 * @LastEditTime: 2020-07-22 22:15:57
 * @LastEditors: 中箭的吴起
 * @Description: navi软件的安装
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\常用小工具软件\命令行备忘录\命令行备忘录 navi 使用教程.md
 * @日行一善，每日一码
--> 

# navi简介
navi 是一个可交互的命令行备忘工具。用户可以执行备忘录中的命令，navi 也支持自定义备忘录以及命令行参数提示。

# 源码安装

# 安装fzf

```shell
# 下载 fzf
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf

# git clone --depth 1 https://github.com.cnpmjs.org/junegunn/fzf.git ~/.fzf # 国内加速地址

# 安装 fzf，执行后会询问一些开关配置，都设置开启即可
~/.fzf/install

# 重载配置文件
source ~/.bashrc
```

# 安装navi

```shell
git clone --depth 1 https://github.com/denisidoro/navi /opt/navi
# git clone --depth 1 https://github.com.cnpmjs.org/denisidoro/navi.git /opt/navi # 国内加速安装

cd ~/.navi
make install 

# alternatively, to set install directory:
# make BIN_DIR=/usr/local/bin install
```