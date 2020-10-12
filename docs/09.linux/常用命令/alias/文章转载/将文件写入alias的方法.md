---
title: 将文件写入alias的方法
date: 2020-10-12 12:09:51
permalink: /pages/866608/
categories:
  - alias
  - 文章转载
tags:
  - 
---
我想扩大这个想法！

# 您要 alias 根据您的问题命令：

`echo "alias wolfr='cd /home/wolf'">>./~bashrc`

现在，您可以键入 `wolfr` 以移至wolf的主目录。

# 这非常相似，也很酷， export 命令：

`echo "export ngse=/etc/nginx/sites-enabled"./~bashrc`

现在，您可以键入 `cp $ngse/my_file /destination_directory/destination_filename` 将文件从启用站点的目录复制到目标位置。

# 除非您执行以下操作，否则所有这些都将无效：

`exec bash`

或者，您可以重新登录或重新启动。

备注：

这个内容可能有问题，毕竟文件路径有问题。