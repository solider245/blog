---
title: 解决Git Pull,push每次都需要输入密码问题
date: 2020-10-12 12:09:51
permalink: /pages/1c95bf/
categories:
  - git
  - git常见问题
tags:
  - 
---
如果我们 git clone 的下载代码的时候是连接的[https://而不是git@git](https://%E8%80%8C%E4%B8%8D%E6%98%AFgit@git) (ssh)的形式，当我们操作 git pull/push 到远程的时候，总是提示我们输入账号和密码才能操作成功，频繁的输入账号和密码会很麻烦。

## 1\. 本地保存帐号密码

git bash 进入你的项目目录，输入：
git config \-\-global credential.helper store

然后你会在你本地生成一个文本，上边记录你的账号和密码。当然这些你可以不用关心。
然后你使用上述的命令配置好之后，再操作一次 git pull，然后它会提示你输入账号密码，这一次之后就不需要再次输入密码了。

## 2\. 使用 SSH 连接

1.  Git Bash 进入 ssh 目录

```
cd ~/.ssh
```

1.  生成 SSH key (文件名：id\_rsa, id\_rsa.pub)

```
 ssh-keygen -t rsa -C "xxxxxx@yy.com"  #建议填写自己真实有效的邮箱地址
```

1.  文本编辑器打开公钥 `id_rsa.pub` 复制内容，添加到 Github setting。
2.  测试

```
ssh -T git@github.com
```

> You've successfully authenticated, but GitHub does not provide shell access.

**说明配置成功**

> 本文作者： Shellming
> 本文链接： [https://shellming.com/2019/05/05/git\-ssh\-pwd/](https://shellming.com/2019/05/05/git-ssh-pwd/)
> 版权声明： 本博客所有文章除特别声明外，均采用 CC BY\-NC\-SA 3.0 许可协议。转载请注明出处！