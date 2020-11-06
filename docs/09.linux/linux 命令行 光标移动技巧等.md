---
title: linux 命令行 光标移动技巧等
date: 2020-10-12 12:09:51
permalink: /pages/6612b0/
categories:
  - 技术
  - linux
tags:
  - 
---
看一个真正的专家操作命令行绝对是一种很好的体验\-光标在单词之间来回穿梭，命令行不同的滚动。
在这里强烈建立适应GUI节目的开发者尝试一下在提示符下面工作。
但是事情也不是那么简单，还是需要知道“如何去做”。在单词之间跳转，使用Ctrl+左右键。

Ctrl+a跳到本行的行首，
Ctrl+e则跳到页尾。
Ctrl+u删除当前光标前面的文字
ctrl+k\-删除当前光标后面的文字
Ctrl+w和Alt+d\-对于当前的单词进行删除操作，w删除光标前面的单词的字符，d则删除后面的字符
Alt+Backsapce\-删除当前光标后面的单词，
如果删除错误，使用Ctrl+y进行恢复Ctrl+L进行清屏操作

ctrl+a:光标移到行首。
ctrl+b:光标左移一个字母
ctrl+c:杀死当前进程。
ctrl+d:退出当前 Shell。
ctrl+e:光标移到行尾。
ctrl+h:删除光标前一个字符，同 backspace 键相同。
ctrl+k:清除光标后至行尾的内容。
ctrl+l:清屏，相当于clear。
ctrl+r:搜索之前打过的命令。会有一个提示，根据你输入的关键字进行搜索bash的history
ctrl+u: 清除光标前至行首间的所有内容。
ctrl+w: 移除光标前的一个单词
ctrl+t: 交换光标位置前的两个字符
ctrl+y: 粘贴或者恢复上次的删除
ctrl+d: 删除光标所在字母;注意和backspace以及ctrl+h的区别，这2个是删除光标前的字符
ctrl+f: 光标右移
ctrl+z : 把当前进程转到后台运行，使用’ fg ‘命令恢复。比如top \-d1 然后ctrl+z ，到后台，然后fg,重新恢复
esc组合
esc+d: 删除光标后的一个词
esc+f: 往右跳一个词
esc+b: 往左跳一个词
esc+t: 交换光标位置前的两个单词。

Ctrl组合

跳转操作

单词间跳转：Alt+左/右键

光标左移一个字符：Ctrl+b

光标右移一个字符：Ctrl+f

跳转到行首：Ctrl+a

跳转到行尾：Ctrl+e

删除操作

删除光标前文字：Ctrl+u

删除光标后文字：Ctrl+k

删除光标前字：Ctrl+w

删除光标所在字符：Ctrl+d

删除光标前一个字符：Ctrl+h

其他操作

撤销操作：Ctrl+y

退出当前shell进程：Ctrl+d

清屏：Ctrl+l

搜索之前命令：Ctrl+r

交换光标前两个字符：Ctrl+t

esc组合

删除光标后一个字：esc+d

光标右移一个字：esc+f

光标左移一个字：esc+b

交换光标前两个字符：Ctrl+t