---
title: ssh权限太开放错误
date: 2020-10-12 12:09:51
permalink: /pages/fab3aa/
categories:
  - git
  - git常见问题
tags:
  - 
---
我的Mac出现问题，无法再在磁盘上保存任何类型的文件。 我必须重新启动OSX Lion并重置文件和ACL的权限。

但是现在当我要提交存储库时，我从ssh收到以下错误：

```
Permissions 0777 for '/Users/username/.ssh/id_rsa' are too open.
It is recommended that your private key files are NOT accessible by others.
This private key will be ignored.

```

我应该赋予id\_rsa文件什么权限级别？

密钥仅可由您读取：

```
chmod 400 ~/.ssh/id_rsa

```

如果您需要密钥可读写：

```
chmod 600 ~/.ssh/id_rsa

```

*600* 似乎也不错（实际上，在大多数情况下更好，因为您以后无需更改文件权限即可对其进行编辑）。

联机帮助页（ `man ssh` ）中 的相关部分

> ```
>  ~/.ssh/id_rsa
>          Contains the private key for authentication.  These files contain sensitive
>          data and should be readable by the user but not
>          accessible by others (read/write/execute).  ssh will simply ignore a private
>          key file if it is
>          accessible by others.  It is possible to specify a
>          passphrase when generating the key which will be used to encrypt the sensitive
>          part of this file using 3DES.
>
>  ~/.ssh/identity.pub
>  ~/.ssh/id_dsa.pub
>  ~/.ssh/id_ecdsa.pub
>  ~/.ssh/id_rsa.pub
>          Contains the public key for authentication.  These files are not sensitive and
>          can (but need not) be readable by anyone.
> ```