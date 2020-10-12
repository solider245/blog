---
title: git push被拒绝：错误：无法推送一些引用
date: 2020-10-12 12:09:51
permalink: /pages/73b752/
categories:
  - git
  - git常见问题
tags:
  - 
---
[git](https://www.codenong.com/tag/git/)[git\-pull](https://www.codenong.com/tag/git-pull/) [git\-push](https://www.codenong.com/tag/git-push/)

## git push rejected: error: failed to push some refs

我知道人们也曾提出过类似的问题，但我相信他们出现问题的原因是不同的。 我进行了一次硬重置，因为我弄糟了我的代码

|

1

 |

 git reset \-\-hard 41651df8fc9

 |

我进行了一些更改，进行了一些提交，现在，我尝试将所有这些提交推入服务器时，出现以下错误：

|

1
2

 |

 ! \[rejected\]        master \-> master (non\-fast\-forward)
error: failed to push some refs to 'git@git.somewhere.git'

 |

Git建议进行git pull，这就是其他人对其他用户的建议。 但是，我相信git pull将把我当前的代码与我不再想要的代码合并(头部修订)。
我该如何进行推送并忘记我前面的版本/修订？

---

git push \-f(如果您有权限)，但这会使从该存储库中提取的其他任何人搞砸，因此请小心。

如果拒绝了该请求，并且您可以访问服务器(如下面的canzar所述)，则可以通过以下方式在服务器上允许此操作：

|

1

 |

git config receive.denyNonFastForwards false

 |

[相关讨论](javascript:void(0))

*   我想我没有远程权限：错误：拒绝非快速转发refs / heads / master(您应该首先拉)Im目前是该仓库中唯一正在工作的人，因此Im不担心任何其他分支或任何东西。有任何想法吗？
*   如果您是该存储库的唯一所有者，请使用 git push \-f，它将使用您当前的存储库替换远程存储库。如果有多用户开发，快进是必不可少的，否则，很容易发生垃圾。
*   如果可以登录到远程服务器，则可以直接进入裸git repo并手动倒回分支，例如使用 git branch \-f，例如 git branch \-f rewind\_the\_one\_I\_broke 8120307。您可以在裸仓库中运行 git log来找到重置点。请注意，这具有与 git push \-f相同的作用，但绕过了钩子。
*   如果您有权访问裸存储库，则可以使用 git config receive.denyNonFastForwards false临时更新存储库配置。我发现我的默认设置为 true。
*   @canzar我的某些 git push \-\-force命令需要使用 git config receive.denyNonFastForwards false。感谢您的参考。
*   git push \-f 实际上会产生该错误

---

如果您是唯一从事该项目的人员，则可以执行以下操作：

|

1
2

 |

 git checkout master
 git push origin +HEAD

 |

这会将源/主提示设置为与主相同的提交(因此删除41651df和源/主之间的提交)

[相关讨论](javascript:void(0))

*   这会摆脱我不再想要的代码并保留我的新代码吗？ (对不起，如果答案很傻)
*   这会将源/主提示设置为与主相同的提交(因此删除41651df和源/主之间的提交)
*   使用您当前位于HEAD的分支更新原始存储库的master分支，从而允许非快速更新。因此，与 git push HEAD \-f相同。对于我来说，我认为，您可以使用更温和的方式来执行此操作，首先使用 git fetch，然后使用 git rebase \-i originmaster，这将使您选择提交。
*   啊。在运行命令之前，应先阅读注释。

---

做就是了

|

1

 |

git pull origin \[branch\]

 |

然后您应该可以推动。

如果您自己拥有提交但尚未将其推送到分支，请尝试

|

1

 |

git pull \-\-rebase origin \[branch\]

 |

然后您应该可以推动。

[相关讨论](javascript:void(0))

*   致命的：找不到远程引用\[分支\]

---

> 'remote: error: denying non\-fast\-forward refs/heads/master (you should
> pull first)'

该消息表明服务器上有一个挂钩正在拒绝快进推送。是的，通常不建议使用它，并且它是一个很好的警卫，但是由于您是唯一使用它的人，并且您想要执行强制推送，因此请与存储库管理员联系，以通过临时删除以下命令来进行非快进推送挂钩或在挂钩中授予您这样做的权限。

[相关讨论](javascript:void(0))

*   或者，让管理员运行 git branch \-f，它具有相同的效果，但不需要大惊小怪的pre\-receive钩子。

---

我要解决的问题是：

|

1
2

 |

git pull origin \[branch\]
git push origin \[branch\]

 |

另外，通过运行以下命令，确保您指向正确的分支：

|

1

 |

git remote set\-url origin \[url\]

 |

---

对我来说，下面的工作是一个接一个地运行

> git pull \-r origin master
>
> git push \-f origin your\_branch

---

我执行了以下步骤来解决此问题。在给我错误的分支上：

*   git pull origin \[branch\-name\]
*   拉动后，遇到了一些合并问题，解决了这些问题，并将更改推到了同一分支。
*   用推入的分支创建了Pull请求... tada，所有更改都在反映出来。