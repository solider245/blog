---
title: tmux入门
date: 2020-10-12 12:09:51
permalink: /pages/01729f/
categories:
  - tmux
  - 个人心得
tags:
  - 
---
# 序言
## 为什么要安装`tmux`？
`tmux`应该算是最重要的命令行工具之一。所以熟悉并掌握这个工具非常有必要。

# 安装

## 通过git安装最新版本
```shell
git clone https://github.com/tmux/tmux.git
cd tmux
sh autogen.sh
./configure && make
```
通过上面的命令，可以快速的安装最新版本的tmux。我这边tmux已经更新到了3.1。
如果你对最新版本的tmux没什么追求的话，可以直接用各个系统自带的软件包安装

## linux主流版本安装
```shell
apt install tmux
yum install tmux
brew install tmux
```
# 走进tmux

## 什么是`session`|`windows`|`pane`|？
用文件结构来表示的话，大概类似这样。
- session 01
  - windows 01
     - pane 01
     - pane 02
     - pane 03
  - windows 02
    - pane 01
    - pane 02
    - pane 03
  - windows 03
    - pane 01
    - pane 02
    - pane 03

![20200708075839_deaf853f60b83b47976df7e2d297963e.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200708075839_deaf853f60b83b47976df7e2d297963e.png)

我们在每个`pane`中工作，一个windows包含了多个pane。然后多个windows组成了session。

![20200708075502_3f844fbbc0d1af61bb8d5ceb3f67f0b8.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200708075502_3f844fbbc0d1af61bb8d5ceb3f67f0b8.png)

如上图所示，或者像下面这张图。

