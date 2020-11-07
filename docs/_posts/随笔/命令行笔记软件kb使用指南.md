---
title: 命令行笔记软件kb使用指南
date: 2020-11-06 18:54:05
permalink: /pages/766c80/
sidebar: auto
categories:
  - 随笔
tags:
  - 
---
## 序言

[kb](https://github.com/gnebbia/kb)是一个极简命令行知识管理软件，依赖`python3.6`以上的版本。
`kb`最大的优点是可以在`powershell`下工作。
`kb`的缺点是增加文件的时候比较麻烦。需要指定文件的位置。
我个人推荐`kb`结合nb来一起使用。
使用`nb`写文件，然后将`nb`写好的文件，让`kb`直接通过文件夹导入。
然后`kb`查询起来也会变得更加的快捷。
<!-- more -->
## 安装

要安装kb的最新稳定版本，只需键入：

```shell
pip install -U kb-manager
```

如果要安装最新版本的kb（可能有一些错误），则应该执行以下操作：

```shell
git clone https://github.com/gnebbia/kb
cd kb
pip install -r requirements.txt
python setup.py install

# or with pip
pip install -U git+https://github.com/gnebbia/kb
```

针对GNU / Linux和MacOS用户的**提示** ：为了获得更好的用户体验，还请设置以下kb bash别名：

```shell
cat <<EOF > ~/.kb_alias
alias kbl="kb list"
alias kbe="kb edit"
alias kba="kb add"
alias kbv="kb view"
alias kbd="kb delete --id"
alias kbg="kb grep"
alias kbt="kb list --tags"
EOF
echo "source ~/.kb_alias" >> ~/.bashrc
source ~/.kb_alias
```

请记住经常通过执行以下操作来升级kb：

```shell
pip install -U kb-manager
```

### `[](#installation-with-homebrew)Installation with homebrew`

要使用自制软件安装，请使用：

```shell
brew tap gnebbia/kb https://github.com/gnebbia/kb.git
brew install gnebbia/kb/kb
```

升级自制软件：

```shell
brew update
brew upgrade gnebbia/kb/kb
```

### `[](#installation-from-aur)Installation from AUR`

Arch Linux用户可以 使用自己喜欢的 [AUR Helper](https://wiki.archlinux.org/index.php/AUR_helpers) 安装 [python\-kb](https://aur.archlinux.org/packages/python-kb) 或 [python\-kb\-git](https://aur.archlinux.org/packages/python-kb-git) 。[](https://wiki.archlinux.org/index.php/AUR_helpers)

稳定：

```shell
yay -S python-kb
```

开发人员：

```shell
yay -S python-kb-git
```

### `[](#notes-for-windows-users)Notes for Windows users`

Windows用户应记住以下几点：

*   不要使用％EDITOR％的记事本，kb与记事本不兼容，合理的替代方法是notepad ++；
*   ％EDITOR％变量应始终用双引号引起来；

```shell
EDITOR=C:\Program Files\Editor\my cool editor.exe      -> WRONG!
EDITOR="C:\Program Files\Editor\my cool editor.exe"    -> OK!
```

要使用cmd.exe设置“ EDITOR”环境变量，只需在插入所需文本编辑器的路径后发出以下命令：

```shell
set EDITOR="C:\path\to\editor\here.exe"
setx EDITOR "\"C:\path\to\editor\here.exe\""
```

要使用Powershell设置“ EDITOR”环境变量，只需在插入所需文本编辑器的路径后发出以下命令：

```shell
$env:EDITOR="C:\path\to\editor\here.exe"
[System.Environment]::SetEnvironmentVariable('EDITOR','"C:\path\to\editor\here.exe"', [System.EnvironmentVariableTarget]::User)
```

#### `[](#setting-aliases-for-cmd)Setting Aliases for cmd`

打开具有管理权限的cmd.exe终端并粘贴以下命令：

```shell
reg add "HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor" /v "AutoRun" /t REG_EXPAND_SZ /d "%USERPROFILE%\autorun.cmd"
(
echo @echo off
echo doskey kbl=kb list $*
echo doskey kbe=kb edit $*
echo doskey kba=kb add $*
echo doskey kbv=kb view $*
echo doskey kbd=kb delete --id $*
echo doskey kbg=kb grep $*
echo doskey kbt=kb list --tags $*
)> %USERPROFILE%\autorun.cmd
```

#### `[](#setting-aliases-for-powershell)Setting Aliases for Powershell`

打开Powershell终端并粘贴以下命令：

```shell
@'
function kbl { kb list $args }
function kbe { kb edit $args }
function kba { kb add  $args }
function kbv { kb view $args }
function kbd { kb delete --id $args }
function kbg { kb grep $args }
function kbt { kb list --tags $args }
'@ >  $env:USERPROFILE\Documents\WindowsPowerShell\profile.ps1
```

### `[](#docker)Docker`

包含docker设置以帮助开发。

要使用docker安装并启动项目：

```shell
docker-compose up -d
docker-compose exec kb bash
```

容器中包含别名， `.bashrc` 因此您可以在运行的容器中使用kb，就像直接将其安装在主机上一样。 该 `./docker/data` 主机上的目录，势必 `/data` 在容器中，这是图像的工作直接也。 要与容器交互，请将主机上的文件放置（或符号链接）到 `./docker/data` 目录中，然后可以 `/data` 在容器 的 目录中 查看和使用该 文件。

## kb常用命令

```shell
kb help # 帮助
kb add ~/Notes/cheatsheets/pytest
# or if aliases are used:
kba ~/Notes/cheatsheets/pytest
# 以上两个命令皆可导入指定文件
kb add ~/Notes/cheatsheets/general/* --category "cheatsheet" # 导入文件夹并归类到指定文件夹
kb list 
kbl 
# 列出所有文件，可以增加关键词，这样会筛选包含关键词的文件。可以是名称也可以是分类
kb delete --id 2 3 4
kbd 2 3 4
# 删除指定ID文件，用空格隔开
kb view id # 查看文件
kbv id # 快捷查看指定id文件
kb edit --id 13
# or
kbe 13
# or if aliases are used:
kbe 13 
# 编辑某文件，不推荐
```
