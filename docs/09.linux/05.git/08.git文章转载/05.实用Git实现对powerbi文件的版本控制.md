---
title: 实用Git实现对powerbi文件的版本控制
date: 2020-10-12 12:09:51
permalink: /pages/c35868/
categories:
  - git
  - git文章转载
tags:
  - 
---
# 使用git实现对Power BI .pbix文件的版本控制 （一）

作者 [ladydumbo](https://littledumbo.com/author/ladydumbo/)

# 之 git详细安装指南以及仓库配置

在开始介绍git的安装之前，我想先和大家聊一下“为什么我们要关心版本控制” 。

对于任何开发人员，无论是小白还是资深，版本控制都是必不可少的。版本控制可以让我们跟踪源文件的更改。通过跟踪更改，开发人员可以快速识别何时发生了更改，发生了什么更改。使用git，开发人员可以“区分”旧文件与新文件的区别，了解到发生了什么更改。

同时，Git是一个分布式版本控制系统。这意味着它没有“中央服务器”，每个人的电脑上都是一个完整的版本库，这样，你在工作的时候，就不需要联网去读取文件啦，因为版本库就在你自己的电脑上。这也提高了它的安全性。

但是目前的问题是：Power BI Desktop创建的PBIX或PBIT是.zip二进制文件。

这意味着，使用版本控制的系统，我们无法“区别”不同的文件，也无法跟踪更改。比如当你将**\[价格\]**度量值更改为**\[价格\-不含增值税\]**时，我们没有办法通过git看到这个更改。此外，由于我们无法“进行差异化”，那么如果有一个以上的开发人员来从事一个项目时，就没有办法合并你们所做的更改。这也就导致了限制了PowerBI项目的开发人员数量。

然而，虽然有上述的这些限制，我们还是可以通过对文件进行“注释”的方法来实现对新旧文件的区分。

所以，在这里我想和大家（像我一样的github新手）分享一下，如何一步一步创建github仓库，并实现对pbix文件的版本控制。

重要概念：（这里引用廖雪峰老师的话）

**什么是版本库呢？**

版本库又名仓库，英文名repository，你可以简单理解成一个目录，这个目录里面的所有文件都可以被Git管理起来，每个文件的修改、删除，Git都能跟踪，以便任何时刻都可以追踪历史，或者在将来某个时刻可以“还原”。

**什么是分支？**

分支就是科幻电影里面的平行宇宙，当你正在电脑前努力学习dax的时候，另一个你正在另一个平行宇宙里努力学习git。

如果两个平行宇宙互不干扰，那对现在的你也没啥影响。不过，在某个时间点，两个平行宇宙合并了，结果，你既学会了dax又学会了git！

Git的分支是与众不同的，无论创建、切换和删除分支，Git在1秒钟之内就能完成。

![](https://lh3.googleusercontent.com/7MvhZqpktQc2rr7yfefUJcnUqhUQtjnyUtPQszhRk_KoTncicqz-JJ5Mnsjh04e7BXnT8kqOrC1Fv2UvkK5Dk02Lg-mVx7T5TXfNVc_KIiP56sgQZpApHUzv36nAOcrcS7R1C-iZ)

首先，第一步我们要做的是，下载安装git，进入官网下载 [https://git\-scm.com/](https://git-scm.com/)，

点击next直至安装完成。

![](https://lh6.googleusercontent.com/nH3ybXJVyTxU7MKzNrmro7uLQZzXGprP-hpO46xv4avTzkc6fKymf9qSaDi7ETWo-2NHpEH5rQgE3u7uosny7PaIb0xpGeYMeirli6Xm2Wo66lQe3AEFAORDEtfar3IsynasIHK0)

![](https://lh3.googleusercontent.com/bZ3g5L8NWTEeSAgDuK8OtagzaCvXbDMiPcYLHLlM_fP-YiEHn-J-mOmsYGtf3vc6zl0hwqLXcHAPUfOZ_oDq2Um4UuV3r2EYyHTsXjRvFExPeeCyDu4uR5ViS02P4c9trZPlioxn)

![](https://lh3.googleusercontent.com/FiwnXTs58AbVc2Z7BhFv1dvUtCwNJQtTeGh_fm2zyDBswbpWFOxTRJo_XlakhBQBMhQbR5yxKa__xjKJgwCYAUjvh9Gb5x7kwOo3HGLy2GNVYI_7kt7z_2LLpOObWgjw9nkFM-l-)

![](https://lh3.googleusercontent.com/toK9-tKm5zkDR-Q92fGwynFLwBrKC_xNaZ1a1fb9CEz00WeT7g2PpURGB0Pxp6GADJ7MBAc-UBaLvrOuckRVR9VyYRAFiAeIq79AYls5cXjIgkAt2cFcvfVRgBK3xXSreFchKXTj)

接下来，注册一个github账户：

![](https://lh5.googleusercontent.com/ZQSxmOJMYltOO-QU3goDIvPXOASFUfLQwDz7YQnYNpdr3WH4qnNXLlc9GUVzHqPiW8IBUn9pNkoOimWi2f1J4Ae7lxtDnrIGd-gbupQ0fPnqDy1WPHiU_xivQh9K3LhA_i9QhXxE)

![](https://lh6.googleusercontent.com/r4HnBhcfE88021DcKzZN1ff7p-RiicRl6yT0r-NkfZclCfg2hP6z77QfNwLoH0CE3F4UoCsjT-GD6pZ0jgENru7AbkB3-1aXEAkvLP3ggGp2pCNBxzDqfGU0qdfcy0JPoOi-pyPO)

注册好账户之后，登陆github，点击创建一个新的仓库。

注：可以创建一个私密的仓库，这样就可以保证数据的安全。

![](https://lh4.googleusercontent.com/eTrotBpIJLMPkk5gll1NoGLwJm-NvdtipGYUrEJT9WIJcx88kRI255lHqwpTEHN8OqX0Z2EXToVDy8CUSyZSH0x9iOH4kV9e7EJOQp-bl41FbACs4mO0uHS6NRDP4XOLFCDPvTGm)

至此，用来存储和管理我的pbix文件的仓库创建成功。接下来，需要在本地创建一个仓库，并把本地仓库关联到远程仓库。

Git的仓库你可以建在你电脑的任何目录下（最好不要包含有中文目录）。在这里，我先新建一个文件夹 “GitTest”，然后打开这个文件夹，在空白处鼠标右击：Git bash here:

![](https://lh5.googleusercontent.com/I09SYPoToyYXIiskZLE6LMJBg97FNURPZoaY1wrdk4dloVe839zePmTGxrksXXMtYKG5z_kuVksi5B0qjD75Pj9oZD_LawvV3atAYlm022d5JoJBwS0X4MUgdIYJ9zDu7dcmegWW)

联结远程仓库，有这几种做法：

![](https://lh3.googleusercontent.com/1U6mixDv5hiVfNbJGmhBTFWbR7kHM5Y0D-9ulZVgZMWOPkAp9WswJm-ugPqvP81LPFcjI22rRwgIOli8-WSEeQfxEAg9ewJTWwqLfaRpoBVopFD11Gy7sKxWiEtX-_cgnSptuVC4)

下面我打算在 GitTest 下面创建本地库，使用第二种方法：

在git面板里输入命令行：

echo “# PowerBIFiles” >> README.md

git init

git add README.md

git commit \-m “first commit”

git remote add origin https://github.com/aision06/PowerBIFiles.git

git push \-u origin master

![](https://lh3.googleusercontent.com/YRezARQNxiQo3W3igkhPqM_KqzP2iYo8OePVwCG0gcR2KHUjMT1Suxp7lncu6oAmgoUECjf0SlwFV5-dyaE1Z5SEJbAw58KYCspbqm4iXgZvPvKieoxmnJHdYDDIcU8i4qKSzHN1)

这里提示，第一条 commit 已经添加并成功推送至远程仓库的当前分支 “master” 中。

之后，我们就可以往仓库里添加文件啦。

添加文件的时候，可以直接把你要管理的pbix文件拖至本地仓库中。

![](https://lh3.googleusercontent.com/dAh3JQ_d-AxT6lkncqJSg9CfSoaC-RcJvjzjXKx-MCLDoLPsxvPz8u-kQVD1nI_CksQRXlNeD1FzgfbfeOEzf5OPd80va5pl7M1PKzFGqD4kbwHotsFtLk-Nyck5Yfe-xGj8C9re)

然后打开git bash，输入 git status 查看仓库的状态：这里提示我们新添加了一个名为 “FFT      KPI.pbix”文件。

![](https://lh5.googleusercontent.com/i9-1XF-XVsjipJNUxBTdPNggBW5cpP3W91dF0vmN62-bfdj2qxhzxwVHJ7mTPc3VjWxM0-VFDVkIq_4f1PjGMcMwEXN1Cah5rIl6qKqA-jPWjsS-4bLOunooTqDMmHud2KGS7k9P)

接下来，我们把这个pbix文件推送到远程仓库中去，这个步骤使用三个命令行实现：

git add xxxxx  \->文件名

git commit \-m “xxxxxxxxx” \-> “xxxxxxx”为你添加的注释·

git push

![](https://lh4.googleusercontent.com/OghXpej7jQqOG5pa-mlqpZp2WFXRsP73pI1L6FplnS-OJOS262GPSw_g6DHLMaVvxjVVEG_FKLSJi2KSUGcb9WfrfxCtocPWmqoH3XuJ3jmjc0cMuXfvpKUlOtQIQjNvYL7D9_cM)

打开你的远程仓库，就可以看到你成功推送的文件啦：

![](https://lh3.googleusercontent.com/6npAtC-MHSLdWBaLCwIhIMHtCUPpCsE7VP_8J8GSu5Fo-pog0W5Mh1Uo1DbOxSxDbJGjlkpiAQbdSQbbach81tPk_lQqlTdj-7TS1x7oIpfKQ2hSM07FIpn-Y-bjIYidpW7kGzjx)

在这里，如果你遇到了文件无法推送的情况，例如，你在控制面板收到了这样的消息：

![](https://lh5.googleusercontent.com/T3wOKfgdF1cCJNdKPddw2XUpueE7B_gwIUET5x89vnW8zgvuz72PBDITafnRnAEbKoO9RBDohwhz72zTYmMlgZROByNdIy9ItBVZJdIF21IR1MJ5YDxZK_U9GX-Vml-M7iwe4nBk)

是因为想要推送的文件超过了最大文件大小的限制，这时，会提示你需要使用git

lfs插件来解决。

**什么是Git LFS?**

Git LFS（Large File Storage） 是 Github 开发的一个 Git 的扩展，用于实现 Git 对大文件的支持。简单的说，就是如果你想传超过100M的二进制文件到GitHub，你就要用Git LFS。

根据提示，进入 [https://git\-lfs.github.com/](https://git-lfs.github.com/)，下载安装扩展件，依据官方页面的指示进行操作：

![](https://lh4.googleusercontent.com/EqXizHQtXCAjv-DCVK9pxEdET1SXI6GrgDHzW0329fZs3TDwqRNpEUFa22v3wiXiC-Ml11CTdLGDr0bV2NLZAkLNgHrU7EBMdVbpQYMdw8ydo8qL-_d0a433CfWJ6FIcx0apAw-B)

注：如果对于同一个文件，你已经遇到了不能推送的情况，此时，需要撤回之前的commit。所以，如果你要上传的文件大于100M，那么建议你在对新文件进行操作之前就配置好git lfs。

假设我对这个文件进行了修改，那么我只需要把这些修改 commit 并 push 到远程仓库。

![](https://lh5.googleusercontent.com/Bt_cr1UPnrEv8qaXFAeab7S5gqKp2ngdEYMWBdLShr9Bb49myaJODdlKsZvmGJKp-RM0eg9EnuYziq6JM2sh5LryU1asjlDW0LXPf7F2zAF-vz8YOYJM2kX2Pgpc53-Vh_r0_Ri_)

在修改并保存了文件之后，先用git status查看一下状态：看到提示 FFT KPI.pbix 被修改，

使用git add 添加这个修改到仓库中，

![](https://lh5.googleusercontent.com/gVxrvCAVrtchgLPzOpObJAMu-zN0iJ5bEyops1lJZxHgfE7ebDrMOpuKlMZinPLrhpR64rb2SLTUvrQwO9QFkOd37XPmZO9vAqaHgkqzcBSSWyBEKFWJSCksKkK2NqTrzUfRZD3G)

commit，并添加一段注释用来标明：

![](https://lh6.googleusercontent.com/S9vbEs7dCDT9U3IzVh0egvYhIT6HSi0avB3K0DdTy6Iu-1cAlQXNvRGRGFRr2bmK1ZX8tzFLERnkj2-VRHmRJTrs3y0opYML7awGzFVk7cm00w_AokUla4hEx1FRlLiCEVNcsvB0)

push到远程仓库里：

![](https://lh5.googleusercontent.com/lEay56JKAWBT4S60H_EhsFCzBg36leca38ABjrWf_bW_TLFtpBhxU7Xfu4vY13zSfzTd8ppPuNpKHlkKeaPhEadMzm8gvcBU3ZG1CZl5P-9SQw0DAGKjs5gZePAqDgDFo-8YfxJq)

在远程仓库里查看新的版本，以及注释：

![](https://lh3.googleusercontent.com/NysUzGzOkLUDHzIa490uX4ir69T5PgbejgC9i4BhEU-snJJv-1s3VFbkJCjKyMr4M6-C7Qv1UsuGw9JWaG5M74_E2uTiwJ3etVyn-Er7wXQUeViX8m8ViLFQI8qc3FyQQiY-pCa0)

点击文件名，还可以继续添加描述，我又在此处添加了 ”Data updated. 15/12/2019”。

![](https://lh6.googleusercontent.com/6MaZiICIyIo9prq0rXT5RXViT5TSAqtetipUFvUyMF_gi8CVFgMSGxh1vda5GbouACerNrj5_cB3g9k6_J6skiV_Kyn-1omv_-RHgShGkEp-dlC0zKwwG01N1Yq7Yb62rPBJr4Fj)

![](https://lh3.googleusercontent.com/s-8wulIPzUNi8I9BLvntiVxcnXicNqFoDVlcSmtwcyP1ilD3APEAphFUj9-9EzkOttKDLB-eEoISQGfrvFp1-847yN5y1GiFqeQPIcnkGXX0jvU4OqmyQbHnwVnikAsaeip4KvTq)

点击查看你所有的commit，你就可以轻松找回自己的注释：

其实，实现版本控制的方法就是，通过阅读每一个 commit 的注释，查询对文件进行的更改，之后，再使用git checkout，就可以找回想要的那一个版本啦。