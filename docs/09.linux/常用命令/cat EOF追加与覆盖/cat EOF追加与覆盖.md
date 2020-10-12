---
title: cat EOF追加与覆盖
date: 2020-10-12 12:09:51
permalink: /pages/ae42b4/
categories:
  - 常用命令
  - cat EOF追加与覆盖
tags:
  - 
---
当需要将多行文件输入到文本时，如果每条都使用echo 到文件时是比较繁琐的，这种情况下可以使用cat EOF进行多行文件的覆盖或追加输入。

### 一、覆盖

这里有两种格式可以使用

**1、格式一**

#!/bin/bash
cat << EOF > /root/test.txt
Hello!
My site is www.361way.com
My site is www.91it.org
Test for cat and EOF!
EOF

**2、格式二**

#!/bin/bash
cat > /root/test.txt <<EOF
Hello!
My site is www.361way.com
My site is www.91it.org
Test for cat and EOF!
EOF

两种写法区别无法是要写入的文件放在中间或最后的问题，至于选哪种看个人喜好吧。

### 二、追加

覆盖的写法基本和追加一样，不同的是单重定向号变成双重定向号。

**1、格式一**

#!/bin/bash
cat << EOF >> /root/test.txt
Hello!
My site is www.361way.com
My site is www.91it.org
Test for cat and EOF!
EOF

**2、格式二**

#!/bin/bash
cat >> /root/test.txt <<EOF
Hello!
My site is www.361way.com
My site is www.91it.org
Test for cat and EOF!
EOF

需要注意的是，不论是覆盖还是追加，在涉及到**变量**操作时是需要进行转义的，例如：

#!/bin/bash
cat <<EOF >> /root/a.txt
PATH=\\$PATH:\\$HOME/bin
export ORACLE\_BASE=/u01/app/oracle
export ORACLE\_HOME=\\$ORACLE\_BASE/10.2.0/db\_1
export ORACLE\_SID=yqpt
export PATH=\\$PATH:\\$ORACLE\_HOME/bin
export NLS\_LANG="AMERICAN\_AMERICA.AL32UTF8"
EOF


如果不是在脚本中，我们可以用Ctrl\-D输出EOF的标识

```bash
# cat > test.txt
abcd
dcba
eftf
Ctrl-D
```

个人心得：

向目标文件追加内容
```shell
cat << EOF >> ~/.bashrc
hello world
第二行内容
第三行内容
EOF
```
将目标文件使用内容覆盖
```shell
cat << EOF > ~/.bashrc
hello world
第二行内容
第三行内容
EOF
```
`>>`表示追加
`>`表示覆盖

如果涉及到变量名的话，需要在前面加反斜杠转义。

```shell
cat <<EOF>>~/.bashrc
if [ -e \$HOME/.bash_aliases ]; then
    source \$HOME/.bash_aliases
fi
EOF
```
![20200710101722_ef42306b3789e9ceb635b755243da71c.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200710101722_ef42306b3789e9ceb635b755243da71c.png)
转义后的的内容追加到文件里是没有反斜杠的。
