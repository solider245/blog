---
title: bash终端技巧大全
date: 2020-10-12 12:09:51
permalink: /pages/0579c7/
categories:
  - linux
  - 常用命令
tags:
  - 
---
#

方便的 Bash 终端技巧大集合

[67](javascript:;) [83](javascript:;) [9](#replies "评论")[](javascript:void(); "内容目录")[

](https://learnku.com/topics/35317/patches/create "发现错别字？请点此纠错改进")

[英文原文](https://github.com/onceupon/Bash-OneLiner) / [翻译](https://learnku.com/laravel/c/translations) / 3390 / 9 / 发布于 8个月前 / [1 个改进](https://learnku.com/laravel/t/35317/patches)

[](javascript:void(0);)

*   Bash 集合

*   方便的 bash 一行命令
*   终端技巧
*   筛选
*   流编辑器
*   Awk
*   Xargs
*   Find（查询）
*   Condition and loop (条件与循环)
*   变量
*   数学
*   Time
*   Download
*   随机
*   Xwindow
*   系统
*   硬件
*   网络
*   其他

[![](https://cdn.learnku.com/uploads/images/201909/28/26855/QnIC9zw12X.jpeg!large)

](https://cdn.learnku.com/uploads/images/201909/28/26855/QnIC9zw12X.jpeg!large)

# Bash 集合[#](#10a2d1)

我很高兴你在这里！几年前我从事生物信息学方面的研究工作。对那些简单的 bash 命令感到惊讶，他们比我的枯燥脚本快很多。通过学习命令行的快捷方式和脚本帮助我节省了很多时间。近年来，我从事云计算相关的工作，并在这里继续记录那些有用的命令。并且我在努力的使他们简短而且迅速。我主要使用 Ubuntu，RedHat ，Linux Mint 以及 CentOS 系统，如果命令在您的系统上不生效，那么我很抱歉。

该博客将重点介绍我从工作以及 LPIC 的考试中获得的用于解析数据和 Linux 系统维护的简单命令，但是他们可能来自于亲爱的 Google 和 Stackoverflow。

英语和 bash 并不是我的母语，请随时纠正我，谢谢。如果你知道其他有趣的命令，请教教我。

这是更新潮的版本 [Bash\-Oneliner](https://onceupon.github.io/Bash-Oneliner/)~

## 方便的 bash 一行命令[#](#1d8669)

*   [终端技巧](https://github.com/onceupon/Bash-OneLiner#terminal-tricks)
*   [变量](https://github.com/onceupon/Bash-OneLiner#variable)
*   [Grep 命令](https://github.com/onceupon/Bash-OneLiner#grep)
*   [Sed 命令](https://github.com/onceupon/Bash-OneLiner#sed)
*   [Awk 命令](https://github.com/onceupon/Bash-OneLiner#awk)
*   [Xargs 命令](https://github.com/onceupon/Bash-OneLiner#xargs)
*   [Find 命令](https://github.com/onceupon/Bash-OneLiner#find)
*   [条件和循环](https://github.com/onceupon/Bash-OneLiner#condition-and-loop)
*   [数学](https://github.com/onceupon/Bash-OneLiner#math)
*   [时间](https://github.com/onceupon/Bash-OneLiner#time)
*   [下载](https://github.com/onceupon/Bash-OneLiner#download)
*   [随机](https://github.com/onceupon/Bash-OneLiner#random)
*   [Xwindow 工具](https://github.com/onceupon/Bash-OneLiner#xwindow)
*   [系统](https://github.com/onceupon/Bash-OneLiner#system)
*   [硬件](https://github.com/onceupon/Bash-OneLiner#hardware)
*   [联网](https://github.com/onceupon/Bash-OneLiner#networking)
*   [其他](https://github.com/onceupon/Bash-OneLiner#others)

## 终端技巧[#](#515390)

##### 使用 Ctrl 键[#](#90d90c)

```php
Ctrl + n : 类似向下的键
Ctrl + p : 类似向上的键
Ctrl + r : 反向搜索命令的历史记录（按住 Ctrl + r )
Ctrl + s : 终端停止输出.（译者注：如 apt / yum，nload，watch 等，按 Enter 继续输出）
Ctrl + q : 在 Ctrl + s 之后重新恢复之前的 terminal.
Ctrl + a : 移动光标到行的开始处
Ctrl + e : 移动光标到行的结尾处
Ctrl + d : 如果当前的 terminal 命令行有输入，Ctrl + d 或删除光标处的字符，否则会退出当前的 terminal
Ctrl + k : 删除从当前光标到结尾的所有字符
Ctrl + x + backspace : 删除当前光标到行开始的所有字符
Ctrl + t : 交换当前光标下的字符和其前面字符的位置。Esc + t 交换光标前面的两个单词
Ctrl + w : 剪切光标之前的单词，然后 Ctrl + y 粘贴它
Ctrl + u : 剪切光标之前的行; 然后 Ctrl + y 粘贴它
Ctrl + _ : 撤销之前的操作
Ctrl + l : 相当于清除
Ctrl + x + Ctrl + e : 召唤起 $EDITOR 环境变量设置的编辑器程序，对多行命令有效

```

##### 更改大小写[#](#d727dd)

```shell
Esc + u
# 将文本从光标的开始到结尾的单词转换为大写
Esc + l
# 将文本从光标的开始到结尾的单词转换为小写
Esc + c
# 将光标下的字母转换为大写
```

##### 运行历史记录编号 (例如 e.g. 53)[#](#ebc6b0)

```shell
!53
```

##### 运行最后一条命令[#](#3079f8)

```shell
!!
```

##### 运行最后一个命令并且使用参入号替换之前运行的参数 (例如最后一个命令 : echo 'aaa' \-> 现在运行: echo 'bbb')[#](#313448)

```shell
#最后的一条命令: echo 'aaa'
^aaa^bbb

#echo 'bbb'
#bbb

#注意只有唯一的第一个 aaa 将会被替代，如果你想替代所有的 aaa，使用「:&」替代：
^aaa^bbb^:&
#或者
!!:gs/aaa/bbb/

```

##### 运行以开头的命令 (e.g. cat 文件名)[#](#a45d04)

```shell
!cat
# 或者
!c
#再次运行cat文件名
```

##### Bash 通配符[#](#7606af)

```shell
# '*' 用作文件名扩展的 "通配符" 。
/b?n/?at      #/bin/cat

# '?' 用作文件名扩展的单字符 "通配符" 。
/etc/pa*wd    #/etc/passwd

# ‘[]’ 用于匹配范围内的字符。
ls -l [a-z]*   #列出所有文件名中带有字母的文件。

# ‘{}’ 可用于匹配多个模式的文件名
ls {*.sh,*.py}   #列出所有.sh和.py文件
```

##### 一些方便的环境变量[#](#44bf14)

```php
$0   :shell或shell脚本的名称。
$1, $2, $3, ... :位置参数。
$#   :位置参数的数量。
$?   :最新的管道退出状态。
$-   :为shell设置的当前选项。
$$   :当前shell（不是subshell）的pid。
$!   :最新后台命令的PID。

$DESKTOP_SESSION     当前显示管理器
$EDITOR   首选文本编辑器。
$LANG   当前语言。
$PATH   搜索可执行文件的目录列表（即准备运行的程序）
$PWD    当前目录
$SHELL  当前 shell
$USER   当前用户名
$HOSTNAME   当前主机名
```

## 筛选[#](#c2fe62)

\[[返回顶部](https://learnku.com/laravel/t/35317#top)\]

##### 筛选类型[#](#8d8469)

```shell
grep = grep -G # Basic Regular Expression (BRE)
fgrep = grep -F # fixed text, ignoring meta-charachetrs
egrep = grep -E # Extended Regular Expression (ERE)
pgrep = grep -P # Perl Compatible Regular Expressions (PCRE)
rgrep = grep -r # recursive
```

##### 筛选并计算空行数[#](#eb1e87)

```shell
grep -c "^$"
```

##### 筛选且仅返回整数[#](#71ed8b)

```shell
grep -o '[0-9]*'
#or
grep -oP '\d'
```

##### 筛选带一定位数的整数（例如 3）[#](#be92fa)

```shell
grep ‘[0-9]\{3\}’
# or
grep -E ‘[0-9]{3}’
# or
grep -P ‘\d{3}’
```

##### 筛选仅 IP 地址[#](#c57726)

```shell
grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
# or
grep -Po '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
```

##### 筛选整个单词（例如 “target” ）[#](#7f1eb5)

```shell
grep -w 'target'

#or using RE
grep '\btarget\b'
```

##### 筛选匹配前后返回的行（例如 “bbo”）[#](#85c355)

```shell
# return also 3 lines after match
grep -A 3 'bbo'

# return also 3 lines before match
grep -B 3 'bbo'

# return also 3 lines before and after match
grep -C 3 'bbo'
```

##### 查找开始字符（例如 “S”）[#](#a949ab)

```shell
grep -o 'S.*'
```

##### 单词中截取文本（例如 w1，w2 ）[#](#549f9b)

```shell
grep -o -P '(?<=w1).*(?=w2)'
```

##### 查找不包含单词的行（例如 bbo ）[#](#9ea8f5)

```shell
grep -v bbo filename
```

##### 查找不以某字符串开头的行（例如 # ）[#](#620727)

```shell
grep -v '^#' file.txt
```

##### 查找变量（例如 bbo="some strings" ）[#](#e28637)

```shell
grep "$boo" filename
#remember to quote the variable!
```

##### 查找仅有一个或者第一个匹配（例如 bbo ）[#](#6279cb)

```shell
grep -m 1 bbo filename
```

##### 查找并返回匹配的行数（例如 bb ）[#](#1c089f)

```shell
grep -c bbo filename
```

##### 出现次数 （例如一行出现 3 次则记为 3 次）[#](#02b114)

```shell
grep -o bbo filename |wc -l
```

##### 区分大小写查找（例如 bbo/BBO/Bbo ）[#](#265924)

```shell
grep -i "bbo" filename
```

##### 匹配颜色标记（例如 bbo )[#](#124f87)

```shell
grep --color bbo filename
```

##### 查找文件夹内所有文件（例如 bbo ）[#](#090651)

```shell
grep -R bbo /path/to/directory
# or
grep -r bbo /path/to/directory
```

##### 查找文件夹内所有文件，不输出文件名（例如 bbo ）[#](#ceb522)

```shell
grep -rh bbo /path/to/directory
```

##### 查找文件夹内所有文件，**只**输出匹配的文件名（例如 bbo ）[#](#2e1ea2)

```shell
grep -rl bbo /path/to/directory
```

##### 或查找（例如 A 或 B 或 C 或 D ）[#](#67542a)

```php
grep 'A\|B\|C\|D'

```

##### 与查找（例如 A 与 B ）[#](#930136)

```shell
grep 'A.*B'
```

##### 正则匹配任意字符（例如 ACB 或 AEB ）[#](#bf0ccf)

```shell
grep 'A.B'
```

##### 正则匹配一个确定或者不确定的字符（例如 color 或 colour ）[#](#5f4cc2)

```shell
grep ‘colou?r’
```

##### 在文件 B 中查找文件 A 的内容[#](#58b558)

```shell
grep -f fileA fileB
```

##### 查找制表符[#](#028f70)

```shell
grep $'\t'
```

##### 在一个变量中查找另一个变量[#](#06fca3)

```shell
$echo "$long_str"|grep -q "$short_str"
if [ $? -eq 0 ]; then echo 'found'; fi
#grep -q will output 0 if match found
#remember to add space between []!
```

##### 查找括号内的内容[#](#8e222c)

```shell
grep -oP '\(\K[^\)]+'
```

##### 数字字符范围查找（例如 AAEL0000\-RA ）[#](#b5af18)

```shell
grep -o -w "\w\{10\}\-R\w\{1\}"
# \w 文字字符 [0-9a-zA-Z_] \W 非文字字符
```

##### 跳过文件目录（例如 bbo ）[#](#d27597)

```shell
grep -d skip 'bbo' /path/to/files/*
```

## 流编辑器[#](#2fc191)

\[[返回顶部](https://learnku.com/laravel/t/35317#top)\]

##### 删除第一行[#](#a651c6)

```shell
sed 1d filename
```

##### 删除前 100 行（删除第 1\-100 行）[#](#e3ce1e)

```shell
sed 1,100d filename
```

##### 删除带字符串的行 (例如： bbo)[#](#7b041d)

```shell
sed "/bbo/d" filename
- case insensitive:
sed "/bbo/Id" filename
```

##### 删除第 n 个字符不等于值的行（例如第 5 个字符不等于 2）[#](#e86208)

```shell
sed -E '/^.{5}[^2]/d'
#aaaa2aaa (you can stay)
#aaaa1aaa (delete!)
```

##### 编辑内嵌（编辑并保存）[#](#6568c5)

```shell
sed -i "/bbo/d" filename
```

##### 使用变量（例如 $i）时，请使用双引号 " "[#](#8201b7)

```shell
# e.g. add >$i to the first line (to make a bioinformatics FASTA file)
sed "1i >$i"
# notice the double quotes! in other examples, you can use a single quote, but here, no way!
# '1i' means insert to first line
```

##### 同时使用环境变量和尾符号[#](#b1691a)

```shell
# 使用反斜杠 $ 符，同时使用双引号来标记变量
sed -e "\$s/\$/\n+--$3-----+/"
```

##### 删除空行[#](#9e7977)

```shell
sed '/^\s*$/d'

# 或

sed '/^$/d'
```

##### 删除最后一行[#](#35f5d6)

```shell
sed '$d'
```

##### 删除文件的最后一个字符[#](#74a9fe)

```shell
sed -i '$ s/.$//' filename
```

##### 文件头部添加字符（例如『\[』）[#](#145bb4)

```shell
sed -i '1s/^/[/' file
```

##### 指定的行增加字符串（例如添加「 something 」到第 1 行和第 3 行）[#](#f14ea7)

```shell
sed -e '1isomething -e '3isomething'
```

##### 添加字符串到文件的结尾（例如『\]』）[#](#b01311)

```shell
sed '$s/$/]/' filename
```

##### 添加新行到结尾[#](#38d975)

```shell
sed '$a\'
```

##### 添加字符串到没一行（例如 bbo）[#](#03700d)

```shell
sed -e 's/^/bbo/' file
```

##### 添加字符串到没一行的结尾（例如『}』）[#](#fb55a9)

```shell
sed -e 's/$/\}\]/' filename
```

##### 每第 n 个字符添加 \\n (例如每四个字符 t 添加 \\n)[#](#e1bd65)

```shell
sed 's/.\{4\}/&\n/g'
```

##### 使用分隔符和下一行 连接 / 结合 / 合并文件。例如 (用「,」去分割)[#](#17a26c)

```shell
sed -s '$a,' *.json > all.json
```

##### 替换 (例如用 B 去替换 A)[#](#d37416)

```shell
sed 's/A/B/g' filename
```

##### 使用通配符进行替换 (例如 aaa = 开头的行替换成 aaa=/my/new/path)[#](#fe2066)

```shell
sed "s/aaa=.*/aaa=\/my\/new\/path/g"
```

##### 选择以字符串开头的行 (例如 bbo)[#](#fbba6d)

```shell
sed -n '/^@S/p'
```

##### 删除带有字符串的行[#](#5964f5)

```shell
sed '/bbo/d' filename
```

##### 打印 / 获取 / 截取一定范围内的行 (例如 500\-5000 之间)[#](#0b3c7b)

```shell
sed -n 500,5000p filename
```

##### 每 n 行打印一次[#](#9ecb78)

```shell
sed -n '0~3p' filename

# catch 0: start; 3: step
```

##### 打印所有奇数行[#](#41a1e7)

```shell
sed -n '1~2p'
```

##### 每隔三行打印一次，包括第一行[#](#7d3d83)

```shell
sed -n '1p;0~3p'
```

##### 删除前导空格和制表符[#](#5cc07b)

```shell
sed -e 's/^[ \t]*//'
# Notice a whitespace before '\t'!!
```

##### 只删除前导空格[#](#60599b)

```shell
sed 's/ *//'

# 注意'*'前的空格!!
```

##### 删除结尾逗号[#](#bb0389)

```shell
sed 's/,$//g'
```

##### 在结尾添加一列[#](#6eb79b)

```shell
sed "s/$/\t$i/"
# $i 是你要添加的值

# 将文件名添加到文件的最后一列
for i in $(ls);do sed -i "s/$/\t$i/" $i;done
```

##### 将文件的扩展名添加到最后一列[#](#5a7622)

```shell
for i in T000086_1.02.n T000086_1.02.p;do sed "s/$/\t${i/*./}/" $i;done >T000086_1.02.np
```

##### 删除换行符[#](#67b7c2)

```shell
sed ':a;N;$!ba;s/\n//g'
```

##### 打印某一行 (例如：第 123 行)[#](#4c4a4c)

```shell
sed -n -e '123p'
```

##### 打印若干行 (例如：第 10 行到第 33 行)[#](#353ab0)

```shell
sed -n '10,33p' <filename
```

##### 改变分隔符[#](#df211f)

```shell
sed 's=/=\\/=g'
```

##### 使用通配符替换 (例如: `A-1-e` 、 `A-2-e` 或者 `A-3-e` ....)[#](#d6f880)

```shell
sed 's/A-.*-e//g' filename
```

##### 删除文件的最后一个字符[#](#74a9fe)

```shell
sed '$ s/.$//'
```

##### 在文件的指定位置插入字符 (例如: AAAAAA—> AAA#AAA)[#](#13be97)

```shell
sed -r -e 's/^.{3}/&#/' file
```

## Awk[#](#742784)

\[[返回顶部](https://github.com/onceupon/Bash-OneLiner#handy-bash-one-liners)\]

##### 设置 tab 为分隔符[#](#67d6b3)

```shell
awk -F $'\t'
```

##### 设置 tab 为输出字段分隔符[#](#5e8920)

```shell
awk -v OFS='\t'
```

##### 传递变量[#](#bf505b)

```shell
a=bbo;b=obb;
awk -v a="$a" -v b="$b" "$1==a && $10=b" filename
```

##### 输出行号和每行的字符数[#](#13e212)

```shell
awk '{print NR,length($0);}' filename
```

##### 输出列数[#](#9ecb20)

```shell
awk '{print NF}'
```

##### 调整列输出顺序[#](#18a8ec)

```shell
awk '{print $2, $1}'
```

##### 检查列中字符是否含有逗号（例如检查第一列）[#](#57a0a6)

```shell
awk '$1~/,/ {print}'
```

##### 切割字符，并循环输出[#](#d87a6f)

```shell
awk '{split($2, a,",");for (i in a) print $1"\t"a[i]}' filename
```

##### 在某个字符出现次数少于 N 次时，打印数据 (例如在 bbo 出现 7 次之后，停止输出数据)[#](#8c7117)

```shell
awk -v N=7 '{print}/bbo/&& --N<=0 {exit}'
```

##### 输出目录下所有为文件名和每个文件的最后一行[#](#33c1df)

```shell
ls|xargs -n1 -I file awk '{s=$0};END{print FILENAME,s}' file
```

##### 在列的前面加字符 （例如在第三列前面加 “chr”）[#](#ab400c)

```shell
awk 'BEGIN{OFS="\t"}$3="chr"$3'
```

##### 删除含有字符的行 (例如删除含有 bbo 的行)[#](#81a46c)

```shell
awk '!/bbo/' file
```

##### 删除最后一列[#](#6f206c)

```shell
awk 'NF{NF-=1};1' file
```

##### NR 和 FNR 的用法[#](#246f6e)

```shell
# 例如以下2个文件:
# fileA:
# a
# b
# c
# fileB:
# d
# e
awk 'print FILENAME, NR,FNR,$0}' fileA fileB
# fileA    1    1    a
# fileA    2    2    b
# fileA    3    3    c
# fileB    4    1    d
# fileB    5    2    e
```

##### 逻辑与[#](#7e035a)

```shell
# 比如下面这两个文件:
# 文件 A:
# 1    0
# 2    1
# 3    1
# 4    0
# 文件 B:
# 1    0
# 2    1
# 3    0
# 4    1

awk -v OFS='\t' 'NR=FNR{a[$1]=$2;next} NF {print $1,((a[$1]=$2)? $2:"0")}' fileA 文件 B
# 1    0
# 2    1
# 3    0
# 4    0
```

##### 将文件中所有的数字进行四舍五入操作[#](#879ab8)

```shell
awk '{while (match($0, /[0-9]+\[0-9]+/)){
    \printf "%s%.2f", substr($0,0,RSTART-1),substr($0,RSTART,RLENGTH)
    \$0=substr($0, RSTART+RLENGTH)
    \}
    \print
    \}'
```

##### 给每一行编码 / 索引[#](#bbf5b7)

```shell
awk '{printf("%s\t%s\n",NR,$0)}'
```

##### 将列数据分解为行[#](#69e84b)

```shell
#例如分开一下内容:
# David    cat,dog
# into
# David    cat
# David    dog

awk '{split($2,a,",");for(i in a)print $1"\t"a[i]}' file

# 详情介绍请点击这里:　http://stackoverflow.com/questions/33408762/bash-turning-single-comma-separated-column-into-multi-line-string
```

##### 平均一个文件 (每一行只能包含一个数字)[#](#69fa0d)

```shell
awk '{s+=$1}END{print s/NR}'
```

##### 以字符串开始打印字段 (例如 Linux)[#](#70a2b1)

```shell
awk '$1 ~ /^Linux/'
```

##### 排序一行数字 (例如 1 40 35 12 23 \-\-> 1 12 23 35 40)[#](#e9ea3a)

```shell
awk ' {split( $0, a, "\t" ); asort( a ); for( i = 1; i <= length(a); i++ ) printf( "%s\t", a[i] ); printf( "\n" ); }'
```

##### 减去之前的行值 (column6，它等于 column4 减去最后一列 5)[#](#b8011a)

```shell
awk '{$6 = $4 - prev5; prev5 = $5; print;}'
```

## Xargs[#](#746e99)

\[[回到顶部](https://github.com/onceupon/Bash-OneLiner#handy-bash-one-liners)\]

##### 将选项卡设置为分隔符 (默认：空格)[#](#89fdf0)

```shell
xargs -d\t
```

##### 每行显示三个项目[#](#d0a4de)

```shell
echo 1 2 3 4 5 6| xargs -n 3
# 1 2 3
# 4 5 6

```

##### 提示在执行之前[#](#9bad0f)

```shell
echo a b c |xargs -p -n 3
```

##### 打印命令和输出[#](#cbe216)

```shell
xargs -t abcd
# bin/echo abcd
# abcd

```

##### 查找且删除[#](#c2f3eb)

```shell
find . -name "*.html"|xargs rm

# when using a backtick
rm `find . -name "*.html"`
```

##### 删除文件名中有空格的文件 (例如 「hello 2001」)[#](#32f449)

```shell
find . -name "*.c" -print0|xargs -0 rm -rf
```

##### 显示限制[#](#933467)

```shell
xargs --show-limits
```

##### 从文件夹中移除文件[#](#709916)

```shell
find . -name "*.bak" -print 0|xargs -0 -I {} mv {} ~/old

# or
find . -name "*.bak" -print 0|xargs -0 -I file mv file ~/old
```

##### 将第 100 个文件移到另一个目录[#](#74b0b4)

```shell
ls |head -100|xargs -I {} mv {} d1
```

##### 平行[#](#b08c7e)

```shell
time echo {1..5} |xargs -n 1 -P 5 sleep

# a lot faster than:
time echo {1..5} |xargs -n1 sleep
```

##### 将所有文件从 A 复制到 B[#](#339181)

```shell
find /dir/to/A -type f -name "*.py" -print 0| xargs -0 -r -I file cp -v -p file --target-directory=/path/to/B

# v: verbose|
# p: keep detail (e.g. owner)
```

##### sed 相关[#](#753159)

```shell
ls |xargs -n1 -I file sed -i '/^Pos/d' filename
```

##### 在文件的第一行增加文件的名称[#](#7c47c1)

```shell
ls |sed 's/.txt//g'|xargs -n1 -I file sed -i -e '1 i\>file\' file.txt
```

##### 统计所有的文件[#](#12462b)

```shell
ls |xargs -n1 wc -l
```

##### 将输出变成一行[#](#b18ddb)

```shell
ls -l| xargs
```

##### 对目录中的文件进行统计[#](#e284a2)

```shell
echo mso{1..8}|xargs -n1 bash -c 'echo -n "$1:"; ls -la "$1"| grep -w 74 |wc -l' --
# "--" 信号选项结束，并进一步进行选项的处理
```

##### 计算所有文件中的行数，也统计总行数。[#](#03dc9c)

```shell
ls|xargs wc -l
```

##### Xargs 以及 grep 命令[#](#3fc94a)

```shell
cat grep_list |xargs -I{} grep {} filename
```

##### Xargs 和 sed 命令 (将所有旧的 ip 地址替换成在 etc 文件下面新的 ip 地址)[#](#9c4ccb)

```shell
grep -rl '192.168.1.111' /etc | xargs sed -i 's/192.168.1.111/192.168.2.111/g'
```

## Find（查询）[#](#53b7d7)

\[[返回顶部](https://learnku.com/laravel/t/35317#top)\]

##### 列出当前目录中的所有子目录 / 文件[#](#41aecd)

```shell
find .
```

##### 列出当前目录下的所有文件[#](#68bf2b)

```shell
find . -type f
```

##### 列出当前文件下的所有目录[#](#da710c)

```shell
find . -type d
```

##### 编辑当前目录下的所有文件（例如，将 “www” 替换为 “ww”）[#](#da757b)

```shell
find . -name '*.php' -exec sed -i 's/www/w/g' {} \;

# 如果没有子目录
replace "www" "w" -- *
# a space before *
```

##### 查询文件 并 打印文件名（例如 “mso”）[#](#6fce98)

```shell
find mso*/ -name M* -printf "%f\n"
```

##### 查找 并 删除 文件大小 小于（例如 74 字节）的文件[#](#f6e422)

```shell
find . -name "*.mso" -size -74c -delete

# M 代表 MB, 等等
```

## Condition and loop (条件与循环)[#](#818a86)

\[[返回顶部](https://learnku.com/laravel/t/35317#top)\]

##### If 语句[#](#0d73cc)

```shell
# 使用 if 和 else 来进行条件判断
if [[ "$c" == "read" ]]; then outputdir="seq"; else outputdir="write" ; fi

# 判断myfile是否包含字符串“test”
if grep -q hello myfile; then …

# 判断mydir 是否是一个目录, 修改 mydir 的内容 并且 执行其他操作:
if cd mydir; then
  echo 'some content' >myfile
else
  echo >&2 "Fatal error. This script requires mydir."
fi

# 判断 variable(变量)  是否为空
if [ ! -s "myvariable" ]
#返回指定对象的长度  如果是 "字符串"  返回 0.

# 判断文件是否存在
if [ -e 'filename' ]
then
  echo -e "file exists!"
fi

# 判断 myfile 文件是否存在   或者  myfile 连接是否存在
if [ -e myfile ] || [ -L myfile ]
then
  echo -e "file exists!"
fi

# 判断 变量 x  是否大于 等于 5
if [ "$x" -ge 5 ]; then …

#  在 bash/ksh/zsh 中 判断 变量 x 是否大于等于 5,:
if ((x >= 5)); then …

# 使用  (( ))(双括号) 进行数学运算  将u+2的计算结果赋值给  j
if ((j==u+2))

# 使用 [[ ]](双中括号)  进行数值比较   在[[]] 中 会将 特殊符号 自动转换为 比较符号 （例如  = 转换为 == ）
if [[ $age -gt 21 ]]
```

[代码已被折叠，点此展开](#)

[More if commands](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_07_01.html)

##### For 语法[#](#3bae28)

```shell
for i in $(ls); do echo file $i;done
#或者
for i in *; do echo file $i; done

# 按任意键继续执行遍历
for i in $(cat tpc_stats_0925.log |grep failed|grep -o '\query\w\{1,2\}');do cat ${i}.log; read -rsp $'Press any key to continue...\n' -n1 key;done

# 当按下一个键会逐行打印文件
oifs="$IFS"; IFS=$'\n'; for line in $(cat myfile); do ...; done
while read -r line; do ...; done <myfile

# If only one word a line, simply （ 遍历文件内容 一行一行的遍历）
for line in $(cat myfile); do echo $line; read -n1; done

#遍历一个数组
for i in "${arrayName[@]}"; do echo $i;done

```

##### While 语句，[#](#df1a5a)

```shell
# 文件的列减法 (例如 a 3 columns file)
while read a b c; do echo $(($c-$b));done < <(head filename)
#在两个 "<" 的中间有个空格

# 汇总 列 减法
i=0; while read a b c; do ((i+=$c-$b)); echo $i; done < <(head filename)

# 继续检查正在运行的进程（例如perl），并在启动后立即启动另一个新进程（例如python）。 （最好使用wait命令！Ctrl + F " wait"）
while [[ $(pidof perl) ]];do echo f;sleep 10;done && python timetorunpython.py
```

##### switch (case in bash)[#](#3bb985)

```shell
read type;
case $type in
  '0')
    echo 'how'
    ;;
  '1')
    echo 'are'
    ;;
  '2')
    echo 'you'
    ;;
esac
```

## 变量[#](#ddc7d2)

\[[返回顶部](https://learnku.com/laravel/t/35317#top)\]

##### 引号内变量解析[#](#f68b7e)

```shell
# foo=bar
 echo "'$foo'"
#'bar'
# 单引号/双引号  quotes around single quotes make the inner single quotes expand variables（在单引号内使用变量 变量会被解析）
```

##### 获取变量长度[#](#0a2635)

```shell
var="some string"
echo ${#var}
# 11
```

##### 获取变量的第一个字节[#](#29dbad)

```shell
var=string
echo "${var:0:1}"
#s

# or
echo ${var%%"${var#?}"}
```

##### 从第一位 或最后一位 开始删除变量中的 n 个字节[#](#41b0c4)

```shell
var="some string"
echo ${var:2}
#me string
```

##### 替换 (例如。删除第一个位置的 0)[#](#36cd54)

```shell
var="0050"
echo ${var[@]#0}
#050
```

##### 替换所有 (例如。将 字符 "a" 替换为 字符 ",")[#](#9368ff)

```shell
{var/a/,}
```

```shell
# 使用 grep
 test="god the father"
 grep ${test// /\\\|} file.txt
 # turning the space into 'or' (\|) in grep （在grep 的空间中将 替换   or 和 (\|) ）
```

##### 将变量中的字符串改为小写（参数扩展）[#](#7c7a5d)

```shell
var=HelloWorld
echo ${var,,}
helloworld
```

##### Expand and then execute variable/argument （先执行脚本进行赋值 再输出变量内容）[#](#194111)

```shell
cmd="bar=foo"
eval "$cmd"
echo "$bar" # foo
```

## 数学[#](#6e6583)

\[[back to top](https://github.com/onceupon/Bash-OneLiner#handy-bash-one-liners)\]

##### bash 中的算术展开 (运算符: +, \-, \*, /, %, 等等)[#](#669dd3)

```使用source或.执行shell脚本
#总结： a++ 先运算a，后a的值加1；++a，则相反，先加一，再参与运算。同理a--,与--a
echo $(( 10 + 5 ))  #15
x=1
echo $(( x++ )) #1 , 注意它仍然是1，因为它是后递增的
echo $(( x++ )) #2
echo $(( ++x )) #4 , 注意，它不是3，因为它是预增量
echo $(( x-- )) #4
echo $(( x-- )) #3
echo $(( --x )) #1
x=2
y=3
echo $(( x ** y )) #8
```

##### 打印出一个数的质因数 (比如： 50)[#](#c6b0d3)

```使用source或.执行shell脚本
factor 50
```

##### 用于产生从某个数到另外一个数之间的所有整数。 (比如： seq 10)[#](#27891e)

```使用source或.执行shell脚本
seq 10|paste -sd+|bc
```

##### 汇总一个文件（文件中每行仅包含一个数字）[#](#d6aafd)

```使用source或.执行shell脚本
awk '{s+=$1} END {print s}' filename
```

##### 列减法[#](#cdb516)

```使用source或.执行shell脚本
cat file| awk -F '\t' 'BEGIN {SUM=0}{SUM+=$3-$2}END{print SUM}'
```

##### 用 expr 进行简单数学运算[#](#f83a42)

```使用source或.执行shell脚本
expr 10+20 #30
expr 10\*20 #600
expr 30 \> 20 #1 (true)
```

##### 更多关于 BC 的数学运算[#](#fff071)

```使用source或.执行shell脚本
# 小数位数/有效数字
echo "scale=2;2/3" | bc
#.66

# 指数运算符
echo "10^2" | bc
#100

# 使用变量
echo "var=5;--var"| bc
#4
```

## Time[#](#a76d4e)

\[[back to top](https://github.com/onceupon/Bash-OneLiner#handy-bash-one-liners)\]

##### 返回执行命令所需的时间[#](#eb0d40)

```shell
time echo hi
```

##### 等待一段时间（例如 10 秒）[#](#ab4fc1)

```shell
sleep 10
```

##### 在一段时间后注销你的帐户（例如 10 秒）[#](#bdae3e)

```shell
TMOUT=10
# 一旦你设置了这个变量，注销计时器开始运行！
```

##### 设置您要运行命令的时长[#](#fad267)

```shell
# 仅仅运行 `sleep 10` 一秒。
timeout 1 sleep 10
```

##### 设置何时要运行命令（例如，从现在开始 1 分钟）[#](#0a0a00)

```shell
at now + 1min  # 时间单位可以是 minutes, hours, days, 或 weeks
⚠️: 命令将使用 /bin/sh
at> echo hihigithub >~/itworks
at> <EOT>   # 按 Ctrl + D 退出
job 1 at Wed Apr 18 11:16:00 2018
```

## Download[#](#801ab2)

\[[回到顶部](https://github.com/onceupon/Bash-OneLiner#handy-bash-one-liners)\]

##### 下载此 README.md 的内容 (你正在看的内容)[#](#9344be)

```shell
curl https://raw.githubusercontent.com/onceupon/Bash-Oneliner/master/README.md | pandoc -f markdown -t man | man -l -

# 或者 w3m (一种基于文本的浏览器和呼叫器)
curl https://raw.githubusercontent.com/onceupon/Bash-Oneliner/master/README.md | pandoc | w3m -T text/html

# 或者使用emacs (在emac文本编辑器中)
emacs --eval '(org-mode)' --insert <(curl https://raw.githubusercontent.com/onceupon/Bash-Oneliner/master/README.md | pandoc -t org)

# 或者使用 emacs (在终端上先按Ctrl+x，再按Ctrl+c退出)
emacs -nw --eval '(org-mode)' --insert <(curl https://raw.githubusercontent.com/onceupon/Bash-Oneliner/master/README.md | pandoc -t org)
```

##### 从一个页面上下载全部内容[#](#f5db5d)

```shell
wget -r -l1 -H -t1 -nd -N -np -A mp3 -e robots=off http://example.com

# -r: recursive and download all links on page递归并下载页面上所有链接
# -l1: only one level link仅一级链接
# -H: span host, visit other hosts跨越主机，访问其他主机
# -t1: numbers of retries重试次数
# -nd: don't make new directories, download to here不要创建新目录，下载到这里
# -N: turn on timestamp打开时间戳
# -nd: no parent没有父级
# -A: type (separate by ,)类型（以，豆号分隔）
# -e robots=off: ignore the robots.txt file which stop wget from crashing the site, sorry example.com忽略robots.txt文件，该文件阻止wget使网站崩溃，抱歉example.com
```

##### 将文件上传到 web 并下载 ([https://transfer.sh/](https://transfer.sh/))[#](#83eead)

```shell
#  上传文件 (例如： filename.txt):
curl --upload-file ./filename.txt https://transfer.sh/filename.txt
# 上面的命令将返回一个url，例如：https://transfer.sh/tG8rM/filename.txt

# 接下来您可以通过以下方式下载它:
curl https://transfer.sh/tG8rM/filename.txt -o filename.txt
```

##### 下载文件（如有需要）[#](#de3041)

```shell
data=file.txt
url=http://www.example.com/$data
if [ ! -s $data ];then
    echo "downloading test data..."
    wget $url
fi
```

##### Wget 命令获取文件名 (当文件名很长时)[#](#97bd4e)

```shell
wget -O filename "http://example.com"
```

##### Wget 命令 将文件保存到文件夹[#](#8285dc)

```shell
wget -P /path/to/directory "http://example.com"
```

##### 指示 curl 遵循任何重定向，直到到达最终目的地:[#](#442e65)

```shell
curl -L google.com
```

## 随机[#](#3bde44)

\[[back to top](https://github.com/onceupon/Bash-OneLiner#handy-bash-one-liners)\]

##### 随机生成密码（例如，生成 5 个长度为 13 的密码）[#](#867270)

```shell
sudo apt install pwgen
pwgen 13 5
#sahcahS9dah4a xieXaiJaey7xa UuMeo0ma7eic9 Ahpah9see3zai acerae7Huigh7
```

##### 从文件中随机选择 100 行[#](#bc446f)

```shell
shuf -n 100 filename
```

##### 随机排序[#](#ae974c)

```shell
for i in a b c d e; do echo $i; done| shuf
```

##### 随机选择在一定范围内的数字（例如，从 0\-100 内随机选择 15 个数字）[#](#dc98ba)

```shell
shuf -i 0-100 -n 15
```

##### 产生一个随机数[#](#9cc4fd)

```shell
echo $RANDOM
```

##### 产生一个 0\-9 内的随机数[#](#6d8967)

```shell
echo $((RANDOM % 10))
```

##### 产生一个 1\-10 内的随机数[#](#81c925)

```shell
echo $(((RANDOM %10)+1))
```

## Xwindow[#](#554971)

\[[回到顶部](https://github.com/onceupon/Bash-OneLiner#handy-bash-one-liners)\]

X11 GUI 应用程序！如果你对纯文本的环境感到厌烦，这里有一些适合你的 GUI 工具。

##### 启用 X11 转发，以便在服务器上使用图形应用程序。[#](#d3c8b8)

```shell
ssh -X user_name@ip_address

# 或者通过 xhost 设置
# --> Install the following for Centos:
# xorg-x11-xauth
# xorg-x11-fonts-*
# xorg-x11-utils
```

##### 小 xwindow 工具[#](#58e2c7)

```shell
xclock
xeyes
xcowsay
```

##### 从 ssh 服务器中打开图片 / 图像[#](#211e2d)

```shell
1\. ssh -X user_name@ip_address
2. apt-get install eog
3. eog picture.png
```

##### 在服务器上观看视频[#](#704b03)

```shell
1\. ssh -X user_name@ip_address
2. sudo apt install mpv
3. mpv myvideo.mp4
```

##### 在服务器上使用 gedit (GUI 编辑)[#](#b11dac)

```shell
1\. ssh -X user_name@ip_address
2. apt-get install gedit
3. gedit filename.txt
```

##### 从 ssh 服务器上打开 PDF[#](#e7dc15)

```shell
1\. ssh -X user_name@ip_address
2. apt-get install evince
3. evince filename.pdf
```

##### 从 ssh 服务器上使用谷歌浏览器[#](#2f2890)

```shell
1\. ssh -X user_name@ip_address
2. apt-get install libxss1 libappindicator1 libindicator7
3. wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
4. sudo apt-get install -f
5. dpkg -i google-chrome*.deb
6. google-chrome
```

## 系统[#](#8a8b89)

\[[back to top](https://github.com/onceupon/Bash-OneLiner#handy-bash-one-liners)\]

##### 跟踪服务的最新日志[#](#6a7156)

```shell
journalctl -u <service_name> -f
```

##### 消除僵尸进程[#](#cc0d6e)

```shell
# 僵尸进程已经死了，所以你不能杀死它。您可以消除通过杀死其父进程。
# 首先，找到僵尸进程的PID
ps aux| grep 'Z'
# 接下来发现僵尸的父进程的PID
pstree -p -s <zombie_PID>
# 然后你可以杀死它的父进程，你会发现僵尸进程已经不见了。
sudo kill 9 <parent_PID>
```

###### 显示内存使用情况[#](#77cc73)

```shell
free -c 10 -mhs 1
# 每隔1秒打印10次
```

##### 显示设备和分区的 CPU 和 IO 统计信息。[#](#7f3667)

```shell
#每秒刷新一次
iostat -x -t 1
```

##### 显示网络接口上的带宽使用情况（例如 enp175s0f0）[#](#2680c4)

```shell
iftop -i enp175s0f0
```

##### 告知系统已运行多长时间以及用户数量[#](#e4e245)

```shell
uptime
```

##### 检查是否是 root 用户运行[#](#1489ee)

```shell
if [ "$EUID" -ne 0 ]; then
        echo "Please run this as root"
        exit 1
fi
```

##### 更改 shell 用户 (例如： bonnie)[#](#ff7278)

```shell
chsh -s /bin/sh bonnie
# /etc/shells: valid login shells
```

##### 更改 root / 虚拟 root / 监狱 (e.g. 更改 root 为 newroot)[#](#4c5e53)

```shell
chroot /home/newroot /bin/bash

# To exit chroot
exit
```

##### 显示文件（例如 filename.txt）的文件状态（大小；访问、修改和更改时间等）[#](#4ebe07)

```shell
stat filename.txt
```

##### 当前进程的快照[#](#ff20b2)

```shell
ps aux
```

##### 显示进程树[#](#c28418)

```shell
pstree
```

##### 找到的最大进程数[#](#9b0910)

```shell
cat /proc/sys/kernel/pid_max
```

##### 打印或控制内核环缓冲区[#](#4f51b6)

```shell
dmesg
```

##### 查看 ip 地址[#](#fbe397)

```shell
$ip add show

# or
ifconfig
```

##### 打印以前和当前的 SysV 运行级别[#](#d1cec9)

```shell
runlevel

#或者
who -r
```

##### 改变 SysV 运行级别 (例如修改为 5)[#](#97b509)

```shell
init 5
#或者
telinit 5
```

##### 在所有运行级别上显示所有可用的服务[#](#b2d3bb)

```shell
chkconfig --list
# 相当于 ubntu 中 chkconfig 的 update-rc.d
```

##### 查看系统的版本[#](#26758a)

```shell
cat /etc/*-release
```

##### Linux 程序员的手册：文件系统的层次结构的说明[#](#73d7b0)

```shell
man hier
```

##### 控制系统和服务管理器[#](#03803d)

```shell
#  检查 cron 的状态
systemctl status cron.service

#  停止一个 cron 服务
systemctl stop cron.service
```

##### 任务列表[#](#ca27b7)

```shell
jobs -l
```

##### 运行一个修改优先级的程序 (例如 ./test.sh)[#](#27673b)

```shell
# 较好的值在 -20 （最有利）到 19 之间调整
# 应用程序越好，优先级越低
# 默认值:10 ,默认优先级:80

nice -10 ./test.sh
```

##### 导出路径[#](#e6f0df)

```shell
export PATH=$PATH:~/path/you/want
```

##### 让文件可执行[#](#9dddcc)

```shell
chmod +x filename
# 现在你可以执行 ./filename
```

##### 打印系统信息[#](#77cd53)

```shell
uname -a

# 检查系统硬件平台 (x86-64)
uname -i
```

##### 上网[#](#9cb9e1)

```shell
links www.google.com
```

##### 增加用户，设置密码[#](#d95eb0)

```shell
useradd username
passwd username
```

##### 编辑 bash 变量（例如显示整个路径）[#](#2f324e)

```shell
1\. joe ~/.bash_profile
2. export PS1='\u@\h:\w\$'
# $PS1 是一个定义命令提示符外观和样式的变量
3\. source ~/.bash_profile
```

##### 编辑环境设置 (例如 alias)[#](#847e52)

```shell
1\. joe ~/.bash_profile
2. alias pd="pwd" //no more need to type that 'w'!
3\. source ~/.bash_profile
```

##### 打印所有的别名[#](#f0ae6b)

```shell
alias -p
```

##### 无别名 (例如别名 ls='ls \-\-color=auto' 之后)[#](#bdf241)

```shell
unalias ls
```

##### 设置和取消设置 shell 选项[#](#9f7e96)

```shell
# 打印所有的 shell 选项
shopt

# 取消(或者停止)别名
shopt -u expand_aliases

# 设置(或者开始)别名
shopt -s expand_aliases
```

##### 列出环境变量 (例如 PATH)[#](#cf924d)

```shell
echo $PATH
#用冒号分隔的目录列表
```

##### 当前用户所有环境变量列表[#](#59ce43)

```shell
env
```

##### Unset 环境变量 (e.g. unset 变量 'MYVAR')[#](#830f41)

```shell
unset MYVAR
```

##### 显示区分格式[#](#696859)

```shell
lsblk
```

##### 通知系统分区表更改[#](#f93fdf)

```shell
partprobe
```

##### 软链接到 bin[#](#3458bf)

```shell
ln -s /path/to/program /home/usr/bin
# 必须是程序的绝对路径
```

##### 显示数据的十六进制视图[#](#4e2be3)

```shell
hexdump -C filename.class
```

##### 跳转到其他节点[#](#2c183c)

```shell
rsh node_name
```

##### 检查端口（占用的网络端口）[#](#428f65)

```shell
netstat -tulpn
```

##### 打印已解析的符号链接或着规范文件名[#](#fa8677)

```shell
readlink filename
```

##### 查找命令的类型及链接到的位置 (e.g. python)[#](#b1c3f8)

```shell
type python
# python 是 /usr/bin/python
# 这里有5中不同的类型，使用 'type -f' 标志进行检查
# 1\. alias    (shell alias)
# 2\. function (shell function, 也会打印函数主体)
# 3\. builtin  (shell builtin)
# 4\. file     (disk file)
# 5\. keyword  (shell reserved word)

# 你也可以使用 `which`
which python
# /usr/bin/python
```

##### 列出所有的函数名[#](#7c8785)

```shell
declare -F
```

##### 列出目录的大小信息[#](#8a767b)

```shell
du -hs .

# or
du -sb
```

##### 复制使用权限目录[#](#90e023)

```shell
cp -rp /path/to/directory
```

##### 储存当前目录[#](#a33031)

```shell
pushd .

# then pop
popd

#或着使用dirs显示当前所在目录的列表。
dirs -l
```

##### 显示磁盘使用情况[#](#01875e)

```shell
df -h

# 或者
du -h

#或者
du -sk /var/log/* |sort -rn |head -10
```

##### 显示当前运行状态[#](#7e19c7)

```shell
runlevel
```

##### 切换运行级别[#](#11ff2b)

```shell
init 3

#或者
telinit 3
```

##### 永久修改运行级别[#](#43700a)

```shell
1\. edit /etc/init/rc-sysinit.conf
2. env DEFAULT_RUNLEVEL=2
```

##### 切换 root 用户[#](#1fbf1d)

```shell
su
```

##### 切换其他用户[#](#40f296)

```shell
su somebody
```

##### 反馈用户状态信息[#](#245643)

```shell
repquota -auvs
```

##### 获取数据库中重要信息[#](#3de4c9)

```shell
getent database_name

# (e.g.  'passwd' 数据库)
getent passwd
# 列出所有用户帐户（所有本地帐户和LDAP）

# (e.g. 获取用户组列表)
getent group
# 在 'group' 数据库保存
```

##### 改变文件的权限[#](#d24610)

```shell
chown user_name filename
chown -R user_name /path/to/directory/
# 改变用户组名称
```

##### 挂载和取消挂载[#](#6abf28)

```shell
# 例如 挂载 /dev/sdb 到 /home/test
mount /dev/sdb /home/test

# 例如 取消挂载 /home/test
umount /home/test
```

##### 列出当前挂载细节[#](#51730d)

```shell
mount
# 或者
df
```

##### 列出当前用户名和用户编号[#](#0034a2)

```shell
cat /etc/passwd
```

##### 获取所有的用户名[#](#0b836a)

```shell
getent passwd| awk '{FS="[:]"; print $1}'
```

##### 展示所有的用户[#](#966083)

```shell
compgen -u
```

##### 展示所有组[#](#3b22f6)

```shell
compgen -g
```

##### 展示所有的用户组[#](#7497f1)

```shell
group username
```

##### 显示 uid，gid，用户组[#](#e314e4)

```shell
id username
```

##### 检测当前是否是 root[#](#51f443)

```shell
if [ $(id -u) -ne 0 ];then
    echo "You are not root!"
    exit;
fi
# 'id -u' output 0 if it's not root
```

##### 找出 CPU 信息[#](#bd664a)

```shell
more /proc/cpuinfo

# 或者
lscpu
```

##### 为用户设置配额 (例如磁盘软大小限制: 120586240; 硬限制: 125829120)[#](#19ccb4)

```shell
setquota username 120586240 125829120 0 0 /home
```

##### 显示用户配额[#](#6db14a)

```shell
quota -v username
```

##### 显示缓存中华当前库[#](#8467b5)

```shell
ldconfig -p
```

##### 打印共享库依赖项 (例如 for 'ls')[#](#60d335)

```shell
ldd /bin/ls
```

##### 检查用户登录[#](#6ea554)

```shell
lastlog
```

##### 编辑所有用户的路径[#](#a15099)

```shell
joe /etc/environment
#编辑这个文件
```

##### 显示和设置用户限制[#](#dbad82)

```shell
ulimit -u
```

##### 哪些端口正在监听来自网络的 TCP 连接[#](#941c03)

```shell
nmap -sT -O localhost
#notice that some companies might not like you using nmap
```

##### 打印内核 / 处理器的数量[#](#be9455)

```shell
nproc --all
```

##### 检查每一个核心状态[#](#f36f75)

```php
1\. top
2. press '1'

```

##### 展示任务和 PID[#](#0812ca)

```shell
jobs -l
```

##### 列出所有正在执行服务[#](#9bd9ed)

```shell
service --status-all
```

##### 计划关闭服务器[#](#5d808e)

```shell
shutdown -r +5 "Server will restart in 5 minutes. Please save your work."
```

##### 取消与预定关闭[#](#f6a5ef)

```shell
shutdown -c
```

##### 向所有用户广播[#](#d0b338)

```shell
wall -n hihi
```

##### 终止一个用户的所有进程[#](#f4e035)

```shell
pkill -U user_name
```

##### 终止程序的所有进程[#](#3affa9)

```shell
kill -9 $(ps aux | grep 'program_name' | awk '{print $2}')
```

##### 在服务器上设置 gedit 首选项[#](#83b2c9)

```php
# 你可能需要去安装以下软件:

apt-get install libglib2.0-bin;
# 或者
yum install dconf dconf-editor;
yum install dbus dbus-x11;

# 检查列表
gsettings list-recursively

# 修改一些设置
gsettings set org.gnome.gedit.preferences.editor highlight-current-line true
gsettings set org.gnome.gedit.preferences.editor scheme 'cobalt'
gsettings set org.gnome.gedit.preferences.editor use-default-font false
gsettings set org.gnome.gedit.preferences.editor editor-font 'Cantarell Regular 12'

```

##### 把用户增加到一个分组 (例如 把用户名为「nice」的永不添加到分组「docker」, 这样此用户就可以在不用 sudo 的情况下运行 docker)[#](#f6b641)

```shell
sudo gpasswd -a nice docker
```

##### 安装没有根目录的 python 包[#](#7b4c0d)

```shell
1\. pip 安装 --用户 package_name
2. 你可能需要将  ~/.local/bin/ 导出到  PATH: export PATH=$PATH:~/.local/bin/
```

##### 删除旧的 Linux 内核 (当 /boot 几乎满的时候...)[#](#69c2f3)

```shell
1\. uname -a  #检查当前内核，哪些是不能移除的
2\. sudo apt-get purge linux-image-X.X.X-X-generic  #替代掉旧的版本
```

##### 更改主机名[#](#2526b5)

```shell
sudo hostname your-new-name

#如果不起作用，也可以:
hostnamectl set-hostname your-new-hostname
# 然后检查:
hostnamectl
# 或者检查 /etc/hostname

# 如果一直不工作....,编辑：
/etc/sysconfig/network
/etc/sysconfig/network-scripts/ifcfg-ensxxx
#增加 主机名="你的新主机名称"
```

##### 安装包列表[#](#da368e)

```shell
apt list --installed

# 或者在 Red Hat:
yum list installed
```

##### 检查哪个文件使设备繁忙[#](#c71c7a)

```shell
lsof /mnt/dir
```

##### 当声音不工作的时候[#](#c349d8)

```shell
killall pulseaudio
# 然后按下 Alt-F2 并输入 pulseaudio
```

##### 当声音不工作的时候[#](#c349d8)

```shell
killall pulseaudio
```

##### 列出关于 SCSI 设备信息列表[#](#e87f48)

```shell
lsscsi
```

##### 设置你自己的 DNS 服务器教程[#](#e31355)

[http://onceuponmine.blogspot.tw/2017/08/se...](http://onceuponmine.blogspot.tw/2017/08/set-up-your-own-dns-server.html)

##### 创建一个简单守护进程的教程[#](#959203)

[http://onceuponmine.blogspot.tw/2017/07/cr...](http://onceuponmine.blogspot.tw/2017/07/create-your-first-simple-daemon.html)

##### 一个使用你的邮箱发送邮件的教程[#](#88f1e5)

[http://onceuponmine.blogspot.tw/2017/10/se...](http://onceuponmine.blogspot.tw/2017/10/setting-up-msmtprc-and-use-your-gmail.html)

##### 使用 telnet 去测试开放的端口，测试是否可以连接到服务器例如服务器 (192.168.2.106) 端口 (53)[#](#7efd24)

```shell
telnet 192.168.2.106 53
```

##### 改变网络最大可传输单位 (mtu) (例如修改到 9000)[#](#09630c)

```shell
ifconfig eth0 mtu 9000
```

##### 或者正在执行的进程 pid (例如 python)[#](#b5f433)

```shell
pidof python

# 或者
ps aux|grep python
```

##### NTP[#](#5c54cb)

```shell
# Start ntp:
ntpd

# 检查 ntp:
ntpq -p
```

##### 清除你服务器中不必要的文件[#](#f378ff)

```shell
sudo apt-get autoremove
sudo apt-get clean
sudo rm -rf ~/.cache/thumbnails/*

# 删除旧的内核
sudo dpkg --list 'linux-image*'
sudo apt-get remove linux-image-OLDER_VERSION
```

##### 增大调整根分区的大小 (根分区是 LVM 逻辑卷)[#](#6f3b99)

```shell
pvscan
lvextend -L +130G /dev/rhel/root -r
# 添加 -r 将在调整卷大小后增加到文件系统
```

##### 创建 UEFI 可引导 USB 驱动器 (比如；/dev/sdc1)[#](#58604d)

```shell
sudo dd if=~/path/to/isofile.iso of=/dev/sdc1 oflag=direct bs=1048576
```

##### 找到并删除包[#](#3ec6ab)

```shell
sudo dpkg -l | grep <package_name>
sudo dpkg --purge <package_name>
```

##### 创建 ssh 隧道[#](#85115d)

```shell
ssh -f -L 9000:targetservername:8088 root@192.168.14.72 -N
#-f: 在后台运行; -L: 监听; -N: 什么也不做
# 你计算机的9000端口现在已经连接上了目标服务器名字192.168.14.72的8088端口
# 所以你现在可以去打开浏览器输入localhost:9000去查看你的目标计算机的8088端口了
```

##### 获取进程的进程 ID (比如： sublime\_text)[#](#cd6177)

```shell
#pidof 获取进程id
pidof sublime_text

#pgrep, 你不必键入整个程序名
pgrep sublim

#pgrep, 如果找到进程，则返回1；如果没有此类进程，则返回0

pgrep -q sublime_text && echo 1 || echo 0

#top, 需要更长的时间

top|grep sublime_text
```

##### 服务器的一些基准测试工具[#](#83da7d)

[aio\-stress](https://openbenchmarking.org/test/pts/aio-stress) \- AIO benchmark. [bandwidth](https://zsmith.co/bandwidth.html) \- memory bandwidth benchmark. [bonnie++](https://www.coker.com.au/bonnie++/) \- hard drive and file system performance benchmark. [dbench](https://dbench.samba.org/) \- generate I/O workloads to either a filesystem or to a networked CIFS or NFS server. [dnsperf](https://www.dnsperf.com/) \- authorative and recursing DNS servers. [filebench](https://github.com/filebench/filebench) \- model based file system workload generator. [fio](https://linux.die.net/man/1/fio) \- I/O benchmark.  [fs\_mark](https://github.com/josefbacik/fs_mark) \- synchronous/async file creation benchmark. [httperf](https://github.com/httperf/httperf) \- measure web server performance. [interbench](https://github.com/ckolivas/interbench) \- linux interactivity benchmark. [ioblazer](https://labs.vmware.com/flings/ioblazer) \- multi\-platform storage stack micro\-benchmark. [iozone](http://www.iozone.org/) \- filesystem benchmark. [iperf3](https://iperf.fr/iperf-download.php) \- measure TCP/UDP/SCTP performance. [kcbench](https://github.com/knurd/kcbench) \- kernel compile benchmark, compiles a kernel and measures the time it takes. [lmbench](http://www.bitmover.com/lmbench/) \- Suite of simple, portable benchmarks. [netperf](https://github.com/HewlettPackard/netperf) \- measure network performance, test unidirectional throughput, and end\-to\-end latency. [netpipe](https://linux.die.net/man/1/netpipe) \- network protocol independent performance evaluator. [nfsometer](http://wiki.linux-nfs.org/wiki/index.php/NFSometer) \- NFS performance framework. [nuttcp](https://www.nuttcp.net/Welcome%20Page.html) \- measure network performance. [phoronix\-test\-suite](https://www.phoronix-test-suite.com/) \- comprehensive automated testing and benchmarking platform. [seeker](https://github.com/fidlej/seeker) \- portable disk seek benchmark. [siege](https://github.com/JoeDog/siege) \- http load tester and benchmark. [sockperf](https://github.com/Mellanox/sockperf) \- network benchmarking utility over socket API.  [spew](https://linux.die.net/man/1/spew) \- measures I/O performance and/or generates I/O load. [stress](https://people.seas.harvard.edu/~apw/stress/) \- workload generator for POSIX systems. [sysbench](https://github.com/akopytov/sysbench) \- scriptable database and system performance benchmark. [tiobench](https://github.com/mkuoppal/tiobench) \- threaded IO benchmark. [unixbench](https://github.com/kdlucas/byte-unixbench) \- the original BYTE UNIX benchmark suite, provide a basic indicator of the performance of a Unix\-like system. [wrk](https://github.com/wg/wrk) \- HTTP benchmark.

##### 显示上次登录用户的列表。[#](#69eb0c)

```shell
lastb
```

##### 显示当前登录用户的列表，打印他们的信息[#](#7a7831)

```shell
who
```

##### 显示谁登录以及他们在做什么[#](#bc971a)

```shell
w
```

##### 打印当前登录到当前主机的用户的用户名。[#](#adc575)

```shell
users
```

##### 在终止程序上停止跟踪一个文件[#](#eb2d59)

```shell
tail -f --pid=<PID> filename.txt
# 用程序的进程 ID 替换 <PID>
```

##### 列出所有已经启动的服务[#](#5e8a1e)

```shell
systemctl list-unit-files|grep enabled
```

## 硬件[#](#ed9beb)

\[[back to top](https://github.com/onceupon/Bash-OneLiner#handy-bash-one-liners)\]

##### 收集和总结机器的所有硬件信息[#](#cc9b6b)

```shell
lshw -json >report.json
# 其他的选项: [ -html ]  [ -short ]  [ -xml ]  [ -json ]  [ -businfo ]  [ -sanitize ] ,etc
```

##### 找出内存设备的细节[#](#b3b00d)

```shell
sudo dmidecode -t memory
```

##### 打印 CPU 硬件细节[#](#08da40)

```shell
dmidecode -t 4
#          类型   信息
#          0   BIOS
#          1   系统
#          2   基板
#          3   机壳
#          4   处理器
#          5   内存控制器
#          6   内存模块
#          7   缓存
#          8   端口连接器
#          9   系统槽
#         11   OEM 字符串
#         13   BIOS 语言
#         15   系统事件日志
#         16   物理内存数组
#         17   存储设备
#         18   32位内存错误
#         19   存储映射地址
#         20   存储设备映射地址
#         21   内置定位设备
#         22   便携式电池
#         23   系统重置
#         24   硬件安全性
#         25   系统电源控制
#         26   电压探头
#         27   冷却装置
#         28   温度探测器
#         29   电流探头
#         30   待外远程访问
#         31   引导完整性服务
#         32   系统启动
#         34   管理装置
#         35   管理设备组件
#         36   管理设备阈值数据
#         37   内存通道
#         38   IPMI 设备
#         39   电力供应
```

[代码已被折叠，点此展开](#)

##### 计算硬盘数量[#](#303faa)

```shell
lsscsi|grep SEAGATE|wc -l
# 或者
sg_map -i -x|grep SEAGATE|wc -l
```

##### 或者硬盘的 UUID (例如 sdb)[#](#8c6467)

```shell
blkid /dev/sdb
```

##### 打印所有硬盘的详细信息[#](#512c66)

```shell
lsblk -io KNAME,TYPE,MODEL,VENDOR,SIZE,ROTA
#其中 ROTA 表示旋转设备/旋转硬盘 (1 为真, 0 为假)
```

##### 列出所有的 PCI (外围设置互连) 设备[#](#51395c)

```shell
lspci
# 列出关于 NIC 信息
lspci | egrep -i --color 'network|ethernet'
```

##### 列出所有 USB 设备[#](#2433f1)

```shell
lsusb
```

##### Linux 模块[#](#2e1890)

```shell
# 显示 Linux 内核中模块状态
lsmod

# 从 Linux 内核中增加或者移除模块
modprobe

# 或者
# Remove a module
rmmod

# 插入模块
insmod
```

##### 控制 IPMI\-enabled 设备 (e.g. BMC)[#](#f50d0e)

```shell
# 远程查看服务器的电源状态
ipmitool -U <bmc_username> -P <bmc_password> -I lanplus -H <bmc_ip_address> power status

# 远程开启服务器
ipmitool -U <bmc_username> -P <bmc_password> -I lanplus -H <bmc_ip_address> power on

# 打开面板识别灯(默认 15秒)
ipmitool chassis identify 255

#或者服务器传感器温度
ipmitool sensors |grep -i Temp

# 重置 BMC
ipmitool bmc reset cold

# Prnt BMC 网络
ipmitool lan print 1

# 设置 BMC 网络
ipmitool -I bmc lan set 1 ipaddr 192.168.0.55
ipmitool -I bmc lan set 1 netmask 255.255.255.0
ipmitool -I bmc lan set 1 defgw ipaddr 192.168.0.1
```

## 网络[#](#7ddbe1)

\[[回到顶部](https://github.com/onceupon/Bash-OneLiner#handy-bash-one-liners)\]

##### 显示 IP 地址[#](#b70777)

```shell
ip a
```

##### 显示路由表[#](#3ff255)

```shell
ip r
```

##### 显示 ARP 缓存 (ARP 缓存显示你连接到的同一网络设备的 MAC 地址)[#](#dc12dc)

```shell
ip n
```

##### 增加临时 IP 地址 (重启后重置) (例如 增加 192.168.140.3/24 到 设备 eno16777736)[#](#f6a737)

```shell
ip address add 192.168.140.3/24 dev eno16777736
```

##### 持久化网络配置的更改[#](#0ec911)

```shell
sudo vi /etc/sysconfig/network-scripts/ifcfg-enoxxx
# 然后编辑字段: BOOTPROT, DEVICE, IPADDR, NETMASK, GATEWAY, DNS1 etc
```

##### 刷新 NetworkManager[#](#b02ddb)

```shell
sudo nmcli c reload
```

##### 重新启动所有界面[#](#55a65c)

```shell
sudo systemctl restart network.service
```

##### 同时查看 hostname, OS, kernal, architecture ![#](#ccc7d3)

```shell
hostnamectl
```

##### 设置主机名 (一次设置所有临时，静态，漂亮的主机名)[#](#5f7b51)

```shell
hostnamectl set-hostname "mynode"
```

## 其他[#](#0d98c7)

\[[回到顶部](https://github.com/onceupon/Bash-OneLiner#handy-bash-one-liners)\]

##### Bash 自动完成 (例如 当你输入「dothis」，然后按下 「tab」, 显示「now tomorrow never」)[#](#707f64)

[更多的案例](https://iridakos.com/tutorials/2018/03/01/bash-programmable-completion-tutorial.html)

```shell
完成 -W  "now tomorrow never" dothis
# ~$ dothis
# 从不     现在       明天
# 输入「n」或者「t」之后，再次按「tab」 键以自动完成
```

##### 重复打印字符串 n 次 (例如重复打印 5 次「hello world」)[#](#b5a571)

```shell
printf 'hello world\n%.0s' {1..5}
```

##### 将字符串编码为 Base64 的字符串[#](#6e6721)

```shell
echo test|base64
#dGVzdAo=
```

##### 不要显示末尾的换行符[#](#0aaad9)

```shell
username=`echo -n "bashoneliner"`
```

##### 或者当前目录的父级目录[#](#2fc30c)

```shell
dirname `pwd`
```

##### 将一个文件复制到多个文件 (例如复制文件 A 到文件 (B\-D))[#](#a29e88)

```shell
tee <fileA fileB fileC fileD >/dev/null
```

##### 删除换行符或者下一行[#](#ea93d4)

```shell
tr --delete '\n' <input.txt >output.txt
```

##### 换行[#](#2629bd)

```shell
tr '\n' ' ' <filename
```

##### 转换大写或者小写[#](#484f0c)

```shell
tr /a-z/ /A-Z/
```

##### 转换一系列的字符 (例如 把 a\-z 都转换为 a)[#](#4f31d3)

```shell
echo 'something' |tr a-z a
# aaaaaaaaa
```

##### 比较两个文件 (例如 fileA, fileB)[#](#561d56)

```shell
diff fileA fileB
# a: 被增加; d:删除; c:被修改

# 或者
sdiff fileA fileB
# 文件差异的并排合并
```

##### 比较两个文件，删除掉尾部回车 (例如 fileA, fileB)[#](#6a5098)

```shell
 diff fileA fileB --strip-trailing-cr
```

##### 给文件编号 (例如给 fileA 编号)[#](#18ace1)

```shell
nl fileA

#或者
nl -nrz fileA
# add leading zeros

#也可以
nl -w1 -s ' '
# making it simple, blank separate
```

##### 使用 tab 键按字段连接两个文件 (默认连接按照文件的第一列连接，默认分隔符是空格)[#](#46c344)

```shell
# 文件 A 和文件 B 应该有相同的行顺序
join -t '\t' fileA fileB

# 使用指定字段加入 (例如 文件 A 的第三列和文件 B 的第五列)
join -1 3 -2 5 fileA fileB
```

##### 将两个或多个文件合并 / 粘贴到列中 (例如 fileA, fileB, fileC)[#](#624378)

```shell
paste fileA fileB fileC
# 默认选项分开
```

##### 反向字符串[#](#73a4ce)

```shell
echo 12345| rev
```

##### 读取 .gz 文件但不解压[#](#7ce7de)

```shell
zmore filename

# 或者
zless filename
```

##### 在后台运行命令，输出错误文件[#](#dd4536)

```shell
some_commands  &>log &

# 或者
some_commands 2>log &

# 或者
some_commands 2>&1| tee logfile

# 或者
some_commands |& tee logfile

# 还可以
some_commands 2>&1 >>outfile
#0: 标准输入; 1: 标准输出; 2: 标准错误
```

##### 在后台运行多个命令[#](#74495c)

```shell
# 按顺序运行
(sleep 2; sleep 3) &

#并行运行
sleep 2 & sleep 3 &
```

##### 即便注销也可以运行进程 (immune to hangups, with output to a non\-tty)[#](#e74f21)

```shell
# 例如即便注销也会运行 myscript.sh 脚本
nohup bash myscript.sh
```

##### 发送邮件[#](#f4f76a)

```shell
下面是邮件的内容 -a /path/to/attach_file.txt -s 'mail.subject' me@gmail.com
# use -a flag to set send from (-a "From: some@mail.tld")
```

##### 将 .xls 转换为 csv[#](#bbc83b)

```shell
xls2csv filename
```

##### 附加到文件 (例如附加 hihi 内容到指定文件)[#](#ed933b)

```shell
echo 'hihi' >>filename
```

##### 制造 BEEP 的声音[#](#2e5fa4)

```shell
speaker-test -t sine -f 1000 -l1
```

##### 设置 beep 声音的持续时间[#](#fe3f2a)

```shell
(speaker-test -t sine -f 1000) & pid=$!;sleep 0.1s;kill -9 $pid
```

##### 历史记录 编辑 / 删除[#](#9a5f2b)

```shell
~/.bash_history

#或者
history -d [line_number]
```

##### 与历史记录的互动[#](#9c8666)

```shell
# list 5 previous command (similar to `history |tail -n 5` but wont print the history command itself)
fc -l -5
```

##### 或者文件最后的历史记录[#](#f116b9)

```shell
head !$
```

##### 清洁屏幕 (注：还挺好使)[#](#792082)

```shell
clear

# 或者
Ctrl+l
```

##### 将数据发送到上次编辑的文件[#](#2073fa)

```shell
cat /directory/to/file
echo 100>!$
```

##### 提取 .xf[#](#728a46)

```php
unxz filename.tar.xz
# 然后
tar -xf filename.tar

```

##### 安装 python 包[#](#21be77)

```shell
pip install packagename
```

##### 删除当前的 bash 命令[#](#e72c46)

```shell
Ctrl+U

# 或者
Ctrl+C

# 或者
Alt+Shift+#
# 成为历史
```

##### 向历史添加一些东西 (例如 「addmetohistory」)[#](#084da5)

```shell
# addmetodistory
# just add a "#" before~~
```

##### 睡眠一会或者稍等片刻或者安排工作[#](#5d3216)

```shell
sleep 5;echo hi
```

##### 使用 rsync 备份[#](#24e3b6)

```shell
rsync -av filename filename.bak
rsync -av directory directory.bak
rsync -av --ignore_existing directory/ directory.bak
rsync -av --update directory directory.bak

rsync -av directory user@ip_address:/path/to/directory.bak
#跳过接收器上更新的文件 (我更喜欢这个!)
```

##### 一次制作所有的目录！[#](#14d40c)

```shell
mkdir -p project/{lib/ext,bin,src,doc/{html,info,pdf},demo/stat}
# -p: 设置为父目录
# 这将制造 project/doc/html/; project/doc/info; project/lib/ext ,etc
```

##### 仅当另一个命令运行返回 0 退出状态的时候运行此命令 (命令完成)[#](#935b6e)

```shell
cd tmp/ && tar xvf ~/a.tar
```

##### 仅当另一个命令运行返回非 0 退出状态的时候运行此命令 (命令未完成)[#](#424628)

```shell
cd tmp/a/b/c ||mkdir -p tmp/a/b/c
```

##### 提取到路径[#](#97ce6b)

```shell
tar xvf -C /path/to/directory filename.gz
```

##### 使用反斜杆 "" 来中断长命令[#](#7b4336)

```shell
cd tmp/a/b/c \
> || \
>mkdir -p tmp/a/b/c
```

##### 得到 pwd[#](#286bdc)

```shell
VAR=$PWD; cd ~; tar xvf -C $VAR file.tar
# PWD 必须是大写字母
```

##### 列出文件的类型 (e.g./tmp/)[#](#04c927)

```shell
file /tmp/
# tmp/: directory
```

##### Bash 脚本[#](#b7947b)

```shell
#!/bin/bash
file=${1#*.}
# remove string before a "."
```

##### Python 简单的 HTTP 服务[#](#2e583c)

```shell
python -m SimpleHTTPServer
# 或者你使用 python3 的时候:
python3 -m http.server
```

##### 读取用户输入[#](#ea819d)

```shell
read input
echo $input
```

##### 生成序列 1\-10[#](#f117e2)

```shell
seq 10
```

##### 查找输入列表 / 文件的平均值[#](#ef9486)

```shell
i=`wc -l filename|cut -d ' ' -f1`; cat filename| echo "scale=2;(`paste -sd+`)/"$i|bc
```

##### 生成所有组合 (e.g. 1,2)[#](#37f1af)

```shell
echo {1,2}{1,2}
# 1 1, 1 2, 2 1, 2 2
```

##### 生成所有组合 (e.g. A,T,C,G)[#](#2a51af)

```shell
set = {A,T,C,G}
group= 5
for ((i=0; i<$group; i++));do
    repetition=$set$repetition;done
    bash -c "echo "$repetition""
```

##### 将文件内容读取到变量[#](#12fe40)

```shell
foo=$(<test1)
```

##### 输出变量[#](#91569f)

```shell
echo ${#foo}
```

##### 打印标签[#](#81a42c)

```shell
echo -e ' \t '
```

##### 数组[#](#0e67d4)

```shell
declare -a array=()

# 或者
declare array=()

# 或者关联数组
declare -A array=()
```

##### 发送一个目录[#](#4913af)

```shell
scp -r directoryname user@ip:/path/to/send
```

##### 将文件分割成较小的文件[#](#aaebfb)

```shell
# 按行分割 (e.g. 1000 lines/smallfile)
split -d -l 1000 largefile.txt

# 按字节分割而不会在文件间断行
split -C 10 largefile.txt
```

##### 创建大量的测试文件 (e.g 100000 个文件，10 字节分割):[#](#0bc420)

```shell
#1\. 创建文件
dd if=/dev/zero of=bigfile bs=1 count=1000000

#2\. 将大文件拆分为100000个10字节文件
 split -b 10 -a 10 bigfile
```

##### 重命名所有文件 (e.g. 将所有文件重命名为 ABC)[#](#e65fcf)

```shell
rename 's/ABC//' *.gz
```

##### 删除文件扩展名 (e.g 删除 filename.gz 的.gz)[#](#75e1b0)

```shell
basename filename.gz .gz

zcat filename.gz> $(basename filename.gz .gz).unpacked
```

##### 叉炸弹 (危险命令的意思)[#](#9fbf6b)

```shell
# 不要在家尝试这个正测试的时候，请移除它
# :(){:|:&};:
```

##### 将文件扩展名添加到所有文件 (例如添加 .txt)[#](#ad5b81)

```shell
rename s/$/.txt/ *
# 你可以使用重命名 -n s/$/.txt/ * 首先去检查结果,如果它仅仅打印这些:
# rename(a, a.txt)
# rename(b, b.txt)
# rename(c, c.txt)
```

##### 使用挤压重复选项 (例如 /t/t \-\-> /t)[#](#25be00)

```shell
tr -s "/t" < filename
```

##### 不要用 echo 打印 nextline[#](#1c5242)

```shell
echo -e 'text here \c'
```

##### 使用最后一个参数[#](#7bc609)

```shell
!$
```

##### 检查最后一个退出代码[#](#43937c)

```shell
echo $?
```

##### 查看文件的前 50 个字符[#](#38b9be)

```shell
head -c 50 file
```

##### 将两行组合成一行[#](#2ace09)

```shell
# 例如
# AAAA
# BBBB
# CCCC
# DDDD
cat filename|paste - -
# AAAABBBB
# CCCCDDDD
cat filename|paste - - - -
# AAAABBBBCCCCDDDD
```

##### Fastq 转 fasta[#](#7ba815)

```shell
cat file.fastq | paste - - - - | sed 's/^@/>/g'| cut -f1-2 | tr '\t' '\n' >file.fa
```

##### 剪切并得到最后一列[#](#d0fc3d)

```shell
cat file|rev | cut -d/ -f1 | rev
```

##### 在变量 / 增量 i++ 中添加一个变数字量 (例如 $val)[#](#fe9fe7)

```shell
((var++))
# 或者
var=$((var+1))

```

##### 清除文件中所有内容 (比如 filename)[#](#40ec7e)

```shell
>filename
```

##### 解压 tar.bz2 文件 (例如解压文件 file.tar.bz2)[#](#d58cff)

```shell
tar xvfj file.tar.bz2
```

##### 解压 tar.xz 文件 (例如解压 file.tar.xz)[#](#fcc90a)

```shell
unxz file.tar.xz
tar xopf file.tar
```

##### 重复输出 y/n 直到终止[#](#73a433)

```shell
# 'y':
yes

# 或者 'n':
yes n

# 或者 'anything':
yes anything

# 例如:
​```bash
yes | rm -r large_directory
```

##### 立即创建一定大小的虚拟文件 (例如 200mb)[#](#e1eefc)

```shell
dd if=/dev/zero of=//dev/shm/200m bs=1024k count=200
# 或者
dd if=/dev/zero of=//dev/shm/200m bs=1M count=200

# 标准输出:
# 200+0 条记录
# 200+0 记录出来
# 209715200 bytes (210 MB) copied, 0.0955679 s, 2.2 GB/s
```

##### 把文件归档[#](#d8e846)

```shell
cat >myfile
让我在这补充一下
exit by control + c
^C
```

##### 保持重复执行同一个命令 (例如 每一秒重复一次 'wc \-l filename')[#](#bd3896)

```shell
watch -n 1 wc -l filename
```

##### 执行时打印命令以及其参数 (例如 echo `expr 10 + 20 `)[#](#8438cc)

```shell
set -x; echo `expr 10 + 20 `
```

##### 为你打印一些有意义的句子 (首先安装 fortune)[#](#d46e14)

```shell
fortune
```

##### 丰富多彩的 (有用的) top 版本 (首先安装 htop)[#](#6e4e57)

```shell
htop
```

##### 按任意键继续[#](#62ab6e)

```shell
read -rsp $'Press any key to continue...\n' -n1 key
```

##### 从终端中运行类似 sql 的命令[#](#ea0c9c)

```shell
# 下载:
# https://github.com/harelba/q
# 例如:
q -d "," "select c3,c4,c5 from /path/to/file.txt where c3='foo' and c5='boo'"
```

##### 将 Screen 用于多个终端回话[#](#cc5d48)

```shell
# 创建会话并附加:
screen

# 创建分离的会话 foo:
screen -S foo -d -m

# 独立会话 foo:
screen: ^a^d

# 会话列表:
screen -ls

# 附加到上一个会话:
screen -r

# 附加到会话 foo:
screen -r foo

# 杀掉会话 foo:
screen -r foo -X quit

# 滚动:
点击屏幕前缀组合 (C-a / control+A),然后按下 Escape.
上下移动方向键(↑ and ↓).

# 重定向屏幕中已经运行进程的输出:
 (C-a / control+A), then hit 'H'

# 存储屏幕的屏幕实处:
Ctrl+A, Shift+H
# 然后再当前的目录下找到 screen.log 文件
```

##### 使用[#](#ecff77)

##### 将 Tmux 用于多个终端回话[#](#cb9404)

```shell
# 创建会话并附加:
tmux

# 附加到会话 foo:
tmux attach -t foo

# 分离的会话 foo:
^bd

# 会话列表:
tmux ls

# 附加上一个会话:
tmux attach

# 杀死会话 foo:
tmux kill-session -t foo

# 创建独立会话 foo:
tmux new -s foo -d

# 将命令发送到 tmux 的所有窗格:
Ctrl-B
:setw synchronize-panes

# 一些 tmux 窗格控制的命令:
Ctrl-B
#   窗格 (分割), 按下 Ctrl+B，然后输入以下字符:
#   %  horizontal split
#   "  vertical split
#   o  swap panes
#   q  show pane numbers
#   x  kill pane
#   空间 - 在布局之间进行切换

#   垂直分布 (行):
select-layout even-vertical
#   或者
Ctrl+b, Alt+2

# 垂直分布 (列):
select-layout even-horizontal
#   或者
Ctrl+b, Alt+1

# Scroll
Ctrl-b 然后 \[ 然后你可以使用你的正常方向键来滚动
Press q to quit scroll mode.
```

[代码已被折叠，点此展开](#)

##### 剪切最后一行[#](#7dd630)

```shell
cat filename|rev|cut -f1|rev
```

##### 将密码传输给 ssh[#](#53fbdf)

```shell
sshpass -p mypassword ssh root@10.102.14.88 "df -h"
```

##### 等待一个 pid (任务) 完成[#](#eeadee)

```shell
wait %1
# 或者
wait $PID
wait ${!}
#wait ${!} 要等待最后一个后台进程 ($! 为最后一个后台进程的 PIID)
```

##### 将 pdf 转换为 txt[#](#4bf29d)

```shell
sudo apt-get install poppler-utils
pdftotext example.pdf example.txt
```

##### 只列出目录[#](#279ae3)

```shell
ls -ld -- */
```

##### 捕获 /j 记录 / 保存终端输出 (捕获你输入和输出的所有内容)[#](#6a4c69)

```shell
script output.txt
# 开始使用终端l
# 退出屏幕会话 (停止保存内容), 退出.
```

##### 以树状格式列出目录的内容。[#](#93685b)

```shell
tree
# 转到要列出的目录，然后键入 tree (sudo apt-get install tree)
# output:
# home/
# └── project
#     ├── 1
#     ├── 2
#     ├── 3
#     ├── 4
#     └── 5
#

# 设置目录深度等级（例如1级）
tree -L 1
# home/
# └── project
```

##### 为 Python 设置 virtualenv（sandbox）[#](#ba4fca)

```shell
# 1\. 安装 virtualenv.
sudo apt-get install virtualenv
# 2\. 为新的隔离环境建立目录（将其命名为 .venv 或您想要的任何名称）。
virtualenv .venv
# 3\. 导入 virtual 执行目录
source .venv/bin/activate
# 4\. 您可以检查一下是否现在在沙盒中
type pip
# 5\. 现在您可以安装您的 pip 包, 这里的 requirements.txt 只是一个包含您想要的所有软件包的 txt 文件 (例如 tornado==4.5.3)。
pip install -r requirements.txt
```

##### 使用 json 数据[#](#b9d80a)

```shell
# 安装非常有用的 jq 包
#sudo apt-get install jq
#e.g. to get all the values of the 'url' key, simply pipe the json to the following jq command(you can use .[]. to select inner json, i.e jq '.[].url')
# 例如，要获取 url 键的所有值，只需将 json 通过管道传递给以下 jq 命令（您可以使用 [] 选择内部 json，即 jq '[].url'）
jq '.url'
```

##### 编辑 history[#](#516dfe)

```shell
history -w
vi ~/.bash_history
history -r
```

##### 十进制转换为二进制（例如，获取 5 的二进制 ）[#](#02dfb0)

```shell
D2B=({0..1}{0..1}{0..1}{0..1}{0..1}{0..1}{0..1}{0..1})
echo -e ${D2B[5]}
#00000101
echo -e ${D2B[255]}
#11111111
```

##### 把输入的行换行以适应指定的宽度 (例如每行 4 个整数)[#](#4acc1d)

```shell
echo "00110010101110001101" | fold -w4
# 0011
# 0010
# 1011
# 1000
# 1101
```

##### 按列对文件进行排序，并保持原始顺序[#](#533b6b)

```shell
sort -k3,3 -s
```

##### 列右对齐 (第二列右对齐)[#](#8e32e8)

```shell
cat file.txt|rev|column -t|rev
```

##### 查看和存储输出[#](#4efea8)

```shell
echo 'hihihihi' | tee outputfile.txt
# tee 带 “-a” 可以附加到文件中
```

##### 使用 cat 显示非打印（Ctrl）字符[#](#7461e0)

```shell
cat -v filename
```

##### 将制表符转换为空格[#](#a8bf39)

```shell
expand filename
```

##### 将空格转换为制表符[#](#56e281)

```shell
unexpand filename
```

##### 以八进制显示文件（您也可以使用 od 显示十六进制，十进制等）[#](#493d2b)

```shell
od filename
```

##### 反转 `cat` 的结果[#](#1d3cbb)

```shell
tac filename
```

##### 反转 `uniq -c` 的结果[#](#06e561)

```shell
while read a b; do yes $b |head -n $a ;done <test.txt
```

> 未来还有更多！

[bash](https://learnku.com/topics/tags/bash/183) [终端](https://learnku.com/topics/tags/terminal_XW/51864)

> 本文中的所有译文仅用于学习和交流目的，转载请务必注明文章译者、出处、和本文链接
> 我们的翻译工作遵照 [CC 协议](https://learnku.com/docs/guide/cc4.0/6589)，如果我们的工作有侵犯到您的权益，请及时联系我们。

---

> 原文地址：[https://github.com/onceupon/Bash\-OneLine...](https://github.com/onceupon/Bash-OneLiner)
>
> 译文地址：[https://learnku.com/laravel/t/35317](https://learnku.com/laravel/t/35317)