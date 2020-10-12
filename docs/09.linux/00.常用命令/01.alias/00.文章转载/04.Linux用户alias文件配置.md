---
title: Linux用户alias文件配置
date: 2020-10-12 12:09:51
permalink: /pages/da8c8f/
categories:
  - alias
  - 文章转载
tags:
  - 
---
修改 ～/.bashrc 文件，以配置用户自己定义的alias

vi ~/.bashrc




```
\# .bash\_profile

\# Get the aliases and functions
if \[ \-f ~/.bashrc \]; then
        . ~/.bashrc
fi

\# User specific environment and startup programs

PATH=$PATH:$HOME/bin

export PATH



# 在文件最后，添加自定义的alias语句

echo "My alias has started successfully!"
echo "Type 'alias' to see more about this!"

\# my
alias la='ls \-al \-\-color=auto'
\# my\-end
```
这次更改需要在下次登录时生效。

若要立即生效，输入：
```
source ～/.bashrc
```