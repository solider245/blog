---
title: 关于git push没有权限的问题，已设置公钥
date: 2020-10-12 12:09:51
permalink: /pages/49d448/
categories:
  - git
  - github常见问题
tags:
  - 
---
首先呢，我已经弄好了ssh的密钥，ssh \-T git@github.com是可以的，返回：
Hi xxxxxx! You've successfully authenticated, but GitHub does not provide shell access.
但是，当我想要git push的时候，总是失败，提示是：
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
FATAL Something's wrong. Maybe you can find the solution here: xxxxxxxxxxxx
请问这是什么情况，

我执行的是
git remote add origin git@github.com:xxxxxxx/test.git
git push \-u origin master

阅读 119.9k

赞 3 踩

收藏 11 关注 13

[评论](javascript:;) 更新于 2017\-08\-07

提交评论

*   [**Aloys寒风**](https://segmentfault.com/u/jiangxinnju)：

    这个仓库是你自己的么？

    取消 提交

    [](Javascript:;)[回复](Javascript:;) 2015\-08\-08

    提交评论

*   [**Relax**](https://segmentfault.com/u/tanxin)：

    是的，

    取消 提交

    [](Javascript:;)[回复](Javascript:;) 2015\-08\-08

    提交评论

*   [**Relax**](https://segmentfault.com/u/tanxin)：

    是的

    取消 提交

    [](Javascript:;)[回复](Javascript:;) 2015\-08\-08

    提交评论

[展开显示更多](javascript:;)

7 个回答

[得票](https://segmentfault.com/q/1010000003061640#comment-area)[时间](https://segmentfault.com/q/1010000003061640?sort=created#comment-area)

 [![avatar](https://cdn.segmentfault.com/v-5efaf824/global/img/user-64.png) **大圣巴巴**](https://segmentfault.com/u/ba_ba)

*   135

我也遇到这个问题了，并且记录了解决方式
[http://youcanping.cn/2017/12/20/ssh\-Permission\-denied/](http://youcanping.cn/2017/12/20/ssh-Permission-denied/)

#### 5\. 看本地的.git/config设置的仓库url地址和github使用的链接地址是否一致如下图,如use https,则url需要用https的仓库地址，我的就是这个问题。

![](https://segmentfault.com/img/remote/1460000012587312?w=444&h=206)

```
> cat .git/config
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
        ignorecase = true
        precomposeunicode = true
[remote "origin"]
        url = https://github.com/youcanping/MyBlog.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
        remote = origin
        merge = refs/heads/master

```

取消 提交

赞 6

已采纳

[评论](javascript:;) [赞赏](javascript:;) [更新于 2018\-03\-07](https://segmentfault.com/q/1010000003061640/a-1020000012587308)

提交评论

*   [**对影成三人**](https://segmentfault.com/u/duiyingchengsanren_5a94fe0c12540)：

    赞，已解决

    取消 提交

    [](Javascript:;)[回复](Javascript:;) 2018\-04\-26

    提交评论

*   [**梦\_57b199846a034**](https://segmentfault.com/u/meng_57b199846a034)：

    执行 > ssh\-add ~/.ssh/id\_rsa时报错
    Could not open a connection to your authentication agent.
    请问是什么原因呢