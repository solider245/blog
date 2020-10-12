---
title: nano
date: 2020-10-12 12:09:51
permalink: /pages/2d4335/
categories:
  - 技术
  - linux
tags:
  - 
---
# Linux下轻型文本编辑器Nano常用快捷键

![](https://csdnimg.cn/release/phoenix/template/new_img/original.png)

[火山哥](https://me.csdn.net/sunchaoenter) 2011\-12\-06 10:42:29 ![](https://csdnimg.cn/release/phoenix/template/new_img/articleRead.png) 27203 ![](https://csdnimg.cn/release/phoenix/template/new_img/collect.png) ![](https://csdnimg.cn/release/phoenix/template/new_img/tobarCollectionActive.png) 收藏

分类专栏： [14 Unix/Linux](https://blog.csdn.net/sunchaoenter/category_942351.html) 文章标签： [文本编辑](https://so.csdn.net/so/search/s.do?q=文本编辑&t=blog&o=vip&s=&l=&f=&viparticle=) [linux](https://so.csdn.net/so/search/s.do?q=linux&t=blog&o=vip&s=&l=&f=&viparticle=) [windows](https://so.csdn.net/so/search/s.do?q=windows&t=blog&o=vip&s=&l=&f=&viparticle=)

最后发布:2011\-12\-06 10:42:29首发:2011\-12\-06 10:42:29

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY\-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：[https://blog.csdn.net/sunchaoenter/article/details/7045083](https://blog.csdn.net/sunchaoenter/article/details/7045083)

版权

**新建／打开文件**

nano 路径+文件名
如果该文件存在，上面的命令将打开这个文件；如果文件不存在则将会创建一个新文件并打开。

Note：在Windows系统中，一个文件应当有后缀名，比如.txt，以供系统进行类型判断，不过Linux并不根据后缀名来判断类型。当然，写上后缀名也无妨，比如example也可以用example.txt。

**光标控制**

移动光标：使用用方向键移动。

选择文字：按住鼠标左键拖动。

**复制、剪切和粘贴**

复制一整行：Alt+6

剪切一整行：Ctrl+K

粘贴：Ctrl+U

如果需要复制／剪切多行或者一行中的一部分，先将光标移动到需要复制／剪切的文本的开头，按Ctrl+6（或者Alt+A）做标记，然后移动光标到待复制／剪切的文本末尾。这时选定的文本会反白，用Alt+6来复制，Ctrl+K来剪切。若在选择文本过程中要取消，只需要再按一次Ctrl+6。

**搜索**

按Ctrl+W，然后输入你要搜索的关键字，回车确定。这将会定位到第一个匹配的文本，接着可以用Alt+W来定位到下一个匹配的文本。

**翻页**

用Ctrl+Y到上一页，Ctrl+V到下一页

**保存**

使用Ctrl+O来保存所做的修改

**退出**

按Ctrl+X

如果你修改了文件，下面会询问你是否需要保存修改。输入Y确认保存，输入N不保存，按Ctrl+C取消返回。

如果输入了Y，下一步会让你输入想要保存的文件名。如果不需要修改文件名直接回车就行；若想要保存成别的名字（也就是另存为）则输入新名称然后确定。这个时候也可用Ctrl+C来取消返回。

**获得帮助**

进入nano界面后，下面有两行菜单，例如，“^G Get Help”。其意义如下：

^G意味着快捷键是Ctrl+G，“Get Help”当然是功能了。

根据这些提示就可以立刻开始使用nano了，也可以Ctrl+G看看帮助。

Note：nano中，黑底白字表示快捷键操作。其中“^”表示Ctrl键，则Ctrl+G就表示成“^G”。“M”表示 Alt键，则Alt+W表示为“M\-W”。



# nano编辑器常用快捷键

![](https://csdnimg.cn/release/phoenix/template/new_img/original.png)

[Aleiz](https://me.csdn.net/tarawin) 2019\-07\-17 13:19:23 ![](https://csdnimg.cn/release/phoenix/template/new_img/articleRead.png) 1590 ![](https://csdnimg.cn/release/phoenix/template/new_img/collect.png) ![](https://csdnimg.cn/release/phoenix/template/new_img/tobarCollectionActive.png) 收藏  1

分类专栏： [Linux](https://blog.csdn.net/tarawin/category_7951724.html) [debian](https://blog.csdn.net/tarawin/category_9135585.html)

最后发布:2019\-07\-17 13:19:23首发:2019\-07\-17 13:19:23

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY\-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

本文链接：[https://blog.csdn.net/tarawin/article/details/96299564](https://blog.csdn.net/tarawin/article/details/96299564)

版权

**如图：**

```
				ctrl+p (上)									 ctrl+y/ctrl+gg (顶)
				   ↑											   ^
											   					   |
 ctrl+b (左)  ←         →  ctrl+f (右)		   ctrl+a(行首) <——        ——> ctrl+e (行尾)
						  										   |
 				   ↓   											   v
		       ctrl+n（下）									ctrl+v (底)

```

| `ctrl+w`：查找        | `ctrl+6`：选择         |
| --------------------- | ---------------------- |
| `ctrl+i`：tab键       | `Alt+6`：复制          |
| `ctrl+d`：Delete键    | `ctrl+u`：粘贴         |
| `ctrl+h`：Backspace键 | `ctrl+k`：剪切一行     |
| `ctrl+\`：查找并替换  | `ctrl+g`：详细使用说明 |



# Ubuntu:文本编辑器nano快捷键一览

*   2015\-05\-10
*   7372
*   [Ubuntu](https://www.polarxiong.com/category/ubuntu/)
*   [nano](https://www.polarxiong.com/tag/nano/), [快捷键](https://www.polarxiong.com/tag/%E5%BF%AB%E6%8D%B7%E9%94%AE/)
*   [0](#comments "评论数")

`nano`是比`vi`更简单易用的文本编辑器，在`nano`界面只列出了几个常用的快捷键，而实际上`nano`支持的快捷键远不止这些。

下面是nano的说明：
The nano editor is designed to emulate the functionality and ease\-of\-use of the UW Pico text editor. There are four main sections of the editor. The top line shows the program version, the current file name being edited, and whether or not the file has been modified. Next is the main editor window showing the file being edited. The status line is the third line from the bottom and shows important messages. The bottom two lines show the most commonly used shortcuts in the editor.

即：编辑器顶行显示程序版本、当前被编辑的文件名、以及文件是否已经编辑过；接着是主编辑框，显示正在编辑的文件；倒数第三行为状态行，用来显示重要的信息；底部的两行则显示编辑器中最常用到的快捷键。

The notation for shortcuts is as follows: Control\-key sequences are notated with a caret (^) symbol and can be entered either by using the Control (Ctrl) key or pressing the Escape (Esc) key twice. Escape\-key sequences are notated with the Meta (M\-) symbol and can be entered using either the Esc, Alt, or Meta key depending on your keyboard setup. Also, pressing Esc twice and then typing a three\-digit decimal number from 000 to 255 will enter the character with the corresponding value. The following keystrokes are available in the main editor window.

即：下面的快捷键符号中，`^`为Control键（`Ctrl`)，或连按两次Escape键（`Esc`）;`M`为Meta键（**Windows下为Alt键**）；另外，连续按下两次Esc键后再输入000\-255之间的三位数字，则会输入该ASCII码对应的字符。

示例：`^G`即按下Ctrl键然后按`G`；`M-/`即按下Alt键然后按`/`键。

```plain
^G      (F1)            Display this help text
                        显示帮助
^X      (F2)            Close the current file buffer / Exit from nano
                        关闭当前文件缓冲区 / 离开 nano
^O      (F3)            Write the current file to disk
                        写入当前文件至磁盘
^J      (F4)            Justify the current paragraph
                        对齐当前段落
^R      (F5)            Insert another file into the current one
                        插入其他文件至当前文件
^W      (F6)            Search for a string or a regular expression
                        查找字符串或正则表示式
^Y      (F7)            Go to previous screen
                        跳至前一屏
^V      (F8)            Go to next screen
                        跳至后一屏
^K      (F9)            Cut the current line and store it in the cutbuffer
                        剪切当前这行并存至剪贴板
^U      (F10)           Uncut from the cutbuffer into the current line
                        从剪贴板粘贴至当前行
^C      (F11)           Display the position of the cursor
                        显示光标位置
^T      (F12)           Invoke the spell checker, if available
                        尝试运行拼写检查

M-\     (M-|)           Go to the first line of the file
                        跳至文件第一行
M-/     (M-?)           Go to the last line of the file
                        跳至文件最后一行

^_      (F13)   (M-G)   Go to line and column number
                        跳至指定行与列位置
^\      (F14)   (M-R)   Replace a string or a regular expression
                        替换字符串或正则表示式
^^      (F15)   (M-A)   Mark text at the cursor position
                        标记游标所在文字
M-W     (F16)           Repeat last search
                        重复上次搜索

M-^     (M-6)           Copy the current line and store it in the cutbuffer
                        拷贝当前行至剪贴板
M-}                     Indent the current line
                        缩进当前行
M-{                     Unindent the current line
                        取消缩进当前行
^F                      Go forward one character
                        向前跳一字符
^B                      Go back one character
                        向后跳一字符
^Space                  Go forward one word
                        向前跳一个词
M-Space                 Go back one word
                        向后跳一个词
^P                      Go to previous line
                        跳至前一行
^N                      Go to next line
                        跳至后一行
^A                      Go to beginning of current line
                        跳至当前行首
^E                      Go to end of current line
                        跳至当前行尾
M-(     (M-9)           Go to beginning of paragraph; then of previous paragraph
                        跳至当前段落开头，如已在段落开头，则调至上一段落起始处
M-)     (M-0)           Go just beyond end of paragraph; then of next paragraph
                        跳至当前段落结尾，如已在段落结尾，则调至下一段落结尾
M-]                     Go to the matching bracket
                        移动至对应括号
M--     (M-_)           Scroll up one line without scrolling the cursor
                        向上卷动一行但不卷动游标
M-+     (M-=)           Scroll down one line without scrolling the cursor
                        向下卷动一行但不卷动游标
M-<     (M-,)           Switch to the previous file buffer
                        切换至上个文件缓冲区
M->     (M-.)           Switch to the next file buffer
                        切换至下个文件缓冲区
M-V                     Insert the next keystroke verbatim
                        插入下一按键原型
^I                      Insert a tab at the cursor position
                        在游标位置插入制表符
^M                      Insert a newline at the cursor position
                        在游标位置插入新行
^D                      Delete the character under the cursor
                        删除游标之下的字符
^H                      Delete the character to the left of the cursor
                        删除游标左侧的字符
M-T                     Cut from the cursor position to the end of the file
                        从游标位置剪切至文件结尾
M-J                     Justify the entire file
                        对齐整个文件
M-D                     Count the number of words, lines, and characters
                        计算字数、行数与字符数
^L                      Refresh (redraw) the current screen
                        刷新当前画面
^Z                      Suspend the editor (if suspend is enabled)
                        暂停编辑器(如果启用了暂停)

(M-X)                   Help mode enable/disable
                        辅助模式 启用/关闭
(M-C)                   Constant cursor position display enable/disable
                        持续显示游标位置 启用/关闭
(M-O)                   Use of one more line for editing enable/disable
                        编辑多行 启用/关闭
(M-S)                   Smooth scrolling enable/disable
                        平滑式卷动画面 启用/关闭
(M-P)                   Whitespace display enable/disable
                        显示空格 启用/关闭
(M-Y)                   Color syntax highlighting enable/disable
                        语法色彩高亮 启用/关闭
(M-H)                   Smart home key enable/disable
                        智能HOME键 启用/关闭
(M-I)                   Auto indent enable/disable
                        自动缩进 启用/关闭
(M-K)                   Cut to end enable/disable
                        剪切至行尾 启用/关闭
(M-L)                   Long line wrapping enable/disable
                        长行转换 启用/关闭
(M-Q)                   Conversion of typed tabs to spaces enable/disable
                        输入的制表符转换为空格 启用/关闭
(M-B)                   Backup files enable/disable
                        备份文件 启用/关闭
(M-F)                   Multiple file buffers enable/disable
                        多重文件缓冲区 启用/关闭
(M-M)                   Mouse support enable/disable
                        鼠标支持 启用/关闭
(M-N)                   No conversion from DOS/Mac format enable/disable
                        不从 DOS/Mac 格式转换 启用/关闭
(M-Z)                   Suspension enable/disable
                        暂停 启用/关闭
(M-$)                   Soft line wrapping enable/disable
                        软换行 启用/关闭
```

\*Putty下左键按下并拖动即复制文本，按下右键即粘贴；
Ubuntu下左键按下并拖动即复制文本，按下鼠标中键即粘贴。\*

