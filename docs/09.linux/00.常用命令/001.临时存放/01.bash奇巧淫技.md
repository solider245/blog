---
title: bash奇巧淫技
date: 2020-10-12 12:09:51
permalink: /pages/0775b9/
categories:
  - linux
  - 常用命令
tags:
  - 
---
本书原作者将书中的内容发布到了[github](https://github.com/dylanaraps/pure-bash-bible)上，我仅仅是将其翻译为中文，并解释了其中的部分语句语法，希望可以对今后的工作有所帮助。

# `[](#以下是翻译后的原文)以下是翻译后的原文`

这本书的目的是汇总只使用内置`bash`的特性来实现总所周知和鲜为人知的各项任务。 使用此参考书中的代码段可以帮助你从脚本中删除不需要的依赖项，并且在大多数情况下可以使它们运行的更快。 我偶然碰到了这些技巧并在开发[neofetch](https://github.com/dylanaraps/neofetch), [pxltrm](https://github.com/dylanaraps/pxltrm) 和一些其他小的项目的时候发现了一些别的技巧。

下面的片段使用`shellcheck`进行了检查，并将测试写在了适用的地方。 想要贡献自己的代码? 阅读 [CONTRIBUTING\-Zh\_CN.md](https://github.com/A-BenMao/pure-bash-bible-zh_CN/blob/master/CONTRIBUTING-Zh_CN.md). 它概述了向参考书中增加片段时，单元测试的工作方式以及其他所需的内容。

看到了一些东西描述是不准确的、有缺陷的更或者是完全错误的？那么请新建一个issue或者发送一个pull request.如果参考书中缺少某些你想要的事物，也请新建一个issue并给出你能找到的解决方法。

# `[](#目-录)目 录`

*   [前言](#%E5%89%8D%E8%A8%80)
*   [字符串](#%E5%AD%97%E7%AC%A6%E4%B8%B2)
    *   [删除字符串前后空格](#%E5%88%A0%E9%99%A4%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%89%8D%E5%90%8E%E7%A9%BA%E6%A0%BC)
    *   [删除字符串中的所有的空白并用空格分割单词](#%E5%88%A0%E9%99%A4%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E6%89%80%E6%9C%89%E7%9A%84%E7%A9%BA%E7%99%BD%E5%B9%B6%E7%94%A8%E7%A9%BA%E6%A0%BC%E5%88%86%E5%89%B2%E5%8D%95%E8%AF%8D)
    *   [在字符串上匹配正则表达式](#%E5%9C%A8%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%8A%E5%8C%B9%E9%85%8D%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F)
    *   [指定分隔符拆分字符串](#%E6%8C%87%E5%AE%9A%E5%88%86%E9%9A%94%E7%AC%A6%E6%8B%86%E5%88%86%E5%AD%97%E7%AC%A6%E4%B8%B2)
    *   [将字符串转换为小写](#%E5%B0%86%E5%AD%97%E7%AC%A6%E4%B8%B2%E8%BD%AC%E6%8D%A2%E4%B8%BA%E5%B0%8F%E5%86%99)
    *   [将字符串转换为大写](#%E5%B0%86%E5%AD%97%E7%AC%A6%E4%B8%B2%E8%BD%AC%E6%8D%A2%E4%B8%BA%E5%A4%A7%E5%86%99)
    *   [反转字符串大小写](#%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%A4%A7%E5%B0%8F%E5%86%99)
    *   [删除字符串中的引号](#%E5%88%A0%E9%99%A4%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E5%BC%95%E5%8F%B7)
    *   [从字符串中删除所有正则实例](#%E4%BB%8E%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E5%88%A0%E9%99%A4%E6%89%80%E6%9C%89%E6%AD%A3%E5%88%99%E5%AE%9E%E4%BE%8B)
    *   [从字符串中删除第一次出现的正则实例](#%E4%BB%8E%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E5%88%A0%E9%99%A4%E7%AC%AC%E4%B8%80%E6%AC%A1%E5%87%BA%E7%8E%B0%E7%9A%84%E6%AD%A3%E5%88%99%E5%AE%9E%E4%BE%8B)
    *   [在字符串开头匹配正则并删除](#%E5%9C%A8%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%BC%80%E5%A4%B4%E5%8C%B9%E9%85%8D%E6%AD%A3%E5%88%99%E5%B9%B6%E5%88%A0%E9%99%A4)
    *   [在字符串末尾匹配正则并删除](#%E5%9C%A8%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%9C%AB%E5%B0%BE%E5%8C%B9%E9%85%8D%E6%AD%A3%E5%88%99%E5%B9%B6%E5%88%A0%E9%99%A4)
    *   [百分号编码字符串](#%E7%99%BE%E5%88%86%E5%8F%B7%E7%BC%96%E7%A0%81%E5%AD%97%E7%AC%A6%E4%B8%B2)
    *   [解码用百分比编码的字符串](#%E8%A7%A3%E7%A0%81%E7%94%A8%E7%99%BE%E5%88%86%E6%AF%94%E7%BC%96%E7%A0%81%E7%9A%84%E5%AD%97%E7%AC%A6%E4%B8%B2)
    *   [检查字符串是否包含子字符串](#%E6%A3%80%E6%9F%A5%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%98%AF%E5%90%A6%E5%8C%85%E5%90%AB%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2)
    *   [检查字符串是否以子字符串开头](#%E6%A3%80%E6%9F%A5%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%98%AF%E5%90%A6%E4%BB%A5%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%BC%80%E5%A4%B4)
    *   [检查字符串是否以子字符串结尾](#%E6%A3%80%E6%9F%A5%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%98%AF%E5%90%A6%E4%BB%A5%E5%AD%90%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%BB%93%E5%B0%BE)
*   [数组](#%E6%95%B0%E7%BB%84)
    *   [反转数组](#%E5%8F%8D%E8%BD%AC%E6%95%B0%E7%BB%84)
    *   [删除重复的数组元素](#%E5%88%A0%E9%99%A4%E9%87%8D%E5%A4%8D%E7%9A%84%E6%95%B0%E7%BB%84%E5%85%83%E7%B4%A0)
    *   [随机返回一个数组元素](#%E9%9A%8F%E6%9C%BA%E8%BF%94%E5%9B%9E%E4%B8%80%E4%B8%AA%E6%95%B0%E7%BB%84%E5%85%83%E7%B4%A0)
    *   [循环迭代一个数组](#%E5%BE%AA%E7%8E%AF%E8%BF%AD%E4%BB%A3%E4%B8%80%E4%B8%AA%E6%95%B0%E7%BB%84)
    *   [在两个值之间转换](#%E5%9C%A8%E4%B8%A4%E4%B8%AA%E5%80%BC%E4%B9%8B%E9%97%B4%E8%BD%AC%E6%8D%A2)
*   [循环](#%E5%BE%AA%E7%8E%AF)
    *   [循环生成范围内的数字](#%E5%BE%AA%E7%8E%AF%E7%94%9F%E6%88%90%E8%8C%83%E5%9B%B4%E5%86%85%E7%9A%84%E6%95%B0%E5%AD%97)
    *   [循环遍历可变数字范围](#%E5%BE%AA%E7%8E%AF%E9%81%8D%E5%8E%86%E5%8F%AF%E5%8F%98%E6%95%B0%E5%AD%97%E8%8C%83%E5%9B%B4)
    *   [循环数组](#%E5%BE%AA%E7%8E%AF%E6%95%B0%E7%BB%84)
    *   [循环输出带索引的数组](#%E5%BE%AA%E7%8E%AF%E8%BE%93%E5%87%BA%E5%B8%A6%E7%B4%A2%E5%BC%95%E7%9A%84%E6%95%B0%E7%BB%84)
    *   [循环遍历文件的内容](#%E5%BE%AA%E7%8E%AF%E9%81%8D%E5%8E%86%E6%96%87%E4%BB%B6%E7%9A%84%E5%86%85%E5%AE%B9)
    *   [循环遍历文件和目录](#%E5%BE%AA%E7%8E%AF%E9%81%8D%E5%8E%86%E6%96%87%E4%BB%B6%E5%92%8C%E7%9B%AE%E5%BD%95)
*   [文本处理](#%E6%96%87%E6%9C%AC%E5%A4%84%E7%90%86)
    *   [读取文件到一个字符串中](#%E8%AF%BB%E5%8F%96%E6%96%87%E4%BB%B6%E5%88%B0%E4%B8%80%E4%B8%AA%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD)
    *   [读取文件到一个数组中 (*按行读取*)](#%E8%AF%BB%E5%8F%96%E6%96%87%E4%BB%B6%E5%88%B0%E4%B8%80%E4%B8%AA%E6%95%B0%E7%BB%84%E4%B8%AD)
    *   [获取文件的前N行](#%E8%8E%B7%E5%8F%96%E6%96%87%E4%BB%B6%E7%9A%84%E5%89%8DN%E8%A1%8C)
    *   [获取文件的最后N行](#%E8%8E%B7%E5%8F%96%E6%96%87%E4%BB%B6%E7%9A%84%E6%9C%80%E5%90%8EN%E8%A1%8C)
    *   [获取文件中的行数](#%E8%8E%B7%E5%8F%96%E6%96%87%E4%BB%B6%E4%B8%AD%E7%9A%84%E8%A1%8C%E6%95%B0)
    *   [计算目录中的文件或目录](#%E8%AE%A1%E7%AE%97%E7%9B%AE%E5%BD%95%E4%B8%AD%E7%9A%84%E6%96%87%E4%BB%B6%E6%88%96%E7%9B%AE%E5%BD%95)
    *   [创建一个空文件](#%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E7%A9%BA%E6%96%87%E4%BB%B6)
    *   [提取两个标记之间的行](#%E6%8F%90%E5%8F%96%E4%B8%A4%E4%B8%AA%E6%A0%87%E8%AE%B0%E4%B9%8B%E9%97%B4%E7%9A%84%E8%A1%8C)
*   [文件路径](#%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84)
    *   [获取文件路径的目录名](#%E8%8E%B7%E5%8F%96%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E7%9A%84%E7%9B%AE%E5%BD%95%E5%90%8D)
    *   [获取文件路径的基本名称](#%E8%8E%B7%E5%8F%96%E6%96%87%E4%BB%B6%E8%B7%AF%E5%BE%84%E7%9A%84%E5%9F%BA%E6%9C%AC%E5%90%8D%E7%A7%B0)
*   [变量](#%E5%8F%98%E9%87%8F)
    *   [分配和访问一个变量](#%E5%88%86%E9%85%8D%E5%92%8C%E8%AE%BF%E9%97%AE%E4%B8%80%E4%B8%AA%E5%8F%98%E9%87%8F)
    *   [根据另一个变量命名变量](#%E6%A0%B9%E6%8D%AE%E5%8F%A6%E4%B8%80%E4%B8%AA%E5%8F%98%E9%87%8F%E5%91%BD%E5%90%8D%E5%8F%98%E9%87%8F)
*   [转义字符](#%E8%BD%AC%E4%B9%89%E5%AD%97%E7%AC%A6)
    *   [文本颜色](#%E6%96%87%E6%9C%AC%E9%A2%9C%E8%89%B2)
    *   [文本属性](#%E6%96%87%E6%9C%AC%E5%B1%9E%E6%80%A7)
    *   [移动光标](#%E7%A7%BB%E5%8A%A8%E5%85%89%E6%A0%87)
    *   [删除文本](#%E5%88%A0%E9%99%A4%E6%96%87%E6%9C%AC)
*   [参数拓展](#%E5%8F%82%E6%95%B0%E6%8B%93%E5%B1%95)
    *   [间接](#%E9%97%B4%E6%8E%A5)
    *   [替换](#%E6%9B%BF%E6%8D%A2)
    *   [长度](#%E9%95%BF%E5%BA%A6)
    *   [扩展](#%E6%89%A9%E5%B1%95)
    *   [改变大小写](#%E6%94%B9%E5%8F%98%E5%A4%A7%E5%B0%8F%E5%86%99)
    *   [默认值](#%E9%BB%98%E8%AE%A4%E5%80%BC)
*   [花括号展开](#%E8%8A%B1%E6%8B%AC%E5%8F%B7%E5%B1%95%E5%BC%80)
    *   [范围](#%E8%8C%83%E5%9B%B4)
    *   [字符串列表](#%E5%AD%97%E7%AC%A6%E4%B8%B2%E5%88%97%E8%A1%A8)
*   [条件表达式](#%E6%9D%A1%E4%BB%B6%E8%A1%A8%E8%BE%BE%E5%BC%8F)
    *   [文件判断](#%E6%96%87%E4%BB%B6%E5%88%A4%E6%96%AD)
    *   [文件比较](#%E6%96%87%E4%BB%B6%E6%AF%94%E8%BE%83)
    *   [条件变量](#%E6%9D%A1%E4%BB%B6%E5%8F%98%E9%87%8F)
    *   [比较变量](#%E6%AF%94%E8%BE%83%E5%8F%98%E9%87%8F)
*   [算术运算符](#%E7%AE%97%E6%9C%AF%E8%BF%90%E7%AE%97%E7%AC%A6)
    *   [指派](#%E6%8C%87%E6%B4%BE)
    *   [四则运算](#%E5%9B%9B%E5%88%99%E8%BF%90%E7%AE%97)
    *   [位运算](#%E4%BD%8D%E8%BF%90%E7%AE%97)
    *   [逻辑运算](#%E9%80%BB%E8%BE%91%E8%BF%90%E7%AE%97)
    *   [复杂运算](#%E5%A4%8D%E6%9D%82%E8%BF%90%E7%AE%97)
*   [算术运算符\-1](#%E7%AE%97%E6%9C%AF%E8%BF%90%E7%AE%97%E7%AC%A6-1)
    *   [用更简单语法设置变量](#%E7%94%A8%E6%9B%B4%E7%AE%80%E5%8D%95%E8%AF%AD%E6%B3%95%E8%AE%BE%E7%BD%AE%E5%8F%98%E9%87%8F)
    *   [三元测试](#%E4%B8%89%E5%85%83%E6%B5%8B%E8%AF%95)
*   [trap命令](#trap%E5%91%BD%E4%BB%A4)
    *   [在脚本退出时执行操作](#%E5%9C%A8%E8%84%9A%E6%9C%AC%E9%80%80%E5%87%BA%E6%97%B6%E6%89%A7%E8%A1%8C%E6%93%8D%E4%BD%9C)
    *   [忽略终端中断（CTRL+C，SIGINT）](#%E5%BF%BD%E7%95%A5%E7%BB%88%E7%AB%AF%E4%B8%AD%E6%96%AD)
    *   [对窗口调整大小时做出反应](#%E5%AF%B9%E7%AA%97%E5%8F%A3%E8%B0%83%E6%95%B4%E5%A4%A7%E5%B0%8F%E6%97%B6%E5%81%9A%E5%87%BA%E5%8F%8D%E5%BA%94)
    *   [在命令之前执行某些操作](#%E5%9C%A8%E5%91%BD%E4%BB%A4%E4%B9%8B%E5%89%8D%E6%89%A7%E8%A1%8C%E6%9F%90%E4%BA%9B%E6%93%8D%E4%BD%9C)
    *   [在shell函数或源文件完成执行时执行某些操作](#%E5%9C%A8shell%E5%87%BD%E6%95%B0%E6%88%96%E6%BA%90%E6%96%87%E4%BB%B6%E5%AE%8C%E6%88%90%E6%89%A7%E8%A1%8C%E6%97%B6%E6%89%A7%E8%A1%8C%E6%9F%90%E4%BA%9B%E6%93%8D%E4%BD%9C)
*   [性能](#%E6%80%A7%E8%83%BD)
    *   [禁用Unicode码](#%E7%A6%81%E7%94%A8Unicode%E7%A0%81)
*   [已过时的语法](#%E5%B7%B2%E8%BF%87%E6%97%B6%E7%9A%84%E8%AF%AD%E6%B3%95)
    *   [释伴声明](#%E9%87%8A%E4%BC%B4%E5%A3%B0%E6%98%8E)
    *   [命令替换](#%E5%91%BD%E4%BB%A4%E6%9B%BF%E6%8D%A2)
    *   [声明函数](#%E5%A3%B0%E6%98%8E%E5%87%BD%E6%95%B0)
*   [内部变量](#%E5%86%85%E9%83%A8%E5%8F%98%E9%87%8F)
    *   [获取`bash`二进制文件的位置](#%E8%8E%B7%E5%8F%96%60bash%60%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%96%87%E4%BB%B6%E7%9A%84%E4%BD%8D%E7%BD%AE)
    *   [获取当前运行`bash`命令的版本](#%E8%8E%B7%E5%8F%96%E5%BD%93%E5%89%8D%E8%BF%90%E8%A1%8C%60bash%60%E5%91%BD%E4%BB%A4%E7%9A%84%E7%89%88%E6%9C%AC)
    *   [打开用户默认的文本编辑器](#%E6%89%93%E5%BC%80%E7%94%A8%E6%88%B7%E9%BB%98%E8%AE%A4%E7%9A%84%E6%96%87%E6%9C%AC%E7%BC%96%E8%BE%91%E5%99%A8)
    *   [获取当前函数的名称](#%E8%8E%B7%E5%8F%96%E5%BD%93%E5%89%8D%E5%87%BD%E6%95%B0%E7%9A%84%E5%90%8D%E7%A7%B0)
    *   [获取系统的主机名](#%E8%8E%B7%E5%8F%96%E7%B3%BB%E7%BB%9F%E7%9A%84%E4%B8%BB%E6%9C%BA%E5%90%8D)
    *   [获取操作系统的架构（32位或64位）](#%E8%8E%B7%E5%8F%96%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%E7%9A%84%E6%9E%B6%E6%9E%84)
    *   [获取操作系统/内核的名称](#%E8%8E%B7%E5%8F%96%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F/%E5%86%85%E6%A0%B8%E7%9A%84%E5%90%8D%E7%A7%B0)
    *   [获取当前的工作目录](#%E8%8E%B7%E5%8F%96%E5%BD%93%E5%89%8D%E7%9A%84%E5%B7%A5%E4%BD%9C%E7%9B%AE%E5%BD%95)
    *   [获取脚本运行的秒数](#%E8%8E%B7%E5%8F%96%E8%84%9A%E6%9C%AC%E8%BF%90%E8%A1%8C%E7%9A%84%E7%A7%92%E6%95%B0)
    *   [获取伪随机整数](#%E8%8E%B7%E5%8F%96%E4%BC%AA%E9%9A%8F%E6%9C%BA%E6%95%B4%E6%95%B0)
*   [有关终端的信息](#%E6%9C%89%E5%85%B3%E7%BB%88%E7%AB%AF%E7%9A%84%E4%BF%A1%E6%81%AF)
    *   [获取终端的总行列数（*来自脚本*）](#%E8%8E%B7%E5%8F%96%E7%BB%88%E7%AB%AF%E7%9A%84%E6%80%BB%E8%A1%8C%E5%88%97%E6%95%B0)
    *   [获取终端的像素大小](#%E8%8E%B7%E5%8F%96%E7%BB%88%E7%AB%AF%E7%9A%84%E5%83%8F%E7%B4%A0%E5%A4%A7%E5%B0%8F)
    *   [获取当前光标位置](#%E8%8E%B7%E5%8F%96%E5%BD%93%E5%89%8D%E5%85%89%E6%A0%87%E4%BD%8D%E7%BD%AE)
*   [转换](#%E8%BD%AC%E6%8D%A2)
    *   [将十六进制颜色转换为RGB](#%E5%B0%86%E5%8D%81%E5%85%AD%E8%BF%9B%E5%88%B6%E9%A2%9C%E8%89%B2%E8%BD%AC%E6%8D%A2%E4%B8%BARGB)
    *   [将RGB颜色转换为十六进制](#%E5%B0%86RGB%E9%A2%9C%E8%89%B2%E8%BD%AC%E6%8D%A2%E4%B8%BA%E5%8D%81%E5%85%AD%E8%BF%9B%E5%88%B6)
*   [代码高尔夫](#%E4%BB%A3%E7%A0%81%E9%AB%98%E5%B0%94%E5%A4%AB)
    *   [更短的`for`循环语法](#%E6%9B%B4%E7%9F%AD%E7%9A%84%60for%60%E5%BE%AA%E7%8E%AF%E8%AF%AD%E6%B3%95)
    *   [更短的无限循环](#%E6%9B%B4%E7%9F%AD%E7%9A%84%E6%97%A0%E9%99%90%E5%BE%AA%E7%8E%AF)
    *   [更短的函数声明](#%E6%9B%B4%E7%9F%AD%E7%9A%84%E5%87%BD%E6%95%B0%E5%A3%B0%E6%98%8E)
    *   [更短的`if`语法](#%E6%9B%B4%E7%9F%AD%E7%9A%84%60if%60%E8%AF%AD%E6%B3%95)
    *   [用`case`语句来更简单的设置变量](#%E7%94%A8%60case%60%E8%AF%AD%E5%8F%A5%E6%9D%A5%E6%9B%B4%E7%AE%80%E5%8D%95%E7%9A%84%E8%AE%BE%E7%BD%AE%E5%8F%98%E9%87%8F)
*   [其他](#%E5%85%B6%E4%BB%96)
    *   [使用`read`作为`sleep`命令的替代品](#%E4%BD%BF%E7%94%A8%60read%60%E4%BD%9C%E4%B8%BA%60sleep%60%E5%91%BD%E4%BB%A4%E7%9A%84%E6%9B%BF%E4%BB%A3%E5%93%81)
    *   [检查一个命令是否在用户的PATH中](#%E6%A3%80%E6%9F%A5%E4%B8%80%E4%B8%AA%E5%91%BD%E4%BB%A4%E6%98%AF%E5%90%A6%E5%9C%A8%E7%94%A8%E6%88%B7%E7%9A%84PATH%E4%B8%AD)
    *   [使用`strftime`获取当前日期](#%E4%BD%BF%E7%94%A8%60strftime%60%E8%8E%B7%E5%8F%96%E5%BD%93%E5%89%8D%E6%97%A5%E6%9C%9F)
    *   [获取当前用户的用户名](#%E8%8E%B7%E5%8F%96%E5%BD%93%E5%89%8D%E7%94%A8%E6%88%B7%E7%9A%84%E7%94%A8%E6%88%B7%E5%90%8D)
    *   [生成一个V4版本的UUID](#%E7%94%9F%E6%88%90%E4%B8%80%E4%B8%AAV4%E7%89%88%E6%9C%AC%E7%9A%84UUID)
    *   [进度条](#%E8%BF%9B%E5%BA%A6%E6%9D%A1)
    *   [获取脚本中的函数列表](#%E8%8E%B7%E5%8F%96%E8%84%9A%E6%9C%AC%E4%B8%AD%E7%9A%84%E5%87%BD%E6%95%B0%E5%88%97%E8%A1%A8)
    *   [绕过shell别名](#%E7%BB%95%E8%BF%87shell%E5%88%AB%E5%90%8D)
    *   [绕过shell函数](#%E7%BB%95%E8%BF%87shell%E5%87%BD%E6%95%B0)
    *   [在后台运行命令](#%E5%9C%A8%E5%90%8E%E5%8F%B0%E8%BF%90%E8%A1%8C%E5%91%BD%E4%BB%A4)
*   [后记](#%E5%90%8E%E8%AE%B0)

# `[](#前言)前言`

纯`bash`脚本替代外部流程和程序的集合。 `bash`脚本语言远比大部分人了解到的更强大，大多数任务都可以在不依赖外部程序的情况下由`bash`独立完成。

在`bash`中调用外部进程是昂贵的，过度使用会导致效率明显的下降。 使用内置方法编写的脚本和程序（*在适合的地方*）将更快，依赖性更小，并能对脚本本身有更好的理解。

本书的目的是为大家用`bash`编写程序和脚本过程中遇到问题时提供了一种思路。 示例展示了将这些解决方案合并到代码中的函数格式。

# `[](#字符串)字符串`

## `[](#删除字符串前后空格)删除字符串前后空格`

这是`sed`，`awk`，`perl`和其他工具的替代品。下面的函数通过查找所有头尾空格并在字符串的开头和结尾删除它来实现这一功能。

`：`内置用于代替临时变量。

**示例函数:**

```shell
trim_string() {
    # Usage: trim_string "   example   string    "
    : "${1#"${1%%[![:space:]]*}"}"
    : "${_%"${_##*[![:space:]]}"}"
    printf '%s\n' "$_"
}
```

**用法示例:**

```shell
$ trim_string "    Hello,  World    "
Hello,  World

$ name="   John Black  "
$ trim_string "$name"
John Black
```

## `[](#删除字符串中的所有的空白并用空格分割单词)删除字符串中的所有的空白并用空格分割单词`

这是`sed`，`awk`，`perl`和其他工具的替代品。 下面的函数通过重复使用单词拆分来创建一个没有前导/尾随空格的新字符串，并用空格分割字符串中的单词。

**示例函数:**

```shell
# shellcheck disable=SC2086,SC2048
trim_all() {
    # Usage: trim_all "   example   string    "
    set -f
    set -- $*
    printf '%s\n' "$*"
    set +f
}
```

**用法示例:**

```shell
$ trim_all "    Hello,    World    "
Hello, World

$ name="   John   Black  is     my    name.    "
$ trim_all "$name"
John Black is my name.
```

## `[](#在字符串上匹配正则表达式)在字符串上匹配正则表达式`

对于使用`sed`的大部分情况，`bash`的正则表达式匹配结果完全可以替代。

**警告**: 这是少数平台相关的“bash”功能之一。 `bash`将使用用户系统上安装的任何正则表达式引擎。 如果要兼容，请坚持使用符合POSIX规范的正则表达式引擎。 绝大部分发行版Linux中的bash均实现了POSIX规范。

**警告**: 此示例仅打印第一个匹配组。 使用时多个匹配组需要进行一些修改。

**示例函数:**

```shell
regex() {
    # Usage: regex "string" "regex"
    [[ $1 =~ $2 ]] && printf '%s\n' "${BASH_REMATCH[1]}"
}
```

**用法示例:**

```shell
$ # 删除开头的空白字符.
$ regex '    hello' '^\s*(.*)'
hello

$ # 验证十六进制颜色.
$ regex "#FFFFFF" '^(#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3}))$'
#FFFFFF

$ # 验证十六进制颜色（无效）.
$ regex "red" '^(#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3}))$'
# no output (invalid)
```

**在脚本中的示例:**

```shell
is_hex_color() {
    if [[ $1 =~ ^(#?([a-fA-F0-9]{6}|[a-fA-F0-9]{3}))$ ]]; then
        printf '%s\n' "${BASH_REMATCH[1]}"
    else
        printf '%s\n' "error: $1 is an invalid color."
        return 1
    fi
}

read -r color
is_hex_color "$color" || color="#FFFFFF"

# Do stuff.
```

## `[](#指定分隔符拆分字符串)指定分隔符拆分字符串`

**警告:** 需要`bash` 4+以上的版本

这是`cut`，`awk`和其他工具的替代品。

**示例函数:**

```shell
split() {
   # Usage: split "string" "delimiter"
   IFS=$'\n' read -d "" -ra arr <<< "${1//$2/$'\n'}"
   printf '%s\n' "${arr[@]}"
}
```

**示例用法:**

```shell
$ split "apples,oranges,pears,grapes" ","
apples
oranges
pears
grapes

$ split "1, 2, 3, 4, 5" ", "
1
2
3
4
5

# 多字符分隔符也可以工作！
$ split "hello---world---my---name---is---john" "---"
hello
world
my
name
is
john
```

## `[](#将字符串转换为小写)将字符串转换为小写`

**警告:** 需要`bash` 4+以上的版本

**示例函数:**

```shell
lower() {
    # Usage: lower "string"
    printf '%s\n' "${1,,}"
}
```

**示例用法:**

```shell
$ lower "HELLO"
hello

$ lower "HeLlO"
hello

$ lower "hello"
hello
```

## `[](#将字符串转换为大写)将字符串转换为大写`

**警告:** 需要`bash` 4+以上的版本

**示例函数:**

```shell
upper() {
    # Usage: upper "string"
    printf '%s\n' "${1^^}"
}
```

**示例用法:**

```shell
$ upper "hello"
HELLO

$ upper "HeLlO"
HELLO

$ upper "HELLO"
HELLO
```

## `[](#反转字符串大小写)反转字符串大小写`

**警告:** 需要`bash` 4+以上的版本

**示例函数:**

```shell
reverse_case() {
    # Usage: reverse_case "string"
    printf '%s\n' "${1~~}"
}
```

**示例用法:**

```shell
$ reverse_case "hello"
HELLO

$ reverse_case "HeLlO"
hElLo

$ reverse_case "HELLO"
hello
```

## `[](#删除字符串中的引号)删除字符串中的引号`

**示例函数:**

```shell
trim_quotes() {
    # Usage: trim_quotes "string"
    : "${1//\'}"
    printf '%s\n' "${_//\"}"
}
```

**示例用法:**

```shell
$ var="'Hello', \"World\""
$ trim_quotes "$var"
Hello, World
```

## `[](#从字符串中删除所有正则实例)从字符串中删除所有正则实例`

**示例函数:**

```shell
strip_all() {
    # Usage: strip_all "string" "pattern"
    printf '%s\n' "${1//$2}"
}
```

**示例用法:**

```shell
$ strip_all "The Quick Brown Fox" "[aeiou]"
Th Qck Brwn Fx

$ strip_all "The Quick Brown Fox" "[[:space:]]"
TheQuickBrownFox

$ strip_all "The Quick Brown Fox" "Quick "
The Brown Fox
```

## `[](#从字符串中删除第一次出现的正则实例)从字符串中删除第一次出现的正则实例`

**示例函数:**

```shell
strip() {
    # Usage: strip "string" "pattern"
    printf '%s\n' "${1/$2}"
}
```

**示例用法:**

```shell
$ strip "The Quick Brown Fox" "[aeiou]"
Th Quick Brown Fox

$ strip "The Quick Brown Fox" "[[:space:]]"
TheQuick Brown Fox
```

## `[](#在字符串开头匹配正则并删除)在字符串开头匹配正则并删除`

**示例函数:**

```shell
lstrip() {
    # Usage: lstrip "string" "pattern"
    printf '%s\n' "${1##$2}"
}
```

**示例用法:**

```shell
$ lstrip "The Quick Brown Fox" "The "
Quick Brown Fox
```

## `[](#在字符串末尾匹配正则并删除)在字符串末尾匹配正则并删除`

**示例函数:**

```shell
rstrip() {
    # Usage: rstrip "string" "pattern"
    printf '%s\n' "${1%%$2}"
}
```

**示例用法:**

```shell
$ rstrip "The Quick Brown Fox" " Fox"
The Quick Brown
```

## `[](#百分号编码字符串)百分号编码字符串`

**示例函数:**

```shell
urlencode() {
    # Usage: urlencode "string"
    local LC_ALL=C
    for (( i = 0; i < ${#1}; i++ )); do
        : "${1:i:1}"
        case "$_" in
            [a-zA-Z0-9.~_-])
                printf '%s' "$_"
            ;;

            *)
                printf '%%%02X' "'$_"
            ;;
        esac
    done
    printf '\n'
}
```

**示例用法:**

```shell
$ urlencode "https://github.com/dylanaraps/pure-bash-bible"
https%3A%2F%2Fgithub.com%2Fdylanaraps%2Fpure-bash-bible
```

## `[](#解码用百分比编码的字符串)解码用百分比编码的字符串`

**示例函数:**

```shell
urldecode() {
    # Usage: urldecode "string"
    : "${1//+/ }"
    printf '%b\n' "${_//%/\\x}"
}
```

**示例用法:**

```shell
$ urldecode "https%3A%2F%2Fgithub.com%2Fdylanaraps%2Fpure-bash-bible"
https://github.com/dylanaraps/pure-bash-bible
```

## `[](#检查字符串是否包含子字符串)检查字符串是否包含子字符串`

**用于测试:**

```shell
if [[ $var == *sub_string* ]]; then
    printf '%s\n' "sub_string is in var."
fi

# 反转 (子串不在字符串中).
if [[ $var != *sub_string* ]]; then
    printf '%s\n' "sub_string is not in var."
fi

# 也可以在数组中运行
if [[ ${arr[*]} == *sub_string* ]]; then
    printf '%s\n' "sub_string is in array."
fi
```

**使用case语句:**

```shell
case "$var" in
    *sub_string*)
        # Do stuff
    ;;

    *sub_string2*)
        # Do more stuff
    ;;

    *)
        # Else
    ;;
esac
```

## `[](#检查字符串是否以子字符串开头)检查字符串是否以子字符串开头`

```shell
if [[ $var == sub_string* ]]; then
    printf '%s\n' "var starts with sub_string."
fi

# 反转 (变量不是以子串开头).
if [[ $var != sub_string* ]]; then
    printf '%s\n' "var does not start with sub_string."
fi
```

## `[](#检查字符串是否以子字符串结尾)检查字符串是否以子字符串结尾`

```shell
if [[ $var == *sub_string ]]; then
    printf '%s\n' "var ends with sub_string."
fi

# Inverse (var does not end with sub_string).
if [[ $var != *sub_string ]]; then
    printf '%s\n' "var does not end with sub_string."
fi
```

# `[](#数组)数组`

## `[](#反转数组)反转数组`

启用`extdebug`允许访问`BASH_ARGV`数组，该数组反向存储当前函数的参数

**示例函数:**

```shell
reverse_array() {
    # Usage: reverse_array "array"
    shopt -s extdebug
    f()(printf '%s\n' "${BASH_ARGV[@]}"); f "$@"
    shopt -u extdebug
}
```

**示例用法:**

```shell
$ reverse_array 1 2 3 4 5
5
4
3
2
1

$ arr=(red blue green)
$ reverse_array "${arr[@]}"
green
blue
red
```

## `[](#删除重复的数组元素)删除重复的数组元素`

创建临时关联数组。设置关联数组值并发生重复赋值时，bash会覆盖该键。这允许我们有效地删除数组重复。

**警告:** 版本要求 `bash` 4+

**示例函数:**

```shell
remove_array_dups() {
    # Usage: remove_array_dups "array"
    declare -A tmp_array

    for i in "$@"; do
        [[ $i ]] && IFS=" " tmp_array["${i:- }"]=1
    done

    printf '%s\n' "${!tmp_array[@]}"
}
```

**示例用法:**

```shell
$ remove_array_dups 1 1 2 2 3 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5
1
2
3
4
5

$ arr=(red red green blue blue)
$ remove_array_dups "${arr[@]}"
red
green
blue
```

## `[](#随机返回一个数组元素)随机返回一个数组元素`

**示例函数:**

```shell
random_array_element() {
    # Usage: random_array_element "array"
    local arr=("$@")
    printf '%s\n' "${arr[RANDOM % $#]}"
}
```

bash的SHELL参数RANDOM可以生成0\-32767的随机数 想设定从1到N的随机数范围的话，可以使用： $ ( ( (RANDOM % n) + 1 ))

**示例用法:**

```shell
$ array=(red green blue yellow brown)
$ random_array_element "${array[@]}"
yellow

# Multiple arguments can also be passed.
$ random_array_element 1 2 3 4 5 6 7
3
```

## `[](#循环迭代一个数组)循环迭代一个数组`

每次`printf`调用时，都会打印下一个数组元素。当打印到达最后一个数组元素时，它再次从第一个元素开始。

```shell
arr=(a b c d)

cycle() {
    printf '%s ' "${arr[${i:=0}]}"
    ((i=i>=${#arr[@]}-1?0:++i))
}
```

## `[](#在两个值之间转换)在两个值之间转换`

这与上面的工作方式相同，这只是一个不同的用例。

```shell
arr=(true false)

cycle() {
    printf '%s ' "${arr[${i:=0}]}"
    ((i=i>=${#arr[@]}-1?0:++i))
}
```

# `[](#循环)循环`

## `[](#循环生成范围内的数字)循环生成范围内的数字`

替代`seq`.

```shell
# Loop from 0-100 (no variable support).
for i in {0..100}; do
    printf '%s\n' "$i"
done
```

## `[](#循环遍历可变数字范围)循环遍历可变数字范围`

替代 `seq`.

```shell
# Loop from 0-VAR.
VAR=50
for ((i=0;i<=VAR;i++)); do
    printf '%s\n' "$i"
done
```

## `[](#循环数组)循环数组`

```shell
arr=(apples oranges tomatoes)

# Just elements.
for element in "${arr[@]}"; do
    printf '%s\n' "$element"
done
```

## `[](#循环输出带索引的数组)循环输出带索引的数组`

```shell
arr=(apples oranges tomatoes)

# 元素和索引.
for i in "${!arr[@]}"; do
	printf '%s %s\n' "$i ${arr[i]}"
done

# 替代方法.
for ((i=0;i<${#arr[@]};i++)); do
    printf '%s %s\n' "$i ${arr[i]}"
done
```

## `[](#循环遍历文件的内容)循环遍历文件的内容`

```shell
while read -r line; do
    printf '%s\n' "$line"
done < "file"
```

## `[](#循环遍历文件和目录)循环遍历文件和目录`

不要 `ls`.

```shell
# 遍历当前目录下的文件和目录.
for file in *; do
    printf '%s\n' "$file"
done

# 遍历目录中的png图片.
for file in ~/Pictures/*.png; do
    printf '%s\n' "$file"
done

# 迭代输出目录.
for dir in ~/Downloads/*/; do
    printf '%s\n' "$dir"
done

# 支持扩展.
for file in /path/to/parentdir/{file1,file2,subdir/file3}; do
    printf '%s\n' "$file"
done

# 递归迭代，输出子目录下的所有文件.
#
shopt -s globstar
for file in ~/Pictures/**/*; do
    printf '%s\n' "$file"
done
shopt -u globstar
```

globstar是Bash 4.0才引入的选项，当设置启用globstar(shopt \-s globstar)时，两个星号意为对通配符进行展开就可以匹配任何当前目录(包括子目录)以及其的文件；若不启用globstar(shopt \-u globstar)，两个星号通配符的作用和一个星号通配符是相同的。

# `[](#文本处理)文本处理`

**警告:** `bash`在小于`<4.4`的版本中不能正确处理二进制数据.

## `[](#读取文件到一个字符串中)读取文件到一个字符串中`

替代 `cat` 命令.

```shell
file_data="$(<"file")"
```

## `[](#读取文件到一个数组中-按行读取)读取文件到一个数组中 (*按行读取*)`

替代 `cat` 命令.

```shell
# Bash <4 (丢弃空行)
IFS=$'\n' read -d "" -ra file_data < "file"

# Bash <4 (保留空行).
while read -r line; do
    file_data+=("$line")
done < "file"

# Bash 4+
mapfile -t file_data < "file"
```

## `[](#获取文件的前n行)获取文件的前N行`

替代 `head` 命令.

**警告:** 版本要求 `bash` 4+

**示例函数:**

```shell
head() {
    # Usage: head "n" "file"
    mapfile -tn "$1" line < "$2"
    printf '%s\n' "${line[@]}"
}
```

**示例用法:**

```shell
$ head 2 ~/.bashrc
# Prompt
PS1='➜ '

$ head 1 ~/.bashrc
# Prompt
```

## `[](#获取文件的最后n行)获取文件的最后N行`

替代 `tail` 命令.

**警告:** 版本要求 `bash` 4+

**示例函数:**

```shell
tail() {
    # Usage: tail "n" "file"
    mapfile -tn 0 line < "$2"
    printf '%s\n' "${line[@]: -$1}"
}
```

**示例用法:**

```shell
$ tail 2 ~/.bashrc
# Enable tmux.
# [[ -z "$TMUX"  ]] && exec tmux

$ tail 1 ~/.bashrc
# [[ -z "$TMUX"  ]] && exec tmux
```

## `[](#获取文件中的行数)获取文件中的行数`

替代 `wc -l`.

**示例函数 (bash 4):**

```shell
lines() {
    # Usage: lines "file"
    mapfile -tn 0 lines < "$1"
    printf '%s\n' "${#lines[@]}"
}
```

**示例函数 (bash 3):**

这个方法比`mapfile`方法使用更少的内存，并且在`bash` 3中工作，但对于更大的文件来说它更慢。

```shell
lines_loop() {
    # Usage: lines_loop "file"
    count=0
    while IFS= read -r _; do
        ((count++))
    done < "$1"
    printf '%s\n' "$count"
}
```

**示例用法:**

```shell
$ lines ~/.bashrc
48

$ lines_loop ~/.bashrc
48
```

## `[](#计算目录中的文件或目录)计算目录中的文件或目录`

这是通过将glob的输出传递给函数然后计算参数的数量来实现的。

**示例函数:**

```shell
count() {
    # Usage: count /path/to/dir/*
    #        count /path/to/dir/*/
    printf '%s\n' "$#"
}
```

**示例用法:**

```shell
# Count all files in dir.
$ count ~/Downloads/*
232

# Count all dirs in dir.
$ count ~/Downloads/*/
45

# Count all jpg files in dir.
$ count ~/Pictures/*.jpg
64
```

## `[](#创建一个空文件)创建一个空文件`

替代 `touch`.

```shell
# 简短的方式.
>file

# 更长的替代品:
:>file
echo -n >file
printf '' >file
```

## `[](#提取两个标记之间的行)提取两个标记之间的行`

**示例函数:**

```shell
extract() {
    # 用法: extract file "opening marker" "closing marker"
    while IFS=$'\n' read -r line; do
        [[ $extract && $line != "$3" ]] &&
            printf '%s\n' "$line"

        [[ $line == "$2" ]] && extract=1
        [[ $line == "$3" ]] && extract=
    done < "$1"
}
```

**示例用法:**

```shell
# 从MarkDown文件中提取代码块.
$ extract ~/projects/pure-bash/README.md '```sh' '```'
# Output here...
```

# `[](#文件路径)文件路径`

## `[](#获取文件路径的目录名)获取文件路径的目录名`

替代 `dirname` 命令.

**示例函数:**

```shell
dirname() {
    # 用法: dirname "path"
    local tmp=${1:-.}

    [[ $tmp != *[!/]* ]] && {
        printf '/\n'
        return
    }

    tmp=${tmp%%"${tmp##*[!/]}"}

    [[ $tmp != */* ]] && {
        printf '.\n'
        return
    }

    tmp=${tmp%/*}
    tmp=${tmp%%"${tmp##*[!/]}"}

    printf '%s\n' "${tmp:-/}"
}
```

**示例用法:**

```shell
$ dirname ~/Pictures/Wallpapers/1.jpg
/home/black/Pictures/Wallpapers

$ dirname ~/Pictures/Downloads/
/home/black/Pictures
```

## `[](#获取文件路径的基本名称)获取文件路径的基本名称`

替代 `basename` 命令.

**示例函数:**

```shell
basename() {
    # 用法: basename "path" ["后缀"]
    local tmp

    tmp=${1%"${1##*[!/]}"}
    tmp=${tmp##*/}
    tmp=${tmp%"${2/"$tmp"}"}

    printf '%s\n' "${tmp:-/}"
}
```

**示例用法:**

```shell
$ basename ~/Pictures/Wallpapers/1.jpg
1.jpg

$ basename ~/Pictures/Wallpapers/1.jpg .jpg
1

$ basename ~/Pictures/Downloads/
Downloads
```

# `[](#变量)变量`

## `[](#分配和访问一个变量)分配和访问一个变量`

```shell
$ hello_world="value"

# 创建一个变量名.
$ var="world"
$ ref="hello_$var"

# 打印存储为 'hello_$var' 变量名称的值.
$ printf '%s\n' "${!ref}"
value
```

或者, 在 `bash` 4.3+以上版本:

```shell
$ hello_world="value"
$ var="world"

# 声明一个名称引用.
$ declare -n ref=hello_$var

$ printf '%s\n' "$ref"
value
```

## `[](#根据另一个变量命名变量)根据另一个变量命名变量`

```shell
$ var="world"
$ declare "hello_$var=value"
$ printf '%s\n' "$hello_world"
value
```

# `[](#转义字符)转义字符`

与流行的看法相反, 使用原始的转义字符并不会出现问题. 使用`tput`抽象相同的ANSI序列，就像手动打印一样. 更糟糕的是，`tput`实际上并不是便携式的. 有许多`tput`变体，每个变体都有不同的命令和语法 (*尝试运行 `tput setaf 3` 在 FreeBSD 系统里*).

## `[](#文本颜色)文本颜色`

**NOTE:** 需要RGB值的序列仅适用于真彩色终端仿真器.

| 序列 | 它将做什么？ | 值 |
| --- | --- | --- |
| `\e[38;5;<NUM>m` | 设置文本前景色. | `0-255` |
| `\e[48;5;<NUM>m` | 设置文本背景颜色. | `0-255` |
| `\e[38;2;<R>;<G>;<B>m` | 将文本前景色设置为RGB颜色. | `R`, `G`, `B` |
| `\e[48;2;<R>;<G>;<B>m` | 将文本背景颜色设置为RGB颜色. | `R`, `G`, `B` |

## `[](#文本属性)文本属性`

| 序列 | 它将做什么？ |
| --- | --- |
| `\e[m` | 重置文本格式和颜色. |
| `\e[1m` | 粗体. |
| `\e[2m` | 微弱的文字. |
| `\e[3m` | 斜体文字. |
| `\e[4m` | 下划线文字. |
| `\e[5m` | 慢速闪烁. |
| `\e[7m` | 交换前景色和背景色. |

## `[](#移动光标)移动光标`

| 序列 | 它将做什么？ | 值 |
| --- | --- | --- |
| `\e[<LINE>;<COLUMN>H` | 将光标移动到绝对位置. | `line`, `column` |
| `\e[H` | 将光标移动到原位 (`0,0`). |  |
| `\e[<NUM>A` | 将光标向上移动N行. | `num` |
| `\e[<NUM>B` | 将光标向下移动N行. | `num` |
| `\e[<NUM>C` | 将光标向右移动N列. | `num` |
| `\e[<NUM>D` | 将光标向左移动N列. | `num` |
| `\e[s` | 保存光标位置. |  |
| `\e[u` | 恢复光标位置. |  |

## `[](#删除文本)删除文本`

| 序列 | 它将做什么？ |
| --- | --- |
| `\e[K` | 从光标位置删除到行尾. |
| `\e[1K` | 从光标位置删除到行首. |
| `\e[2K` | 擦除整个当前行. |
| `\e[J` | 从当前行删除到屏幕底部. |
| `\e[1J` | 从当前行删除到屏幕顶部. |
| `\e[2J` | 清除屏幕. |
| `\e[2J\e[H` | 清除屏幕并将光标移动到 `0,0`. |

# `[](#参数拓展)参数拓展`

## `[](#间接)间接`

| 参数 | 它将做什么？ |
| --- | --- |
| `${!VAR}` | 根据`VAR`的值访问一个变量. |
| `${!VAR*}` | 扩展为以`VAR`开头的变量名列表，并用`IFS`分隔. |
| `${!VAR@}` | 扩展为以`VAR`开头的变量名列表，并用`IFS`分隔. 如果是双引号，则每个变量名称都会扩展为单独的单词. |

## `[](#替换)替换`

| 参数 | 它将做什么？ |
| --- | --- |
| `${VAR#PATTERN}` | 删除第一次匹配的模式及其左边的字符. |
| `${VAR##PATTERN}` | 删除最后一次匹配的模式及其左边的字符. |
| `${VAR%PATTERN}` | 删除最后一次匹配的模式及其右边的字符. |
| `${VAR%%PATTERN}` | 删除第一次匹配的模式及其右边的字符. |
| `${VAR/PATTERN/REPLACE}` | 替换第一次匹配的字符. |
| `${VAR//PATTERN/REPLACE}` | 替换所有匹配的字符. |
| `${VAR/PATTERN}` | 删除第一次匹配的字符. |
| `${VAR//PATTERN}` | 删除所有匹配的字符. |

## `[](#长度)长度`

| 参数 | 它将做什么？ |
| --- | --- |
| `${#VAR}` | 字符变量的长度. |
| `${#ARR[@]}` | 数组的长度. |

## `[](#扩展)扩展`

| 参数 | 它将做什么？ | 版本要求 | | \-\-\-\-\-\-\-\-\- | \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- | | `${VAR:OFFSET}` | 从变量中删除第OFFSET个字符及之前的字符. | `${VAR:OFFSET:LENGTH}` | 获得从`OFFSET`字符之后`LENGTH`个字符的字符串.
(`${VAR:10:10}`: 获得从第10个字符到第20个字符的字符串) | `${VAR:: OFFSET}` | 从变量中获取前`OFFSET`个字符. | `${VAR:: -OFFSET}` | 从变量中移除前`OFFSET`个字符. | `${VAR: -OFFSET}` | 从变量中获取最后`OFFSET`个字符. | `${VAR:OFFSET:-OFFSET}` | 删除前`OFFSET`个字符以及最后`OFFSET`个字符. | `bash 4.2+` |

## `[](#改变大小写)改变大小写`

| 参数 | 它将做什么？ | 版本要求 |
| --- | --- | --- |
| `${VAR^}` | 大写第一个字符. | `bash 4+` |
| `${VAR^^}` | 大写所有字符. | `bash 4+` |
| `${VAR,}` | 小写第一个字符. | `bash 4+` |
| `${VAR,,}` | 小写所有字符. | `bash 4+` |
| `${VAR~}` | 反转第一个字符. | `bash 4+` |
| `${VAR~~}` | 反转所有字符. | `bash 4+` |

## `[](#默认值)默认值`

| 参数 | 它将做什么？ |
| --- | --- |
| `${VAR:-STRING}` | 如果 `VAR` 为空或未设置，使用 `STRING` 作为它的值. |
| `${VAR-STRING}` | 如果 `VAR` 未设置, 使用 `STRING` 作为它的值. |
| `${VAR:=STRING}` | 如果 `VAR` 为空或未设置, 设置 `VAR` 的值为 `STRING`. |
| `${VAR=STRING}` | 如果 `VAR` 未设置, 设置 `VAR` 的值为 `STRING`. |
| `${VAR:+STRING}` | 如果 `VAR` 不为空, 使用 `STRING` 作为它的值. |
| `${VAR+STRING}` | 如果 `VAR` 已设置, 使用 `STRING` 作为它的值. |
| `${VAR:?STRING}` | 如果为空或未设置，则显示一个错误. |
| `${VAR?STRING}` | 如果未设置则显示一个错误. |

# `[](#花括号展开)花括号展开`

## `[](#范围)范围`

```shell
# 符号: {<START>..<END>}

# 打印 1-100 之间的数字.
echo {1..100}

# 打印一个范围内的浮点数.
echo 1.{1..9}

# 打印a-z间的字符.
echo {a..z}
echo {A..Z}

# 嵌套.
echo {A..Z}{0..9}

# 打印用零填充的数字.
# 警告: bash 4+
echo {01..100}

# 更改步长.
# 符号: {<START>..<END>..<INCREMENT>}
# 警告: bash 4+
echo {1..10..2} # 每次增加2.
```

## `[](#字符串列表)字符串列表`

```shell
echo {apples,oranges,pears,grapes}

# 示例用法:
# 删除~/Downloads/目录下的 Movies, Music 和 ISOS 文件夹 .
rm -rf ~/Downloads/{Movies,Music,ISOS}
```

# `[](#条件表达式)条件表达式`

## `[](#文件判断)文件判断`

| 表达式 | 值 | 它有什么作用？ |
| --- | --- | --- |
| `-a` | `file` | 文件存在 |
| `-b` | `file` | 文件存在并且是块特殊文件. |
| `-c` | `file` | 文件存在并且是字符特殊文件. |
| `-d` | `file` | 文件存在且是目录. |
| `-e` | `file` | 文件存在. |
| `-f` | `file` | 文件存在且是常规文件. |
| `-g` | `file` | 文件存在且其set\-group\-id位已设置. |
| `-h` | `file` | 文件存在并且是符号链接. |
| `-k` | `file` | 文件存在且其sticky\-bit已设置 |
| `-p` | `file` | 文件存在并且是命名管道 (*FIFO*). |
| `-r` | `file` | 文件存在且可读. |
| `-s` | `file` | 文件存在且其大小大于零. |
| `-t` | `fd` | 文件描述符是打开的并且引用到一个终端. |
| `-u` | `file` | 文件存在且其set\-user\-id位已设置. |
| `-w` | `file` | 文件存在且可写. |
| `-x` | `file` | 文件存在且可执行. |
| `-G` | `file` | 文件存在且拥有者是一个有效组ID. |
| `-L` | `file` | 文件存在并且是符号链接. |
| `-N` | `file` | 文件存在且自上次读取后已被修改. |
| `-O` | `file` | 文件存在并且拥有者是一个有效用户ID. |
| `-S` | `file` | 文件存在且是套接字. |

## `[](#文件比较)文件比较`

| 表达式 | 它有什么作用？ |
| --- | --- |
| `file -ef file2` | 是否两个文件都引用相同的inode和设备编号. |
| `file -nt file2` | 是否 `file` 比 `file2`更新 (*使用修改时间*) 或者 `file` 存在而 `file2` 不存在. |
| `file -ot file2` | 是否 `file` 比 `file2`更老 (*使用修改时间*) 或者 `file2` 存在而 `file` 不存在. |

## `[](#条件变量)条件变量`

| 表达式 | 值 | 它有什么作用？ |
| --- | --- | --- |
| `-o` | `opt` | 是否启用了shell选项. |
| `-v` | `var` | 是否变量具有指定的值. |
| `-R` | `var` | 是否变量是一个名称引用. |
| `-z` | `var` | 是否字符串的长度为零. |
| `-n` | `var` | 是否字符串的长度不为零. |

## `[](#比较变量)比较变量`

| 表达式 | 它有什么作用？ |
| --- | --- |
| `var = var2` | 等于. |
| `var == var2` | 等于 (*同义词 `=`*). |
| `var != var2` | 不等于. |
| `var < var2` | 小于 (*以ASCII字母顺序排列.*) |
| `var > var2` | 大于 (*以ASCII字母顺序排列.*) |

# `[](#算术运算符)算术运算符`

## `[](#指派)指派`

| 操作符 | 它有什么作用？ |
| --- | --- |
| `=` | 初始化或更改变量的值。 |

## `[](#四则运算)四则运算`

| 操作符 | 它有什么作用？ |
| --- | --- |
| `+` | 加 |
| `-` | 减 |
| `*` | 乘 |
| `/` | 除 |
| `**` | 幂运算 |
| `%` | 求模 |
| `+=` | 先加后赋值 (*`x += y`等同于`x = x + y`*) |
| `-=` | 先减后赋值 (*`x -= y`等同于`x = x - y`*) |
| `*=` | 先乘后赋值 (*`x *= y`等同于`x = x * y`*) |
| `/=` | 先除后赋值 (*`x /= y`等同于`x = x / y`*) |
| `%=` | 先取模后赋值 (*`x %= y`等同于`x = x % y`*) |

## `[](#位运算)位运算`

| 操作符 | 它有什么作用？ |
| --- | --- |
| `<<` | 按位左移 |
| `<<=` | 按位左移后赋值 |
| `>>` | 按位右移 |
| `>>=` | 按位右移后赋值 |
| `&` | 按位与操作 |
| `&=` | 按位与操作后赋值 |
| `|` | 按位或操作 |
| `|=` | 按位或操作赋值 |
| `~` | 按位非操作 |
| `^` | 按位异或操作 |
| `^=` | 按位异或操作后赋值 |

## `[](#逻辑运算)逻辑运算`

| 操作符 | 它有什么作用？ |
| --- | --- |
| `!` | NOT |
| `&&` | AND |
| `||` | OR |

## `[](#复杂运算)复杂运算`

| 操作符 | 它有什么作用？ | 例子 |
| --- | --- | --- |
| `,` | 逗号分隔符 | `((a=1,b=2,c=3))` |

# `[](#算术运算符-1)算术运算符-1`

## `[](#用更简单语法设置变量)用更简单语法设置变量`

```shell
# 简单的数学运算
((var=1+2))

# 递减/递增变量
((var++))
((var--))
((var+=1))
((var-=1))

# 使用变量
((var=var2*arr[2]))
```

## `[](#三元测试)三元测试`

```shell
# 如果var2大于var，则将var的值设置为var2，否则设置为var.
# var: 要设置的变量.
# var2>var: 条件测试.
# ?var2: 如果条件测试成功时生效.
# :var: 条件测试失败时生效.
((var=var2>var?var2:var))
```

# `[](#trap命令)trap命令`

Traps允许脚本在各种信号上执行代码。在 [pxltrm](https://github.com/dylanaraps/pxltrm) (*用bash编写的像素艺术编辑器*) traps 用于在窗口大小调整时重绘用户界面。另一个用例是在脚本退出时清理临时文件。

Traps应该在脚本开头附近添加，以便捕获任何早期错误.

**NOTE:** 有关信号的完整列表，请参阅 `trap -l`.

## `[](#在脚本退出时执行操作)在脚本退出时执行操作`

```shell
# 脚本退出时清除屏幕。
trap 'printf \\e[2J\\e[H\\e[m' EXIT
```

## `[](#忽略终端中断ctrlcsigint)忽略终端中断（CTRL+C，SIGINT）`

```shell
trap '' INT
```

## `[](#对窗口调整大小时做出反应)对窗口调整大小时做出反应`

```shell
# 在窗口调整大小时调用函数.
trap 'code_here' SIGWINCH
```

## `[](#在命令之前执行某些操作)在命令之前执行某些操作`

```shell
trap 'code_here' DEBUG
```

## `[](#在shell函数或源文件完成执行时执行某些操作)在shell函数或源文件完成执行时执行某些操作`

```shell
trap 'code_here' RETURN
```

# `[](#性能)性能`

## `[](#禁用unicode码)禁用Unicode码`

如果不需要unicode，则可以禁用它以提高性能。结果可能会有所不同，但是[neofetch](https://github.com/dylanaraps/neofetch) 和其他程序有明显改善。

```shell
# 禁用 unicode.
LC_ALL=C
LANG=C
```

# `[](#已过时的语法)已过时的语法`

## `[](#释伴声明)释伴声明`

使用 `#!/usr/bin/env bash` 而不是 `#!/bin/bash`.

*   前者搜索用户的 `PATH` 以查找 `bash` 二进制文件.
*   后者假设它始终安装在 `/bin/` 目录，可能导致问题.

```shell
# 正确的方式:

    #!/usr/bin/env bash

# 错误的方式:

    #!/bin/bash
```

## `[](#命令替换)命令替换`

使用 `$()`而不是 `` ` ` ``.

```shell
# 正确的方式.
var="$(command)"

# 错误的方式.
var=`command`

# $() 很容易嵌套，而``不能.
var="$(command "$(command)")"
```

## `[](#声明函数)声明函数`

不要使用`function`关键字，它会降低与旧版本`bash`的兼容性.

```shell
# 正确的方式.
do_something() {
    # ...
}

# 错误的方式.
function do_something() {
    # ...
}
```

# `[](#内部变量)内部变量`

## [](#获取bash二进制文件的位置)获取`bash`二进制文件的位置

```shell
"$BASH"
```

## [](#获取当前运行bash命令的版本)获取当前运行`bash`命令的版本

```shell
# 作为字符串.
"$BASH_VERSION"

# 作为数组.
"${BASH_VERSINFO[@]}"
```

## `[](#打开用户默认的文本编辑器)打开用户默认的文本编辑器`

```shell
"$EDITOR" "$file"

# NOTE: 这个变量可能是空的，设置一个失败调用值.
"${EDITOR:-vi}" "$file"
```

## `[](#获取当前函数的名称)获取当前函数的名称`

```shell
# 当前函数.
"${FUNCNAME[0]}"

# 父函数.
"${FUNCNAME[1]}"

# 等等.
"${FUNCNAME[2]}"
"${FUNCNAME[3]}"

# 包括父类的所有函数
"${FUNCNAME[@]}"
```

## `[](#获取系统的主机名)获取系统的主机名`

```shell
"$HOSTNAME"

# NOTE: 这个变量可能是空的.
# (可选):将失败调用设置为hostname命令
"${HOSTNAME:-$(hostname)}"
```

## `[](#获取操作系统的架构32位或64位)获取操作系统的架构（32位或64位）`

```shell
"$HOSTTYPE"
```

## `[](#获取操作系统内核的名称)获取操作系统/内核的名称`

这可用于条件判断不同的操作系统，而无需调用`uname`。

```shell
"$OSTYPE"
```

## `[](#获取当前的工作目录)获取当前的工作目录`

这是内置`pwd`的替代方案。

```shell
"$PWD"
```

## `[](#获取脚本运行的秒数)获取脚本运行的秒数`

```shell
"$SECONDS"
```

## `[](#获取伪随机整数)获取伪随机整数`

每次使用`$RANDOM`时, 返回`0` and `32767`之间的不同整数。 此变量不应用于与安全性相关的任何内容（包括加密密钥等）。

```shell
"$RANDOM"
```

# `[](#有关终端的信息)有关终端的信息`

## `[](#获取终端的总行列数来自脚本)获取终端的总行列数（*来自脚本*）`

在纯bash中编写脚本和`stty`/`tput`无法调用时，这很方便。

**示例函数:**

```shell
get_term_size() {
    # 用法: get_term_size

    # (:;:) 是一个短暂暂停，以确保变量立即导出
    shopt -s checkwinsize; (:;:)
    printf '%s\n' "$LINES $COLUMNS"
}
```

**示例用法:**

```shell
# 输出: 行数 列数
$ get_term_size
15 55
```

## `[](#获取终端的像素大小)获取终端的像素大小`

**警告**: 这在某些终端仿真器中不起作用。

**示例函数:**

```shell
get_window_size() {
    # 用法: get_window_size
    printf '%b' "${TMUX:+\\ePtmux;\\e}\\e[14t${TMUX:+\\e\\\\}"
    IFS=';t' read -d t -t 0.05 -sra term_size
    printf '%s\n' "${term_size[1]}x${term_size[2]}"
}
```

**示例用法:**

```shell
# 输出: 长度x高度
$ get_window_size
1200x800

# 输出 (失败):
$ get_window_size
x
```

## `[](#获取当前光标位置)获取当前光标位置`

用纯bash创建TUI时，是很有用的。 TUI是指文本用户界面(Text\-based User Interface)，通过文本实现交互窗口展示内容，定位光标和鼠标实现用户交互。

**示例函数:**

```shell
get_cursor_pos() {
    # 用法: get_cursor_pos
    IFS='[;' read -p $'\e[6n' -d R -rs _ y x _
    printf '%s\n' "$x $y"
}
```

**示例用法:**

```shell
# Output: X Y
$ get_cursor_pos
1 8
```

# `[](#转换)转换`

## `[](#将十六进制颜色转换为rgb)将十六进制颜色转换为RGB`

**示例函数:**

```shell
hex_to_rgb() {
    # Usage: hex_to_rgb "#FFFFFF"
    #        hex_to_rgb "000000"
    : "${1/\#}"
    ((r=16#${_:0:2},g=16#${_:2:2},b=16#${_:4:2}))
    printf '%s\n' "$r $g $b"
}
```

**示例用法:**

```shell
$ hex_to_rgb "#FFFFFF"
255 255 255
```

## `[](#将rgb颜色转换为十六进制)将RGB颜色转换为十六进制`

**示例函数:**

```shell
rgb_to_hex() {
    # Usage: rgb_to_hex "r" "g" "b"
    printf '#%02x%02x%02x\n' "$1" "$2" "$3"
}
```

**示例用法:**

```shell
$ rgb_to_hex "255" "255" "255"
#FFFFFF
```

# `[](#代码高尔夫)代码高尔夫`

[CODE GOLF](https://en.wikipedia.org/wiki/Code_golf)，看看谁写的代码最短！

## [](#更短的for循环语法)更短的`for`循环语法

```shell
# Tiny C风格.
for((;i++<10;)){ echo "$i";}

# 未记载的方法.
for i in {1..10};{ echo "$i";}

# 扩展.
for i in {1..10}; do echo "$i"; done

# C语言风格.
for((i=0;i<=10;i++)); do echo "$i"; done
```

## `[](#更短的无限循环)更短的无限循环`

```shell
# 普通方法
while :; do echo hi; done

# 更短的方式
for((;;)){ echo hi;}
```

## `[](#更短的函数声明)更短的函数声明`

```shell
# 普通方法
f(){ echo hi;}

# 用于子shell
f()(echo hi)

# 用于四则运算
# 这可以被用来分配整数值。
# Example: f a=1
#          f a++
f()(($1))

# 用作测试，循环等
# NOTE: ‘while’, ‘until’, ‘case’, ‘(())’, ‘[[]]’ 也可以使用.
f()if true; then echo "$1"; fi
f()for i in "$@"; do echo "$i"; done
```

## [](#更短的if语法)更短的`if`语法

```shell
# 一行
# Note: 当第一段是正确时执行第三段
# Note: 此处利用了逻辑运算符的短路规则
[[ $var == hello ]] && echo hi || echo bye
[[ $var == hello ]] && { echo hi; echo there; } || echo bye

# 多行（没有else，单条语句）
# Note: 退出状态可能与if语句不同
[[ $var == hello ]] &&
    echo hi

# 多行 (没有 else)
[[ $var == hello ]] && {
    echo hi
    # ...
}
```

## [](#用case语句来更简单的设置变量)用`case`语句来更简单的设置变量

内置的`：`可以用来避免在case语句中重复的实用`variable =`。 `$ _`变量存储最后一个命令的最后一个参数。 `：`总会成功，所以它可以用来存储变量值。

```shell
case "$OSTYPE" in
    "darwin"*)
        : "MacOS"
    ;;

    "linux"*)
        : "Linux"
    ;;

    *"bsd"* | "dragonfly" | "bitrig")
        : "BSD"
    ;;

    "cygwin" | "msys" | "win32")
        : "Windows"
    ;;

    *)
        printf '%s\n' "Unknown OS detected, aborting..." >&2
        exit 1
    ;;
esac

# 最后，获取变量值.
os="$_"
```

# `[](#其他)其他`

## [](#使用read作为sleep命令的替代品)使用`read`作为`sleep`命令的替代品

令人惊讶的是，`sleep`是一个外部命令而不是`bash`内置的。

**警告:** 要求`bash`版本 4+

**示例函数:**

```shell
read_sleep() {
    # 用法: sleep 1
    #        sleep 0.2
    read -rt "$1" <> <(:) || :
}
```

**示例用法:**

```shell
read_sleep 1
read_sleep 0.1
read_sleep 30
```

对于性能要求较高的情况下，打开和关闭过多的文件描述符是不实用的，对于`read`的所有调用，文件描述符的分配只能进行一次：:

(请参阅最原始的功能实现 [https://blog.dhampir.no/content/sleeping\-without\-a\-subprocess\-in\-bash\-and\-how\-to\-sleep\-forever](https://blog.dhampir.no/content/sleeping-without-a-subprocess-in-bash-and-how-to-sleep-forever))

```shell
exec {sleep_fd}<> <(:)
while some_quick_test; do
    # equivalent of sleep 0.001
    read -t 0.001 -u $sleep_fd
done
```

## `[](#检查一个命令是否在用户的path中)检查一个命令是否在用户的PATH中`

```shell
# 有3种方法可以使用，任何一种都正确。
type -p executable_name &>/dev/null
hash executable_name &>/dev/null
command -v executable_name &>/dev/null

# 用作检测.
if type -p executable_name &>/dev/null; then
    # Program is in PATH.
fi

# 反向检测.
if ! type -p executable_name &>/dev/null; then
    # Program is not in PATH.
fi

# 示例（如果未安装程序，则提前退出）.
if ! type -p convert &>/dev/null; then
    printf '%s\n' "error: convert is not installed, exiting..."
    exit 1
fi
```

## [](#使用strftime获取当前日期)使用`strftime`获取当前日期

Bash的`printf`有一个内置的获取日期的方法，可用来代替`date`命令。

**警告:** 要求`bash`版本 4+

**示例函数:**

```shell
date() {
    # 用法: date "format"
    # 通过 "man strftime"看格式
		printf "%($1)T\\n" "-1"
}
```

*   了解时间格式: ['man strftime'](http://www.man7.org/linux/man-pages/man3/strftime.3.html) .

**示例用法:**

```shell
# 使用上述函数.
$ date "%a %d %b  - %l:%M %p"
Fri 15 Jun  - 10:00 AM

# 直接使用printf.
$ printf '%(%a %d %b  - %l:%M %p)T\n' "-1"
Fri 15 Jun  - 10:00 AM

# 使用printf分配变量.
$ printf -v date '%(%a %d %b  - %l:%M %p)T\n' '-1'
$ printf '%s\n' "$date"
Fri 15 Jun  - 10:00 AM
```

## `[](#获取当前用户的用户名)获取当前用户的用户名`

**警告:** 要求`bash`版本 4.4+

```shell
$ : \\u
# Expand the parameter as if it were a prompt string.
$ printf '%s\n' "${_@P}"
black
```

## `[](#生成一个v4版本的uuid)生成一个V4版本的UUID`

**警告**: 生成的值不具有加密安全性。

**示例函数:**

```shell
uuid() {
    # 用法: uuid
    C="89ab"

    for ((N=0;N<16;++N)); do
        B="$((RANDOM%256))"

        case "$N" in
            6)  printf '4%x' "$((B%16))" ;;
            8)  printf '%c%x' "${C:$RANDOM%${#C}:1}" "$((B%16))" ;;

            3|5|7|9)
                printf '%02x-' "$B"
            ;;

            *)
                printf '%02x' "$B"
            ;;
        esac
    done

    printf '\n'
}
```

**示例用法:**

```shell
$ uuid
d5b6c731-1310-4c24-9fe3-55d556d44374
```

## `[](#进度条)进度条`

这是一种绘制进度条的简单方法，无需在函数本身中使用for循环。

**示例函数:**

```shell
bar() {
    # 用法: bar 1 10
    #           ^----- 已经完成的百分比 (0-100).
    #             ^--- 字符总长度.
    ((elapsed=$1*$2/100))

    # 创建空格表示的进度条
    printf -v prog  "%${elapsed}s"
    printf -v total "%$(($2-elapsed))s"

    printf '%s\r' "[${prog// /-}${total}]"
}
```

**示例用法:**

```shell
for ((i=0;i<=100;i++)); do
    # 纯粹的暂停动作 (为了本例可以更好的演示).
    (:;:) && (:;:) && (:;:) && (:;:) && (:;:)

    # Print the bar.
    bar "$i" "10"
done

printf '\n'
```

## `[](#获取脚本中的函数列表)获取脚本中的函数列表`

```shell
get_functions() {
    # Usage: get_functions
    IFS=$'\n' read -d "" -ra functions < <(declare -F)
    printf '%s\n' "${functions[@]//declare -f }"
}
```

## `[](#绕过shell别名)绕过shell别名`

```shell
# alias
ls

# command
# shellcheck disable=SC1001
\ls
```

## `[](#绕过shell函数)绕过shell函数`

```shell
# function
ls

# command
command ls
```

*   command命令 调用指定的指令并执行，命令执行时不查询shell函数。command命令只能够执行shell内部的命令。

## `[](#在后台运行命令)在后台运行命令`

这将运行给定命令并使其保持后台运行，即使终端或SSH连接中断后也是如此。但是会忽略所有输出。

```shell
bkr() {
    (nohup "$@" &>/dev/null &)
}

bkr ./some_script.sh
```

# `[](#后记)后记`

感谢各位的阅读，如果对语法有啥疑问或者文章中有错误的地方，请及时告知，谢谢！

Rock on. 🤘