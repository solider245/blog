---
title: alias个人心得
date: 2020-10-12 12:09:51
permalink: /pages/56868a/
categories:
  - 常用命令
  - alias
tags:
  - 
---
# 序言

一直都在用别名，但是都不是很清楚，写个心得总结下。

# alias的存放位置

## 系统目录/etc/bashrc

一般在`/etc/bashrc`这里修改的目录是属于所有用户都可以生效的。大多数情况下，如果没有必要，请设置用户级的别名。

## 用户级别名存放目录~/.bashrc

一般存放在~/.bashrc中，直接在~/.bashrc中修改即可。

### 直接在~/.bashrc中添加别名

#### 使用vim修改文件
例如，使用
```shell
vim ~/.bashrc
```
然后将
```shell
alias ll = 'ls -l'
alias rm = 'rm -i'
```
增加到文件中即可。
#### 使用echo修改文件
也可以使用echo命令直接追加。

```shell
echo "alias ll = 'ls -l'" >>~/.bashrc  # 双引号中的内容可以修改
echo "alias rm = 'rm -i'" >>~/.bashrc
```
这种方法要简单的多。

### 创建别名管理文件
创建别名管理文件是大家推荐的alias命令管理办法。他使得文件更简洁，日后查看起来也更加的方便。
#### 在~/.bashrc中添加以下内容

```shell
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```
你可以使用vim编辑，也可以使用cat EOF命令追加
```shell
cat >> ~/.bashrc <<EOF
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
EOF
```
#### 创建~/.bash_aliases的文件

在`~/.bash_aliases`文件中增加你的别名，这样是最好的。

```shell
echo "alias ll = 'ls -l'" >>~/.bashrc_aliases
echo "alias rm = 'rm -i'" >>~/.bashrc_aliases
```
批量追加别名的办法:
```shell
cat <<EOF>>~/.bashrc_aliases
alias ll = 'ls -l'
alias rm = 'rm -i'
# 这里可以继续追加你想要的别名
EOF
```

## 使修改内容生效

`source ~/.bashrc`


