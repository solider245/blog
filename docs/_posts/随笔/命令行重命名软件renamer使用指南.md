---
title: 命令行重命名软件renamer使用指南
date: 2020-11-06 18:54:05
permalink: /pages/a87c54/
sidebar: auto
categories:
  - 随笔
tags:
  - 
---
## 序言

重命名器[renamer](https://github.com/75lb/renamer)是一个命令行实用程序，可帮助重命名文件和文件夹。它通过插件是灵活和可扩展的。

## 安装

```sh
npm install -g renamer
```

## 使用案例

> 下面的示例使用双引号来适合Windows用户。MacOS和Linux用户应使用单引号

```shell
# 使用示范
renamer [options] [file...]
# 文本替换
renamer --find jpeg --replace jpg *
# 递归作用于所有文件夹和文件
renamer --find jpeg --replace jpg "**"
```

## 其他官方实例

```shell
#该*命令中的通配符表示“当前工作目录中的所有文件和目录”。
renamer -d --find "[bad]" --replace "[good]" *
#**此命令中的通配符从当前工作目录向下递归匹配所有文件和目录。
renamer -d --find "pic" --replace "photo" "**"
#如果**模式后跟一个/，则仅目录和子目录匹配。
renamer -d --find pic --replace photo "**/"
#如果省略，则--replace默认为空字符串。
renamer -d --find "Season 1 - " *
#本示例仅重命名文件扩展名。
renamer -d --path-element ext --find txt --replace log *
```

## 总结

个人感觉貌似不是特别好用，继续寻找下一个。