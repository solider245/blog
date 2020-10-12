---
title: Vim 入门教程 & 指南
date: 2020-10-12 12:09:51
permalink: /pages/e08149/
categories:
  - linux
  - vim
tags:
  - 
---
文章目录 \[[隐藏](#)\]

- [说在前面](#说在前面)
- [有用的链接](#有用的链接)
- [Vim 的模式编辑](#vim-的模式编辑)
- [Vim 原生按键功能说明](#vim-原生按键功能说明)
  - [一般命令模式](#一般命令模式)
  - [切换到编辑模式](#切换到编辑模式)
  - [切换到命令行模式](#切换到命令行模式)
- [Vim 的配置文件 ~/.vimrc](#vim-的配置文件-vimrc)
  - [设置选项](#设置选项)
    - [布尔选项](#布尔选项)
    - [键值选项](#键值选项)
  - [打印信息和注释](#打印信息和注释)
  - [Mapping 按键映射](#mapping-按键映射)
  - [Leaders 映射前缀键](#leaders-映射前缀键)
  - [自定义命令 command](#自定义命令-command)
    - [参数处理](#参数处理)
    - [补全行为](#补全行为)
      - [自定义补全](#自定义补全)
    - [范围处理](#范围处理)
    - [特殊情况](#特殊情况)
  - [自动命令 autocmd](#自动命令-autocmd)
    - [自动命令的语法结构](#自动命令的语法结构)
    - [自动命令组 augroup](#自动命令组-augroup)
  - [折叠](#折叠)
    - [手动折叠（set foldmethod=manual）](#手动折叠set-foldmethodmanual)
    - [indent 依缩进折叠（set foldmethod=indent）](#indent依缩进折叠set-foldmethodindent)
    - [依标志折叠（set foldmethod=marker）](#依标志折叠set-foldmethodmarker)
- [Vimscript 基础语法](#vimscript-基础语法)
  - [变量](#变量)
  - [变量作用域](#变量作用域)
  - [条件选择与比较](#条件选择与比较)
  - [运算符优先级](#运算符优先级)
  - [循环](#循环)
    - [For 循环](#for-循环)
      - [固定循环次数](#固定循环次数)
    - [While 循环](#while-循环)
    - [循环控制 break 和 continue](#循环控制-break-和-continue)
  - [函数](#函数)
    - [可变参数](#可变参数)
    - [函数的调用](#函数的调用)
    - [函数的附加属性](#函数的附加属性)
  - [匿名函数表达式 lambda](#匿名函数表达式-lambda)
  - [常用内建函数](#常用内建函数)
    - [字符串处理函数（utf\-8 编码）](#字符串处理函数utf-8-编码)
    - [列表或字典处理函数](#列表或字典处理函数)
    - [浮点数运算和逻辑运算](#浮点数运算和逻辑运算)
    - [文件和目录相关函数](#文件和目录相关函数)
    - [系统命令和时间函数](#系统命令和时间函数)
  - [Execute 命令](#execute-命令)
  - [Normal 命令](#normal-命令)
    - [Execute 与 Normal联用](#execute-与-normal联用)
  - [正则表达式](#正则表达式)
    - [匹配量词](#匹配量词)
    - [常用的元字符](#常用的元字符)
- [编译 Vim8](#编译-vim8)
- [说在最后](#说在最后)

# 说在前面

第一次接触到 Vim 还是在 2017 年暑假学习 Linux 的时候，当时我是阅读[《鸟哥的 Linux 私房菜》](http://linux.vbird.org/)并在 [VirtualBox](https://www.virtualbox.org/wiki/Downloads) 虚拟机里安装了个 CentOS 7 来进行 Linux 学习的。不得不说《鸟哥的 Linux 私房菜》里的“废话”真的多，不过这符合“私房菜”这个书名，极具个人特色。我看的 PDF 有 1158 页，阅读和练习我花了一年的时间。 ![:-o](https://starrycat.me/wp-content/plugins/WP-Alu2Button/static/img/icon_surprised.gif) 如果你想快速学习 Linux，十分不推荐（不如上个 [ArchLinux](https://wiki.archlinux.org/index.php/Installation_guide_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))，Arch 邪教徒如是说）。话题回到 Vim 上来，鸟哥书里关于 Vim 的介绍还是比较详细的，具体在第九章：[vim 程序编辑器](http://linux.vbird.org/linux_basic/0310vi.php)。在所有的 Linux 发行版中都会有一个文本编辑器 Vi(m)，Vim 是 Vi 进阶版。在一年的 Linux 学习中，基本上都是在终端 tty 上进行的，基本模拟了使用 Linux 服务器的情况——没有图形界面，只有黑乎乎的窗口！！在这种情况下编辑代码文件，Vim 几乎是你唯一的选择，当然 Linux 上还有其他类似工具，如 nano，Emacs 等。说是唯一是因为几乎所有的发行版都预装 Vi(m)，许多软件默认调用 Vi(m)编辑，而对 Linux 初学者来说搜索到的资料几乎都是使用 Vi(m) 编辑文件。我就是这样入了 Vim 的坑。 ![:-D](https://starrycat.me/wp-content/plugins/WP-Alu2Button/static/img/icon_biggrin.gif)

在一年的 Linux 学习中，使用到 Vim 编辑文件的情况也不多，而且大多是简单的编辑，所以一年下来，我用 Vim 也仅仅是会按 i 输入，按 <Esc> 键切回 NORMAL 模式，按 nG 跳转第 n 行，使用 /? 查找字符，dd 删除一行，yy 复制一行，p 粘贴，:wq 保存退出。 ![:oops:](https://starrycat.me/wp-content/plugins/WP-Alu2Button/static/img/icon_redface.gif) 直到 2018 年暑假学习完 Linux 基础后才回顾并开始认真的学习 Vim，之前在 Win下常用 [Notepad++](https://notepad-plus-plus.org/download/)，真切的感觉到熟练掌握一种编辑器对于效率能有意想不到的提高。在这重新学习使用 Vim 的半年里，碰到不少关于 Vim 学习资料，对于 Vim 也不像当初的那样仅有模糊的概念了，而本文将分享总结自己的 Vim 学习经历，希望对 Vim 初学者能有帮助。 ![8-)](https://starrycat.me/wp-content/plugins/WP-Alu2Button/static/img/icon_cool.gif)

文章十分长，阅读过程中请善用右下角的小菜单打开文章目录。

# 有用的链接

| 链接 | 说明 |
| --- | --- |
| [《鸟哥的 Linux 私房菜》之《vim 程序编辑器》](http://linux.vbird.org/linux_basic/0310vi.php) | 很不错 Vim 的简介，Vim 的模式输入，常用的按键说明和配置说明。 |
| 帮助文档 `:help` ，中文版（2017年7月的翻译）：[在线](http://vimcdoc.sourceforge.net/doc/help.html) [下载](https://github.com/yianwillis/vimcdoc/releases) | 善用 :help 查看官方文档，英文不好可查看在线中文版或下载。解压：`tar zxvf vimcdoc-<version>.tar.gz` 后，`cd` 进解压目录 `vimcdoc-`，执行 `./vimcdoc.sh -i` 安装即可。这样你的 :help 就变为中文了，翻译虽然是两年前的了，不过对于基础学习影响不大。 |
| [Vim 从入门到精通](https://github.com/wsdjeg/vim-galore-zh_cn) | GitHub 上 Vim 社区的入门教程，中文版。 |
| [笨方法学 Vimscript](http://learnvimscriptthehardway.onefloweroneworld.com/) [英文原版](http://learnvimscriptthehardway.stevelosh.com/) | 使用 `Vimscript` 自定义配置 Vim。 |
| [VimL 语言编程指北路](https://github.com/lymslive/vimllearn) | 侧重于 `VimL` （即 Vimscript）脚本语言编程。 |
| [VimAwesome](https://vimawesome.com/) | Vim 插件集合网站。 |
| [Vim Colors](http://vimcolors.com/) | Vim 主题配色集合预览。 |
| [Vivify](https://bytefluent.com/vivify/) | 在线自定义主题配色。 |
| [Vimcn](https://vimcn.org/) [Vim China](https://vim-china.org/) | Vim 中文论坛 |
| [Vim 知乎话题](https://www.zhihu.com/topic#Vim) | Vim 知乎话题。 |
| [Telegram@VimHub](https://t.me/VimHub) | Telegram 上的 Vim 中文用户交流群。 |

# Vim 的模式编辑

Vim 的一大特色，采用了模式编辑的概念，一般分为三种模式：

*   一般命令模式（command\-mode）：默认打开 vim 就会进入这个模式，也简称为一般模式，可以“上下左右”移动光标浏览文件，可以删除字符及删除整行，也可以复制、粘贴整行。按下  `v`、`V`、`Ctrl+V` 可进入可视化模式反白选择字符或行或块。
*   编辑模式（insert\-mode）：按下 `i`、`I`、`o`、`O`、`a`、`A`、`r`、`R` 中任一字母就可进入编辑模式，可以添加、修改文件内容，此时 vim 窗口左下方会出现 `-- INSERT --` 或者 `-- REPLACE --` 表示可以编辑。
*   命令行命令模式（command\-line\-mode）：在一般命令模式中，按下 `:`、`/`、`?` 中任一字符，光标就会移动到最底下那一行。在此模式中，可以执行 vim 命令，如读取、存储文件、搜索文件、替换字符、退出 vim、设置 vim 选项等等。

以上三种模式的作用及切换可用下图表示：

![https://starrycat.me/wp-content/uploads/2019/02/10001.png](https://starrycat.me/wp-content/uploads/2019/02/10001.png "Vim 入门教程 & 指南")

# Vim 原生按键功能说明

Vim 另一大特色就是拥有着强大快捷键编辑功能，而且还可以自定义，让你的编辑摆脱鼠标的束缚。熟练的掌握 vim 的快捷键编辑，能够让你的编辑效率大大提高。下面让我们先来看看常用的 vim 原生按键各自的作用吧！ ![:idea:](https://starrycat.me/wp-content/plugins/WP-Alu2Button/static/img/icon_idea.gif)

## 一般命令模式

一般模式下的按键说明，包括光标移动、复制粘贴、搜索替换等。

| 移动光标 |
| `h` 或向左方向键(←) | 光标向左移动一个字符 |
| `j` 或向下方向键(↓) | 光标向下移动一个字符 |
| `k` 或向上方向键(↑) | 光标向上移动一个字符 |
| `l` 或向右方向键(→) | 光标向右移动一个字符 |
| 如果你将右手放在主键盘上的话，你会发现 `hjkl` 是排列在一起的，因此可以使用这四个按键来快速移动光标，这样你的手就可以不离开主键盘区域进行编辑了。 | 如果想要进行多次移动的话，例如向下移动 30 行，可以使用 30j 或 30↓ 的组合按键，即加上想要进行的次数（数字）后，按下动作即可！ |
| Ctrl+F | 屏幕向下移动一页，相当于 <PageDown> 按键 |
| Ctrl+B | 屏幕向上移动一页，相当于 <PageUp> 按键 |
| n<Space> | n 表示数字，例如 20。按下数字后再按空格键，光标会向右移动这一行的 n 个字符。例如 20 则光标会向后面移动 20 个字符距离。 |
| `0` 或 <Home> | 这是数字 0：移动到这一行的最前面字符 |
| `$` 或 <End> | 移动到这一行的最后面字符 |
| `G` | 移动到文件的最后一行 |
| `nG` | n 为数字。移动到文件的第 n 行。例如 20G 则会移动到文件的第 20 行。（可配合 `:set number` 显示行号） |
| `gg` | 移动到文件的第一行，相当于 1G 啊！ |
| n<Enter> | n 为数字。游标向下移动 n 行 |
| 搜索与替换 |
| `/`word | 向光标之下搜索一个名称为 word 的字符。例如要在文件内搜索 starry 这个字符，就输入 /starry 即可！ |
| `?`word | 向光标之上搜索一个名称为 word 的字符。 |
| `n` | 这个 n 是英文按键。代表重复前一个搜索动作。举例来说，如果刚刚我们执行 /starry 去向下搜索 starry 这个字符，则按下 n 后，会向下继续搜索下一个名称为 starry 的字符。如果是执行 ?starry 的话，那么按下 n 则会向上继续搜索名称为 starry 的字符！ |
| `N` | 这个 N 是英文按键。与 n 刚好相反，为反向进行前一个搜索动作。例如 /starry 后，按下 N 则表示向上搜索 starry。 |
| 使用 /word 配合 n 及 N 是非常有帮助的！可以让你重复的找到一些你搜索的关键字！ |
| :n1,n2`s`/word1/word2/`g` | n1 与 n2 为数字，在第 n1 与第 n2 行之间搜索 word1 这个字符，并将该字符替换为 word2！举例来说，在第 100 到第 200 行之间搜索 starry 并替换为 STARRY，则：:100,200s/starry/STARRY/g |
| :`1,$`s/word1/word2/g | 从第一行到最后一行搜索 word1 字符，并将该字符替换为 word2！ |
| :1,$s/word1/word2/`gc` | 从第一行到最后一行搜索 word1 字符，并将该字符替换为 word2！且在替换前显示提示字符给使用者确认（confirm）是否需要替换！ |
| 请注意！以上搜索替换方法针对的是字符！！ | 例如： starrycat 将会替换为 STARRYcat。如果要精确替换 starry 这个单词字符，请使用 vim 正则表达式，如 `\<` 匹配单词开头，`\>` 匹配单词结尾。\\<starry\\> 将匹配单词字符 starry，而不会匹配到 starrycat。另外Starry是否被替换为STARRY受选项 &ignorecase 影响，即是否忽略大小写。或者使用 `\c` 或 `\C` 强制指定，如\\<starry\\>\\C 将匹配单词字符 starry，而不会匹配到 Starry。 |
| 删除、复制与粘贴 |
| x,X | 在一行字当中，x 为向后删除一个字符（相当于 <Del> 按键），X 为向前删除一个字符（相当于 <BS> 亦即是退格键）。 |
| `dd` | 删除光标所在的那一整行 |
| ndd | n 为数字。删除光标所在的向下 n 行，例如 20dd 则是删除 20 行 |
| d1G | 删除光标所在行到第一行的所有内容 |
| dG | 删除光标所在行到最后一行的所有内容 |
| `yy` | 复制光标所在的那一行 |
| nyy | n 为数字。复制光标所在的向下 n 行，例如 20yy 则是复制 20 行 |
| y1G | 复制光标所在行到第一行的所有内容 |
| yG | 复制光标所在行到最后一行的所有内容 |
| `p`,`P` | p 为将已复制的内容在光标下一行粘贴上，P 则为贴在光标上一行！举例来说，我目前光标在第 20 行，且已经复制了 10 行内容。则按下 p 后，那 10 行内容会贴在原本的 20 行之后，亦即由第 21 行开始粘贴。但如果是按下 P 呢？那么原本的第 20 行会被推到变成第 30 行。 |
| `u` | 撤销前一次操作 |
| `Ctrl+R` | 重做前一次被撤销操作 |
| `.` | 不要怀疑！这就是小数点！意思是重复前一次操作的意思。如果你想要重复删除、重复粘贴等等动作，按下小数点 . 就好了！ |

## 切换到编辑模式

| 进入插入或取代的编辑模式 |
| i,I | 进入插入模式（Insert mode） | i 为从目前光标所在处插入，I 为在目前所在行的第一个非空白字符处开始插入。 |
| a,A | 进入插入模式（Insert mode） | a 为从目前光标所在的下一个字符处开始插入，A 为从光标所在行的最后一个字符处开始插入。 |
| o,O | 进入插入模式（Insert mode） | 这是英文字母 o 的大小写。o 为在目前行所在的下一行处插入新的一行；O 为在目前光标所在处的上一行插入新的一行！ |
| r,R | 进入取代模式（Replace mode） | r 只会取代光标所在的那一个字符一次；R 会一直取代光标所在的字符，直到按下 <Esc> 为止。 |
| Vim 窗口的下方有什么？ | 按下上面这些按键，在 vim 窗口的左下方处会出现 — INSERT — 或 — REPLACE — 的字样。由名称就知道该操作了吧！！ | 特别注意的是，我们上面也提过了，你想要在文件里面输入字符时，一定要在左下方处看到 INSERT 或 REPLACE 才能输入喔！ |
| `<Esc>` | 退出编辑模式，回到一般命令模式中。 |

## 切换到命令行模式

| 命令行模式的储存、离开等命令 |
| `:w` | 将编辑的内容写入硬盘中。 |
| :w`!` | 若文件属性为只读时，强制写入该文件。不过，到底能不能写入，还是跟你对该文件的文件权限有关啊！ |
| `:q` | 离开vim |
| :q`!` | 若修改过文件，又不想储存，使用 ! 为强制离开不储存文件。 |
| 注意一下啊，那个惊叹号（`!`）在 vim 当中，常常具有强制的意思~ |
| `:wq` | 储存后离开，若为 :wq`!` 则为强制储存后离开。 |
| `ZZ` | 这是大写的 Z 喔！若文件没有改动，则不储存离开，若文件已经被改动过，则储存后离开！ |
| `:w filename` | 将编辑的内容储存成另一个文件。（类似另存为） |
| `:r filename` | 在编辑的内容中，读入另一个文件的内容。亦即将 filename 这个文件内容加到光标所在行后面。 |
| :n1,n2 w filename | 将 n1 行到 n2 行的内容储存成 filename 这个文件。 |
| 多文件编辑 |
| `:n` | 编辑下一个文件 |
| `:N` | 编辑下一个文件 |

希望初学者不要被上面的按键表吓跑了，我在这里列下来只是为了以后查找方便，另外，鸟哥列出来的更多。其实我在学习 Linux 基础的一年里，记得住的 vim 按键不超过十个，只要你开始让 vim 成为你的首选编辑器，很快就能掌握常用的按键了。

# Vim 的配置文件 ~/.vimrc

Vim 的系统全局配置文件为 `/etc/vimrc`，用户的配置文件为 `~/.vimrc`。我们常常修改的是 ~/.vimrc文件，因为有时候我们并不想自己的设置影响到整个系统。如果没有 ~/.vimrc 这个文件，你可以手动创建它。~/vimrc 里包含着 Vimscript 代码，每次启动 vim 时，vim 都会自动执行其中的代码。下面我们将会使用 ~/.vimrc 自定义配置我们的 vim，接下来我们将会学习到 vim 的脚本语言 Vimscript，做好准备了嘛  ![:mrgreen:](https://starrycat.me/wp-content/plugins/WP-Alu2Button/static/img/icon_mrgreen.gif)

## 设置选项

作为一个号称高度自定义的文本编辑器，自然少不了丰富的设置选项，仅仅是默认 vim（不含配置文件和插件）就有着庞大的选项集，可以方便地自定义你的 vim。我自己接触 vim 也才两年，而vim 可是个27年老家伙，我也仅仅了解一小部分选项。Vim 主要有两种选项：布尔选项（值为 `on` 或 `off`）和键值选项。设置选项使用 `set` 命令。

### 布尔选项

执行以下命令：

:set number

|

1

 |

:set  number

 |

观察窗口左侧，你现在可以看到行号了，再执行命令：

:set nonumber

|

1

 |

:set  nonumber

 |

行号消失了。可见 `number` 是一个布尔选项：可以 off、可以 on，由选项前是否有 `no` 决定。

### 键值选项

顾名思义，选项有一个或多个键值，选项值可以是数字或字符串，多个值使用英文逗号 `,` 分开。设置命令形如 :set option=val1,val2。此外还支持 `+=` 增量与 `-=` 减量语法，如 :set option+=val3 或 :set option\-=val2，表示在原来的“值集合”的基础上增加某个值或移除某个值。

尝试改变主题暗与亮：

:set background=dark :set background=light

|

1

2

 |

:set  background\=dark

:set  background\=light

 |

在选项名前面加个 `&` 符号，就将一个选项变成了相应的选项值变量（用 `let` 命令定义）：

:set option=value :let &option = value

|

1

2

 |

:set  option\=value

:let  &option  \=  value

 |

以上两条命令是等效的。查看某个选项的当前值（使用 `?`）：

:set option?

|

1

 |

:set  option?

 |

命令 set 设置的是全局选项，你可以加入 ~/.vimrc 配置文件。设置局部选项可以使用 `setlocal` 命令，局部选项只影响当前缓冲文件或窗口（`buffer`/`window`），可以与全局不同。不过并不是所有选项都有局部值意义，在每个选项的帮助文档中，会指明该选项是全局的或局部的。更多关于选项的说明请使用 :help `options`查看。

## 打印信息和注释

使用 `echo` 或 `echom` 可以打印信息：

:echo 'Hello, World!' Hello, World! :echom 'Hello, Vim!' Hello, Vim!

|

1

2

3

4

 |

:echo  'Hello, World!'

Hello,  World!

:echom  'Hello, Vim!'

Hello,  Vim!

 |

两个的区别在于使用 echom 打印的信息会保留下来，使用 `:messages` 命令可以查看：

:messages Hello, Vim!

|

1

2

 |

:messages

Hello,  Vim!

 |

添加 `"` 字符来注释：

" Line numbers on 显示行号 set number

|

1

2

 |

" Line numbers on 显示行号

set  number

 |

## Mapping 按键映射

按键映射可以让你自定义属于你自己的快捷键，按键映射有着模式映射的概念，你可以在不同的模式中定义不同的映射，而且他们不会冲突。映射可又分为递归映射 `*map` 和非递归映射 `*noremap`，为了避免未来设置的按键映射出现由递归导致失效问题，在此只讲非递归映射，如果想深究的童鞋可以看 [笨方法学 Vimscript – 精确映射](http://learnvimscriptthehardway.onefloweroneworld.com/chapters/05.html), 下面我们来学习按键映射。

首先，看一下按键映射的基本结构：

" 映射模式 映射键 被映射键 :\[\*\]noremap {lhs} {rhs}

|

1

2

 |

" 映射模式  映射键 被映射键

:\[\*\]noremap  { lhs}  {rhs}

 |

结构还挺简单的嘛，让我们打开 vim 来试试，随意在文本中敲写几行文字，然后运行命令：

:noremap \- dd

|

1

 |

:noremap  \-  dd

 |

然后尝试按下 `-`，发现了什么？没错，光标所在行被删除了，就好像执行了 `dd` 命令一样，\- 被映射为 dd。

对于一些特殊键，映射时需要注意（:help `key-notation`）：

| 特殊键 | 映射时的表示 |
| --- | --- |
| Ctrl 键 | `<C-...>`<C\-d> 表示 Ctrl+D |
| Shift 键 | `<S-...>` 对于大写字母直接使用即可，无需使用 Shift 键 |
| Alt 键或 Meta 键 | `<A-...>`, `<M-...>` |
| 空格键 | `<Space>` |
| 制表键 | <Tab> |
| 回车键 | `<CR>` |
| Esc 键 | `<Esc>` |
| 退格键 | <BS> |
| 删除键 | <Del> |
| 插入键 | <Insert> |
| 反斜杠 \\ | <Bslash> |
| 竖线 | | `<Bar>` 或 \\| 或 ^V|（这里 ^V 表示 CTRL+V；要输入一个 CTRL+V 你必须按键两次；在这里不能使用 <> 记法 <C\-v>） |
| 方向键 | <Up> <Down> <Left> <Right> |
| 功能键 | `<F1> - <F12>` |
| 特殊关键字 |
| 特定脚本 ID（特殊键码<SNR>，后跟一个特定脚本唯一的数字编号，和一个下划线） | `<SID>` |
| 特定插件（无法用键盘输入的特殊代码） | `<Plug>` |

映射 Ctrl+D 为 dd 命令，执行：

:noremap <C\-d> dd

|

1

 |

:noremap  <C\-d \>  dd

 |

按下 Ctrl+D 就执行了 dd 命令。使用 `unmap` 取消映射：

:unmap <C\-d>

|

1

 |

:unmap  <C\-d \>

 |

如果确定使用某种映射，你可以加入 ~/.vimrc，这样每次打开 vim 都能使用那个映射了。不过不推荐映射 vim 原生的按键，比如上面那几个表格里的，除非原生按键很长，因为当你使用默认无配置 vim，你或许会忘了原生按键。 ![:cry:](https://starrycat.me/wp-content/plugins/WP-Alu2Button/static/img/icon_cry.gif) 而按键映射更多使用在未来你使用插件的时候，或者你自定义的一些函数或命令，可以简化使用。使用 :help `mapping` 查看非递归映射 \*noremap 系列有哪些 mapping 和他们使用在哪些模式。

## Leaders 映射前缀键

Vim 可以映射多个按键，执行下列命令。

:nnoremap \-d dd :nnoremap \-c ddO

|

1

2

 |

:nnoremap  \-d  dd

:nnoremap  \-c  ddO

 |

Normal 模式下快速敲入 `-d` 或 `-c` 查看效果。第一个映射作用是删除一行，第二个是删除一行并进入 insert 模式。

这就意味着你可以用一个你不常用的按键（如 `-` ）作为“前缀”，后接其它字符作为一个整体进行映射。加入那么一个“前缀”可以尽量避免与原生按键的冲突，形成自己一套按键映射，而且你可以方便的更换它，也便于他人使用你的按键映射配置，还有许多插件会使用 `<Leader>` 键配置快捷键。默认的 <Leader> 键为 `\`，可以设置为 `-`：

:let mapleader='\-'

|

1

 |

:let mapleader\='\-'

 |

还有其他很少用到的按键可以设置为 <Leader> 键，如 `,`（我正在用的）、`;`、`<Space>` 等等。然后前面的映射可以改为：

:nnoremap <Leader>d dd :nnoremap <Leader>c ddO

|

1

2

 |

:nnoremap  <Leader\>d dd

:nnoremap  <Leader\>c ddO

 |

试试按下你的 <Leader> 键和 d，这么做会删除一行。另外 vim 还有一个“前缀”键为 `<LocalLeader>`，这个是专门用在特定类型的文件的 <Leader> 键，默认也是 `\`，更多用在插件开发中。

## 自定义命令 command

Vim 允许你通过 `command` 命令创建自定义命令，你可以像运行其他命令行命令一样运行你自定义的命令。定义命令与定义映射很相似，不过定义命令还有一个可选的命令属性 {attr}：

:command\[!\] \[{attr}...\] {cmd} {rep}

|

1

 |

:command\[!\]  \[ {attr}...\]  {cmd}  {rep}

 |

其中 `!` 表示强制重新定义命令，忽略与之前自定义的同名命令的冲突报错。{cmd} 为你自定义命令的名字，必须以大写字母开始，但不能用 `:X` `:Next` 和 `:Print`，因为这是 vim 的内置命令，还有不能使用下划线 `_`。一个简单的例子：

:command! \-bang Q q<bang>

|

1

 |

:command!  \-bang  Q  q<bang\>

 |

其中 `-bang`，`<bang>` 表示这个命令可以使用强制修饰符 `!`，所以这个自定义命令让我们即使使用了 Q 也能退出 vim，使用 Q! 强制退出 vim。如果要默认使用 Q 强制退出 vim，记得要把 `<bang>` 改为 `!`，要不然会没有效果。

命令属性可分四大类: 参数处理、补全行为、范围处理和特殊情况。

### 参数处理

缺省时，用户自定义命令不接受参数 （如果使用了任何参数会报错）。但通过使用 `-nargs` 属性可以允许命令接受参数，有效的值为:

*   \-nargs=`0`     不接受有参数 （缺省情况）
*   \-nargs=`1`     仅接受一个参数，空格也行
*   \-nargs=`*`     接受 0 个或更多的参数 ，以空格分隔
*   \-nargs=`?`     接受 0 个或 1 个参数
*   \-nargs=`+`    接受 1 个或更多的参数 ，以空格分隔

一个参数如果有空格，可以用反斜杠 `\` 转义。

### 补全行为

命令行中，不仅命令名可以补全，命令参数也可以补全。`-complete` 属性指定命令根据什么来补全参数，其取值范围非常广，这里仅介绍几种主要的补全行为，全部列表请参考 :help `command-complete`。

*   \-complete=environment     环境变量名
*   \-complete=`file`                  文件和目录名，类似 :edit命令按 <Tab> 后会补全文件名
*   \-complete=filetype              文件类型名
*   \-complete=function            函数名
*   \-complete=help                  帮助主题
*   \-complete=option               选项
*   \-complete=`shellcmd`        外部 shell 命令
*   \-complete=tag                    标签，类似 :tag 所需的参数

#### 自定义补全

自定义一个全部列表之外补全

*keyboard\_arrow\_down*

如果你自定义的某个命令实现比较复杂的功能 ，参照全部列表后，依然找不到你想要的补全行为，你可以指定一个函数来实现补全（:help `command-completion-custom`）：

*   \-complete=`custom,{func}`
*   \-complete=`customlist,{func}`

其中 {func} 为你指定的函数名，该函数有三个参数：

*   ArgLead                当前自动补全的部分参数前缀
*   CmdLine               完整的命令行
*   CursorPos             当前光标在命令行的位置 （字节位置，从 1 开始）

当用户按下补全键（一般是 `<Tab>` ），vim 会自动将这三个参数传给自定义补全函数。用户在这个函数的实现中可利用这三个参数所提供的信息（也许不一定要用到全部），返回合适的候选补全项：

*   对于 `custom` 参数，函数应该返回字符串，每行一个候选补全项，用换行符分隔。在函数返回时 vim 将用它的正则表达式引擎来进行过滤，这种方式在大多数情况下效率更高。
*   对于 `customlist` 参数，函数应该返回 vim 列表形式的候选补全项，忽略列表里的非字符串项目。但 vim 不会过滤返回的补全候选，用户提供的函数应该自己过滤候选。

### 范围处理

缺省时，用户定义的命令不接受一个行号范围（在命令前加 `n,m`），但使用 `-range` 属性可以使命令接受一个范围 ：

*   `-range`             允许使用范围，缺省为当前行
*   \-range=`%`        允许使用范围，缺省是整个文件 ，即 `1,$`
*   \-range=N           :help `command-range`
*   \-count=N           :help `command-count`

特殊地址 `.` `$` `%` 所表示的范围（在允许 \-range 时）：

*   \-addr=`lines`                      行的范围 （这是缺省），即 `.` 当前行，`*` 末行，`%` 当前 buffer 即整个文件
*   \-addr=arguments               参数的范围
*   \-addr=`buffers`                  缓冲区的范围 （也包括未载入的缓冲区）
*   \-addr=`loaded_buffers`     载入缓冲区的范围
*   \-addr=windows                  窗口的范围
*   \-addr=tabs                         标签页的范围

### 特殊情况

有如下特殊情况：

*   `-bang`                   该命令可以使用一个 `!` 修饰符（和 :q 或 :w 类似）
*   `-bar`                      该自定义命令后面允许用 `|` 分隔，接续另一个命令。那么命令参数中就不允许有 | 。后接一个 `"` 即可以注释。
*   \-register                  该命令的第一个参数可以是一个可选的寄存器名（和 :del，:put，:yank 类似）
*   \-buffer                     该命令仅在当前缓冲区里有效

## 自动命令 autocmd

自动命令可以让 vim 自动执行某些指定的命令，这些指定的命令会在某些事件发生的时候执行。

### 自动命令的语法结构

自动命令用 `autocmd` 定义，至少包含三个部分：

:autocmd {event} {pat} {cmd} ^ ^ ^ | | | | | 事件发生且满足条件时要执行的命令 | | | 用于事件过滤的模式（pattern），一般指是否匹配当前文件 | 多个模式用英文逗号分开 :help autocmd\-patterns | 要监听的事件，比如读写文件，切换窗口等 多个事件用英文逗号分开 :help autocmd\-events

|

1

2

3

4

5

6

7

8

9

10

 |

:autocmd  {event}  {pat}  {cmd}

^^  ^

||  |

||  事件发生且满足条件时要执行的命令

||

|用于事件过滤的模式（pattern），一般指是否匹配当前文件

|多个模式用英文逗号分开  :help autocmd\-patterns

|

要监听的事件，比如读写文件，切换窗口等

多个事件用英文逗号分开  :help autocmd \-events

 |

一个应用的例子，根据文件类型执行某些设定：

:autocmd FileType yml setlocal expandtab shiftwidth=2 softtabstop=2

|

1

 |

:autocmd FileType yml setlocal expandtab shiftwidth\=2  softtabstop\=2

 |

此外，vim 在运行时会很有很多事件发生，每个事件可能执行着许多命令，自动命令会按照定义时的顺序执行。通过 `:au` 就可以查看它们的执行顺序，你会发现列表意外的长，自动命令在 vim 中十分重要，文件类型检测与语法高亮着色，就是通过自动命令实现的。当你安装一些复杂插件，可能会自动执行更多的命令。

### 自动命令组 augroup

因为 autocmd 定义自动命令时是将其添加到相应事件自动命令列表末尾的，所以如果在 ~/.vimrc 中定义了自动命令，每次你重新加载你的 ~/.vimrc，自动命令列表出现会重复命令并会重复执行。你的 ~/.vimrc 再加上插件就会有很多自动命令，这样会影响 vim 的速度，而且有些自动命令在第二次执行将会有可能引发错误。为了解决这个问题，vim 提出了自动命令组 `augroup` 的概念。其实在定义自动命令还有一个可选部分 \[group\]，就是自动命令组的组名，需要避免和事件名重名。如果指定了组名，自动命令就会添加到这个自动命令组中。你可以认为每个组都为不同事件维护了不同的自动命令列表，同一事件在不同组内关联着各自不同的命令列表。当自动命令缺省组名部分，就会添加到当前组（由 `augroup` {name} 指定，默认的 {name} 为 `END`）。

Vim 脚本中自动命令定义的一般规范是：

augroup Group\_Name " 指定当前组名 autocmd! " 删除该组内原来所有旧的自动命令 autocmd {event} {pat} {cmd} " 重新定义新的自动命令，可以有多行 autocmd autocmd {event} {pat} {cmd} " 类似的自动命令建议放在同一个组中 augroup END " 最后用 END 选回默认当前组名

|

1

2

3

4

5

 |

augroup  Group\_Name                " 指定当前组名

autocmd!                      " 删除该组内原来所有旧的自动命令

autocmd  {event} {pat}  {cmd}    " 重新定义新的自动命令，可以有多行 autocmd

autocmd  {event}  {pat}  {cmd}   " 类似的自动命令建议放在同一个组中

augroup  END                       " 最后用 END 选回默认当前组名

 |

## 折叠

折叠用于把缓冲区内某一范围内的文本行显示为屏幕上的一行。就像一张纸，要它缩短些，可以把它折叠起来：

+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+ | 行 1 | | 行 2 | | 行 3 | |\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ | \\ \\ \\\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\\ / 被折叠的行 / /\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/ | 行 12 | | 行 13 | | 行 14 | +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+

|

1

2

3

4

5

6

7

8

9

10

11

12

13

 |

+\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- +

|  行  1 |

|  行  2 |

|  行  3 |

|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  |

\\ \\

 \\\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\\

 /  被折叠的行 /

/\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/

|  行  12 |

|  行  13 |

|  行  14 |

+\-\-\-\-\-\-\-\- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- +

 |

被折叠的文本仍然在缓冲区内而没有改变，只是改变了文本行显示的方式。折叠的好处是，通过把多行的一节折叠成带有折叠提示的一行，会让你更好地了解文本的宏观结构。

Vim 折叠文本有 6 种不同的方式，可以通过 `:set foldmethod` 选择（阅读 :help `usr_28`）：

*   `manual`    手动折叠
*   `indent`     依缩进折叠
*   `marker`    依标志折叠
*   syntax        依语法折叠
*   expr           依表达式折叠
*   diff             折叠未被改动的行

下面介绍一些常用的折叠方法。

### 手动折叠（set foldmethod=manual）

所有的折叠命令都以 `z` 开头。展开你的想像力，这个字母看起来就像一张折叠起来的纸的侧面。而 `z` 后面可用的字母，由于采用了帮助记忆方法选择，很容易记得住：

*   `zf`                  F\-old creation（创建折叠）
*   `zo`                 O\-pen a fold（打开折叠）
*   `zc`                 C\-lose a fold（关闭折叠）
*   `zr`                  打开所有折叠（按层打开，因为 vim 折叠可以套嵌）
*   `zm`                与上面相反，关闭所有折叠
*   `zR`                 打开所有折叠（这次是全部了）
*   `zM`                与上面相反，关闭所有折叠

在折叠处移动光标可打开折叠，另外你可以用 `zn` 命令快速禁止折叠功能。然后 `zN` 恢复原来的折叠。`zi` 切换于两者之间。以下步骤是一种实用的操作方法：

1.  创建折叠，以获取你的文件的概览
2.  移动到你要操作的地方
3.  执行 zi 以便一边看着文本，一边编辑
4.  再执行 zi 以便移动到另一处

### indent 依缩进折叠（set foldmethod=indent）

缩进折叠适用于 Python 等缩进严格的编程语言。缩进多少和折叠深度之间的关系依赖于 `shiftwidth` 选项，每个 `shiftwidth` 选项规定的缩进宽度。折叠深度 +1，这被称为一个折叠级别。其实在你使用 `zr` 和 `zm` 命令的时候，你实际上是在增加或减少 `foldlevel` 选项。你也可以直接设置它：

:set foldlevel=3

|

1

 |

:set  foldlevel\=3

 |

这意味着，所有缩进等于或大于 shiftwidth 三倍的折叠将被关闭。折叠级别设定得越低，越多的折叠将被关闭。当 foldlevel 为0时，所有的折叠都将被关闭，zM 把 foldlevel 设为0。相反的命令 zR 把 foldlevel 设为文件中最深的折叠级别，所有的折叠都将被打开。

### 依标志折叠（set foldmethod=marker）

在文本中使用标志指定一个折叠区的起点和终点，标志折叠可以精确地控制一个折叠究竟包含哪些行文本。可以使用选项 `foldmarker` 设定折叠标志，默认值为 `{{{,}}}`，配合 vim 的注释符号 `"`，我改为了更简单的 `{,}` 来折叠我的 ~/.vimrc：

" Fold { set foldmethod=marker set foldlevel=0 set foldmarker={,} " }

|

1

2

3

4

5

 |

" Fold {

set  foldmethod\=marker

set  foldlevel\=0

set  foldmarker\={ ,}

" }

 |

# Vimscript 基础语法

## 变量

变量的定义用 `:let`命令，删除用 `:unlet`命令。

Vimscript 中的数据类型：

| 类型 | ID | 描述 |
| --- | --- | --- |
| Number | 0 | 4字节或8字节（vim8）有符号整数，支持按二进制、八进制、十六进制的表示法，自动转为字符串将转为十进制。支持数学运算 + – \* / %。 |
| String | 1 | 空字符终止的无符号字符。一般字符串用单引号 `'string'`，转义字符用双引号 `"\n"`（:help `expr-quote`），使用 `.` 连接字符串。查看有关操作 String 的内置函数（:help `string-functions`）。 |
| Funcref | 2 | 函数引用。函数引用变量可以通过 `function()` 函数、`funcref()` 函数或者 `lambda` 匿名函数表达式得到。（:help `Funcref`） |
| List | 3 | 列表，有序集合。类似于 Python 中的列表，索引从 0 开始，支持负索引，\-1 表示倒数第一个元素，列表变量表示对列表实体的引用。同样，Vimscript 中也提供大量操作列表的函数（:help `list-functions`）。 |
| Dictionary | 4 | 字典，无序集合。类似于 Python 中的字典，字典变量表示对字典实体的引用。同样，字典在 Vimscript 中也有着重要的作用，任何更复杂的数据结构都能在字典的基础上构造。上面许多关于列表的函数，也可作用于字典。只是有些参数意义可能不一样，对于字典时，一般以键来操作。（:help `dict-functions`） |
| Float | 5 | 浮点数。浮点数的精度和取值范围取决于编译 vim 时使用的库如何理解 `double`，运行时无法改变。 |
| Boolean | 6 | 布尔型，值为 `true` 或 `false`。 |
| None | 7 |
| Job | 8 |
| Channel | 9 |
| Blob | 10 |

## 变量作用域

在 Vimscript 中 ，可以给变量都加上一个冒号前缀，表示该变量的作用域。

| 变量前缀 | 描述 |
| --- | --- |
| `g:` | 全局作用域 |
| `l:` | 局部作用域，只能在函数体内使用 |
| `s:` | 脚本作用域，只能在当前脚本内使用，包括该脚本的函数体内。 |
| `a:` | 参数作用域。特指函数的参数，在函数体内引用传入的实参，需要加上 a: 前缀，但定义函数时的形参，不能加 a: 前缀。a: 还隐含一个限定是只读性，即在函数体内不能修改的参数。 |
| `v:` | Vim 特殊变量 |
| b: | 当前缓冲区作用域 |
| w: | 当前窗口作用域 |
| t: | 当前标签页作用域 |
| 注：当前位置即光标所在位置 |

## 条件选择与比较

Vimscript 使用 `if` 语句实现分支选择。

if {expr1} {block1} elseif {expr2} {block2} elseif {expr3} {block3} ... else {blockn} endif

|

1

2

3

4

5

6

7

8

9

10

 |

if  {expr1}

{block1}

elseif  {expr2}

{block2}

elseif  {expr3}

{block3}

...

else

{blockn}

endif

 |

其中条件表达式{expr}的值为逻辑真假，即 `v:true` 或 `v:false`。数字 0 为假，其他为真，字符串 ‘0’ 为假，其他为真 。其他数据类型不能判断真假，但可以利用内建函数 `empty()` 来帮忙，它可以接收任何类型的一个参数，如果它是“空”的，就返回真（ v:true），否则返回假（v:false），用 `!empty()` 取反判断。

数和字符串支持的比较运算符包括：==、!=、>、>=、< 和 <=。但在字符串判断相等时建议使用 `==#`（大小写敏感），`==?`（大小写不敏感），以避免因用户设置选项 `&ignorecase` 导致判断结果与预期相反。

Vimscript 支持逻辑运算：短路与（`&&`）、短路或（`||`）、非（`!`）。Vimscript 支持三目运算符：

" 计算 expr1，若值为真，则计算 expr2 作为结果；否则计算 expr3 作为结果 expr1 ? expr2 : expr3

|

1

2

 |

" 计算 expr1，若值为真，则计算 expr2 作为结果；否则计算 expr3 作为结果

expr1  ?  expr2  : expr3

 |

## 运算符优先级

可以通过 :help `expression-syntax` 查看表达式语法表，其中也基本是按运算符优先级从低到高排列的，请经常查阅。

## 循环

Vimscript 支持两种循环：`for` 循环和 `while` 循环。

### For 循环

与 C语言的 for(int i =  1; i < 10; i++) 语句不同，Vimscript 使用 `for ... in ...` 语句。遍历列表：

:let list = \[1, 2, 3, 4, 5\] :for i in list :echo i :endfor

|

1

2

3

4

 |

:let list  \=  \[ 1,  2,  3, 4,  5\]

:for  i  in  list

:echo  i

:endfor

 |

变量 `i` 叫做“循环变量”，循环结束后仍然存在。遍历列表保证是有序的。利用内建字典函数 `items(dict)` 可以得到字典的键\-值对列表，然后遍历字典键值对：

:let dict = {'a':1, 'b':2, 'c':3, 'd':4, 'd':5,} :for \[key,val\] in items(dict) :echo key . '=>' . val :endfor

|

1

2

3

4

 |

:let dict  \=  { 'a':1,  'b':2 ,  'c':3,  'd' :4,  'd':5, }

:for  \[key,val \]  in  items(dict)

:echo  key  . '=>'  .  val

:endfor

 |

字典内的元素是无序的。利用内建字典函数 `keys(dict)` 可以得到字典的键列表，然后就可以单独遍历键了：

:for key in keys(dict) :echo key . '=>' . dict\[key\] :endfor

|

1

2

3

 |

:for  key in  keys (dict)

:echo  key  . '=>'  .  dict\[key \]

:endfor

 |

效果和上例一样。利用内建字典函数 `values(dict)` 还可以得到字典的值列表，然后就可以单独遍历值了：

:for val in values(dict) :echo val :endfor

|

1

2

3

 |

:for  val in  values (dict)

:echo  val

:endfor

 |

#### 固定循环次数

利用 vim 内建 `range()` 函数（:help `range()`）可以生成一个整数列表，如 range(5) = \[0, 1, 2, 3, 4\]，range(0, 5) = \[0, 1, 2, 3, 4, 5\] 等。一个简单的例子，以下语句输出 5 次 Hello, World!：

:for i in range(5) :echo 'Hello, World!' :endfor

|

1

2

3

 |

:for  i  in  range(5)

:echo  'Hello, World!'

:endfor

 |

循环体中并没有用到循环变量 i，它只是帮忙计数而已。

### While 循环

Vimscript 也支持经典的 `while` 循环，当条件满足（表达式的结果非零）时，循环执行循环体中的命令：

:let i = 0 :while i < 5 :echo i :let i += 1 :endwhile

|

1

2

3

4

5

 |

:let i  \=  0

:while  i  <  5

:echo  i

:let i  +=  1

:endwhile

 |

用 while 循环必须在循环前定义循环变量，且需在循环体内更新循环变量以防止出现死循环，如果出现死循环，vim 没响应，一般可用 `Ctrl+C` 中断脚本或命令执行。如果发现循环体里有命令出错，则从 `endwhile` 之后继续执行。

### 循环控制 break 和 continue

*   `break`      提前结束整个循环，流程跳转到 endfor 或 endwhile 之后。
*   `continue` 提前结束本次循环，开始下次循环，流程跳转到循环开始，对于 for 循环来说，循环变量将获取下一个值，对于 while 循环来说，会再次执行条件判断。
*   结合 `if` 条件语句，在特定条件下才改变流程。

## 函数

Vimscript 中定义函数（:help `function`）：

function\[!\] 函数名(参数列表) 附加属性 函数体 endfunction

|

1

2

3

 |

function\[!\]  函数名(参数列表) 附加属性

函数体

endfunction

 |

其中 `!` 表示强制重新定义函数。函数名可以由字母、数字与下划线 `_` 组成，但必须以大写字母或者 `s:`（脚本中的函数，:help `local-function`）开头 。注意 `b:` 或 `g:` 是不允许的。函数参数可以没有，多个参数用英文逗号 `,` 分隔。函数体中用 `return` 返回值，如果没有 return 语句则默认返回 `0`。

### 可变参数

函数参数还可以为可变参数，即参数个数是可以不确定的。当然，普通参数的个数是确定的。

*   在函数参数列表的最后使用 `...` 表示接受可变参数。
*   在函数体中，分别用 `a:1`、`a:2`、 `……` 等表示第一个、第二个可变参数。用 `a:0` 表 示可变参数的数量（可以为 0），`a:000` 是包含所有可变参数的列表，a:000\[0\] 就是 a:1。
*   命名参数最多允许 `20` 个，可变参数的数量没有明确限制。

### 函数的调用

在其他地方调用函数一般用 `:call` 命令，如果要观察函数返回值，请使用 `:echo` 命令，还可以用 `:let` 定义一个变量保存函数的返回结果。

call 函数名(参数) echo 函数名(参数) let 返回值 = 函数名(参数)

|

1

2

3

 |

call  函数名(参数)

echo  函数名(参数)

let  返回值  \=  函数名(参数)

 |

### 函数的附加属性

函数的附加属性有 `range`、`abort`、`dict` 和 `closure`，他们和函数的参数一样是可选的，以空格分隔。

| 附加属性 | 描述 |
| --- | --- |
| range | 需要在 call 之前有行范围参数，如 :4,8call Cont()，该函数自己能理解并处理行范围，隐式传入 `a:firstline`\=4 和 `a:lastline`\=8，函数将在选定行范围内作用。行范围也可以通过 `V` 行可视化模式选定。 |
| abort | 该函数在遇到错误时立即中止，函数体后的语句不会执行。当然，调用这个出错函数之后的语句仍然会执行。 |
| dict | 该函数必须通过某个字典的元素才能调用，元素的值为该函数的引用（:help `Funcref`）。通过字典元素的值对应的键来调用该函数，其中函数局部变量 `self` 这时设为该字典，此时该函数类似于面向对象编程的方法。（:help `Dictionary-function`） |
| closure | 此时该函数可以访问外部作用域的变量和参数，通常这被称为闭包（:help `func-closure`）。为了方便我们把这个外部的变量和参数命名为闭包变量，闭包变量通常在外层函数（为了方便我们命名为工厂函数）中定义，该函数，相对的为内层函数（为了方便我们命名为闭包函数）。这时学过 C语言的你可能发现了一些问题，不要惊讶，在 Vimscript 里你可以套嵌定义函数。在工厂函数中请使用函数 `funcref()` 而不是用 function() 引用闭包函数，这样可以保证闭包函数稳定而不会被随意重新定义。在工厂函数返回后，闭包变量理论上要释放的，也就无从其他地方再次访问了，但实际上闭包函数仍然可以访问。可以那么理解（我的脑洞），工厂函数创造了某变量，而该变量被工厂函数套嵌定义的函数引用了，承包了该变量，成为了闭包变量，而承包它的函数成为了闭包函数，在工厂函数返回后，各个闭包函数对自己的闭包变量有唯一使用权，同一个闭包变量在各个闭包函数中并行互不影响。 |

## 匿名函数表达式 lambda

{args \-> expr1}

|

1

 |

{args  \->  expr1}

 |

匿名函数表达式创建一个新的无名函数，简单的返回 expr1 的计算结果。`->` 前的部分类似与普通函数的参数列表，`->` 后是一个表达式，且使用 args 参数时不用加 `:a` 前缀，该表达式的值就是以后调用该 `lambda` 时的结果。匿名函数表达式可能访问外层变量和参数，这通常被称为闭包。（:help `closure`）

## 常用内建函数

Vim 提供很多有用内建函数，善用这些函数，可以给我们带来很大的帮助。第一次阅读本文可跳过这部分，点击右下角的小菜单打开文章目录快速跳至下一节。使用 :help `function-list` 会按类别列出内置函数，使用 :help `functions` 则会按字母序列出内置函数，在函数名上使用 `Ctrl+]` 可以快速跳转至该函数的详细说明。在这里仅以表格形式列出一些常用的内建函数。

### 字符串处理函数（utf\-8 编码）

| 函数 | 说明 |
| --- | --- |
| nr2char() | 将 utf\-8 编码值转为对应字符 |
| char2nr() | 得到字符的 utf\-8 编码值，或得到字符串首字符的 utf\-8 编码值 |
| str2nr() | 将字符串转为整数 |
| str2float() | 将字符串转为浮点数 |
| printf() | 使用 `%` 格式化字符串，用法类似 C语言 |
| escape({string}, {chars}) | 在 {string} 里用反斜杠 `\` 转义 {chars} 里的字符 |
| fnameescape() | 转义特殊字符以适于 vim 命令，主要用于转义文件名参数 |
| shellescape() | 转义特殊字符以适于 shell 命令 |
| tolower() | 将字符串转为小写 |
| toupper() | 将字符串转为大写 |
| tr({src}, {fromstr}, {tostr}) | 按 一 一 对应的方式转换字符串。也就是说，{fromstr} 的第一个字符被翻译成 {tostr} 的第一个字符，依此类推。和 unix 命令 `tr` 完全相同。例如 :tr(‘hello there’, ‘ht’, ‘HT’) 返回 ‘Hello THere’ |
| expand() | 将特殊关键字 `%`（当前文件名）、`#`（轮换文件名）和 `<cword>`（光标所在的单词）等展开 |
| repeat({expr}, {count}) | 将字符串 {expr} 重复 {count} 次串接生成长字符串 |
| eval() | 将字符串当作表达式来计算，并返回结果 |

### 列表或字典处理函数

| 列表或字典处理函数 | 说明 |
| --- | --- |
| len() | 返回列表或字典元素个数 |
| empty() | 检查列表或字典是否为空，空则返回数值 1，否则返回 0 |
| extend() | 在列表后附加另一个列表，或从一个字典增加元素到另一个字典。用 `+` 操作符连接两个列表将生成一个新列表。 |
| remove() | 删除列表里一或多个元素，或删除字典某个键的元素 |
| count() | 计算列表或字典里某值的出现次数 |
| 列表处理函数 |
| insert() | 在列表某处插入元素 |
| add() | 在列表后附加元素 |
| match() | 返回能匹配成功的元素索引 |
| sort() | 给列表排序 |
| 字典处理函数 |
| has\_key() | 检查某键是否出现在字典里 |
| keys() | 得到字典的键列表 |
| items() | 得到字典的键\-值组对的列表 |

### 浮点数运算和逻辑运算

| 浮点数运算 | 说明 |
| --- | --- |
| float2nr() | 把浮点数转换为整数 |
| abs() | 取绝对值 （也适用于整数） |
| round() | 四舍五入，最后保留一位小数 |
| trunc() | 删除小数点后的值 |
| pow() | 求幂 |
| sqrt() | 开平方 |
| sin()等 | 三角函数 |
| 逻辑运算 |
| and() | 按位与 |
| invert() | 按位取反 |
| or() | 按位或 |
| xor() | 按位异或 |

### 文件和目录相关函数

| 文件和目录相关函数 | 说明 |
| --- | --- |
| finddir({name}\[, {path}\[, {count}\]\]) | 在路径 {path} 里查找目录 {name}，支持向下和向上的递归目录搜索，返回第一个找到的目录路径。如果找到的目录路径在当前目录之下，返回相对路径，否则，返回完整路径。如果省略 {path}，使用选项 `&path` 代替。如果给出可选的 {count}，寻找 {path} 里 {name} 第 {count} 次出现，而不是第一次。如果 {count} 为负，返回所有的匹配组成的列表。 |
| findfile({name}\[, {path}\[, {count}\]\]) | 类似于 finddir()，不过寻找文件而不是目录。 |
| resolve() | 解析链接实际文件名 |
| simplify() | 简化文件名路径 |
| pathshorten() | 缩写文件名的中间路径（取首字母） |
| fnamemodify({fname}, {mods}) | 从文件名 {fname} 中获取其目录、全路径名、后缀名等相关名字的字符串（通过 {mods}）。修饰符 {mods} 以冒号开头接一个单字符，表示不同意义，可多个拼接使用，但必须按如下顺序给出 |
| 修饰符 | 注意：环境变量不能用于 {fname}，需要先用 `expand()` 扩展。 |
| `:p` | 文件完整路径名 |
| `:~` | 路径名缩减为基于主目录的相对路径。若文件不在主目录下，则文件名不会被改变。 |
| `:.` | 路径名缩减为基于当前目录的相对路径。若文件不在当前目录下，则文件名不会被改变。 |
| `:h` | 父目录名（文件名头部，除去文件名的最后一部分以及路径分隔符），不能与 :e、:r 或 :t 一起使用。 |
| `:t` | 文件名的尾部（文件名的最后一部分，纯文件名）。必须在 :r 或 :e 之前。 |
| `:r` | 文件名的根部 （除去最后的扩展名）。如果只有扩展名（文件名以’.’开始，例如’.vimrc’），则不会被删除。可以重复使用，以删除多个扩展名（最后一个先被删除）。 |
| `:e` | 扩展名（即文件名后缀）。只有单独使用时才有意义。如果没有扩展名，那结果为空。如果文件名只是一个扩展名（以’.’开始的文件名），则结果为空。可以重复使用来包含更多的扩展名。如果没有足够的扩展名（但是至少有一个），那么就尽可能多的包含。 |
| executable() | 检查是否存在可执行文件 |
| exepath() | 返回可执行程序的完整路径 |
| filereadable() | 检查文件是否可读 |
| filewriteable() | 检查文件是否可写 |
| getcwd() | 获取当前工作目录名 |
| getfperm() | 返回文件权限（类 `rwxrw-rw-` 字符串） |
| getfsize() | 返回文件字节大小（目录返回 0，找不到文件返回 \-1，文件过大，超出了 vim 的数值的范围，返回 \-2） |
| getftype() | 返回文件类型的描述（普通文件 `file`，目录 `dir`，符号链接 `link` 等） |
| readfile({fname} \[, {binary} \[, {max}\]\]) | 读文件 {fname} 至一个字符串列表，文件每行一项。如果 {binary} 包含 `b`，使用二进制模式，如果给出 {max}，指定读入的最大行数。 |
| writefile({list}, {fname} \[, {flags}\]) | 将字符串列表 {list} 写入文件 {fname}，每项一行文本。如果 {flags} 包含 `b`，使用二进制模式，如果 {flags} 包含 `a`，使用附加模式。 |
| isdirectory() | 检查目录是否存在 |

### 系统命令和时间函数

| 系统命令和时间函数 | 说明 |
| --- | --- |
| system({expr} \[, {input}\]) | 执行外部系统命令 {expr}，结果为字符串形式返回。如果给出 {input} 且为字符串，该字符串被写到文件里，并传给外部系统命令作为标准输入。此外，vim 的命令行中，可用 `:!` 叹号开头，调用外部系统命令。 |
| systemlist({expr} \[, {input}\]) | 和 system() 相同，但返回由行组成的列表。输出的工作方式和 readfile() 带 {binary} 参数设为 `b` 相同。 |
| localtime() | 返回当前时间，以 1970 年 01 月 01 日开始的秒数计算。 |
| strftime({format} \[, {time}\]) | 返回字符串，即经过 {format} 字符串的格式转换的日期和时间。使用给定的 {time}，如果没有给出时间，使用当前时间。可以接受的 {format} 取决于你的系统。可用时间格式 {format} 与 C语言的同名标准函数相同，如 strftime(‘%Y\-%m\-%d’) 将返回类似 2019\-03\-02 的字符串。 |
| reltime(\[{start} \[, {end}\]\]) | 返回更精确的时间，具体格式与系统有关，可用来计算命令或函数执行的时间。没有参数，返回当前时间。带一个参数 {start}，返回从开始时刻 {start} 到现在所经过的时间。带两个参数，返回 {start} 和 {end} 之间跨越的时间。{start} 和 {end} 参数必须是 reltime() 返回的值。 |

## Execute 命令

execute 命令可以将字符串当作 Vimscript 的 Ex 命令来执行。

:execute {expr1} . {expr2} | " 注释

|

1

 |

:execute  {expr1}  .  {expr2}  | " 注释

 |

计算各表达式，返回的字符串用 `.` 连接成为一个字符串并作为 ex 命令执行。`:execute`、`:echo` 和 `:echon` 后面不能直接跟注释，你需要在注释前加上 `|`。一般情况下，我们会把 `:execute` 命令封装在脚本或函数中。

## Normal 命令

不知道你是否还记得前面介绍的 vim 常用原生按键表，其中一般命令模式（command\-mode）的表格最长，日常的文本编辑命令很多使用在 normal 模式下。使用 `normal` 命令可以让我们在 ex 命令行模式（或脚本中）使用 normal 模式下的文本编辑命令。

:normal\[!\] {commands}

|

1

 |

:normal\[!\]  { commands}

 |

其中 {commands} 为在 normal 模式下的命令，执行 normal 命令相当于你在 normal 模式下输入命令。normal 命令会接受 nnoremap 映射，这会在脚本中造成麻烦，因为你不知道用户使用了什么样 nnoremap，你将得不到预期的效果。而给 normal 命令加上 ! 可以避免映射，建议你一直使用 `normal!` 命令。

### Execute 与 Normal联用

normal 命令后的参数（normal 模式下命令按键序列），只适于可打印字符，对 于特殊字符需要进行转义。用 `:execute`命令套 `:normal` 命令，可以方便使用 `\` 转义不可打印字符。此外，:execute 还可以使 :normal 也用上变量。

function Delete\_contents\_after\_word(count, word, cases) abort let n = a:count let w = a:word if a:cases == 0 " 0 则不区分大小写 execute 'normal! ' . 'gg/' . '\\<' . w . '\\>' . '\\c' . "\\<CR>" . n . 'dd' else execute 'normal! ' . 'gg/' . '\\<' . w . '\\>' . '\\C' . "\\<CR>" . n . 'dd' endif endfunction " 移动到文件的开头，查找单词 hello 的首次出现的地方，并删掉包括 hello 所在行以下 3 行。 :call Delete\_contents\_after\_word(3, hello, 1)

|

1

2

3

4

5

6

7

8

9

10

11

 |

function  Delete\_contents\_after\_word(count, word,  cases)  abort

let n  \=  a:count

let w  \=  a:word

if  a:cases  \==  0    " 0 则不区分大小写

execute  'normal! '  . 'gg/'  .  '\\<'  .  w  .  '\\>'  .  '\\c' .  "\\<CR>"  .  n .  'dd'

else

execute  'normal! '  . 'gg/'  .  '\\<'  .  w  .  '\\>'  .  '\\C' .  "\\<CR>"  .  n .  'dd'

endif

endfunction

" 移动到文件的开头，查找单词 hello 的首次出现的地方，并删掉包括 hello 所在行以下 3 行。

:call  Delete\_contents\_after\_word(3, hello,  1)

 |

## 正则表达式

Vim支持 4 套正则表达式模式，可以在 `/` 或 `?` 命令行中添加特殊前导字符来表示本次搜索采用哪套正则表达式：

*   \\v (very magic) 最接近 Perl 语言的正则表达式。除 `[a-zA-Z0-9_]` 外，其他字符都有特殊含义，即魔法字符。
*   \\m (magic) 这是 vim 的标准（默认）正则表达式。主要特征是括号与加号都是字面意义，不是魔法字符，需要在前面多加一个反斜杠 `\` 来表示魔法意义。
*   \\M (nomagic) 更少的魔法字符，点号 `.` 与星号 `*` 都是字面意义，另外可通过 `:set nomagic` 启用，用 `:set magic` 返回默认模式。
*   \\V (very nomgic) 只有反斜杠 `\` 本身及终止字符 （`/` 或 `?`）有特殊意义，其他所有字符按字面意义匹配。

在一种正则表达式模式中，如果一个字符是魔法字符，反斜杠转义后就表示字面意义 ；反之如果一个字符不是魔法字符，加反斜杠转义后就可能成为魔法字符表示特殊意义。下面只讲 vim 的标准（默认）正则表达式。

### 匹配量词

匹配量词不能单独使用，须用于表示字符（或类别）的后面，表示匹配前面那个字符多少次。

| 匹配量词 | 限定 |
| --- | --- |
| `*` | 匹配 0 个或多个 |
| `\+` | 匹配 1 个或多个 |
| `\=` 或 `\?` | 匹配 0 个或 1 个，\\? 不能在 ? 命令（逆向查找）中使用 |
| `\{n,m}` | 匹配 n 个到 m 个 |
| `\{n}` | 匹配恰好 n 个 |
| \\{n,} | 匹配最少 n 个 |
| \\{,m} | 匹配最多 n 个（包括 0 个） |
| \\{} | 匹配任意个，等同于 \* |
| \\{\-n,m}, \\{\-n}, \\{\-n,}, \\{\-,m}, \\{\-} | 匹配个数尽可能的少（非贪婪匹配） |

### 常用的元字符

| 字符 | 描述 |
| --- | --- |
| `.` | 匹配任意一个字符 |
| `\e` | 匹配 <Esc> |
| \\t | 匹配制表 <Tab> |
| `\r` | 匹配回车 <CR> |
| `\n` | 匹配换行符 |
| \\b | 匹配退格 <BS> |
| `[`abcwxyz`]` | 匹配方括号中的任意一个字符。可以使用 `-` 表示字符范围，若要表示减号本身，则需要加在方括号内的开头，如 \[\-a\-z\] 表示小写字母或减号。若要匹配方括号本身，则须用 `\[` 或 `\]`。 |
| \[`^`abcwxyz\] | 在方括号内开头加 `^`，表示匹配除方括号中字符之外的任意字符 |
| `\d` | 匹配数字字符，等同于 \[0\-9\] |
| \\D | 匹配数字字符之外的任意字符，等同于 \[^0\-9\] |
| `\x` | 匹配十六进制数字字符，等同于 \[0\-9A\-Fa\-f\] |
| `\a` | 匹配英文字母字符，等同于 \[a\-zA\-Z\] |
| \\l | 匹配小写字母，等同于 \[a\-z\] |
| \\u | 匹配大写字母，等同于 \[A\-Z\] |
| `\w` | 匹配单词字符，等同于 \[a\-zA\-Z0\-9\_\] |
| `\h` | 匹配单词首字符，等同于 \[a\-zA\-Z\_\] |
| `\s` | 匹配空白字符，等同于 `[ \t]`（<Space> 和 <Tab>） |
| 与选项相关的字符类 | 相应选项指定字符集 |
| \\i | 由选项 &isident 指定的标识字符 |
| \\k | 由选项 &iskeword 指定的关键字字符 |
| \\f | 由选项 &isfname 指定的可用于文件名和路径名的字符 |
| \\p | 由选项 &isprint 指定的可打印字符 |
| \\I \\K \\F \\P | 在以上小写版本基础上排除数字字符 |
| 匹配定位点 |
| `^` | 匹配行首 |
| `$` | 匹配行尾 |
| `\<` | 匹配单词词首 |
| `\>` | 匹配单词词尾。在 vim 编辑过程中，按 `*` 或 `#` 命令，用于搜索当前光标下的单词，就会在当前单词前后自动加上 `\<` 与 `\>` 表示界定匹配整个单词。 |
| \\zs | 标定匹配结果的开始部分 |
| \\ze | 标定匹配结果的结束部分 |
| \\%^ | 匹配文件首 |
| \\%$ | 匹配文件尾 |
| \\%# | 匹配当前光标位置 |
| \\%’m | 匹配标记 m 位置，m 可以是任一个命令标记（:help mark）。 |
| `\%l` | 匹配行，在 \\% 与 l 之间应该是一个有效的数字行号，表示匹配相应的行，若在行号前再加个 < 表示匹配该行之前的行，加个 > 则表示匹配之后的行。 |
| \\%c | 匹配列，与 \\%l 用法类似 |
| 大小写匹配 | 在默认情况下，正则表达式匹配受选项 `&ignorecase` 影响，但如果在一个模式中任意地方加上了 \\c 或 \\C 控制符，就强行区分或不区分大小写。一般是加在表达式末尾，方便临时改变主意再怎么区分大小写。 |
| `\c` | 不区分大小写 |
| `\C` | 区分大小写 |

# 编译 Vim8

系统自带的 vim 版本太老怎么办？想使用新版 vim8 特性？对于 Win 平台可以上 GitHub 取得最新的 build ：[vim\-win32\-installer](https://github.com/vim/vim-win32-installer/releases)，下载对应系统的 .exe 文件安装即可；对于 Unix，自己动手，丰衣足食，当然是获取源码自行编译啦！以 Debian 系为例：

避免冲突，删除原有 vim：

$ sudo apt\-get remove \-\-purge vim gvim vim\-tiny vim\-common vim\-gui\-common \\ vim\-runtime vim\-gnome vim\-nox

|

1

2

 |

$  sudo apt\-get remove \-\-purge vim gvim vim\-tiny vim\-common vim\-gui\-common \\

vim \-runtime vim\-gnome vim\-nox

 |

安装依赖：

$ sudo apt\-get install lua5.1 liblua5.1\-dev python\-dev python3\-dev \\ ruby\-dev libperl\-dev tcl\-dev \\ libncurses\-dev \\ gcc git

|

1

2

3

4

5

6

 |

$  sudo apt\-get install lua5.1  liblua5.1\- dev python\-dev python3\-dev \\

 ruby\- dev libperl\-dev tcl\-dev  \\

 libncurses5\- dev libgnome2\-dev libgnomeui\-dev \\

 libgtk2. 0\-dev libatk1.0\-dev libbonoboui2\-dev  \\

 libcairo2\- dev libx11\-dev libxpm\-dev libxt\-dev  \\

 gcc git

 |

从 GitHub 获取源代码：

$ git clone https://github.com/vim/vim.git

|

1

 |

$  git clone  https: //github.com/vim/vim.git

 |

配置编译参数：

$ cd vim $ ./configure \-\-with\-features=huge \\ \-\-enable\-multibyte \\ \-\-enable\-luainterp=yes \\ \-\-enable\-pythoninterp=yes \\ \-\-enable\-python3interp=yes \\ \-\-enable\-rubyinterp=yes \\ \-\-enable\-perlinterp=yes \\ \-\-enable\-tclinterp=yes \\ \-\-enable\-cscope \\ \-\-enable\-gui=auto \\ \-\-enable\-fail\-if\-missing \\ \-\-with\-python\-command=python2.7 \\ \-\-with\-python3\-command=python3.7 \\ \-\-with\-compiledby=StarryLeo

|

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

 |

$  cd vim

$  ./configure  \-\- with\-features\=huge  \\

\-\-enable\-multibyte \\

\-\-enable\-luainterp \=yes  \\

\-\-enable\-pythoninterp \=yes  \\

\-\-enable\-python3interp \=yes  \\

\-\-enable\-rubyinterp \=yes  \\

\-\-enable\-perlinterp \=yes  \\

\-\-enable\-tclinterp \=yes  \\

\-\-enable\-cscope \\

\-\-enable\-gui \=auto  \\

\-\-enable\-fail \-if\-missing  \\

\-\-with\-python \-command\=python2.7  \\

\-\-with\-python3 \-command\=python3.7  \\

\-\-with\-compiledby \=StarryLeo

 |

编译并安装：

$ make $ sudo make install Or $ sudo apt\-get checkinstall $ make $ sudo checkinstall

|

1

2

3

4

5

6

 |

$  make

$  sudo make install

Or

$  sudo apt\-get checkinstall

$  make

$  sudo checkinstall

 |

使用 checkinstall 可打包为 deb 或 rpm，方便安装和卸载。查看 vim 版本信息：

$ vim \-\-version

|

1

 |

$  vim  \-\-version

 |

# 说在最后

Vim 的学习曲线是陡峭滴，度过前期阶段就好很多了。另外，想愉快使用 vim，少不了折腾配置文件 ~/.vimrc 和插件。在此推一波自己的 vim 配置 ![:oops:](https://starrycat.me/wp-content/plugins/WP-Alu2Button/static/img/icon_redface.gif)