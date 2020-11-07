---
title: 命令行笔记软件nb使用指南
date: 2020-11-06 18:54:05
permalink: /pages/4d6f83/
sidebar: auto
categories:
  - 随笔
tags:
  - 
---
## 序言

一直在找各种好用的命令行笔记软件。突然发现`nb`软件似乎很不错，因此打算总结一下他的用法。
老规矩，在看教程前，建议大家先看[官方教程](https://xwmx.github.io/nb)

## 安装
### `Ubuntu, Windows WSL, and others`
> 推荐大家直接使用Npm安装。

要使用 [npm](https://www.npmjs.com/package/nb.sh) 安装 ：

```shell
npm install -g nb.sh
```

### `macOS / Homebrew`

要使用 [Homebrew](https://brew.sh/) 安装 ：

```shell
brew tap xwmx/taps
brew install nb
```

### 个人心得
因为没有MAC，所以我直接使用的是Npm安装。安装起来非常快，装好后直接软件就可以直接启用了。
其他安装方法则属于定制化以及高级需求，有需要的朋友可以直接看官方教程安装，这里就不多赘述了。

## `nb`软件的初级使用

### `nb`软件的框架

打开命令行，输入：
```
nb
```
如果成功了，就表示你的软件安装好了。

接下来，简单的了解一下`nb`软件的框架，我们就可以开始愉快的使用他了。

![20201028114513_7f2402f876d31f753bff3b04967138f2.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20201028114513_7f2402f876d31f753bff3b04967138f2.png)

**nb软件的框架**：
1. 命令
2. 目前使用的笔记本
3. 该笔记本下的笔记
4. 命令提示

### `nb`软件的增删查改

![20201028154655_e7c64151cc6a7d4d205022fa6a111fed.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20201028154655_e7c64151cc6a7d4d205022fa6a111fed.png)

如上图所示。

### `nb`软件常见使用命令
```shell
nb # 列出所有笔记本与笔记
nb add name.md # 创建一个笔记，不写名字默认标题为当前时间
nb notebooks add <笔记本名称> # 创建一个新的笔记本
nb use 笔记本 # 切换到指定笔记本
nb q "example query" #在当前笔记本查询相关内容
nb search "example query" --all # 在所有未归档的笔记本中查询相关的内容
nb e id # 编辑指定的笔记
nb d id # 删除指定的笔记
nb rename id new_name # 将指定ID笔记重命名为一个新名字
nb rename xxx.md xxx.org # 指定后缀将改变文件保存格式
nb move id 笔记本名称 # 将目标笔记移动到指定笔记本
nb import (<path> | <url>) # 从本地或者远程地址导入一个笔记
nb help # 打开nb帮助命令
nb help 命令 # 打开该命令的帮助
```
## `nb`软件日常用法示例

```sh
nb add # 创建一个随笔
# 开始输入内容
nb rename id 随笔1 # 将随笔创建一个新的名字
nb notebooks add 随笔 # 创建一个随笔笔记本
nb move 随笔1 随笔 # 将随笔1移动到随笔笔记本下
nb q "Python" --all # 全局搜索包含Python内容的笔记 
nb e id # 编辑某个笔记
nb d id # 删除某个笔记 
```

## `nb`软件高级用法

通过使用 [`nb remote`](#remote) 以下命令 设置远程URL，可以将每个笔记本与远程git存储库同步 ：

```shell
# set the current notebook's remote to a private GitHub repository
nb remote set https://github.com/example/example.git

# set the remote for the notebook named "example"
nb example:remote set https://github.com/example/example.git
```
每次在该笔记本中运行命令时，任何带有远程URL的笔记本都会自动同步。

当您 `nb` 在多个系统上 使用 时，您可以将两个系统上的笔记本都设置到同一远程，并且 `nb` 每次笔记本发生更改时都将在后台保持所有同步。

由于每个笔记本都有自己的git历史记录，因此您可以使某些笔记本与远程同步，而其他笔记本仅在该系统上本地可用。

许多服务都提供免费的私有git存储库，因此git同步 `nb` 很容易，免费且独立于供应商。 您也可以使用Dropbox，Drive，Box，Syncthing或其他同步工具通过更改 `nb` 目录 来同步笔记 ， [`nb set nb_dir <path>`](#nb_dir) 并且git sync 仍可同时进行。

当你有一个现有 `nb` 的git仓库的笔记本电脑，只需将URL传递到 [`nb notebooks add`](#notebooks) 和 `nb` 会克隆您现有的笔记本电脑，并开始自动同步变化：

```sh
# create a new notebook named "example" cloned from a private GitLab repository
# 直接创建一个关联远程仓库的笔记本
nb notebooks add example https://gitlab.com/example/example.git

```

通过删除遥控器来关闭笔记本的同步：

```sh
# remove the remote from the current notebook
nb remote remove

# remove the remote from the notebook named "example"
nb example:remote remove

```

可以使用打开或关闭自动git同步 [`nb set auto_sync`](#auto_sync) 。

要手动同步，请使用 [`nb sync`](#sync) ：

```sh
# manually sync the current notebook
nb sync

# manually sync the notebook named "example"
nb example:sync

```

要绕过 `nb` 同步并 `git` 直接在笔记本中 运行 命令，请使用 [`nb git`](#git) ：

```shell
# run `git fetch` in the current notebook
nb git fetch origin

# run `git status` in the notebook named "example"
nb example:git status

```

#### [](#private-repositories-and-git-credentials)私人存储库和Git凭证

与私有存储库同步需要将git配置为不提示输入凭据。 对于通过HTTPS克隆的存储库， [可以使用git缓存凭据](https://docs.github.com/en/free-pro-team@latest/github/using-git/caching-your-github-credentials-in-git) 。 对于通过SSH克隆的存储库， [可以将密钥添加到ssh\-agent](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) 。

[`nb sync`](#sync) 在笔记本中 使用 可确定您的配置是否有效。 如果 `nb sync` 显示密码提示，请按照上述说明配置您的凭据。 密码提示可用于进行身份验证，但 `nb` 不以任何方式缓存或以其他方式处理git凭据，因此，如果未配置凭据，则每次同步期间可能会有多个密码提示。

#### [](#sync-conflict-resolution)同步冲突解决

`nb` 自动处理git操作，因此您永远不需要直接使用 `git` 命令行工具。 `nb` 同步时合并更改，并使用几种不同的策略来处理冲突。

当 [`nb sync`](#sync) 在文本文件中遇到冲突并且无法干净地合并重叠的本地和远程更改时， `nb` 请将这两个版本保存在文件中，并用git冲突标记分隔开，并显示一条消息，指出哪个文件包含冲突的文本。 使用 [`nb edit`](#edit) 删除冲突标志和删除任何不需要的文本。

例如，在以下文件中，在两个系统上更改了第二个列表项，而git无法确定我们要保留哪个列表项：

```shell
# Example Title

- List Item apple
- List Item pluot
- List Item plum

```

本地更改位于以 `<<<<<<<` 和 开头的行之间 `=======` ，而远程更改位于 `=======` 和 处之间 `>>>>>>>` 。

通过保持这两个项目解决这个矛盾，只需编辑与文件 `nb edit` 并删除开头的行 `<<<<<<<` ， `=======` 以及 `>>>>>>>` ：

```
# Example Title

- List Item apple
- List Item apricot
- List Item pluot
- List Item plum

```

当 `nb` 二进制文件（例如加密的便笺）中发生冲突时，文件的两个版本均作为单独的文件保存在笔记本中，并 `--conflicted-copy` 从远程附加到版本的文件名中。 要解决二进制文件的冲突副本，请比较两个版本并手动合并它们，然后删除 `--conflicted-copy` 。

如果你遇到冲突 `nb` 说，它无法在所有的合并， [`nb git`](#git) 以及 [`nb run`](#run) 可用于笔记本电脑中执行Git和外壳操作，手动解决冲突。 还请 [打开一个问题，](https://github.com/xwmx/nb/issues/new) 其中包含任何相关详细信息，这些信息可以为自动处理此类案件的策略提供信息。

## 总结
作为一个命令行笔记，`nb`的功能非常强大。而且关联远程仓库的作用，使得可以利用`nb`来有效的管理自己的知识仓库。
他解决了命令行下如何使用笔记的问题，个人非常看好这个软件。
你也可以查看该软件的[github](https://github.com/xwmx/nb)仓库，方便自己更好的理解。