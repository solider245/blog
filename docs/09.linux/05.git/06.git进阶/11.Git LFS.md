---
title: Git LFS
date: 2020-10-12 12:09:51
permalink: /pages/d8b4bb/
categories:
  - git
  - git进阶
tags:
  - 
---
# Git LFS

### 什么是Git LFS？

Git是一个 *分布式* 版本控制系统，这意味着存储库的整个历史记录都在克隆过程中转移到了客户端。 对于包含大文件（尤其是定期修改的大文件）的项目，此初始克隆可能会花费大量时间，因为客户端必须下载每个文件的每个版本。 Git LFS（大文件存储）是Atlassian，GitHub和其他一些开源贡献者开发的Git扩展，它通过 *延迟* 下载大文件的相关版本来减少大文件在存储库中的影响 。 具体来说，大型文件是在结帐过程中下载的，而不是在克隆或提取过程中下载的。

Git LFS通过用微小的 *指针* 文件 替换存储库中的大文件来做到这一点 。 在正常使用期间，您将永远不会看到这些指针文件，因为它们是由Git LFS自动处理的：

1.  将文件添加到存储库时，Git LFS会用指针替换其内容，并将文件内容存储在本地Git LFS缓存中。

    ![git lfs-git添加](https://wac-cdn.atlassian.com/dam/jcr:9abf0939-a978-4867-a751-28bd1ca318de/01.2017-12-12-00-28-43.svg)
2.  当您将新提交推送到服务器时，新推送的提交引用的所有Git LFS文件都会从本地Git LFS缓存转移到绑定到Git存储库的远程Git LFS存储。

    ![git lfs-git推送](https://wac-cdn.atlassian.com/dam/jcr:cb729dbe-3c28-4775-821d-0e2518668d8b/02.2017-12-12-00-28-43.svg)
3.  当您签出包含Git LFS指针的提交时，它们将替换为本地Git LFS缓存中的文件，或者从远程Git LFS存储区下载。 ![git lfs-git结帐](https://wac-cdn.atlassian.com/dam/jcr:7e70a242-db91-4093-b178-c1281fe3ddbb/03.2017-12-12-00-28-43.svg "git lfs-git结帐")

Git LFS是无缝的：在工作副本中，您只会看到实际的文件内容。 这意味着您可以使用Git LFS，而无需更改现有的Git工作流程。 您只需 按常规进行 `git checkout` ，编辑 `git add` ，和 `git commit` 。 `git clone` 而且， `git pull` 由于您仅下载 *实际* 签出 的提交所引用的大文件的版本 ，而不是曾经存在的文件的每个版本，因此 操作将大大加快 。

要使用Git LFS，您将需要一个支持Git LFS的主机，例如 [Bitbucket Cloud](https://bitbucket.org/) 或 [Bitbucket Server](https://www.atlassian.com/software/bitbucket/server) 。 存储库用户将需要 [安装Git LFS命令行客户端](#installing-git-lfs) ，或者需要 [安装](#installing-git-lfs) Git LFS的GUI客户端，例如 [Sourcetree](https://www.sourcetreeapp.com/) 。 有趣的事实：发明了Sourcetree的Atlassian开发人员Steve Streeting也是Git LFS项目的主要贡献者，因此Sourcetree和Git LFS可以很好地合作。

什么是Git LFS？

*   [安装Git LFS](#installing-git-lfs)
*   [创建一个新的Git LFS存储库](#creating-new-repository)
*   [克隆现有的Git LFS存储库](#clone-respository)
*   [加快克隆速度](#speeding-up-clones)
*   [拉出并签出](#pulling-and-checking-out)
*   [加快拉力](#speeding-up-pulls)
*   [使用Git LFS跟踪文件](#tracking-files)
*   [承诺和推动](#committing-and-pushing)
*   [在主机之间移动Git LFS存储库](#moving-between-hosts)
*   [获取额外的Git LFS历史记录](#fetching-history)
*   [删除本地Git LFS文件](#deleting-local-files)
*   [从服务器删除远程Git LFS文件](#deleting-remote-files)
*   [查找引用Git LFS对象的路径或提交](#finding-references)
*   [包含/排除Git LFS文件](#including-excluding-files)
*   [锁定Git LFS文件](#locking-files)
*   [Git LFS如何工作](#how-git-lfs-works)

### 安装Git LFS

1.  有三种简单的方法来安装Git LFS：

    一个。 使用您喜欢的软件包管理器进行安装。 `git-lfs` 软件包可用于Homebrew，MacPorts，dnf和 [packagecloud](https://github.com/github/git-lfs/blob/master/INSTALLING.md) ； 要么

    b。 从项目网站 下载并安装 [Git LFS](https://git-lfs.github.com/) ； 要么

    C。 安装 [Sourcetree](https://www.sourcetreeapp.com/) ，它是与Git LFS捆绑在一起的免费Git GUI客户端。

2.  一旦git\-lfs在您的路径上，请运行git lfs install初始化Git LFS（如果您安装了Sourcetree，则可以跳过此步骤）：

    ```
    $ git lfs install
    Git LFS initialized.

    ```

    您只需要运行 `git lfs install` 一次。 为您的系统初始化后，当您克隆包含Git LFS内容的存储库时，Git LFS将自动自举。

### 创建一个新的Git LFS存储库

要创建一个新的Git LFS感知存储库，您需要在创建存储库后运行git lfs install：

```
# initialize Git
$ mkdir Atlasteroids
$ cd Atlasteroids
$ git init
Initialized empty Git repository in /Users/tpettersen/Atlasteroids/.git/
# initialize Git LFS
$ git lfs install
Updated pre-push hook.
Git LFS initialized.

```

这将 在您的存储库中 安装一个特殊的 `pre-push` [Git挂钩](https://www.atlassian.com/git/tutorials/git-hooks) ，该 [挂钩将](https://www.atlassian.com/git/tutorials/git-hooks) 在您将Git LFS文件传输到服务器时 `git push` 。

已为所有 [Bitbucket Cloud](https://bitbucket.org/) 存储库 自动启用Git LFS 。 对于 [Bitbucket Server](https://www.atlassian.com/software/bitbucket/server) ，您需要在存储库设置中启用Git LFS：

![Bitbucket服务器Git LFS](https://wac-cdn.atlassian.com/dam/jcr:2d4bd71b-5205-4297-aec9-f0c91bfb6ad2/05.png?cdnVersion=1084)

为存储库初始化Git LFS后，您可以使用指定要跟踪的文件 [`git lfs track`](#tracking-files) 。

### 克隆现有的Git LFS存储库

安装Git LFS后，您可以使用正常克隆Git LFS存储库 `git clone` 。 在克隆过程结束时，Git将检出默认分支（通常为 `master` ），并且将自动为您下载完成检出过程所需的所有Git LFS文件。 例如：

```
$ git clone git@bitbucket.org:tpettersen/Atlasteroids.git
Cloning into 'Atlasteroids'...
remote: Counting objects: 156, done.
remote: Compressing objects: 100% (154/154), done.
remote: Total 156 (delta 87), reused 0 (delta 0)
Receiving objects: 100% (156/156), 54.04 KiB | 31.00 KiB/s, done.
Resolving deltas: 100% (87/87), done.
Checking connectivity... done.
Downloading Assets/Sprites/projectiles-spritesheet.png (21.14 KB)
Downloading Assets/Sprites/productlogos_cmyk-spritesheet.png (301.96 KB)
Downloading Assets/Sprites/shuttle2.png (1.62 KB)
Downloading Assets/Sprites/space1.png (1.11 MB)
Checking out files: 100% (81/81), done.

```

`PNGs` Git LFS跟踪该存储库中 有四个 。 运行git clone时，由于从存储库中检出了指针文件，因此一次下载了一个Git LFS文件。

### 加快克隆速度

如果要克隆具有大量LFS文件的存储库，则显式 `git lfs clone` 命令可提供更好的性能：

```
$ git lfs clone git@bitbucket.org:tpettersen/Atlasteroids.git
Cloning into 'Atlasteroids'...
remote: Counting objects: 156, done.
remote: Compressing objects: 100% (154/154), done.
remote: Total 156 (delta 87), reused 0 (delta 0)
Receiving objects: 100% (156/156), 54.04 KiB | 0 bytes/s, done.
Resolving deltas: 100% (87/87), done.
Checking connectivity... done.
Git LFS: (4 of 4 files) 1.14 MB / 1.15 MB

```

该 `git lfs clone` 命令不会等待 一次下载一个Git LFS文件，而是 等到结帐完成后再批量下载所有必需的Git LFS文件。 这利用了并行下载的优势，并大大减少了产生的HTTP请求和进程的数量（这对于提高Windows的性能尤为重要）。

### 拉出并签出

就像克隆一样，您可以使用normal从Git LFS存储库中提取 `git pull` 。 提取完成后，所有需要的Git LFS文件都会作为自动结帐过程的一部分进行下载：

```
$ git pull
Updating 4784e9d..7039f0a
Downloading Assets/Sprites/powerup.png (21.14 KB)
Fast-forward
Assets/Sprites/powerup.png | 3 +
Assets/Sprites/powerup.png.meta | 4133 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
2 files changed, 4136 insertions(+)
create mode 100644 Assets/Sprites/projectiles-spritesheet.png
create mode 100644 Assets/Sprites/projectiles-spritesheet.png.meta

```

无需显式命令即可检索Git LFS内容。 但是，如果由于意外原因导致检出失败，则可以使用以下命令下载当前提交的所有丢失的Git LFS内容 `git lfs pull` ：

```
$ git lfs pull
Git LFS: (4 of 4 files) 1.14 MB / 1.15 MB

```

### 加快拉力

像一样 `git lfs clone` ， `git lfs pull` 批量下载Git LFS文件。 如果您知道自上次上拉以来已更改了大量文件，则不妨在签出期间禁用自动Git LFS下载，然后使用显式批量下载Git LFS内容 `git lfs pull` 。 这可以通过 `-c` 在调用时 使用 选项 覆盖Git配置来完成 `git pull` ：

```
$ git -c filter.lfs.smudge= -c filter.lfs.required=false pull && git lfs pull

```

由于键入的内容很多，因此您不妨创建一个简单的 [Git别名](https://blogs.atlassian.com/2014/10/advanced-git-aliases/) 来为您执行批处理的Git和Git LFS拉取：

```
$ git config --global alias.plfs "\!git -c filter.lfs.smudge= -c filter.lfs.required=false pull && git lfs pull"
$ git plfs

```

当需要下载大量的Git LFS文件时（同样，尤其是在Windows上），这将大大提高性能。

### 使用Git LFS跟踪文件

在将新的大文件类型添加到存储库时，需要通过使用以下 `git lfs track` 命令 指定模式来告诉Git LFS跟踪它 ：

```
$ git lfs track "*.ogg"
Tracking *.ogg

```

请注意，周围的引号 `"*.ogg"` 很重要。 省略它们将使您的shell扩展通配符，并且将为 `.ogg` 当前目录中的 每个 文件 创建单独的条目 ：

```
# probably not what you want
$ git lfs track *.ogg
Tracking explode.ogg
Tracking music.ogg
Tracking phaser.ogg

```

Git LFS支持的模式与所支持的模式相同 [`.gitignore`](https://www.atlassian.com/git/tutorials/gitignore) ，例如：

```
# track all .ogg files in any directory
$ git lfs track "*.ogg"
# track files named music.ogg in any directory
$ git lfs track "music.ogg"
# track all files in the Assets directory and all subdirectories
$ git lfs track "Assets/"
# track all files in the Assets directory but *not* subdirectories
$ git lfs track "Assets/*"
# track all ogg files in Assets/Audio
$ git lfs track "Assets/Audio/*.ogg"
# track all ogg files in any directory named Music
$ git lfs track "**/Music/*.ogg"
# track png files containing "xxhdpi" in their name, in any directory
$ git lfs track "*xxhdpi*.png

```

这些模式是相对于您运行 `git lfs track` 命令 的目录的 。 为了简单起见，最好 `git lfs track` 从存储库的根目录 运行 。 需要注意的是Git的LFS不支持 *负的模式* 一样 `.gitignore` 呢。

运行后 `git lfs track` ，您会注意到 `.gitattributes` 在从中运行命令的目录中 命名 了 一个新文件 。 `.gitattributes` 是一种Git机制，用于将特殊行为绑定到某些文件模式。 Git LFS自动创建或更新 `.gitattributes` 文件，以将跟踪的文件模式绑定到Git LFS过滤器。 但是，您需要将对 `.gitattributes` 文件的 任何更改 自己提交到存储库：

```
$ git lfs track "*.ogg"
Tracking *.ogg
$ git add .gitattributes
$ git diff --cached
diff --git a/.gitattributes b/.gitattributes
new file mode 100644
index 0000000..b6dd0bb
--- /dev/null
+++ b/.gitattributes
@@ -0,0 +1 @@
+*.ogg filter=lfs diff=lfs merge=lfs -text
$ git commit -m "Track ogg files with Git LFS"

```

为了便于维护，最简单的方法 `.gitattributes` 是始终 `git lfs track` 从存储库的根目录 运行 ，将所有Git LFS模式保存在一个 文件中 。 但是，您可以 `.gitattributes` 通过 `git lfs track` 不带任何参数 的调用 来显示Git LFS当前跟踪的所有模式的列表（及其 定义 的 文件） ：

```
$ git lfs track
Listing tracked paths
*.stl (.gitattributes)
*.png (Assets/Sprites/.gitattributes)
*.ogg (Assets/Audio/.gitattributes)

```

您可以通过从 `.gitattributes` 文件中 删除适当的行 或运行以下 `git lfs untrack` 命令 来停止使用Git LFS跟踪特定模式 ：

```
$ git lfs untrack "*.ogg"
Untracking *.ogg
$ git diff
diff --git a/.gitattributes b/.gitattributes
index b6dd0bb..e69de29 100644
--- a/.gitattributes
+++ b/.gitattributes
@@ -1 +0,0 @@
-*.ogg filter=lfs diff=lfs merge=lfs -text

```

运行后， `git lfs untrack` 您将不得不再次将更改提交给 `.gitattributes` 自己。

### 承诺和推动

您可以正常提交并推送到包含Git LFS内容的存储库。 如果您已对Git LFS跟踪的文件进行了更改，那么 `git push` 当Git LFS内容传输到服务器时 ，您将看到一些其他输出 ：

```
$ git push
Git LFS: (3 of 3 files) 4.68 MB / 4.68 MB
Counting objects: 8, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 1.16 KiB | 0 bytes/s, done.
Total 8 (delta 1), reused 0 (delta 0)
To git@bitbucket.org:tpettersen/atlasteroids.git
7039f0a..b3684d3 master -> master

```

如果由于某种原因传输LFS文件失败，则推送将被中止，您可以放心地重试。 与Git一样，Git LFS存储也是 *可寻址的内容* ：内容是根据密钥存储的，该密钥是内容本身的SHA\-256哈希。 这意味着重新尝试将Git LFS文件传输到服务器总是安全的。 您不能用错误的版本意外覆盖Git LFS文件的内容。

### 在主机之间移动Git LFS存储库

要将Git LFS存储库从一个托管提供程序迁移到另一个托管提供程序，可以使用 `git lfs fetch` 和 `git lfs push` 结合使用 `--all option` 指定的。

例如，要将所有Git和Git LFS存储库从名为 `github` 的远程 `bitbucket` 移动 到名为 😉 的远程 ：

```
# create a bare clone of the GitHub repository
$ git clone --bare git@github.com:kannonboy/atlasteroids.git
$ cd atlasteroids
# set up named remotes for Bitbucket and GitHub
$ git remote add bitbucket git@bitbucket.org:tpettersen/atlasteroids.git
$ git remote add github git@github.com:kannonboy/atlasteroids.git
# fetch all Git LFS content from GitHub
$ git lfs fetch --all github
# push all Git and Git LFS content to Bitbucket
$ git push --mirror bitbucket
$ git lfs push --all bitbucket

```

### 获取额外的Git LFS历史记录

Git LFS通常仅下载您实际在本地检出的提交所需的文件。 但是，您可以使用以下命令强制Git LFS为其他最近修改的分支下载额外的内容 `git lfs fetch --recent` ：

```
$ git lfs fetch --recent
Fetching master
Git LFS: (0 of 0 files, 14 skipped) 0 B / 0 B, 2.83 MB skipped Fetching recent branches within 7 days
Fetching origin/power-ups
Git LFS: (8 of 8 files, 4 skipped) 408.42 KB / 408.42 KB, 2.81 MB skipped
Fetching origin/more-music
Git LFS: (1 of 1 files, 14 skipped) 1.68 MB / 1.68 MB, 2.83 MB skipped

```

这对于在外出午餐时批量下载新的Git LFS内容很有用，或者如果您打算与队友一起审查工作，并且由于互联网连接受限而无法在以后下载内容，这将非常有用。 例如，您可能希望 `git lfs fetch --recent` 在跳上飞机之前 先跑步 ！

Git LFS会考虑包含最近提交超过7天的提交的任何分支或标签。 您可以通过设置 `lfs.fetchrecentrefsdays` 属性 来配置被视为最近的天数 ：

```
# download Git LFS content for branches or tags updated in the last 10 days
$ git config lfs.fetchrecentrefsdays 10

```

默认情况下， `git lfs fetch --recent` 仅在最近分支或标记的尖端下载Git LFS内容以进行提交。

![git lfs-git lfs获取--recent](https://wac-cdn.atlassian.com/dam/jcr:ce62b78b-dc55-49aa-9b4e-33158f7a0d51/06.svg?cdnVersion=1084)

但是，您可以通过配置以下 `lfs.fetchrecentcommitsdays` 属性 来配置Git LFS以下载内容，以便在最近的分支和标签上进行较早的提交 ：

```
# download the latest 3 days of Git LFS content for each recent branch or tag
$ git config lfs.fetchrecentcommitsdays 3

```

使用此设置小心：如果你有快速移动的分支机构，这可能会导致一个 *巨大的* 下载数据量。 但是，如果您需要查看分支上的插页式广告更改，跨分支的樱桃采摘提交或重写历史记录，它可能会很有用。

![git lfs-git lfs提取-最近提交](https://wac-cdn.atlassian.com/dam/jcr:4909bcee-61de-4b76-bc7a-b924e84e2695/07.svg?cdnVersion=1084)

如 [在主机之间移动Git LFS存储库中所述](#moving-between-hosts) ，您还可以选择通过 以下方式为存储库 获取 *所有* Git LFS内容 `git lfs fetch --all` ：

```
$ git lfs fetch --all
Scanning for all objects ever referenced...
✔ 23 objects found
Fetching objects...
Git LFS: (9 of 9 files, 14 skipped) 2.06 MB / 2.08 MB, 2.83 MB skipped

```

### 删除本地Git LFS文件

您可以使用以下 `git lfs prune` 命令 从本地Git LFS缓存中删除文件 ：

```
$ git lfs prune
✔ 4 local objects, 33 retained
Pruning 4 files, (2.1 MB)
✔ Deleted 4 files

```

这将删除所有被认为是 *旧的* 本地Git LFS文件 。 旧文件是以下 **未** 引用的 任何文件 ：

*   当前签出的提交
*   尚未被推送（到源或 `lfs.pruneremotetocheck` 设置为 任何 内容）的提交
*   最近一次提交

默认情况下，最近的提交是最近 *十天* 内 创建的任何提交 。 通过添加以下内容计算得出：

*   [获取额外的Git LFS历史记录](#fetching-history) （默认为*7* ）中 `lfs.fetchrecentrefsdays` 讨论 的 属性 的值 ； 至[](#fetching-history)
*   `lfs.pruneoffsetdays` 属性 的值 （默认为 *3* ）

![git lfs修剪](https://wac-cdn.atlassian.com/dam/jcr:fda8acc7-67bc-4af0-b047-f6a226aa68bb/08.svg?cdnVersion=1084)

您可以配置修剪偏移量以将Git LFS内容保留更长的时间：

```
# don't prune commits younger than four weeks (7 + 21)
$ git config lfs.pruneoffsetdays 21

```

与Git的内置垃圾收集不同，Git LFS内容 *不会* 自动修剪，因此 `git lfs prune` 定期 运行 是保持本地存储库大小减小的一个好主意。

您可以测试修剪操作的效果 `git lfs prune --dry-run` ：

```
$ git lfs prune --dry-run
✔ 4 local objects, 33 retained
4 files would be pruned (2.1 MB)

```

以及确切的Git LFS对象将被修剪 `git lfs prune --verbose --dry-run` ：

```
$ git lfs prune --dry-run --verbose
✔ 4 local objects, 33 retained
4 files would be pruned (2.1 MB)
* 4a3a36141cdcbe2a17f7bcf1a161d3394cf435ac386d1bff70bd4dad6cd96c48 (2.0 MB)
* 67ad640e562b99219111ed8941cb56a275ef8d43e67a3dac0027b4acd5de4a3e (6.3 KB)
* 6f506528dbf04a97e84d90cc45840f4a8100389f570b67ac206ba802c5cb798f (1.7 MB)
* a1d7f7cdd6dba7307b2bac2bcfa0973244688361a48d2cebe3f3bc30babcf1ab (615.7 KB)

```

通过 `--verbose` 模式 输出的长十六进制字符串 是要修剪的Git LFS对象的SHA\-256哈希（也称为对象ID或OID）。 您可以使用“ [查找路径”中](#finding-references) 的技术 [或引用Git LFS对象的提交中](#finding-references) 的技术， [找到](#finding-references) 有关将被修剪的对象的更多信息。

作为一项附加的安全检查，您可以使用该 `--verify-remote` 选项在删除之前，检查远程Git LFS存储区是否具有您的Git LFS对象的副本：

```
$ git lfs prune --verify-remote
✔ 16 local objects, 2 retained, 12 verified with remote
Pruning 14 files, (1.7 MB)
✔ Deleted 14 files

```

这使修剪过程明显变慢，但是您可以从服务器上恢复所有修剪的对象，从而使您高枕无忧。 您可以 `--verify-remote` 通过 `lfs.pruneverifyremotealways` 全局 配置 属性 为系统永久 启用该 选项 ：

```
$ git config --global lfs.pruneverifyremotealways true

```

或者，您可以通过忽略 `--global` 上述命令中 的 选项 来仅对上下文存储库启用远程验证 。

### 从服务器删除远程Git LFS文件

Git LFS命令行客户端不支持从服务器删除文件，因此如何删除它们取决于您的托管服务提供商。

在Bitbucket Cloud中，您可以通过 **存储库设置> Git LFS** 查看和删除Git LFS文件 ：

![Bitbucket Cloud-从服务器删除lfs](https://wac-cdn.atlassian.com/dam/jcr:46218516-f4aa-490a-9afc-c36ca863c98f/09.png?cdnVersion=1084)

请注意，每个Git LFS文件均通过其SHA\-256 OID进行索引； 通过UI看不到引用每个文件的路径。 这是因为在可能引用给定对象的许多不同提交中可能有许多不同的路径，因此查找它们将是一个非常缓慢的过程。

要确定给定的Git LFS文件实际包含什么，您可以使用三个选项：

*   在Bitbucket Git LFS UI的左栏中查看文件预览图像和文件类型
*   使用Bitbucket Git LFS UI右栏中的链接下载文件\-搜索引用Git LFS对象的SHA\-256 OID的提交，如下一节所述

### 查找引用Git LFS对象的路径或提交

如果您具有Git LFS SHA\-256 OID，则可以使用以下命令确定引用它的提交 `git log --all -p -S <OID>` ：

```
$ git log --all -p -S 3b6124b8b01d601fa20b47f5be14e1be3ea7759838c1aac8f36df4859164e4cc
commit 22a98faa153d08804a63a74a729d8846e6525cb0
Author: Tim Pettersen <tpettersen@atlassian.com>
Date: Wed Jul 27 11:03:27 2016 +1000
Projectiles and exploding asteroids
diff --git a/Assets/Sprites/projectiles-spritesheet.png
new file mode 100755
index 0000000..49d7baf
--- /dev/null
+++ b/Assets/Sprites/projectiles-spritesheet.png
@@ -0,0 +1,3 @@
+version https://git-lfs.github.com/spec/v1
+oid sha256:3b6124b8b01d601fa20b47f5be14e1be3ea7759838c1aac8f36df4859164e4cc
+size 21647

```

该 `git log` 咒语通过 添加或删除 包含指定字符串（Git LFS SHA\-256 OID） 的行（ ）的 `-p` 任何分支（ `--all` ） 上的提交 生成补丁（ `-S` ）。

该修补程序将向您显示LFS对象的提交和路径，以及添加对象和提交时间。 您可以简单地检出提交，Git LFS将在需要时下载文件并将其放置在您的工作副本中。

如果您怀疑某个特定的Git LFS对象位于当前的HEAD或某个特定的分支中，则可以 `git grep` 用来查找引用它的文件路径：

```
# find a particular object by OID in HEAD
$ git grep 3b6124b8b01d601fa20b47f5be14e1be3ea7759838c1aac8f36df4859164e4cc HEAD
HEAD:Assets/Sprites/projectiles-spritesheet.png:oid sha256:3b6124b8b01d601fa20b47f5be14e1be3ea7759838c1aac8f36df4859164e4cc
# find a particular object by OID on the "power-ups" branch
$ git grep e88868213a5dc8533fc9031f558f2c0dc34d6936f380ff4ed12c2685040098d4 power-ups
power-ups:Assets/Sprites/shield2.png:oid sha256:e88868213a5dc8533fc9031f558f2c0dc34d6936f380ff4ed12c2685040098d4

```

您可以使用 包含Git LFS对象的ref，commit或tree进行 替换 `HEAD` 或 替换 `power-ups` 。

### 包含/排除Git LFS文件

在某些情况下，您可能只想为特定提交下载可用的Git LFS内容的子集。 例如，在配置CI构建以运行单元测试时，您可能只需要源代码，因此可能要排除构建代码不需要的重量级文件。

您可以使用 `git lfs fetch -X` （或 `--exclude` ） 排除模式或子目录 ：

```
$ git lfs fetch -X "Assets/**"

```

或者，您可能只希望包含特定的模式或子目录。 例如，音频工程师可以 使用 （或 ） 来获取正义 `ogg` 和 `wav` 文件 ： `git lfs fetch -I` `--include`

```
$ git lfs fetch -I "*.ogg,*.wav"

```

如果合并包括和排除，只有匹配的包括病毒码文件 *和* 不匹配的排除模式将是牵强。 例如，您可以使用以下方法获取 *Assets* 目录中的 *所有内容* `gifs` ：

```
$ git lfs fetch -I "Assets/**" -X "*.gif"

```

排除和包括支持相同的图案作为 [`git lfs track`](#tracking-files) 和 `.gitignore` 。 您可以通过设置 `lfs.fetchinclude` 和 `lfs.fetchexclude` config属性， 使这些模式对于特定存储库而言是永久性的 ：

```
$ git config lfs.fetchinclude "Assets/**"
$ git config lfs.fetchexclude "*.gif"

```

通过附加 `--global` 选项， 这些设置也可以应用于系统上的每个存储库 。

### 锁定Git LFS文件

不幸的是，没有解决二进制合并冲突的简便方法。 使用Git LFS文件锁定，您可以按扩展名或文件名锁定文件，并防止二进制文件在合并过程中被覆盖。

为了利用LFS的文件锁定功能，您首先需要告诉Git哪些类型的文件是可锁定的。 在下面的示例中，在git lfs track命令后附加了\-\-lockable标志，该命令既将PSD文件存储在LFS中，又将它们标记为可锁定。

```
$ git lfs track "*.psd" --lockable

```

然后将以下内容添加到您的.gitattributes文件中：

```
*.psd filter=lfs diff=lfs merge=lfs -text lockable
```

当准备对LFS文件进行更改时，您将使用lock命令以便将文件注册为在Git服务器上锁定的文件。

```
$ git lfs lock images/foo.psd
Locked images/foo.psd
```

一旦不再需要文件锁定，您可以使用Git LFS的unlock命令将其删除。

```
$ git lfs unlock images/foo.psd
```

可以 `git push` 使用 `--force` 标志 覆盖Git LFS文件锁，类似于 。 `--force` 除非您完全确定自己知道自己在做什么，否则 不要使用该 标志。

```
$ git lfs unlock images/foo.psd --force
```

### Git LFS如何工作

如果您有兴趣了解有关清洁和污迹过滤器，预推钩以及Git LFS背后的其他有趣计算机科学的更多信息，请在LinuxCon 2016上从Atlassian的Git LFS上查看以下演示文稿：