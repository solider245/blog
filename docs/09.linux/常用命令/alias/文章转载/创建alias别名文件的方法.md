---
title: 创建alias别名文件的方法
date: 2020-10-12 12:09:51
permalink: /pages/2e4c52/
categories:
  - alias
  - 文章转载
tags:
  - 
---
有很多创建别名的方法。 最常用的方法是：

1.  直接在 `~/.bashrc` 文件中 添加别名

    例如：将这些行附加到 `~/.bashrc` 文件

    ```
    alias ll='ls -l'
    alias rm='rm -i'
    ```

    下次（在您注销/登录或完成后 `. ~/.bashrc` ）键入 命令时，将执行 `rm` 该 `rm -i` 命令。

2.  第二种方法使您可以创建单独的别名文件，因此不必将它们放在中 `.bashrc` ，而是 放置 到您选择的文件中。 首先，编辑 `~/.bashrc` 文件并添加以下行（如果尚不存在），或取消注释（如果存在）：

    ```
    if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
    fi
    ```

    保存并关闭文件。 之后，您要做的就是创建一个 `~/.bash_aliases` 文件，并在其中添加别名，其别名与第一种方法中指定的格式相同。

    我 `~/.bash_aliases` 文件的 内容 ：

    ```
    alias cs='cd;ls'
    ```