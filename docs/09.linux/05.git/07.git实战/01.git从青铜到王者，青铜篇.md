---
title: git从青铜到王者，青铜篇
date: 2020-10-12 12:09:51
permalink: /pages/da502b/
categories:
  - git
  - git实战
tags:
  - 
---
# 序言
现在很多git教学，把一大堆的名词与操作堆砌到新手面前让很多人不知所措，十分茫然。包括我个人在内，经常看的多，但是用的少，最后也是稀里糊涂的，所以打算写这篇文章，尝试给Git的一些操作和命令来分层级，以方便大家更好的学习和入门Git。

# Git青铜选手用法大全

我个人认为，作为Git的青铜选手主要以下几点:
1. Git的安装
2. Git的更新
3. Git的的配置
4. 用Git生成sshkey
5. 从GitHub远程仓库下载到本地仓库

如果能做到以上5点，基本上算是入门了，下面说下具体的用法。

## Git的安装

主要分为三大系统Windows、MAC、Linux。
### Windows下安装Git
推荐下载GitHubdesktop，包含了Git的图形界面，对于新手来说还挺友好。
![20200627101026_674196ebfb70e95655d93fc7eccb7a4f.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200627101026_674196ebfb70e95655d93fc7eccb7a4f.png)
另外，强烈推荐大家使用Windows下的wsl2来操作Git，会得到更加完善的体验。

### MAC下安装Git

```shell
brew install git
```
直接通过brew来安装

### linux下安装Git

#### Ubuntu下安装Git
```shell
sudo apt install git-all
```
#### centos下安装Git
```shell
yum install Git
```
主流的基本就这两个，其他的一般都不推荐。安装好之后可以使用
```shell
git --version
```
命令来查看Git当前的版本。

## Git的更新
下载完了Git之后，一般来说不是最新的，尤其是centos版本的，版本更新比较慢，所以需要进行更新。
```shell
git clone https://github.com/git/git.git
git clone https://github.91chifun.workers.dev//https://github.com/git/git.git # 国内加速地址
```

## Git的卸载

正常来说Git不需要卸载，只需要不用即可。如果一定要卸载的话，Windows下会出现很多很复杂的问题，这里不多说，只说mac系统和linux下一般的卸载方法。

### mac系统下卸载Git
*   查看Git安装位置，使用命令 `which －a git`
*   终端运行 `sh /usr/local/git/uninstall.sh` 卸载

![20200627102358_1975564173ea9eacb81932798a9bbe94.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200627102358_1975564173ea9eacb81932798a9bbe94.png)

### linux系统下卸载Git
```shell
which -a git # 查找Git的位置
cd /usr/bin/git # 一般默认这个位置具体根据你上面查找的位置来看
sudo rm －rf git* # 删除Git文件夹
```

## Git 的配置
### Git常见有三种配置：

* `.git/config` # 目录配置
* `~/.gitconfig` # 当前用户配置，最常见的配置
* `/etc/gitconfig` # 全局配置

一般来说，我们配置好当前用户即可。
### Git配置用户与邮箱

``` shell
git config --global user.name "solider245" #配置用户
git config --global user.email solider245@gmail.com #配置邮箱可以改成自己的
```
### 检查Git配置信息
配置完了之后记得检查配置信息:

```shell
git config --list #如果想要检查你的配置，可以使用 git config --list 命令来列出所有 Git 当时能找到的配置
```

## 生成ssh密钥

```shell
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
默认会在相应路径下（/your\_home\_path）生成`id_rsa`和`id_rsa.pub`两个文件，如下面代码所示:
```shell
ssh-keygen -t rsa -C "your_email@example.com"
# Creates a new ssh key using the provided email
Generating public/private rsa key pair.
Enter file in which to save the key (/your_home_path/.ssh/id_rsa):
```
id_rsa是私钥与id_rsa.pub是公钥这两个文件都很重要，记得妥善保存。

## 将ssh key添加到GitHub中
用自己喜欢的文本编辑器打开`id_rsa.pub`文件，里面的信息即为SSH key，将这些信息复制到GitHub的`Add SSH key`页面即可

不同的操作系统，均有一些命令，直接将SSH key从文件拷贝到粘贴板中，如下：

**mac**

```ruby
pbcopy < ~/.ssh/id_rsa.pub
# Copies the contents of the id_rsa.pub file to your clipboard

```

**windows**

```ruby
clip < ~/.ssh/id_rsa.pub
# Copies the contents of the id_rsa.pub file to your clipboard

```

**linux**

```ruby
sudo apt-get install xclip
# Downloads and installs xclip. If you don't have `apt-get`, you might need to use another installer (like `yum`)

xclip -sel clip < ~/.ssh/id_rsa.pub
# Copies the contents of the id_rsa.pub file to your clipboard
```

## 从GitHub下载文件到本地

打开GitHub或者gitee，找一个你喜欢的文件直接使用
```shell
git clone <url>
```
下载到本地，成功之后，一个青铜级别的GIT选手即诞生了！