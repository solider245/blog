---
title: Git技巧和问题解决方案
date: 2020-10-12 12:09:51
permalink: /pages/a15cc0/
categories:
  - git
  - git常见问题
tags:
  - 
---
# 目录

*   [1\. 不显示中文](#1-%E4%B8%8D%E6%98%BE%E7%A4%BA%E4%B8%AD%E6%96%87)
*   [2\. 添加远程跟踪分支](#2-%E6%B7%BB%E5%8A%A0%E8%BF%9C%E7%A8%8B%E8%B7%9F%E8%B8%AA%E5%88%86%E6%94%AF)
*   [3\. 彻底删除文件或目录](#3-%E5%BD%BB%E5%BA%95%E5%88%A0%E9%99%A4%E6%96%87%E4%BB%B6%E6%88%96%E7%9B%AE%E5%BD%95)
*   [4\. Git命令自动补全](#4-git%E5%91%BD%E4%BB%A4%E8%87%AA%E5%8A%A8%E8%A1%A5%E5%85%A8)
*   [5\. 本地分支覆盖(替换)远程仓库中的分支](#5-%E6%9C%AC%E5%9C%B0%E5%88%86%E6%94%AF%E8%A6%86%E7%9B%96%E6%9B%BF%E6%8D%A2%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93%E4%B8%AD%E7%9A%84%E5%88%86%E6%94%AF)
*   [6\. 远程仓库中的分支覆盖(替换)本地分支](#6-%E8%BF%9C%E7%A8%8B%E4%BB%93%E5%BA%93%E4%B8%AD%E7%9A%84%E5%88%86%E6%94%AF%E8%A6%86%E7%9B%96%E6%9B%BF%E6%8D%A2%E6%9C%AC%E5%9C%B0%E5%88%86%E6%94%AF)
    *   [6.1. 方案1: 强制pull](#61-%E6%96%B9%E6%A1%881-%E5%BC%BA%E5%88%B6pull)
    *   [6.2. 方案2: 先fetch再将reset到远程分支](#62-%E6%96%B9%E6%A1%882-%E5%85%88fetch%E5%86%8D%E5%B0%86reset%E5%88%B0%E8%BF%9C%E7%A8%8B%E5%88%86%E6%94%AF)
*   [7\. 删除远程分支或tag](#7-%E5%88%A0%E9%99%A4%E8%BF%9C%E7%A8%8B%E5%88%86%E6%94%AF%E6%88%96tag)
    *   [7.1. Git v1.7.0 之后的新方法](#71-git-v170-%E4%B9%8B%E5%90%8E%E7%9A%84%E6%96%B0%E6%96%B9%E6%B3%95)
        *   [7.1.1. 删除远程分支](#711-%E5%88%A0%E9%99%A4%E8%BF%9C%E7%A8%8B%E5%88%86%E6%94%AF)
        *   [7.1.2. 删除远程标签](#712-%E5%88%A0%E9%99%A4%E8%BF%9C%E7%A8%8B%E6%A0%87%E7%AD%BE)
    *   [7.2. Git v1.7.0 之前的旧方法](#72-git-v170-%E4%B9%8B%E5%89%8D%E7%9A%84%E6%97%A7%E6%96%B9%E6%B3%95)
        *   [7.2.1. 删除远程分支](#721-%E5%88%A0%E9%99%A4%E8%BF%9C%E7%A8%8B%E5%88%86%E6%94%AF)
        *   [7.2.2. 删除远程标签](#722-%E5%88%A0%E9%99%A4%E8%BF%9C%E7%A8%8B%E6%A0%87%E7%AD%BE)
*   [8\. 禁止快进式合并](#8-%E7%A6%81%E6%AD%A2%E5%BF%AB%E8%BF%9B%E5%BC%8F%E5%90%88%E5%B9%B6)
*   [9\. 创建空分支（独立分支、孤儿分支）](#9-%E5%88%9B%E5%BB%BA%E7%A9%BA%E5%88%86%E6%94%AF%E7%8B%AC%E7%AB%8B%E5%88%86%E6%94%AF%E5%AD%A4%E5%84%BF%E5%88%86%E6%94%AF)
*   [10\. 合并不相关的分支（没有共同历史的分支）](#10-%E5%90%88%E5%B9%B6%E4%B8%8D%E7%9B%B8%E5%85%B3%E7%9A%84%E5%88%86%E6%94%AF%E6%B2%A1%E6%9C%89%E5%85%B1%E5%90%8C%E5%8E%86%E5%8F%B2%E7%9A%84%E5%88%86%E6%94%AF)
*   [11\. 只合分支并保持历史的线性](#11-%E5%8F%AA%E5%90%88%E5%88%86%E6%94%AF%E5%B9%B6%E4%BF%9D%E6%8C%81%E5%8E%86%E5%8F%B2%E7%9A%84%E7%BA%BF%E6%80%A7)
*   [12\. 一次合并多个分支](#12-%E4%B8%80%E6%AC%A1%E5%90%88%E5%B9%B6%E5%A4%9A%E4%B8%AA%E5%88%86%E6%94%AF)
*   [13\. 用变基的方式pull](#13-%E7%94%A8%E5%8F%98%E5%9F%BA%E7%9A%84%E6%96%B9%E5%BC%8Fpull)
*   [14\. 合并多个提交](#14-%E5%90%88%E5%B9%B6%E5%A4%9A%E4%B8%AA%E6%8F%90%E4%BA%A4)
*   [15\. 添加所有文件](#15-%E6%B7%BB%E5%8A%A0%E6%89%80%E6%9C%89%E6%96%87%E4%BB%B6)
*   [16\. 查看所有分支的日志](#16-%E6%9F%A5%E7%9C%8B%E6%89%80%E8%83%BD%E5%88%86%E6%94%AF%E7%9A%84%E6%97%A5%E5%BF%97)
*   [相关文章](#%E7%9B%B8%E5%85%B3%E6%96%87%E7%AB%A0)

# 内容

# 1\. 不显示中文

使用 `git status` 查看文件的状态时，如果文件名是中文，会显示形如 "\\345\\270\\270\\347\\224\\250\\346\\212\\200\\345\\267\\247.pages" 的情况；
**解决方案：**
配置core.quotepath的值为假：

```csharp
git config --global core.quotepath false

```

# 2\. 添加远程跟踪分支

当使用命令 `git clone -b <远程分支> --single-branch <远程仓库> [本地目录]` 只克隆指定的远程分支时，在本地仓库只会有指定远程分支的远程跟踪分支，如果要追加该远程仓库的其它分支的远程跟踪分支，可以按照如下操作：

**解决方案：**

1.  添加远程跟踪分支

    ```csharp
    git remote set-branches --add <远程仓库> <远程分支>...

    ```

2.  取回相应的`远程分支` 的更新到该远程跟踪分支；
    如果省略了 `本地分支` (如下)则只是取回指定 `远程仓库` 的指定 `远程分支` 的更新到到相应的远程跟踪分支；

    ```css
    git fetch <远程仓库> [远程分支]

    ```

3.  创建跟踪分支

    ```xml
    git branch --track <分支名> [<远程跟踪分支>]

    ```

# 把本地项目推送到新的远程仓库

当你想把本地已存在的项目放到远程仓库时，我们通常会在远程git上创建一个全新的空仓库，然后就会遇到这个问题：如何把已存在的项目上传到远程仓库，并跟踪该远程仓库？

**解决方案：**
**注意：** 如果该项目中已经有本地仓库了(即已经进行本地的版本控制了)，则需要跳过前3步，从第4步开始；

1.  在项目根目录下创建（初始化）本地仓库；

    ```kotlin
    git init

    ```

2.  暂存所有文件；

    ```csharp
    git add *

    ```

3.  提交一次更新；

    ```bash
    git commit -m "第1次提交"

    ```

4.  添加远程仓库；

    ```xml
    git remote add <远程仓库名> <远程仓库的URL>

    ```

    **备注：** `远程仓库名`是自定义的，只是为了方便引用；
5.  推送本地分支到远程仓库，并跟踪远程分支；

    ```xml
    git push -u <远程仓库名> <本地分支>

    ```

# 3\. 彻底删除文件或目录

如果我们直接删除某个文件或者目录，然后提交，这并不会把该文件从仓库中真正的删除，这个文件仍然存在仓库中，并为之前的版本会包含它；若需要从仓库中彻底删除文件或者目录（就像这个文件从一开始就不存在一样），则需要用 git 的 filter\-branch 命令，它是 git 用来过滤的命令，具体解决方案如下：

**解决方案：**

1.  从仓库中彻底删除文件：
    命令如下：

    ```swift
    git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch <被删除的文件路径名>' --prune-empty --tag-name-filter cat -- --all

    ```

    其中，`被删除的文件路径名` 就是你要删除的文件或目录 相对于 相对于git仓库根目录 的相对路径。
    **注意：**

    *   路径名不能以 `/` 开头，否则路径名会被认为是从 git 的安装目录开始的；
    *   如果要删除的目标不是文件夹，则需要在 `git rm --cached` 命令后面添加 `-r` 选项，表示递归处理，将指定目录下的所有文件与子目录一并删除掉；
2.  强制推送修改后的更新到远程仓库：

    ```undefined
    git push --force --all

    ```

    `--force` 选项表示以强制的方式推送；

3.  清理和回收空间：
    通过以上步骤就已经从仓库的所有版本中删除了相应的文件或目录，但是原来的提交对象将被存储在.git/refs/original中，所以，若想彻底删除他们，则可以使用如下命令：

    ```ruby
    $ rm -rf .git/refs/original/
    $ git reflog expire --expire=now --all
    $ git gc --prune=now
    $ git gc --aggressive --prune=now

    ```

# 4\. Git命令自动补全

通过按 Tab 键，shell 客户端一般会自动补全 命令 和 文件路径，但是它无法补全 git 的参数命令，因为 git 的很多子命令都是以参数形式使用的；不过，可以通过 `git-completion.bash` 脚本来实现 git 命令的自动补全， `git-completion.bash` 的安装步骤如下：

**git\-completion.bash的安装步骤：**

1.  下载 `git-completion.bash` 并放到 Home 目录下；

    ```ruby
    curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -o ~/.git-completion.bash

    ```

2.  将下面的代码追加到到 shell 的启动配置文件中 `~/.bash_profile`；

    ```bash
    if [ -f ~/.git-completion.bash ]; then
    . ~/.git-completion.bash
    fi

    ```

3.  使配置生效

    ```bash
    source ~/.bash_profile

    ```

4.  需要补全提示时，可按 TAB 键进行命令的自动补全或提示；

# 5\. 本地分支覆盖(替换)远程仓库中的分支

当你想用本地分支覆盖远程仓库中的分支时，可用如下命令，详情见 *7\. 推送push*
**语法：**

```css
git push [-f | --force] [--force-with-lease] [远程仓库S] [本地分支L][:<远程分支R>]

```

**选项：**
`-f | --force` : 强制推送，如果 `远程分支` 与 `本地分支` 不一致，则会用 `本地分支` 覆盖 `远程分支`；
`--force-with-lease` : 比 `-f | --force` 更安全一些强制推送，如果 `远端仓库` 的 目标分支 有其他人推送了新的提交，且这些提交还没有被 `fetch` 到 `本地仓库`，那么推送将会被拒绝；

**示例：**

```dart
git push --force-with-lease origin 工具:工具

```

# 6\. 远程仓库中的分支覆盖(替换)本地分支

## 6.1. 方案1: 强制pull

当你想弃用本地分支，采用远程仓库中的分支时来替换本地分支时，可用如下命令，详情见 *拉取pull*
**语法：**

```css
git pull [-f | --force] [<远程仓库> [[远程分支][:<本地分支>]]

```

**选项：**
`-f | --force` : 强制拉取并合并到 `本地分支`，如果 `远程分支`与 `本地分支` 不一致，则会用 `远程分支` 覆盖 `本地分支`；

**示例：**

```undefined
git pull --force origin 工具:工具

```

## 6.2. 方案2: 先fetch再将reset到远程分支

```go
1. 拉取远程分支 `git fetch` ；
2. 将当前分支重置到远程分支 `git reset --hard origin/master` ；

```

# 7\. 删除远程分支或tag

## 7.1. Git v1.7.0 之后的新方法

### 7.1.1. 删除远程分支

**语法：**

```jsx
git push [-d | --delete]  <远程仓库S>  <分支R>

```

删除 `远程仓库S` 的 `分支R`；

**示例:**

```cpp
git push --delete  origin  工具

```

删除 `origin` 仓库中 的 `工具` 分支；

### 7.1.2. 删除远程标签

**删除远程标签的语法：**
**语法：**

```xml
git push [-d | --delete]  <远程仓库S>  tag <标签T>

```

删除 `远程仓库S` 的 `标签T`；

**示例:**

```css
git push -d origin tag v1.0

```

删除 `origin` 仓库中 的 `v1.0` 标签；

## 7.2. Git v1.7.0 之前的旧方法

### 7.2.1. 删除远程分支

**语法：**

```xml
git push  <远程仓库S>  :<分支R>

```

删除 `远程仓库S` 的 `分支R`；可以理解为：把空推送到 `远程仓库S` 的 `分支R`；即：将 `远程仓库S` 的 `分支R` 置空；

**示例:**

```undefined
git push origin  :工具

```

删除 `origin` 仓库中 的 `工具` 分支；

### 7.2.2. 删除远程标签

**语法：**

```ruby
git push  <远程仓库S>  :refs/tags/<标签T>

```

删除 `远程仓库S` 的 `标签T`；可以理解为：把空推送到 `远程仓库S` 的 `标签T`；即：将 `远程仓库S` 的 `标签T` 置空；

**示例:**

```ruby
git push  origin tag :refs/tags/v1.0

```

删除 `origin` 仓库中 的 `v1.0` 标签；

# 8\. 禁止快进式合并

git在执行合并操作时（无论是通过 merge 命令，还是通过 pull 命令），比如 将 分支B 合并进 分支A 中，如果 分支A 完全包含在 分支B 的历史中（如下图），

![](https://upload-images.jianshu.io/upload_images/3987507-353f9892fe21eaca.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/280/format/webp)

快进合并前

那么，git 默认会以快进的方式进行合并，合并后的效果如下：

![](https://upload-images.jianshu.io/upload_images/3987507-ed8c126c723ab971.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/280/format/webp)

快进式合并

非快进式合并的效果如下：

![](https://upload-images.jianshu.io/upload_images/3987507-a3c4ff3c936b1edb.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/345/format/webp)

非快进式合并

如果想禁用快进式合并，可以给命令传递 `--no-ff` 选项， `ff` 是 快进的英文 `fast farward` 缩写；如下：

**merge命令：**

```xml
git merge  --no-ff  <分支B>

```

**pull命令：**

```undefined
git pull --no-ff

```

merge 和 pull 命令中 与快进式合并相关的选项如下：

*   `--ff` : 当可以快进合并时，使用快进合并的方式进行合并。这是默认行为。
*   `--no-ff` : 即使可以快进合并，不会使用快进式合并，而是也创建一个合并提交。这是合并注释（可能有符号）标记时的默认行为。
*   `--ff-only` : 如果可以快进式合并，则会进行快进式合并；否则，取消合并操作；

# 9\. 创建空分支（独立分支、孤儿分支）

我们可以通过以下命令创建新分支：

*   `git branch <新分支名>`
*   `git checkout -b <新分支名>`

这种方式创建的新分支 都是 基于当前的 HEAD 来创建分支的，新的分支会和当前 HEAD 拥有共同的 提交历史；
例如，假设当前 HEAD 在 分支A 上，如下图所示，

![](https://upload-images.jianshu.io/upload_images/3987507-f5436d3dbbdb7fa7.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/280/format/webp)

创建独立分支前

通过 `git branch 分支B` 或 `git checkout -b 分支B` 来创建 分支B 后，分支图如下所示：

![](https://upload-images.jianshu.io/upload_images/3987507-1fd6c33a7bdae308.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/280/format/webp)

创建非独立分支

新建的 分支B 和 分支A 会有相同提交历史；

如果我们想创建一个没有任何历史的分支，我们可以用 带 `--orphan` 选项的 checkout 命令，语法如下：

```css
git checkout --orphan <新分支名> [开始点]

```

`--orphan` 选项指定创建一个 孤儿分支 ，即：独立的分支、没有任何提交历史的分支；并且会切换到这个新的分支；
此时，你通过 branch 命令列出的分支列表里是没有这个分支的，因为该分支里没有任何提交，分支没有可被引用的提交对象；
并且，此时，新分支的 暂存区 中存放的是 `开始点` 处目录树中的所有文件，如果没有指定 `开始点` 参数，则默认会把 当前的 HEAD 作为开始点；
如果不想要暂存区的任何东西，可以执行 `git rm -rf .` 命令清空暂存区；
如果想将 `开始点` 处的整个目录树作为新分支的第一个版本进行提交，直接执行 commit 命令 `git commit -m "提交信息"` 即可；

如：当前在HEAD分支A，执行如下命令：

```bash
git checkout --orphan 分支B
git commit -m "提交信息"

```

分支图如下所示：

![](https://upload-images.jianshu.io/upload_images/3987507-1c0ae16b48ebf2b6.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/302/format/webp)

创建独立分支

*合并独立分支的方法请看[合并不相关的分支（没有共同历史的分支）](#10-%E5%90%88%E5%B9%B6%E4%B8%8D%E7%9B%B8%E5%85%B3%E7%9A%84%E5%88%86%E6%94%AF%E6%B2%A1%E6%9C%89%E5%85%B1%E5%90%8C%E5%8E%86%E5%8F%B2%E7%9A%84%E5%88%86%E6%94%AF)*

# 10\. 合并不相关的分支（没有共同历史的分支）

Git默认的合并操作只会对有共同提交历史的分支进行合并；

![](https://upload-images.jianshu.io/upload_images/3987507-e1a27432714c1748.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/279/format/webp)

有共同历史的分支

不过，对没有共同提交历史的分支进行合并的情况也是存在的，比如：

*   合并孤儿分支；
*   两个仓库，但文件内容相似，甚至就是同一个项目，需要将这两个仓库中的分支进行合并

![](https://upload-images.jianshu.io/upload_images/3987507-7771b2d04dd4f42e.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/211/format/webp)

不相关的分支

若想对没有共同历史的分支进行合并，只需给 `merge` 或 `pull` 命令（pull命令也会有合并的操作）添加 `--allow-unrelated-histories` 选项，语法如下：
**merge语法：**

```xml
git merge  --allow-unrelated-histories  <分支名>

```

**pull语法：**

```undefined
git pull  --allow-unrelated-histories

```

![](https://upload-images.jianshu.io/upload_images/3987507-e275fc852407f559.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/277/format/webp)

不相关分支的合并

# 11\. 只合分支并保持历史的线性

假设有 分支A 和 分支B ，当前在 分支A，如下图：

![](https://upload-images.jianshu.io/upload_images/3987507-e1a27432714c1748.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/279/format/webp)

squash合并前

当我们进行合并分支时，通常会将指定分支的变更合并到当前分支中，并产生一个提交，该提交会有两个父提交的引用；如下图：

![](https://upload-images.jianshu.io/upload_images/3987507-ac9c012363fb2a30.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/345/format/webp)

非squash合并

如果我们想合并其它分支的变更，但又想保持当前分支的线性，使分支的提交历史上没有分支交汇的情况，即：每一个提交对象都有一个父提交的对象，而非多个父提交对象；那该怎么操作呢？

我们可以给 `merge` 或 `pull` 命令（pull命令也会有合并的操作）添加 `--squash` 选项，语法如下：
**merge语法：**

```xml
git merge  --squash  <分支名>

```

**pull语法：**

```undefined
git pull  --squash

```

**注意：** 执行完 `--squash` 的合并操作后，git默认不会生成合并的变更提交，只是把合并的变更放在暂存区中，并附有默认的提交信息，你需要再手动进行提交下；

**示例：**

```undefined
git merge  --squash  分支B
git commit

```

![](https://upload-images.jianshu.io/upload_images/3987507-01f3acf51cee0735.jpg?imageMogr2/auto-orient/strip|imageView2/2/w/347/format/webp)

squash合并

# 12\. 一次合并多个分支

通常我们使用 merge 命令 将一个分支合并到当前分支中，merge 命令也可以一次将多个分支合并到当前分支中，语法如下：

```css
git merge  <分支B> [分支C]...

```

将 `分支B`、`分支C`等等 合并到当前分支中；

# 13\. 用变基的方式pull

**语法：**

```css
git pull -r [<远程仓库> [[远程分支][:<本地分支>]]
git pull --rebase [<远程仓库> [[远程分支][:<本地分支>]]

```

**说明：**
从 `远程仓库` 获取指定的 `远程分支` 的更新到相应的远程跟踪分支，并以变基 rebase 的方式合并到 `本地分支`，并将本地分支中新的提交拼接到上游分支的后面；
如果 `本地分支` 不存在，则会创建该本地分支；

**示例：**

```undefined
git pull -r

```

# 14\. 合并多个提交

为了保持分支提交历史的清晰、独立，我们经常需要将几个提交合并成一个；但 Git 没有专门为合并提交提供相应的命令，为解决这个问题，我专门研究了几种方法来实现 提交的合并，详见 [Git中合并多个提交的各种方法](https://www.jianshu.com/p/1268c8704e1b)

# 15\. 添加所有文件

`git add` 命令可以添加指定的 文件 或 目录，但有时，我们经常需要添加所有的变更；

下面是一次添加所有变更的各种方法：

*   `git add .` ： 添加新文件(new)和被修改(modified)文件，不包括被删除(deleted)文件；在Shell里，后面的 `.` 代表当前目录， 所以相当于将当前目录传给了 `add` 命令；
*   `git add *` ：添加所有非隐藏的的文件的变化；`*` 是 shell 语言中的通配符，能匹配所有非隐藏的文件 和 目录，所以相当于将匹配的到文件和目录都传给了 `add` 命令；
*   `git add -A` ：添加所有变化；
*   `git add -u` ： 添加被修改(modified)和 被删除(deleted)文件，不包括新文件(new)；
*   `git commit -a` ： 自动暂存 所有已跟踪的文件（被修改(modified)和 被删除(deleted)文件，但不包括新文件(new)），并直接提交；

# 16\. 查看所有分支的日志

`git log` 命令默认只能查看指定分支的提交历史，可视化命令 `gitk` 也是，如果想查看所有分支的提交历史，可以给 `git log` 或者 `gitk` 添加 `--all` 选项；如下：

```bash
git log --all

```

可视化界面查看

```undefined
gitk --all

```

# 相关文章

*   [Git并行工作流程规范](https://www.jianshu.com/p/d7a3a4935440)
*   [Git基础教程](https://www.jianshu.com/p/fd40460ffb37)
*   [Git命令大全](https://www.jianshu.com/p/15a4dee9c5df)
*   [Git技巧和问题解决方案](https://www.jianshu.com/p/d21838dc5947)
*   [Git中合并多个提交的各种方法](https://www.jianshu.com/p/1268c8704e1b)
*   [Git并行工作流程规范设计记录](https://www.jianshu.com/p/7f4b47d2507d)
*   [弃用SVN选择Git的理由](https://www.jianshu.com/p/bdc9a46c3394)
*   [Git和Subversion的命令的对比](https://www.jianshu.com/u/7ecaba2d594c)
*   [分布式和集中式版本控制系统的区别](https://www.jianshu.com/p/7d55f32b7c9f)
*   [Git的存储机制](https://www.jianshu.com/p/caa4695af535)