![20200708075608_f42392d22983d49cd09dd86c62c36330.png](https://images-1255533533.cos.ap-shanghai.myqcloud.com/20200708075608_f42392d22983d49cd09dd86c62c36330.png)


这些图如果刚开始看不懂也没关系，后面慢慢就懂了。

## 启动tmux

```shell
tmux  
```
第一次启动输入上面这行命令即可。
其他命令
```shell
tmux detach # 断开当前会话，在后台运行。俗称的退出当前界面
# 快捷键prefix +d
```

## 什么是`tmux`键？
进入tmux界面后，我们需要输入一个命令来激活tmux。默认的按键是`ctrl+b`,又叫`prefix key`长按ctrl键，然后再按键盘上的b键盘。这里激活之后，tmux并不会有任何动作，因为他还需要你输入额外的命令才会进行下一步动作。

## 熟悉tmux主要界面结构以及常用命令

输入`prefix key`再按下面这些键，会获得这些效果。


### 常用`session`操作

#### 关闭所有会话：

```shell
tmux ls | grep : | cut -d. -f1 | awk '{print substr($1, 0, length($1)-1)}' | xargs kill
```


按键| 命令
------- | -------
:new<回车> | 启动新会话
s | 列出所有会话
$ | 重命名当前会话


### 窗口 (标签页)


快捷键 | 作用
------- | -------
c | 创建新窗口
w | 列出所有窗口
n | 后一个窗口
p | 前一个窗口
f | 查找窗口
, | 重命名当前窗口
& | 关闭当前窗口

### 常用界面移动命令
按键 | 作用 | 备注
---------|----------|:---------
 % | 垂直分割 | 百分号
 " | 水平分割 | 分号
 → | 向右 | 按一次则移动，长按则移动界面
 ←|向左|同上
 ↓|向下|同上
 ↑|向上|同上
 x|关闭窗口|
 z|切换|最大化与最小化来回切换
解析：
>比较常见的操作，就是百分号垂直分屏，分号水平分屏。然后通过上下左右来跳动，通过长按上下左右来微调界面
按z来最大化，方便作业，作业完了后再按z切换回去。
有时候命令要强行关闭，就按x

## 文本复制模式：

按下 `PREFIX-[` 进入文本复制模式。可以使用方向键在屏幕中移动光标。默认情况下，方向键是启用的。在配置文件中启用 Vim 键盘布局来切换窗口、调整窗格大小。Tmux 也支持 Vi 模式。要是想启用 Vi 模式，只需要把下面这一行添加到 .tmux.conf 中：

```
setw -g mode-keys vi

```

启用这条配置后，就可以使用 h、j、k、l 来移动光标了。

想要退出文本复制模式的话，按下回车键就可以了。然后按下 `PREFIX-]` 粘贴刚才复制的文本。

一次移动一格效率低下，在 Vi 模式启用的情况下，可以辅助一些别的快捷键高效工作。

例如，可以使用 w 键逐词移动，使用 b 键逐词回退。使用 f 键加上任意字符跳转到当前行第一次出现该字符的位置，使用 F 键达到相反的效果。


column0 | column1 | column2
------- | ------- | -------
vi | emacs | 功能
^ | M-m | 反缩进
Escape | C-g | 清除选定内容
Enter | M-w | 复制选定内容
j | Down | 光标下移
h | Left | 光标左移
l | Right | 光标右移
L | |光标移到尾行
M | M-r | 光标移到中间行
H | M-R | 光标移到首行
k | Up | 光标上移
d | C-u | 删除整行
D | C-k | 删除到行末
$ | C-e | 移到行尾
: | g | 前往指定行
C-d | M-Down | 向下滚动半屏
C-u | M-Up | 向上滚动半屏
C-f | Page down | 下一页
w | M-f | 下一个词
p | C-y | 粘贴
C-b | Page up | 上一页
b | M-b | 上一个词
q | Escape | 退出
C-Down or J | C-Down | 向下翻
C-Up or K | C-Up | 向下翻
n | n | 继续搜索
? | C-r | 向前搜索
/ | C-s | 向后搜索
0 | C-a | 移到行首
Space | C-Space | 开始选中
 空| C-t | 字符调序

## 杂项：


命令 | 作用
------- | -------
d | 退出 tmux（tmux 仍在后台运行）
t | 窗口中央显示一个数字时钟
? | 列出所有快捷键
: | 命令提示符

# tmux的配置


## 配置选项：

```shell
# 鼠标支持 - 设置为 on 来启用鼠标(与 2.1 之前的版本有区别，请自行查阅 man page)
* set -g mouse on

# 设置默认终端模式为 256color
set -g default-terminal "screen-256color"

# 启用活动警告
setw -g monitor-activity on
set -g visual-activity on

# 居中窗口列表
set -g status-justify centre

# 最大化/恢复窗格
unbind Up bind Up new-window -d -n tmp \; swap-pane -s tmp.1 \; select-window -t tmp
unbind Down
bind Down last-window \; swap-pane -s tmp.1 \; kill-window -t tmp

```
## tmux插件管理TPM
### TPM的下载
```shell
mkdir -p ~/.tmux/plugins # 创建文件夹
cd ~/.tmux/plugins
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
# 国内用户可以用下面这个加速地址
git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tpm.git ~/.tmux/plugins/tpm
```
### 常用插件安装
```shell
git clone https://github.com/tmux-plugins/tmux-resurrect.git ~/.tmux/plugins
# 国内用户加速地址
git clone https://github.91chifun.workers.dev//https://github.com/tmux-plugins/tmux-resurrect.git
```
![](https://images-1255533533.cos.ap-shanghai.myqcloud.com/img/20200709043627.png)

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

## [](#参考配置文件tmuxconf)参考配置文件（~/.tmux.conf）：

下面这份配置是我使用 Tmux 几年来逐渐精简后的配置，请自取。

```shell
# -----------------------------------------------------------------------------
# Tmux 基本配置 - 要求 Tmux >= 2.3
# 如果不想使用插件，只需要将此节的内容写入 ~/.tmux.conf 即可
# -----------------------------------------------------------------------------

# C-b 和 VIM 冲突，修改 Prefix 组合键为 Control-Z，按键距离近
# set -g prefix C-z             # 修改键位

set -g base-index         1     # 窗口编号从 1 开始计数
set -g display-panes-time 10000 # PREFIX-Q 显示编号的驻留时长，单位 ms
set -g mouse              on    # 开启鼠标
set -g pane-base-index    1     # 窗格编号从 1 开始计数
set -g renumber-windows   on    # 关掉某个窗口后，编号重排

setw -g allow-rename      off   # 禁止活动进程修改窗口名
setw -g automatic-rename  off   # 禁止自动命名新窗口
setw -g mode-keys         vi    # 进入复制模式的时候使用 vi 键位（默认是 EMACS）

# -----------------------------------------------------------------------------
# 使用插件 - via tpm
#   1. 执行 git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
#   2. 执行 bash ~/.tmux/plugins/tpm/bin/install_plugins
# -----------------------------------------------------------------------------

setenv -g TMUX_PLUGIN_MANAGER_PATH '~/.tmux/plugins'

# 推荐的插件（请去每个插件的仓库下读一读使用教程）
set -g @plugin 'seebi/tmux-colors-solarized'
set -g @plugin 'tmux-plugins/tmux-pain-control'
set -g @plugin 'tmux-plugins/tmux-prefix-highlight'
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-yank'
set -g @plugin 'tmux-plugins/tpm'                   # 引入tpm插件
set -g @plugin 'tmux-plugins/tmux-sensible'

# tmux-resurrect
set -g @resurrect-dir '~/.tmux/resurrect' #可以修改为自己指定的地址
set -g @resurrect-save 'S' # 修改保存指令为S
set -g @resurrect-restore 'R' # 修改恢复指令为R
set -g @resurrect-strategy-vim 'session' # for vim
set -g @resurrect-strategy-nvim 'session' # for neovim
set -g @resurrect-capture-pane-contents 'on' # 开启恢复面板内容功能
set -g @resurrect-save-shell-history 'on' # 开启恢复shell的历史记录
# 修改会话数据的保持路径，此处不能使用除了$HOME, $HOSTNAME, ~之外的环境变量

# tmux-continuum
set -g @continuum-save-interval '1440' # 每1440分钟备份一次，也就是每24小时备份一次
set -g @continuum-restore 'on' # 启用自动恢复——tmux启动时就恢复最后一次保存的会话环境
# 如果不想要启动时自动恢复的功能了，直接移除上面这行就行。想要绝对确定自动恢复不会发生，就在用户根目录下创建一个tmux_no_auto_restore空文件（创建命令：touch ~/tmux_no_auto_restore），该文件存在时，自动恢复将不触发。
set -g @continuum-boot 'on'     # 开启插件状态栏，显示备份时间间隔
# tmux-prefix-highlight
set -g status-right '#{prefix_highlight} #H | %a %Y-%m-%d %H:%M'
set -g @prefix_highlight_show_copy_mode 'on'
set -g @prefix_highlight_copy_mode_attr 'fg=white,bg=blue'


# tmux-resurrect插件配置
run-shell ~/.tmux/plugins/tmux-resurrect/resurrect.tmux
# tmux-continuum插件配置
run-shell ~/.tmux/plugins/tmux-continuum/continuum.tmux

# 初始化 TPM 插件管理器 (放在配置文件的最后)

run '~/.tmux/plugins/tpm/tpm'

# -----------------------------------------------------------------------------
# 结束
# -----------------------------------------------------------------------------
```

插件说明：
1.通过`tpm`安装
如果你可以使用`git`链接到`github`的话，那么大多数情况下，支持tpm的插件你只需要在`~/.tmux.conf`文件里使用：
```shell
set -g @plugin `插件名` # 引入插件
```
引入插件，然后在tmux终端界面，使用`prefix +I`(大写的i，可以直接使用shift+i代替)就可以默认安装了。
2.手动安装
如果你不支持的话，那你就需要将文件手动下载到`~/.tmux/plugins`文件夹，然后`~/.tmux.conf`文件里，使用
```shell
run-shell ~/.tmux/plugins/插件名/插件文件
```
通过这种

