---
title: key_load_public- invalid format 怎么办？
date: 2020-10-12 12:09:51
permalink: /pages/9416bf/
categories:
  - git
  - git常见问题
tags:
  - 
---
首先查看秘钥是否存在

`cd ~/.ssh && ll`

正常应该是存在的，不然就直接进都进不去了。

执行修复公钥命令，解决问题

```
ssh-keygen -f ~/.ssh/id_rsa -y > ~/.ssh/id_rsa.pub
```