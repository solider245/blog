---
title: ssh agent详解
date: 2020-10-12 12:09:51
permalink: /pages/e17c77/
categories:
  - linux
  - ssh
tags:
  - 
---
## 什么是 ssh agent?

ssh agent ，意为 ssh 代理，是一个密钥管理器，用来管理一个多个密钥，并为其他需要使用 ssh key 的程序提供代理。

首发于：

[ssh agent详解 ​www.thisfaner.com![图标](https://pic1.zhimg.com/v2-c83c6ce362050d5868eae82978e2a53c_180x120.jpg)](https://link.zhihu.com/?target=https%3A//www.thisfaner.com/p/ssh-agent/)

## 为什么需要 ssh agent?

我在之前的文章 [SSH\-key的生成与在Git中的使用](https://link.zhihu.com/?target=https%3A//www.thisfaner.com/p/ssh-key-git-usage/) 中介绍过，什么是 ssh ?

Secure Shell (SSH) 是一个允许两台电脑之间通过安全的连接进行数据交换的 **网络协议**。通过**加密**保证了数据的保密性和完整性。SSH采用 **公钥** 加密技术来**验证远程主机**，以及 (必要时) 允许远程主机验证用户。

既然 ssh 是一个用来保证安全并进行验证的网络协议，那么自然会有 **其他程序** 想要通过它来进行远程主机的用户验证，比如说 git。

而为了让其他程序更方便的使用这套加密技术，就有了 ssh agent。

当把私钥交给 ssh agent 管理的好处：

*   当 其他程序 需要身份验证的时候 可以将验证申请交给 ssh\-agent 来完成整个认证过程。使用不同的密钥连接到不同的主机时，需要要手动指定对应的密钥，而ssh代理可以自动帮助我们选择对应的密钥进行认证。
*   避免重复输入密码：如果您的私钥使用密码短语来加密了的话，每一次使用 SSH 密钥对进行登录的时候，您都必须输入正确的密码短语。而 SSH agent 程序能够将您的已解密的私钥缓存起来，在需要的时候提供给您的 SSH 客户端。这样子，您就只需要在使用 `ssh-add` 时将私钥加入 SSH agent 缓存的时候，输入一次密码短语就可以了。这为经常使用 SSH 连接用户提供了不少便利。

ssh\-agent 工作原理：（本地客户端）

![](https://pic3.zhimg.com/v2-e9a1e8a001832bdf209ee1814e82bf62_b.jpg)

![](https://pic3.zhimg.com/80/v2-e9a1e8a001832bdf209ee1814e82bf62_720w.jpg)

SSH只是一种协议，其开源实现有OpenSSH，并且存在服务端（sshd） 和 客户端 (ssh)，Windows中的客户端还有 putty；而这两种客户端都有各自不同的 ssh agent：

*   `ssh-agent` 命令：是客户端ssh的默认代理
*   pagent ： 是 客户端 putty 的代理

## 如何配置 ssh agent

首先需要运行 ssh agent

*   在 Linux中： `ssh-agent` 在 **X会话** 或 \*\*登录会话 \*\*之初就已经启动
*   在Windows中： 计算机管理 服务 OpenSSH Authentication Agent 设置为自动启动。

*   在Windows中更多配置 ssh\-agent 自动启动的方法，见下文的 ”配置ssh\-agent自动启动” 。

也可以手动运行，有两条命令可以用来启动：

*   `ssh-agent $SHELL` ：它会在当前 shell 中启动一个默认 shell，作为当前 shell 的子 shell，ssh\-agent 会在子shell中运行；也可以明确指定 `$SHELL` ，比如 `ssh-agent bash` ， `ssh-agent` 会随者当前 ssh 会话的结束而结束，这是一种安全机制。
*   eval \`shell\-agent\` ， 在windows中为 `eval $(ssh-agent)` ： 它并不会启动一个子shell，而是直接启动一个 ssh\-agent 进程；此时当我们退出当前 bash 后，ssh\-agent 进程并不会自动关闭。我们可以在当前bash退出之前，使用 `ssh-agent -k` ，或者在当前 bash 退出之后，使用 `kill` 命令，关闭对应的 ssh\-agent 进程。

运行 ssh agent 以后，会加载默认的私钥，

如果有多个密钥，则需要在 `~/.ssh/config` 中进行配置：

*   一般来说 ssh agent 程序可以根据配置自动加载并管理这些密钥；但如果发现某个密钥没有加载则
*   也可以手动使用 `ssh-add` 命令将某个私钥交给 ssh\-agent 保管，

## ssh\-agent 相关问题

当我们在中尝试使用Git并通过SSH协议进行 push 或 pull 时，如果远程Github服务器无法使用SSH agent 提供的密钥进行身份验证，则可能会收到下面的某一条消息：

*   **Permission denied (publickey)**
*   No suitable response from remote
*   repository access denied

**可能的两种原因：**

1.  你的 公钥 并没有添加到Github服务器中。检查GitHub是否有添加。
2.  您的密钥未加载到 ssh agent 中 。解决方法：

*   检查相应的 ssh 密钥是否被加载：

```bash
ssh-add -l
```

*   如果没有被加载，则使用下面的命令加载私钥

```bash
# 后面可以同时跟多个私钥
ssh-add ~/.ssh/<private_key_file>
```

*   运行 `ssh-add` 时， 如果提示 “**Could not open a connection to your authentication agent**.” 说明你的`ssh-agent`并没有运行；使用下面的命令运行ssh agent，再使用`ssh-add`命令添加你的ssh key。

```text
# 先启动，再运行
# macOS/Linux
eval `ssh-agent`
ssh-add ~/.ssh/other_id_rsa

# 在Windows中的git-bash中
eval $(ssh-agent)
ssh-add ~/.ssh/other_id_rsa
```

## 配置ssh\-agent自动启动

> 在 Linux中 `ssh-agent` 在 **X会话** 或 **登录会话** 之初就已经启动，一般都不会有问题。

而在 Windows 中，我们可以这样配置：

*   在 计算机管理 服务 OpenSSH Authentication Agent 设置为自动启动。
*   也可以为 `git bash` 、 `powershell` 和 cmder 分别添加如下配置

### git bash

**方式一： Git for windows 提供的方式**

在 `.profile` 或 `.bashrc` 添加 ：

```text
# 在.profile 或  .bashrc 添加
# Git for windows 提供的方式
# ssh-agent auto-launch (0 = agent running with key; 1 = w/o key; 2 = not run.)
agent_run_state=$(ssh-add -l >| /dev/null 2>&1; echo $?)
if   [ $agent_run_state = 2 ]; then
  eval $(ssh-agent -s)
  ssh-add ~/.ssh/one_rsa
  ssh-add ~/.ssh/two_rsa
elif [ $agent_run_state = 1 ]; then
  ssh-add ~/.ssh/one_rsa
  ssh-add ~/.ssh/two_rsa
fi
# 记得还要在 ~/.bash_logout 中添加，来关闭 ssh-agent
# ssh-agent -k
```

新建 `~/.bash_logout` 文件，添加：

```text
# 记得还要在 ~/.bash_logout 中添加，来关闭 ssh-agent
ssh-agent -k
```

**方式二：GitHub 提供的方式**

复制以下行并将其粘贴到 Git shell 中的 `~/.profile` 或 `~/.bashrc` 文件中：

```text
env=~/.ssh/agent.env

agent_load_env () { test -f "$env" && . "$env" >| /dev/null ; }

agent_start () {
    (umask 077; ssh-agent >| "$env")
    . "$env" >| /dev/null ; }

agent_load_env

# agent_run_state: 0=agent running w/ key; 1=agent w/o key; 2= agent not running
agent_run_state=$(ssh-add -l >| /dev/null 2>&1; echo $?)

if [ ! "$SSH_AUTH_SOCK" ] || [ $agent_run_state = 2 ]; then
    agent_start
    ssh-add
elif [ "$SSH_AUTH_SOCK" ] && [ $agent_run_state = 1 ]; then
    ssh-add
fi

unset env
```

现在，当您初次运行 Git Bash 时，系统将提示您输入密码：

```text
> Initializing new SSH agent...
> succeeded
> Enter passphrase for /c/Users/you/.ssh/id_rsa:
> Identity added: /c/Users/you/.ssh/id_rsa (/c/Users/you/.ssh/id_rsa)
> Welcome to Git (version 1.6.0.2-preview20080923)
>
> Run 'git help git' to display the help index.
> Run 'git help ' to display help for specific commands.
```

`ssh-agent` 进程将继续运行，直到您注销、关闭计算机或终止该进程。

### powershell

在 PowerShell的配置文件中添加，通过 在 powershell 中运行 `notepad $PROFILE` 来打开配置文件

```text
# Start SshAgent if not already
# Need this if you are using github as your remote git repository
if (! (ps | ? { $_.Name -eq 'ssh-agent'})) {
    Start-SshAgent
}
```

### cmd

如果你使用的是 [cmder](https://link.zhihu.com/?target=https%3A//www.thisfaner.com/p/cmder/) ，则还可以为 cmd 进行如下配置：

*   首先在 cmder 中确认当前在 cmd 标签页中
*   再测试以下 `git push` 命令，或 运行 `ssh -T` `git@github.com` 来进行测试
*   如果还是提示 `Permission denied` ，则进行下面的操作：

在 cmd 模式中运行 `start-ssh-agent` 即可启动 ssh\-agent ，然后进行 代码推送，推送完成后可选择输入`exit`退出 ssh\-agent。

如果想要 ssh\-agent 在 cmd 模式中自动启动，需要在 `%CMDER_ROOT%/config/user-profile.cmd` 文件中取消注释 `@call "%GIT_INSTALL_ROOT%/cmd/start-ssh-agent.cmd"`