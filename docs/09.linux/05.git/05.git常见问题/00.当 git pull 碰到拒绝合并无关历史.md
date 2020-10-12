---
title: 当 git pull 碰到拒绝合并无关历史
date: 2020-10-12 12:09:51
permalink: /pages/f7b1ef/
categories:
  - git
  - git常见问题
tags:
  - 
---
1. ### 问题描述

   很久之前在 [github](https://github.com/lddtime) 上建了个仓库，里面只有一个 `README.md` 文件。
   突然有天，我想把本地的一个项目传上去，然后就碰到了这样一个问题！
   当我 [添加远程仓库](https://git-scm.com/docs/git-remote) 后准备提交代码时，git 提示我请先使用 `git pull` 。
   没毛病，老铁，就应该这样！
   但当我 `git pull origin master` 时就出现了这样一条错误：

   ```
   fatal: refusing to merge unrelated histories  // 拒绝合并无关历史
   ```

   ### 解决办法

   在拉取时使用以下命令：

   ```
   git pull origin master --allow-unrelated-histories
   ```

   对此，git 的 [官方文档](https://git-scm.com/docs) 是这样描述的：

   > By default, git merge command refuses to merge histories that do not share a common ancestor. This option can be used to override this safety when merging histories of two projects that started their lives independently. As that is a very rare occasion, no configuration variable to enable this by default exists and will not be added.
   >
   > 默认情况下，git合并命令拒绝合并没有共同祖先的历史。当两个项目的历史独立地开始时，这个选项可以被用来覆盖这个安全。由于这是一个非常少见的情况，因此没有默认存在的配置变量，也不会添加。（有道翻译）

   ### 总结

   本文所提到的情况只是一个很简单的问题，`--allow-unrelated-histories` 似乎并不能解决所有人的麻烦。
   比如这位网友碰到的问题 [Git没有共同祖先的两个分支如何合并](https://www.oschina.net/question/2771965_2191842) , 远程仓库和本地的差异很零散而且似乎都很重要，使用 `--allow-unrelated-histories` 合并出的结果可能就会不尽人意，所以还要具体情况具体分析喽！

   ### 参考

   1.  [git无法pull仓库refusing to merge unrelated histories](http://blog.csdn.net/lindexi_gd/article/details/52554159)
   2.  [Git refusing to merge unrelated histories](https://stackoverflow.com/questions/37937984/git-refusing-to-merge-unrelated-histories)（建议翻墙）
   3.  [Git没有共同祖先的两个分支如何合并？](https://www.oschina.net/question/2771965_2191842)