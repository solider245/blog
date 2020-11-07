---
title: 命令行备忘录工具navi使用指南
date: 2020-11-06 18:54:05
permalink: /pages/1377eb/
sidebar: auto
categories:
  - 随笔
tags:
  - 
---
## 序言

[navi](https://github.com/denisidoro/navi)是一个强大的命令行工具软件。好的命令行软件就像一个好看的美女，她越是漂亮，维护成本就越高。
好的工具也同样如此，越是强大的工具，依赖的东西也就越多，同时维护成本也就越高。
navi使用rush语言开发，因此依赖cargo。
使用`FZF\skim\alfred`来作为搜索引擎，因此必须安装这三者中的一个。
不过没关系，简单使用navi对于大多数人来说，依然可以做到。


## 安装

### 官方推荐使用brew安装

```shell
brew install navi
```

由于大多数人没有安装brew或者Linuxbrew，而navi在使用上依赖cargo，所以这里推荐使用cargo来安装navi。
在使用cargo前，让我们先安装cargo。

```shell
sudo apt install cargo # ubuntu安装cargo
sudo yum install cargo # centos安装cargo
#如果无法安装，请先将你软件包的源更换为国内的阿里/华为/腾讯源
cargo install navi # cargo安装navi
```

cargo如果无法安装，请更换为清华源:
```shell
vim ~/.cargo/config #编辑cargo源配置文件
#将以下内容复制到上述文件当中
[source.crates-io]
replace-with = 'tuna'

[source.tuna]
registry = "https://mirrors.tuna.tsinghua.edu.cn/git/crates.io-index.git"
```

安装好了软件后，需要将navi的安装路径追加到你的配置文件当中。
```shell
echo 'export PATH=$HOME/.cargo/bin:$PATH/' >>~/.bashrc #如果你使用的是zshrc则为~/.zshrc
echo 'export PATH=$HOME/.cargo/bin:$PATH/' >>~/.zshrc
```
## 使用navi

### 安装fzf
navi使用fzf进行搜索，使用前请确定你又没有安装好fzf。如果没有，可以使用下列办法安装。

```shell
git clone --depth=1 https://github.com.cnpmjs.org/junegunn/fzf.git ~/.fzf #国内用户
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
#ubuntu用户可以这样安装
sudo apt install fzf -y
```


第一次使用的时候直接输入`navi`即可。如果你没有备忘录的话，系统会询问你是否下载自带的备忘录。
![20201102062635_bbf3203a17da674a2ea927da9e74e56e.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20201102062635_bbf3203a17da674a2ea927da9e74e56e.png)
如上图所示，如果你网络正常当然没问题，但是如果你是国内用户的话，就无法下载下来了。
你也可以直接输入：
```shell
navi repo browse
```
来直接查看仓库。然后根据你的需要来下载对应的命令。
因此使用以下代码来导入即可：
```shell
navi repo add https://github.com.cnpmjs.org/denisidoro/cheats.git
```
选择你需要的命令就可以下载了。
### 从tldr下载
你也可以下载tldr的命令。
```diff 
navi repo add denisidoro/navi-tldr-pages
#国内用户请用下面这个下载，记得把前面的-去掉
-navi repo add https://github.com.cnpmjs.org/denisidoro/navi-tldr-pages.git
-navi repo add https://hub.fastgit.org/denisidoro/navi-tldr-pages.git
-navi repo add https://github.91chifun.workers.dev//https://github.com/denisidoro/navi-tldr-pages.git

```