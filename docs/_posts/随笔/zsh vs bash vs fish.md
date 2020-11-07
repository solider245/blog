---
title: zsh vs bash vs fish
date: 2020-11-06 18:54:07
permalink: /pages/3c100a/
sidebar: auto
categories:
  - 随笔
tags:
  - 
---
## 序言
v2ex论法一个关于[zsh vs bash](https://www.v2ex.com/t/718204#reply85)的帖子，我觉得讨论的非常好，把大家的言论做一个汇总。

## 基本观点

1. bash适用性最广，但是基础配置简单，不过现在有oh-my-bash可以帮忙配置
2. fish上手最简单，但是兼容性不高，有时候需要结合bash使用，这也是官方推荐的用法
3. zsh配置最多，框架也多，但是有时候会遇到性能问题，导致太慢

## 小总结

1. 新手直接使用[fish](https://github.com/fish-shell/fish-shell)，[oh-my-fish](https://github.com/oh-my-fish/oh-my-fish)开箱可用，遇到不兼容的就切换到shell
2. 有一定基础的使用zsh，默认可以使用Oh-my-zsh，也可以使用zinit, [zimfw](https://github.com/zimfw/zimfw),[powerlevel10k](https://github.com/romkatv/powerlevel10k)
3. 如果是大佬，可以直接使用shell自己搭配组件是最强的
4. 如果是win平台用的比较多，现在也可以使用pwsh。
5. zsh 在一些低性能嵌入式设备上很慢……我在 rpi4 上的 docker 里尝试打开 zsh 大概要十几秒，所以对性能有严苛要求的环境还是用 bash 或者 sh
## zsh常见框架简评

### [zimfw](https://github.com/zimfw/zimfw)

>这是我在尝试了主流的 manager 后，觉得易用性和功能上最好的，集轻量、速度于一身。

### [powerlevel10k](https://github.com/romkatv/powerlevel10k)

>Prompt 的话，最好的就是 powerlevel10k （ https://github.com/romkatv/powerlevel10k ），没有之一，它的“异步”加载，可以使得我们“忽略”zsh 在用了 plugin 后加载速度慢的缺点。

## shell历史快速导读

> bash 和 zsh 都要追溯到 Unix 第七版的 Bourne shell, 这是几乎所有 Unix 世界 shell 的起源.
Ken Thompson 编写的 Unix 里包括一个 shell, 后来被称为 Thompson shell, 功能非常简单, 因此 Bourne 改进了这个 shell, 就叫 Bourne shell, 但是 Berkeley 的 Bill Joy (也是 vi 的作者和 Sun 创始人)觉得 Bourne shell 还是不好(比如流传到现在的鬼畜的语法), 就自己写了一个语法类似于 C 的 shell, 就叫 C shell, 然后随着 2BSD 发布.后来的几乎所有 shell (不包括微软家的和 fish)几乎都受到 csh 和 Bourne shell 的影响.
Almquist 基于 System V release 4 的 shell 写的轻量级 shell 叫 Almquist shell (ash) , 仅兼容 Bourne shell
Debian 改进的 ash 叫 dash, 而 dash 被移植到 busybox 里.
tcsh 是 csh 的改进, 现在是 FreeBSD 的默认 shell, 也是 macOS 10.3 前的默认 shell, macOS 下的 csh 实际就是 tcsh.
Bell 实验室的 Korn 改进了 Bourne shell, 吸收了一些 csh 的功能, 就叫 Korn Shell
ksh 是因为需要商用 Unix 授权,因此有人重写了 ksh, 叫 public domain Korn shell (pdksh)
OpenBSD 使用的默认 shell 就是 pdksh
MirBSD (OpenBSD 的早期 fork) 包含了 pdksh, 叫 mksh, 是现在 Android 的默认 shell ( adb shell 命令)
Bash(Bourne again shell)是 GNU 工程实现了 shell, 也是大多数 GNU Linux 的默认 shell, 也曾经是 macOS 的默认 shell (10.4-10.14), 兼容 Bourne shell 但吸收了 csh 和 ksh 的一些功能,
Z shell 是 Paul Falstad 编写的兼容 Bourne shell 但吸收了 csh 和 ksh 的一些功能的 shell
所以 bash 和 zsh 是近乎同一时间出现(89 年, 90 年)的两个不同的项目, 其相同点就是采用了 Bourne shell 的语法,因此部分兼容.