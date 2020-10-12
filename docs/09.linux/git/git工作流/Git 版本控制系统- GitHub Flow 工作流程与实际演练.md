---
title: Git 版本控制系统- GitHub Flow 工作流程与实际演练
date: 2020-10-12 12:09:51
permalink: /pages/86f61c/
categories:
  - git
  - git工作流
tags:
  - 
---
## 前言

随着专案越来越大，协作人员越来越多，冲突发生的机率也越来越高，订定良好的团队规范就显得更为重要，Workflow 因此而诞生，常见的对象有Git Flow、GitHub Flow 或GitLab flow 等，主要都是被用来解决团队间无规范可遵循造成冲突的问题，透过共同遵循的处理流程，达到有条理的进行团队协作开发。 此篇将介绍目前主流的GitHub Flow 工作流程是如何运作，并透过实际演练说明它所能带给团队的好处。

## [](#筆記重點 "笔记重点")笔记重点

*   GitHub Flow 介绍
*   建立Organization 组织
*   GitHub Flow 实际演练
*   Heroku 自动部属

## [](#GitHub-Flow-介紹 "GitHub Flow 介绍")GitHub Flow 介绍

让我们先来看 [官方](https://guides.github.com/introduction/flow/) 的介绍：

> GitHub flow is a lightweight, branch\-based workflow that supports teams and projects where deployments are made regularly.

你现在一定很困惑，没关系，我当时看到也是满脸问号，简单来讲呢，GitHub Flow是基于创建分支所运作，最大的特点在于其流程非常简单，你不需要像Git Flow一样创建多达5种的分支，有新功能需求时在创建对应的 `feature` 分支即可，其中的主要流程为：

*   创建分支(Create a branch)
*   提交修改(Add commits)
*   开启PR (Open a Pull Request)
*   代码审核(Discuss and review your code)
*   部属(Deploy)
*   合并(Merge)

刚刚我们提到了创建 `feature` 分支的部分，当你的功能开发完成后，即透过PR (Pull Request)与负责人做沟通，如果有看过我上一篇文章的人应该很熟悉了才对，接着负责人收到你的PR后会与你讨论相关的内容，确认没问题即合并到 `master` 分支，而 `master` 分支上的每个版本都是可以进行部属的，这点在我们实际演练时会再做讨论，最后即完成了此次的GitHub Flow流程，日后有新功能需求时，就只是再重跑一次流程而已。

你可能还是听得雾煞煞，简单来讲呢，就是我们只会接触到对应的 `feature` 分支，当我们的 `feature` 分支开发完成后，即发送PR给负责人，如果确认没问题负责人就会将这个PR ( `feature` 分支)合并到 `master` 分支，在合并完成后即自动部属至伺服器，因为放在 `master` 分支上的每个版本都是可以直接部属的。

现在你可能就有点头绪了，为了加强对GitHub Flow 的了解，让我们来实际演练一番吧！

## [](#建立-Organization-組織 "建立Organization 组织")建立Organization 组织

这边要强调，GitHub Flow 只是一种工作流程，你可以把它用在开源专案或私有专案上，并没有说一定要用在哪里，它更像是一种共识，下面我们会以GitHub 中的组织( Organization) 为对象做介绍，说明团队间是如何使用GitHub Flow 做运作的，让我们先在GitHub 建立一个组织：

![建立组织](https://i.imgur.com/xjHMkOR.png)

在GitHub 建立组织相当简单，就如同新增远端数据库一般，透过点选即可完成，之后会跳出邀请成员的画面：

![邀请成员](https://i.imgur.com/DPpflYE.png)

这边我们一样使用两支帐号来做示范，被邀请的成员需透过Email 接收邀请才会正式加入组织，最后的结果为：

![组织画面](https://i.imgur.com/b8R9FAb.png)

由于是示范用的，其他细项我们就不做讨论，到这边就已经完成创建组织的动作了，接下来让我们正式进入到GitHub Flow 的实际演练章节吧！

## [](#GitHub-Flow-實際演練 "GitHub Flow 实际演练")GitHub Flow 实际演练

目前我们登入的帐号为lanroya，也就是组织的管理者，你可以把它当作专案的负责人，他使用了express\-generator 生成专案的初始环境：

|

1
2
3
4
5

 |

express \-e express\-project

cd express\-project

npm i

 |

复制

新增 `.gitignore` 档案：

|

1

 |

touch .gitignore

 |

复制

忽略 `node_modules` 资料夹：

|

1
2
3

 |

// .gitignore

node\_modules/

 |

复制

初始化Git 环境：

|

1
2
3
4
5

 |

git init

git add .

git commit \-m '建立環境'

 |

复制

此时的线路图状态为：

![查看目前commit 纪录-1](https://i.imgur.com/WScL3cV.png)

目前初始环境已经建立完成，你总不可能要求成员使用USB 来copy 你的档案吧？ 如同新增帐号底下的远端数据库一般，在组织新增一个远端数据库：

![在组织新增远端数据库](https://i.imgur.com/o8xQyJ0.png)

我们选择将组织的远端数据库设为公开状态，当然你也可以设为私有的，但要注意，以预设来说，成员是无法Fork 私有远端数据库的，你必须到组织的设定将其选项打开，成员才可以进行Fork，组织的远端数据库与帐号底下的远端数据库基本上没啥差别，一个是挂在组织底下，一个是挂在帐号底下而已：

![远端数据库成功建立](https://i.imgur.com/blOjpEv.png)

添加组织的远端数据库位址：

|

1

 |

git remote add origin https://github.com/roxog/express\-project.git

 |

复制

将专案推至远端：

|

1

 |

git push \-u origin master

 |

复制

专案已成功推至远端：

![成功推至远端数据库](https://i.imgur.com/wcd7EAH.png)

到这边负责人的操作就先告一段落了，接下来换成员建立 `feature` 分支并开发新功能的部分，我们采用GitHub Flow来运作，登入awdr74100帐号并Fork组织的专案：

![fork 组织的专案](https://i.imgur.com/kEOSyF1.png)

此时会跳出选择Fork 至哪一个帐号的提示，选择成员(awdr74100)，之后就会Fork 至帐号底下：

![成功fork 专案](https://i.imgur.com/7SJKkug.png)

在来的操作就如同帐号底下的远端数据库一般，由于我们本地还未有这个资料，这边先克隆回本地：

|

1
2
3

 |

git clone https://github.com/awdr74100/express\-project.git project

cd project

 |

复制

查看线路图状态：

![查看目前commit 纪录-2](https://i.imgur.com/6U2F8t3.png)

本文重点来了，GitHub Flow的第一步是在 `master` 分支建立 `feature` 的分支，假设我今天要开发的功能是修改路由，可以这样做：

|

1
2
3
4
5

 |

git checkout \-b feature/edit\_router

... edit /routes/index.js

git commit \-am '修改 router 標題'

 |

复制

分支的名称是可随意命名的，但必须具备其描述性，目前我们已经完成GitHub Flow 的第一与第二个步骤了，线路图状态为：

![查看目前commit 纪录-3](https://i.imgur.com/q76yMKN.png)

假设新功能已经开发完成了，先将新提交推至帐号底下的远端数据库：

|

1

 |

git push \-u origin \-\-all

 |

复制

接着进行GitHub Flow 的第三步骤，开启PR (Pull Request)：

![开启PR](https://i.imgur.com/ZFiRooC.png)

这边要注意来源与目的的选择，你是将 `feature/edit_router` 推到专案的 `master` 分支，并不是 `master` 推 `master` ，如果确认没问题，就发送RP吧，此时GitHub Flow的第三步骤也就完成了。

这边做一个补充，其实也不算补充，如果你有看过上一篇文章的人应该都知道该怎么做了，如果未来要同步组织的远端资料库时，必须添加数据库的位址：

|

1

 |

git remote add source https://github.com/roxog/express\-project.git

 |

复制

这样之后就可以使用 `fetch` 或 `pull` 将负责人合并后的资料给拉下来，达到同步更新的作用，接下来切换到负责人的帐号(lanroya)来处理PR吧：

![处理PR](https://i.imgur.com/gro36Go.png)

目前来到了GitHub Flow的第四个步骤，也就是代码审核的部分，这边介绍一个蛮有趣的功能，切换到 `Files changed` 选项：

![files changed 功能](https://i.imgur.com/e2vijFv.png)

你可以点击更动代码旁边的 `+` 按钮，或是直接将更动代码整个选起来以进行讨论，看起来会像这样个样子：

![代码审核](https://i.imgur.com/sFVSx2r.png)

点击 `Add single comment` 即可添加讨论，此时有关的人员都会收到此次的评论通知，现在的 `Conversation` 看起来会像这样：

![add single comment](https://i.imgur.com/P1KQp2O.png)

假设此次的讨论已经完成，可以点击 `Resolve conversation` 关闭对话，最后确认没问题的话，点击 `Merge pull request` 合并PR：

![合并PR](https://i.imgur.com/rJg3ywT.png)

到这边我们就跑完GitHub Flow的全部步骤了，此时你可能会想，第五个步骤怎么没有说明呢？ 在前面我们有一直强调 `master` 分支的每个版本都是可以直接部属至伺服器的，这也就代表说当我们合并这一个PR时，进而生成的提交就等于production的版本，在这边你先理解大概的概念就好，下面我们会介绍如何使用heroku自动完成部署动作。

现在你已经会使用GitHub Flow运作整个提交流程了，其实就是一直围绕在 `master` 开 `feature` 分支，将 `feature` 分支推上fork的远端数据库，之后开启PR发送 `feature` 分支合并 `master` 分支的请求，之后又有新功能要开发时，先将本地数据库与组织数据库做同步：

|

1
2
3

 |

git pull source master

git push origin master

 |

复制

此时的线路图状态为：

![查看目前commit 纪录-4](https://i.imgur.com/OtLgsKR.png)

要开发新功能就在开一个 `feature` 分支，之后再重跑一次GitHub Flow的流程，这边要养成一个好习惯先 `pull` 在 `push` ，也就是先拉在推，你没办法保证在过程中是否会有其他成员提交PR并审核通过，如同我们之前所说，历史纪录不同，肯定会发生冲突，这边要特别注意。

## [](#Heroku-自動部屬 "Heroku 自动部属")Heroku 自动部属

这边我们来补充何谓 `master` 分支上的每个版本都是可部属状态的，通常这个动作会在初始化专案时进行，但为了避免大家混淆，刚刚没有操作到这一部分，回到lanroya帐号操作Git：

|

1
2
3

 |

heroku login

heroku create

 |

复制

上面操作主要用来在heroku 开一个伺服器，这边我们并不会强调heroku 的使用方式，在之后的express 章节会再做说明，目前主要用来示范何谓自动部属，此时的专案会新增heroku 的远端位址：

![查看所有远端数据库](https://i.imgur.com/E57QN7r.png)

将专案推至heroku 并查看：

|

1
2
3

 |

git push heroku origin master

heroku open

 |

复制

此时会跳出以下画面：

![查看heroku 部属画面-5](https://i.imgur.com/lWGK47s.png)

我们的express 专案已成功部属在heroku，你可以把它想像成GitHub Page 的感觉，目前的线路图状态为：

![查看目前commit 纪录](https://i.imgur.com/2qH9EL3.png)

`master` 分支新增了 `heroku/master` 的参考，接着到刚刚新增的heroku伺服器设定介面：

![heroku 启用自动部属功能](https://i.imgur.com/7bcH581.png)

点击 `Enable Automatic Deploys` 启用自动部属功能，这样就完成了，此后组织专案中的 `master` 分支只要有变动，heroku都会自动帮你完成部属的动作，让我们来测试一次：

> 当前为成员(awdr74100) 的操作

|

1
2
3
4
5
6
7

 |

git checkout \-b feature/change\_router\_title

... edit router title

git commit \-am '再次修改標題'

git push origin \-\-all

 |

复制

开启PR：

![再次开启PR](https://i.imgur.com/MLB56GZ.png)

负责人通过PR：

![通过PR](https://i.imgur.com/O4nJ1yJ.png)

当你按下 `Merge pull request` 合并PR时，因为 `master` 分支移动了，heroku就会开始自动部属的动作：

![heroku 自动部属](https://i.imgur.com/iRXVQ03.png)

结果页面：

![结果页面](https://i.imgur.com/QPrM9cr.png)

是不是很酷？ 我们就再也不需要手动Push至heroku了，事实上，类似的PaaS都有这个功能，比如说我自己非常喜欢的 [ZEIT Now](https://vercel.com/) 也有这个功能，之后有机会再做示范。

到这边我们的Git 学习路程就告一段落啰。