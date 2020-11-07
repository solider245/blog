---
title: 命令行备忘录工具eg使用指南
date: 2020-11-06 18:54:05
permalink: /pages/b980c1/
sidebar: auto
categories:
  - 随笔
tags:
  - 
---
## 序言

[eg官方github仓库](https://github.com/srsudar/eg)
`eg` 提供了命令行工具的常见用法示例。

手册页很棒。 `find` 再次 如何 工作？ `man find` 会告诉您，但您必须仔细研究所有标志和选项，才能弄清楚基本用法。 那使用 `tar` 呢？ 即使 [没有手册的例子](http://xkcd.com/1168/) ，手册页 `tar` 也 [难以理解](http://xkcd.com/1168/) 。

不再！

`eg` 将在命令行上为您提供有用的示例。 可以将它视为的辅助工具 `man` 。

> `eg` 来自 *exempli gratia* ，发音类似字母：“ ee gee”。

![eg示例图](https://github.com/srsudar/eg/raw/master/eg-demo.gif)

<!-- more -->

## 安装

两种安装方式：
```shell
pip install eg 
#or
brew install eg-examples
```

两种方法都可以安装，开箱即用。具体使用方法如下：
```shell
eg # 默认是eg -h 提供帮助
eg <参数名> # 例如eg git 会显示git的示例
eg -l # 查看目前所拥有的案例
eg -e <参数名> #编辑某个示例
```

源码安装：
克隆仓库，并创建一个符号链接 `eg_exec.py` 。 确保为符号链接选择的位置在路径上：

```shell
git clone https://github.com/srsudar/eg ./
ln -s /absolute/path/to/eg-repo/eg_exec.py /usr/local/bin/eg
```

> 请注意， `eg_exec.py` 为了支持Python 3和2 ， 在0.1.x版本 中 更改 的位置 已经开始。旧的符号链接将打印一条消息，说明更改的内容，但是您必须更新链接以指向新的位置。 或者，您可以使用 `pip` 或 安装 `brew` 。

`eg` 不附带二进制文件。 依赖关系非常适中，不需要您安装任何东西（ 如果要运行测试，则 除了 [pytest](https://docs.pytest.org) 以外 ）。 如果发现其他问题，请打开一个问题。

这个就是eg的主要用法了。

## 自定义配置

eg一般不需要自定义，但是有时候还是有人有需求，所以这里就写下。

```shell    
vim ~/.egrc # eg配置文件所在地，默认为空
#eg配置设置在这里进行修改，直接将下面内容复制到你的配置文件即可，需要的功能删除掉前面的#号即可
[eg-config]
custom-dir = ~/software/eg/custom-dir #配置自定义目录，可以修改为一个你喜欢的地方
#color = false # 关闭色彩显示
#squeeze = true #删除多余的换行符
```

注：你可以在自定义文件夹下创建同名命令的Markdown文件。这样的话，当你使用eg搜寻命令的时候，他会优先显示你的自定义命令。

例如，你在

## 总结
`eg`最大的好处是简单、便捷、依赖少。可以说是开箱即用，设置少。由于文件本身非常小，所以作为其他命令行备忘录工具的补充软件来使用可以说是非常的好。

