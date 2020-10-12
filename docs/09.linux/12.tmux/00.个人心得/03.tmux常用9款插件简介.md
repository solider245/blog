---
title: tmux常用9款插件简介
date: 2020-10-12 12:09:51
permalink: /pages/44814c/
categories:
  - tmux
  - 个人心得
tags:
  - 
---
# 序言

tmux使用tpm来管理插件，大多数情况下直接使用tpm安装即可。

| 序号 | 插件名                     | 作用            | 插件配置                                           | conf配置                                    | 下载链接                                                                       | 国内加速链接                                                                                                              |
|----|-------------------------|---------------|------------------------------------------------|-------------------------------------------|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| 1  | Tmux Resurrect          | 环境恢复          | set -g @plugin 'tmux-plugins/tmux-resurrect'   | run-shell ~/.tmux/plugins/resurrect.tmux  | git clone https://github.com/tmux-plugins/tmux-resurrect ~/.tmux/plugins   | git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-resurrect.git ~/.tmux/plugins   |
| 2  | tmux-continuum          | 保存环境          | set -g @plugin 'tmux-plugins/tmux-continuum'   | run-shell ~/.tmux/plugins/continuum.tmux  | git clone https://github.com/tmux-plugins/tmux-continuum ~/.tmux/plugins   | git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-continuum.git ~/.tmux/plugins   |
| 3  | Tmux Sidebar            | 文件侧边栏         | set -g @plugin 'tmux-plugins/tmux-sidebar'     | run-shell ~/.tmux/plugins/sidebar.tmux    | git clone https://github.com/tmux-plugins/tmux-sidebar ~/.tmux/plugins     | git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-sidebar.git ~/.tmux/plugins     |
| 4  | Tmux sessionist         | session管理     | set -g @plugin 'tmux-plugins/tmux-sessionist'  | run-shell ~/.tmux/plugins/sessionist.tmux | git clone https://github.com/tmux-plugins/tmux-sessionist ~/.tmux/plugins  | git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-sessionist.git ~/.tmux/plugins  |
| 5  | Tmux Logging            | 日志管理          | set -g @plugin 'tmux-plugins/tmux-logging'     | run-shell ~/.tmux/plugins/logging.tmux    | git clone https://github.com/tmux-plugins/tmux-logging ~/.tmux/plugins     | git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-logging.git ~/.tmux/plugins     |
| 6  | tmux-yank               | 系统粘贴板         | set -g @plugin 'tmux-plugins/tmux-yank'        | run-shell ~/.tmux/plugins/yank.tmux       | git clone https://github.com/tmux-plugins/tmux-yank ~/.tmux/plugins        | git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-yank.git ~/.tmux/plugins        |
| 7  | Tmux CPU and GPU status | 显示CPU/GPU负荷插件 | set -g @plugin 'tmux-plugins/tmux-cpu'         | run-shell ~/.tmux/plugins/cpu.tmux        | git clone https://github.com/tmux-plugins/tmux-cpu ~/.tmux/plugins         | git clone https://github.com/tmux-plugins/tmux-cpu ~/.tmux/plugins                                                  |
| 8  | Tmux sensible           | 通用环境设置        | set -g @plugin 'tmux-plugins/tmux-sensible'    | run-shell ~/.tmux/plugins/sensible.tmux   | git clone https://github.com/tmux-plugins/tmux-sensible ~/.tmux/plugins    | git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-sensible.git ~/.tmux/plugins    |
| 9  | Tmux sysstat plugin     | 显示系统指标        | set -g @plugin 'samoshkin/tmux-plugin-sysstat' | run-shell ~/.tmux/plugins/sysstat.tmux    | git clone https://github.com/samoshkin/tmux-plugin-sysstat ~/.tmux/plugins | git clone https://github.91chifun.workers.dev//https://github.com/samoshkin/tmux-plugin-sysstat.git ~/.tmux/plugins |

上面是tmux9款常用的插件。

# TPM 安装方法。

在终端输入：
```shell
vim ~/.tmux.conf
```
然后将下面这些内容粘贴进去即可。
```shell
set -g @plugin 'tmux-plugins/tmux-resurrect' 
set -g @plugin 'tmux-plugins/tmux-continuum'
set -g @plugin 'tmux-plugins/tmux-sidebar'
set -g @plugin 'tmux-plugins/tmux-sessionist'
set -g @plugin 'tmux-plugins/tmux-logging'
set -g @plugin 'tmux-plugins/tmux-yank'
set -g @plugin 'tmux-plugins/tmux-cpu'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'samoshkin/tmux-plugin-sysstat'
```
退出之后，输入`prefix+I`，即可自动安装。
安装好了之后，输入:
```shell
source ~/.tmux.conf
```
即可生效。

# 手动安装
有些朋友无法使用git连接github，所以这个时候 就需要使用git加速地址才行。
```shell
git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-resurrect.git ~/.tmux/plugins
git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-continuum.git ~/.tmux/plugins
git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-sidebar.git ~/.tmux/plugins
git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-sessionist.git ~/.tmux/plugins
git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-logging.git ~/.tmux/plugins
git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-yank.git ~/.tmux/plugins
git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-cpu.git ~/.tmux/plugins
git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-sensible.git ~/.tmux/plugins
git clone https://github.91chifun.workers.dev//https://github.com/samoshkin/tmux-plugin-sysstat.git ~/.tmux/plugins
```

这里我直接使用加速好的地址，帮助大家加速下载。如果有你不需要的插件的话，请在git前面加#键注销即可。

下载好了之后，还要配置`tmux.conf`
```shell
vim ~/.tmux.conf
```
然后：
```shell
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'
set -g @plugin 'tmux-plugins/tmux-sidebar'
set -g @plugin 'tmux-plugins/tmux-sessionist'
set -g @plugin 'tmux-plugins/tmux-logging'
set -g @plugin 'tmux-plugins/tmux-yank'
set -g @plugin 'tmux-plugins/tmux-cpu'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'samoshkin/tmux-plugin-sysstat'
```
先将上列内容粘贴到插件部分。
然后再复制下面的内容：
```shell
run-shell ~/.tmux/plugins/resurrect.tmux
run-shell ~/.tmux/plugins/continuum.tmux
run-shell ~/.tmux/plugins/sidebar.tmux
run-shell ~/.tmux/plugins/sessionist.tmux
run-shell ~/.tmux/plugins/logging.tmux
run-shell ~/.tmux/plugins/yank.tmux
run-shell ~/.tmux/plugins/cpu.tmux
run-shell ~/.tmux/plugins/sensible.tmux
run-shell ~/.tmux/plugins/sysstat.tmux
```
到配置的底部。
但是记得不能超过`run '~/.tmux/plugins/tpm/tpm'`这行文字。

这里需要注意的是，你的插件名字和你的路径是要一致的。
你可以打开`~/.tmux/plugins`，去那个文件夹查看你的插件是否都下载到了那里。
