---
title: fish与oh-my-fish快速上手指南
date: 2020-11-06 18:54:06
permalink: /pages/3bbc1d/
sidebar: auto
categories:
  - 随笔
tags:
  - 
---
## 序言
[fish](https://github.com/fish-shell/fish-shell)是开箱即用最好的shell，而[oh-my-fish](https://github.com/oh-my-fish/oh-my-fish)则是fish的增强版。
在简单使用、入门使用、快速使用上面，使用fish和oh-my-fish则变得很有必要。

## fish常用命令汇总

```shell
#Ubuntu平台安装
sudo apt-add-repository ppa:fish-shell/release-3
sudo apt-get update -y
sudo apt-get install -y fish #现在很多ubuntu可以直接执行第三步安装fish
#centos平台安装
cd /etc/yum.repos.d/
wget https://download.opensuse.org/repositories/shells:fish:release:3/CentOS_8/shells:fish:release:3.repo
yum install -y fish 
#如果希望将fish用作默认外壳
chsh -s /usr/local/bin/fish #如果出现兼容问题直接输入bash返回默认shell
#如果尚未添加/etc/shells fish，以允许fish作为您的登录shell，请使用以下命令
echo /usr/local/bin/fish | sudo tee -a /etc/shells
# fish配置文件存放位置
vim ~/.config/fish/config.fish
# web配置界面（默认8000端口）
fish_config
```
fish的用法就是安装，然后开箱即用。遇到兼容性问题就直接输入`bash`返回到默认shell即可。

## oh-my-fish 使用指南

```shell
#oh-my-fish一键安装脚本
curl -L https://get.oh-my.fish | fish
#如果你没有网络或者无法链接github就不要折腾了
```

正常来说，如果你可以直接安装fish那就直接安装，可以使用一键安装脚本安装oh-my-fish那就直接使用。
如果需要折腾就不要管了，还不如去折腾zsh。
fish的目的就是开箱可用。
