---
title: git通过命令更换远程仓库地址-----和更换地址后对项目进行操作显示无权限问题
date: 2020-10-12 12:09:51
permalink: /pages/a3273f/
categories:
  - git
  - git常见问题
tags:
  - 
---
       声明：写这篇博客呢，是为了帮助那些像我一样没太注意细节而导致更换远程地址后再次对项目进行操作显示无权限问题的朋友。那么下面我说一下具体场景吧
        具体场景是这样的我们的项目存储在码云的远程服务器上，我们通过git对项目进行操作和同时开发。突然有一天我们老大通知我们git的远程仓库地址需要变换一下！！！ 正题来了

## 1 怎么更换git远程仓库地址

方法一 ： 通过命令直接修改远程仓库地址

```
git remote 查看所有远程仓库
git remote xxx 查看指定远程仓库地址
git remote set-url origin 你新的远程仓库地址
```

方法二： 先删除在添加你的远程仓库

```
git remote rm origin
git remote add origin 你的新远程仓库地址
```

方法三： 直接修改你本地的.git文件

```
这里需要注意的问题是需要进入你的项目目录中
例如：你的项目名为test，那么你就进入test文件夹。
**.git文件是隐藏文件你需要显示隐藏文件才能看见**
```

![这里写图片描述](https://img-blog.csdn.net/20180418103422391?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzM3MDM0Mjk0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

```
进入.git文件编辑.git文件中的config文件修改config文件中的url路径为你的新远程仓库地址路径。
```

![这里写图片描述](https://img-blog.csdn.net/20180418103545665?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzM3MDM0Mjk0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

上面内容信息就是修改git远程仓库地址方法，方法都是正确的我比较喜欢使用第一种命令方法，简单快捷。但是我修改完成之后呢，在去操作的时候他就提示我没有权限了，我确定我是有权限的那是怎么回事呢？你们可能有的人没有预见过，可能有的人预见过。我说下我的问题所在吧。

git 的连接方式分为两种见下图
![这里写图片描述](https://img-blog.csdn.net/2018041810402841?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzM3MDM0Mjk0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
通过这个图片我们可以看出来git的连接方式分为两种一种是https连接，一种是ssh连接。问题的原因就是在于我一直对远程操作库的连接都是https连接。但是我们老大在更换远程仓库的时候给我们发送的连接是ssh连接。我通过上面的三种方法对远程仓库的位置进行了更改，更改后的url路径是ssh连接路径。但是我在码云上的个人信息设置中没有填写我的ssh,所以就造成了我无权限的问题。那么我们就来建立一下ssh连接吧。

1 首先需要在我们的远程码云上设置自己的ssh，可能大家使用的代码托管平台不同，但是思路应该是一样的。
![这里写图片描述](https://img-blog.csdn.net/20180418105422478?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzM3MDM0Mjk0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
进入自己的个人资料中点击设置，选择公钥设置。公钥key标题可以随意

生成我们自己的公钥
1 找到自己的本机用户地址我用的是windows系统，点击进入C盘，点击进入用户，点击进入你的用户文件夹（我的文件夹叫做lqf，你的可能是zhangsan lisi 什么的是由你最初设置电脑是设置的）。 进入了你的文件夹之后你会找到一个.ssh文件夹进入其中。
![这里写图片描述](https://img-blog.csdn.net/20180418110305709?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzM3MDM0Mjk0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
如上图所示，如果此文件中有红箭头标识的文件就直接打开复制文件中内容粘贴到git远程ssh设置中的公钥位置保存就可以了。这时你就可以正常通过ssh进行远程操作了。

如果你的上图中没有红箭头的标识那么需要你自动生成一下。
步骤：
![这里写图片描述](https://img-blog.csdn.net/20180418110716843?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L20wXzM3MDM0Mjk0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
右键打开git Bash Here

输入命令 ssh\-keygen.exe 就会自动生成id\_rsa.pub文件了，打开文件中的内容复制粘贴到git远程仓库中ssh设置的公钥位置就可以了。