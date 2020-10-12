---
title: 给你的git commit加点料
date: 2020-10-12 12:09:51
permalink: /pages/fa0a52/
categories:
  - git
  - git进阶
tags:
  - 
---
# 给你的git commit加点料

> 本文由[风萧萧梦潇](https://blog.csdn.net/fengxiaoxiao_1)投稿，转载请注明出处。如有错误，请不吝指正。

在工作中，我们通常使用git来管理代码，当我们对代码进行某项改动后，都可以通过git commit对代码进行提交。git规定提交时必须要写提交信息，作为改动说明，保存在commit历史中，方便回溯。但你仔细研究过git commit吗？或者换句话说你注意过应该怎样写commit信息和优化commit信息吗？本文将回答这些问题，希望对大家有所帮助。

### 一、git commit的意义

为了对每次提交进行提交说明，方便之后回溯和团队协作，Git 每次提交代码，都要写 Commit message（提交说明），否则就不允许提交。当参与团队协作时，我们共同维护一个maste或dev的代码，如果其他人改动了仓库代码，我们肯定想知道他到底改动了什么，这次改动会对我们有什么影响。怎么看呢，直接看代码肯定没错，但不是最好的方式。其实最方便的方式就是查看提交历史了。如果提交信息写的足够好的话，不需要看代码我们也清楚改动了什么，这样就可以提高协作效率和沟通成本了。

试想谁不想看到下面这样优雅清晰明了提交历史呢，如果再能自动生成ChangeLog文档自然是极好的。我想没有哪个程序员能抵挡得住这种诱惑吧。

![在这里插入图片描述](https://user-gold-cdn.xitu.io/2019/5/26/16af2c25e49d93bd?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

![在这里插入图片描述](https://user-gold-cdn.xitu.io/2019/5/26/16af2c25e484625c?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

总体来说，规范 commit信息的意义如下：

*   可读性即提供本次代码改动的信息，方便其他人浏览和理解
*   可回溯性即方便查找特定提交说明，回溯某些commit（比如新增特性、修复bug等）
*   自动化性即可根据commit信息自动生成ChangeLog（改动说明）

鉴于此，我们需要写出清晰规范的git commit。那么什么的规范的commit信息呢，请继续看下去。

### 二、git commit 规范

为引导用户为开源社区做贡献，angular较早提出了进行pr时的commit说明规范（详见[Git Commit Guidelines](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits)），后被很多开源项目所接受，形成了一套[约定式提交规范](https://www.conventionalcommits.org/zh/v1.0.0-beta.3/)。首先让我们从一条提交记录出发看一下angular是如何写提交信息的。

![在这里插入图片描述](https://user-gold-cdn.xitu.io/2019/5/26/16af2c25e492e504?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

如上所示，angular提交信息遵循如下格式：

```
<type>(<scope>): <subject> # header信息头必须
<BLANK LINE>
<body> # 信息体
<BLANK LINE>
<footer> # 结束部分
复制代码
```

*   header 信息头（必须）`<type>(<scope>): <subject>`

    信息头必须要有type，它严格限定为如下值：

    ```
    feat: A new feature
    fix: A bug fix
    docs: Documentation only changes
    style: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
    refactor: A code change that neither fixes a bug nor adds a feature
    perf: A code change that improves performance
    test: Adding missing or correcting existing tests
    chore: Changes to the build process or auxiliary tools and libraries such as documentation generation
    复制代码
    ```

    另外如果本次提交是回退之前的提交，应该以revert:开头，跟着要回退提交的header信息，在body中写：This reverts commit <hash>

    其他开源项目的type类型也类似，像electron的type类型如下所示，详见[Commit message guidelines](https://electronjs.org/docs/development/pull-requests)：

    ```
    fix: A bug fix
    feat: A new feature
    docs: Documentation changes
    test: Adding missing tests or correcting existing tests
    build: Changes that affect the build system
    ci: Changes to our CI configuration files and scripts
    perf: A code change that improves performance
    refactor: A code change that neither fixes a bug nor adds a feature
    style: Changes that do not affect the meaning of the code (linting)
    vendor: Bumping a dependency like libchromiumcontent or node
    复制代码
    ```

    接下来是scope。它指定了本次提交的影响范围，比如数据层、控制层、视图层等等，视项目不同而定。如果影响范围较大，可以使用通配符\*。scope可以忽略。

    最后是subject，指出本次提交的主题，是对本次提交的简短描述，不超过50个字符。注意它和前面的冒号之间要有空格，和type一样，必须要有。subject内容有以下规定：

    1.  以动词开头，使用第一人称现在时，比如change，而不是changed或changes
    2.  首字母小写
    3.  结尾不加句号（.）

    type和subject决定了本次提交信息的质量，是灵魂所在。

*   body 信息体（可忽略）

    是对header中subject的补充，可以写一些本次提交改动了哪里和有什么影响等内容。注意时态同样要使用一般现在时，比如改动要写change，不能用changed或changes。

*   footer 信息尾部（可忽略）

    尾部可以包含一些类似做出了哪些重大改变这样的内容，也可以写关闭了那些issue。另外Breaking Changes要以`BREAKING CHANGE:`打头，后面跟空格或两个新行和具体内容。关闭了那些bug要使用`Closes`打头，哪怕只关闭了一个，例如`Closes #234`

angular关于commit message的详细规范请参见[Git Commit Message Conventions文档](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#heading=h.gbbngquhe0qa)。

### 三、git commit的优秀辅助工具

看来要写出符合git commit规范的信息也是不容易的，不过社区也为我们提供了一些辅助工具来帮助进行提交，下面根据使用目的来简单介绍一下这些工具。

#### 1、生成commit信息

[cz\-cli](https://github.com/commitizen/cz-cli) 是一款可以交互式建立提交信息的工具。它帮助我们从type开始一步步建立提交信息，具体效果如图所示，通过上下键控制指向你想要的type类型。

![在这里插入图片描述](https://user-gold-cdn.xitu.io/2019/5/26/16af2c25eca8de8b?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

> 注意：
>
> *   windows下使用git bash 运行该工具不能上下选择，可以使用powershell代替。
> *   此工具要配合adapter（类似模板）使用，来提供交互提交的样式包括type类型和提交的结构，可自定义。

全局环境下安装使用方法如下：

```
# 需要同时安装commitizen和cz-conventional-changelog，后者是adapter
$ npm install -g commitizen cz-conventional-changelog
# 配置安装的adapter
$ echo '{ "path": "cz-conventional-changelog" }' > ~/.czrc
# 使用
$ git cz
复制代码
```

本地环境下（非全局安装）使用方法如下：

```
# 安装commitizen
$ npm install --save-dev commitizen
# 接下来安装适配器
# for npm >= 5.2
$ npx commitizen init cz-conventional-changelog --save-dev --save-exact
# for npm < 5.2
$ ./node_modules/.bin/commitizen init cz-conventional-changelog --save-dev --save-exact

// package.json script字段中添加commit命令
"scripts": {
   "commit": "git-cz"
}
// use
$ npm run commit

// 如果不希望每次使用npm run commit写提交信息的话，可以使用git hook，把git commit命令替换成交互式提交，注意windows下不生效
"husky": {
  "hooks": {
    "prepare-commit-msg": "exec < /dev/tty && git cz --hook",
  }
}
复制代码
```

#### 2、校验commit信息

[commitlint](https://github.com/conventional-changelog/commitlint)是一款提交信息校验工具，原理是可用git hooks在真正进行git commit入库操作前对信息进行验证，不符合规则的commit信息将会被阻止提交入库，如下所示。

![在这里插入图片描述](https://user-gold-cdn.xitu.io/2019/5/26/16af2c25ef6ea25f?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

使用方式也很简单：

```
# 安装 commitlint cli and conventional config
$ npm install --save-dev @commitlint/{config-conventional,cli}
# Windows下自带命令行工具不会识别/{x,x}，所以使用以下语句安装
$ npm install --save-dev @commitlint/config-conventional @commitlint/cli

# 生成commitlint配置文件，这步是必须的，不然提交会报错，达不到效果
$ echo "module.exports = {extends: ['@commitlint/config-conventional']}" > commitlint.config.js
复制代码
```

> 注意：使用commitlint时需要建立校验文件commitlint.config.js，不然会校验失败

如果大家自己写过git hooks，那么可以把commitlint添加到git commit前的校验中，如果不是很熟的话可以借助一些工具，比如husky。

```
# 安装husky
$ npm i -D husky
# package.json文件添加如下字段
"husky": {
  "hooks": {
    "commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
  }
}
复制代码
```

当然如果认为遵守规则很累，可以在git commit时使用 \-\-no\-verify参数跳过验证，直接提交。不过这样使用该插件就没意义了。所以尽量保证自己写的commit信息符合规范。

#### 3、生成changelog文档

changelog是改动日志，包含我们发布的版本信息，以及每次版本更新的东西。

[conventional\-changelog\-cli](https://github.com/conventional-changelog/conventional-changelog/tree/master/packages/conventional-changelog-cli)是一款changelog生成工具，通过提取commit信息（默认提取类型为feat、fix和包含breaking change的提交信息）为我们自动化生成changelog文档。

全局使用方法如下：

```
# 安装conventional-changelog-cli
$ npm install -g conventional-changelog-cli
$ cd my-project
# 保留原changelog文档，生成本次改变
$ conventional-changelog -p angular -i CHANGELOG.md -s
# 完全重新生成changelog文档
$ conventional-changelog -p angular -i CHANGELOG.md -s -r 0
复制代码
```

如果不想全局安装的话，可以使用npm run script方式运行，如下所示

```
$ npm i -D conventional-changelog-cli

// package.json script字段中添加version命令
"script": {
  "version": "conventional-changelog -p angular -i CHANGELOG.md -s && git add CHANGELOG.md"
}
// use
$ npm run version
复制代码
```

conventional\-changelog\-cli生成changelog是根据到目前为止的所有提交信息同最新一次tag作比较得到的所有feature、bug、breaking change信息进行文档的生成，所以要在每次版本更新并生成changelog文档后对分支打tag，再push到远程分支。

这里摘取conventional\-changelog\-cli推荐的整体流程：

*   Make changes 改动代码
*   Commit those changes 使用git commit提交改动信息
*   Make sure Travis turns green 确保提交信息都符合规则
*   Bump version in package.json 更改package.json中的版本
*   conventionalChangelog 使用该工具生成changelog
*   Commit package.json and CHANGELOG.md files 提交package.json和changelog文档
*   Tag 给分支打标签
*   Push 推送到远程分支

#### 4、高级工具

社区同样提供了一些高级工具来自动化进行上述的某些流程，可以说提供了一条龙服务。具体工具如下：

[standard\-version](https://github.com/conventional-changelog/standard-version): 更新版本、生成changelog、打tag

[semantic\-release](https://github.com/semantic-release/semantic-release): 更新版本、生成changelog、打tag、推送代码发布

具体使用方法请自行查看文档，这里不再赘述。

### 四、修改及美化commit信息

前面讲了这么多git commit规范，可能大家要问了，我也准备从现在开始写符合规范的提交信息，那之前项目中的不符合规范的信息怎么办呢？其实之前的提交信息也是有办法修改的，关键就是使用`git rebase`命令。此外还有一个问题就是我写了很多条提交信息，但其实都是干的同一件事（这很常见，比如说要修复某个bug，改好之后发现这个bug在其他设备上并没有改好，于是又改好之后提交了一次，但都是改的同一个问题），有办法将他们合并成一条吗？其实有的，关键也在于`git rebase`。是不是瞬间感觉这个命令很强大，想要迫不及待的试一下呢。

好吧，不卖关子了，直接来到正题，如何使用`git rebase`进行变基操作。先说一下如果直接使用`git rebase [target-branch]`，虽然可以帮我们在本分支基于目标分支进行变基操作，但它只会让两个分支的所有提交连成一条线，不能修改具体提交信息，所以需要使用`git rebase -i`进行交互式操作。首先了解一下`git rebase -i`的几个操作。

![在这里插入图片描述](https://user-gold-cdn.xitu.io/2019/5/26/16af2c25f1d7ac7d?imageView2/0/w/1280/h/960/format/webp/ignore-error/1)

如上图所示，git rebase提供了几个操作来对提交信息进行处理，这里挑几个常用的介绍一下。

*   pick 缩写为p，保留本次提交包括文件改动和提交信息
*   reword 缩写为r，保留本次改动，但重写提交信息
*   edit 缩写为e，保留本次改动，而且可以附加改动、编辑提交信息
*   squash 缩写为s，保留改动，但本次提交会附加到上次提交中，也就是和上次提交合并（提交信息也会合并）
*   fixup 缩写为f，同squash，不同的是会丢弃掉本次提交的说明信息
*   drop 缩写为d，丢掉本次提交（包括文件改动和提交信息）

另外还要知道`git rebase --continue`命令用来告诉git继续进行合并，一般在解决冲突后使用（一般来讲如果所有的提交没有冲突的话，可以一直走下去，直到出现成功的提示。但如果两次提交合并涉及到冲突，就需要解决冲突并在git add后使用该命令继续走下去）；`git rebase --abort`命令用来终止变基操作，一般在不想进行rebase时使用（大部分时间是因为玩脱了，rebase到了一种不可预知的地步，不知道干啥了，就只能终止了）。直到出现类似“Successfully rebased and updated refs/heads/dev.”的消息就说明本次变基成功了。下面具体讲一下如何修改和美化提交信息。

#### 1、修改commit信息

修改提交信息可以分为以下几个步骤，当然具体步骤还要具体情况具体分析，有些可以忽略。

1.  暂存工作状态：使用`git stash`将当前工作状态进行暂存，如果没有需要暂存的工作状态请忽略

2.  转到需要修改的提交上：使用`git rebase -i [commit-id]^`将 HEAD 移动到需要修改的 commit\-id 上，因为该\[commit\-id\]也在修改之列，所以要基于它的上一个提交变基，或者直接使用\[commit\-id\]^

3.  将pick修改为想要进行的操作命令：进行编辑时一般要把所有需要修改的commit的pick改为r或e，提示：如果多的话可以使用vim的全局替换

4.  重新编辑commit信息

5.  附加修改：如果需要在该分支上修改其他内容，可以在改动文件后直接使用`git add` 将其添加到暂存区，并使用 `git commit –amend` 追加改动到提交。如果不需要请忽略

6.  继续进行变基操作：使用`git rebase –continue`继续，一般如果提交没有冲突或者附加修改的话，不需要手动输入，git会自动进行下一次操作。

7.  变基完成：重复以上步骤，直到出现变基成功文字。如果暂存过工作状态，需要使用`git stash pop`恢复之前的工作状态，结束。

#### 2、commit信息的美化

我们大多数时候只会使用`git merge`来将开发代码合并到主分支。不过这样会导致主分支包含我们合并分支的所有提交信息。长此以往，会让commit history越来越繁杂，但其实合并的代码完全可以用一条提交信息比如`feat: 添加某项新特性`来代替。当然还有其他原因会导致commit信息重复且不必要。比如当我们在拿不准bug到底有没有修复成果时可能会多次改动代码进行测试，如果每次改动测试都进行了提交，就会产生多次commit信息，如果不对这些commit做合并的话，在我们将代码合并到开发主分支时就会产生很多繁杂的commit信息，不过由于这些commit信息都是为解决同样的事情服务的，完全可以合到一起。所以如果你嫌弃commit信息太啰嗦冗余，那么就需要对其进行美化了。美化主要有两种方式：`git rebase` 和 `git merge --squash`，这里将介绍它们的使用，并进行对比。

1.  rebase merge

    > 注意：如果要合并的commit历史过多并且对git rebase命令使用不熟练，请慎用，不然可能会被各种冲突逼疯的！

    如果我们想将dev的提交信息进行美化并合并到master分支，可以进行如下操作：

    *   先切换到 dev 分支：`git checkout dev`
    *   基于master进行变基操作：`git rebase -i master`，其中具体的操作请参见上一小节，不同的不过是把一些提交的pick改为s而已，即提交信息合并到上一次提交。
    *   切换回目标分支：`git checkout master`
    *   合并: `git merge dev`
2.  squash merge

    同样以dev分支合并到master为例：

    *   切换到目标分支：`git checkout master`
    *   以 squash 的形式 merge：`git merge --squash dev`
    *   提交：修改冲突后进行提交

两种方式都能实现提交信息的合并，保持 master 分支干净整洁。不过它们也有很大不同。

squash merge会把分支的所有提交一股脑应用在目标分支上，然后你要修改冲突后再提交，生成一次commit，而这次commit包含dev的所有改动。产生的这次新的commit的作者自然也就是做了本次将dev分支合并到master分支操作的人，他可能并不是原dev分支的作者，也就掩盖了真实的作者。此外无论改动有多少，只会产生一次提交记录。

rebase merge拥有更高的可操作性，它允许我们可以选择保留几条有意义的提交，而不像squash merge只有一条。当然有更高的操作自由度也意味着步骤比较繁琐，不像squash merge简单方便。当然变基操作完成后在主分支上使用`git merge`进行合并，原作者信息会得到保留。

总之，如果你想要更快进行提交合并，能容忍原作者信息丢失的话，可以选择squash merge；如果你想要保留多条有意义的提交信息和需要保留原作者信息的话，rebase merge可能要更适合你。

话说回来，其实`git rebase`命令非常强大，不仅能做本分支commit信息的修改、合并，还能使用`git rebase [startpoint] [endpoint] --onto [branchName]`将本分支的某一段commit集合合并到另一分支。嗯，git很是博大精深呢，要想达到精通，我还有很长一段路要走！

#### 参考资料：

1.  [你可能会忽略的 Git 提交规范](http://blog.didispace.com/git-commit-specification/)
2.  [Commit message 和 Change log 编写指南](http://www.ruanyifeng.com/blog/2016/01/commit_message_change_log.html)
3.  [Git Commit Message Conventions](https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit#)
4.  [【Git】rebase 用法小结](https://www.jianshu.com/p/4a8f4af4e803)
5.  [merge squash 和 merge rebase 区别](https://liuliqiang.info/post/difference-between-merge-squash-and-rebase/)
6.  [git笔记\-进阶](http://www.360doc.com/content/12/0216/14/1016783_187073843.shtml)

关注下面的标签，发现更多相似文章