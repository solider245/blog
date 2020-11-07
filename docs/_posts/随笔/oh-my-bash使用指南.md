---
title: oh-my-bash使用指南
date: 2020-11-06 18:54:06
permalink: /pages/1302d2/
sidebar: auto
categories:
  - 随笔
tags:
  - 
---
## 序言

在oh-my-zsh的刺激下，[oh-my-bash](https://github.com/ohmybash/oh-my-bash/)也一样出现了。
oh-my-bash是bash的增强，由于出来不是太久，所以支持的插件并不多。
![20201029151230_dd7f4e86d10fff24674ff3a286983ea1.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20201029151230_dd7f4e86d10fff24674ff3a286983ea1.png)

如果你是bash的原教旨用户的话，那么你可以尝试一下。

## 安装

### 一键安装脚本
```shell
#curl安装脚本
bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"
#wget安装脚本
bash -c "$(wget https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh -O -)"
```
### 手动安装

##### `1. Clone the repository:`

```shell
git clone git://github.com/ohmybash/oh-my-bash.git ~/.oh-my-bash
#国内用户
git clone --depth=1 https://hub.fastgit.org/ohmybash/oh-my-bash.git ~/.oh-my-bash
```

##### [](#2-optionally-backup-your-existing-bashrc-file)2.（ *可选* ）备份您的现有 `~/.bashrc` 文件：

```shell
cp ~/.bashrc ~/.bashrc.orig
```

##### `[](#3-create-a-new-sh-configuration-file)3. Create a new sh configuration file`

您可以通过复制我们为您提供的模板来创建新的sh config文件。

```shell
cp ~/.oh-my-bash/templates/bashrc.osh-template ~/.bashrc
```

##### `[](#4-reload-your-bashrc)4. Reload your .bashrc`

```shell
source ~/.bashrc
```

##### `[](#5-initialize-your-new-bash-configuration)5. Initialize your new bash configuration`

一旦打开一个新的终端窗口，它将以Oh My Bash的配置加载sh。

## 最终效果如下

![20201029152440_25116691c84ecb093350ab4c3b9d48ca.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20201029152440_25116691c84ecb093350ab4c3b9d48ca.png)