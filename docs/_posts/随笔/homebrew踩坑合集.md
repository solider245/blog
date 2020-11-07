---
title: homebrew踩坑合集
date: 2020-11-06 18:54:06
permalink: /pages/24b646/
sidebar: auto
categories:
  - 随笔
tags:
  - 
---
## 序言
homebrew很强大，然而 还是那句话，越漂亮的女人越难伺候，越强大的工具也是一样的道理。

homebrew是用ruby语言开发的，包管理器使用的是gem。
所以，安装homebrew前你最好可以把这两个事情搞定。

homebrew使用的是国外的源，所以如果你不能很完美的连接外网的话，最好现在就开始放弃，因为会有一大堆的麻烦事等着你。

## 安装

### 一键安装脚本

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```
安装完成后，如果系统提示你没有将路径添加到你的配置，那么输入以下内容：
```shell
export PATH=/home/linuxbrew/.linuxbrew/Homebrew/bin:$PATH #将 brew 添加到 PATH
#你也可以直接输入下面的内容，他会直接将内容追加到你的配置文件
echo 'export PATH=/home/linuxbrew/.linuxbrew/Homebrew/bin:$PATH'>>~/.zshrc
source ~/.zshrc

echo 'export PATH=/home/linuxbrew/.linuxbrew/Homebrew/bin:$PATH'>>~/.bashrc
source ~/.bashrc
```

如果不成功，可以使用下列代码：
```shell
echo 'export PATH="/home/linuxbrew/.linuxbrew/bin:/home/linuxbrew/.linuxbrew/sbin/:$PATH"' >>~/.bashrc
echo 'export MANPATH="/home/linuxbrew/.linuxbrew/share/man:$MANPATH"' >>~/.bashrc
echo 'export INFOPATH="/home/linuxbrew/.linuxbrew/share/info:$INFOPATH"' >>~/.bashrc
```