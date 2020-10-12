---
title: echo添加文件失败
date: 2020-10-12 12:09:51
permalink: /pages/63ba44/
categories:
  - 技术
  - linux
tags:
  - 
---
重定向是在甚至启动sudo之前由外壳完成的。 因此，要么确保重定向发生在具有正确权限的shell中

```
sudo bash -c 'echo "hello" > f.txt'
```

或使用T恤

```
echo "hello" | sudo tee f.txt  # add -a for append (>>)
```