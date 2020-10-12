---
title: pbix文件的版本控制 （二）
date: 2020-10-12 12:09:51
permalink: /pages/bbf1cd/
categories:
  - git
  - git文章转载
tags:
  - 
---
# 使用git找回自己想要的文件，以及其他工具推荐

首先，需要获得你想要的那一条commit sha，（sha就类似于id，每一条commit都有自己独特的sha）比如我现在想要看到我的“第一版”文件：

打开git bash后 输入 git log，

![](https://lh6.googleusercontent.com/_W2N5RrImuQYkn50CRaE3BvLEozMwusVH3GkyFDthRDJ3qbrrDg3rYo4H42wVHfzCC0e2fw1doU_DnDlpz3TH8DLyQ2ndhkp2c8Zhg-j5HAG52MSoAadAZ0VIuSRW9u1mVAXpdFJ)

复制sha：8cf7494dfe37c18dc0495afda3c72ea619a6eda9

或者直接在github页面上复制：

![](https://lh3.googleusercontent.com/QD1vxlOvA5zecv3v4XVTJT1n7UlD3twyoai38HU0lQZ7SIlRxjpXxFdVUUAxcH4Qbn8Hv8lLl6ixDRrg5XiazoIGQ8bdRYCD6Omz8Q3Ta0Wp6bA1h8grn5YQeKkzEe093lSccK3s)

此时，假设你有两种想法：

第一种，你想要保留你其余的commit，只是想单独取出这一条commit中的文件，就需要：

git fetch origin xxxxxxxshaxxxxxxx

![](https://lh6.googleusercontent.com/FelZ9YfvGoOmhh6Y0tYMxBy57l425mvg1rCJWVZT05rQKxvx7qcbmtDlWxV65AvaBga0PITnAybPKn__rCYyQ8aMNwZq9XjKjh1vGQIkCgpqiYnqh8AXTZ1j_yyuThvJlCuVRQVD)

![](https://lh3.googleusercontent.com/ElWTEey8673HI_L-w0p8nSygsZ4I0gdu51Zu73GsiU_b75lIm-U0W_7sR2ib8ZxBbfSRNJXn7Z94OSaIgkOpg8EDZYGT9UMIJgnTwuSPdXTRvd_zEV23il5DDtMEWoD7_nqhrqyu)

git checkout FETCH\_HEAD

执行完上述命令，再打开你的本地仓库，你会发现，你回到了这一条commit时的所存储的文件状态。

这时，你可以使用下面的命令创建一个新的分支，用来存储你想要的文件版本：

git checkout \-b “develope”按照提示，将你取出的这一条commit推送到新的分支里，这样你就可以单独获得你想要的文件了。

![](https://lh4.googleusercontent.com/L4aWqoq9dtOoMg1G4RksUm0JZICKwyO8aItRAsFTay2_upvKhpw35Ld0QtLiyYVJbdNnahEPPp5tWKzwDk8azBhM94Z9J_KeRCT7g-S7UEhc0FFo5i6fTU-vTkvifE5NZabO2YU8)

而且，你推送到仓库里所有的文件都不会丢失，你只需要切换分支就可以找到其他文件。

注：**如何切换分支**？使用 git checkout xxxxx (xxxxx为分支的名字)

第二种，如果你不再需要这条commit之后的提交或修改，则可使用reset强制回到这条提交。

git reset –hard commit\_sha

我在这里只是简单地描述了一下我是如何利用git对pbix文件实现版本控制的，只是git强大功能的凤毛麟角，同时，如果你觉得git对你来说过于复杂或者不顺手，还有其他的方式来做版本控制：

第一种，使用One drive business。

在one drive for business中，服务器会把同一个文件在不同时间的上传，自动识别为不同的版本。可以在文件详情中查看不同的历史版本，并恢复（restore)某一个历史版本。

![](https://lh4.googleusercontent.com/iYIDdxP3rA9AUpfF-z8EkDqNoyx6yAx1R_JYBMcdmgNNx7Swy0uQaPqBLAC7ItHoB32u41GNP16q33nGwUTcDsvdDYb9NSe8Q5uE1Y9-1EhqAWvTYI2Y_Nr7do74_Ikip0t6V1Z0)

如果你有一个office 365账号，并且可以使用One drive for business，固然好啦，简单好用，不需要额外安装其他工具。这也是微软官方建议的一种方式。但缺点是，付费。

另外还有一个工具，做开发的朋友可能会熟悉：AzureDevOps， 以前的Team Foundation Server。

TFS通常被用来持续整合一个开发项目，所以它也整合了git的功能。可以使用git或通过visual studio来联结使用。和OneDrive for Business不同，TFS可以注册账号，免费试用。感兴趣的朋友可以自己深入了解一下。在这里就不多说啦。

如果你也和我一样，看到那么多的version就头疼，那就赶快实践一下版本控制吧。