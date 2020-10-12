---
title: cp命令一次复制多个文件
date: 2020-10-12 12:09:51
permalink: /pages/572c32/
categories:
  - linux
  - 常用命令
tags:
  - 
---
\```bash

cp my-first-post.md my-first-post2.md

\```

上面的命令会将my-first-post.md复制一份，并且命名为my-first-post2。



如果你对Linux命令了解的比较多的话，我们可以使用`echo`,`cp`,`xargs`组合命令，来一次性生成4个文件。如果不了解也没关系，直接复制下面的代码即可。





\``` bash

echo 'my-first-post3.md my-first-post4.md my-first-post5.md my-first-post6.md my-first-post7.md' | xargs -n 1 cp my-first-post.md

\```

以上代码会复制my-first-post.md文件并依次生成四个文件。如下图。



![20200613114524_14e62bafa7361b78b8478c27e28a292c.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200613114524_14e62bafa7361b78b8478c27e28a292c.png)

![image-20200613114646454](../../../../AppData/Roaming/Typora/typora-user-images/image-20200613114646454.png)

cp命令的常见几个参数。

