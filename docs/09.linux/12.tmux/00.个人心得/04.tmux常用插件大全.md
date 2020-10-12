---
title: tmux常用插件大全
date: 2020-10-12 12:09:51
permalink: /pages/18e346/
categories:
  - tmux
  - 个人心得
tags:
  - 
---
# `Tmux Sidebar`

`tmux-sidebar` 做一件事：它打开一个列出当前路径的树目录。 它快速，方便，并且与vim一起使用效果很好。

[![屏幕截图](https://github.com/tmux-plugins/tmux-sidebar/raw/master/screenshot.gif)](https://github.com/tmux-plugins/tmux-sidebar/blob/master/screenshot.gif)

一些使插件比每次手动执行相同操作更具吸引力的功能：

*   **快速**
    比手动执行每个步骤快得多。
*   **智能调整**
    边栏会记住它的大小，因此下次打开它时，它将具有 **完全相同的** 宽度。 这是每个目录的属性，因此您可以为多个目录设置正确的大小。
*   **切换**
    相同的键绑定将打开和关闭侧栏。
*   **不间断的工作流程**
    主 `prefix + Tab` 键绑定可打开侧栏，但 **不会** 将光标移到 侧栏 。
*   **窗格布局保持不变**
    无论您喜欢哪种窗格布局，侧边栏都会尽力避免弄乱窗格拆分。 打开，然后关闭侧边栏，一切都应该看起来一样。

要求： `tmux 1.9` 更高， `tree` 推荐但不是必需

经过测试并在Linux，OSX和Cygwin上工作。

### `[](#key-bindings)Key bindings`

*   `prefix + Tab` \-使用目录树切换侧边栏
*   `prefix + Backspace` \-切换侧栏并将光标移至侧栏（将其聚焦）

### `[](#installation-with-tmux-plugin-manager-recommended)Installation with [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) (recommended)`

将插件添加到TPM插件列表中 `.tmux.conf` ：

```
set -g @plugin 'tmux-plugins/tmux-sidebar'

```

点击 `prefix + I` 获取插件并将其来源。 您现在应该可以使用该插件了。

### `[](#manual-installation)Manual Installation`

克隆仓库：

```
$ git clone https://github.com/tmux-plugins/tmux-sidebar ~/clone/path

```

将此行添加到以下内容的底部 `.tmux.conf` ：

```
run-shell ~/clone/path/sidebar.tmux

```

重新加载TMUX环境：

```
# type this in terminal
$ tmux source-file ~/.tmux.conf
```

# `Tmux sessionist`

轻量级的tmux实用程序，用于操纵tmux会话。

经过测试并在Linux，OSX和Cygwin上工作。

### `[](#problems)Problem(s)`

会话是tmux环境中的二等公民：

*   没有用于创建或删除会话的默认键绑定
*   创建会话很麻烦，只需 `tmux new-session -s name` 在tmux内部 尝试 （提示：您首先必须分离）
*   默认情况下删除（杀死）当前会话会分离tmux（为什么？）
*   当会话数超过5个时，无法快速切换会话

这个插件解决了以上问题。

### `[](#features)Features`

*   `prefix + g` \-提示输入会话名称并切换到该名称。 执行“同类”名称完成。
    比 `prefix + s` 长会话列表 的内置 提示要 快 。
*   `prefix + C` （Shift + C）\-提示按名称创建新会话。
*   `prefix + X` （shift + x）\-在不分离tmux的情况下终止当前会话。
*   `prefix + S` （Shift + s）\-切换到上一个会话。
    与内置的相同 `prefix + L` ，每个人似乎都被其他绑定取代。
*   `prefix + @` \-将当前窗格升级为新会话。
    类似于如何 `prefix + !` 将当前窗格拆分为新窗口。
*   `prefix + t<secondary-key>` \-将当前标记的窗格（ `prefix + m` ）加入当前会话/窗口，并切换到该 窗格
    *   辅助键
        *   `h` ， `-` ， `"` ：加入水平
        *   `v` ， `|` ， `%` ：垂直加盟
        *   `f` ， `@` ：加入全屏

### `[](#installation-with-tmux-plugin-manager-recommended)Installation with [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) (recommended)`

将插件添加到TPM插件列表中 `.tmux.conf` ：

```
set -g @plugin 'tmux-plugins/tmux-sessionist'

```

点击 `prefix + I` 获取插件并将其来源。 您现在可以使用该插件。

### `[](#manual-installation)Manual Installation`

克隆仓库：

```
$ git clone https://github.com/tmux-plugins/tmux-sessionist ~/clone/path

```

将此行添加到以下内容的底部 `.tmux.conf` ：

```
run-shell ~/clone/path/sessionist.tmux

```

重新加载TMUX环境 `$ tmux source-file ~/.tmux.conf` 。 您现在可以使用该插件。

### `[](#other-plugins)Other plugins`

这些对你也可能有用：

*   [疼痛控制](https://github.com/tmux-plugins/tmux-pain-control) \-用于控制窗格的有用的标准绑定
*   [日志记录](https://github.com/tmux-plugins/tmux-logging) \-轻松进行日志记录和屏幕捕获

# `Tmux Logging`

特征：

1.  在当前窗格中记录所有输出
    开始记录后，键入的所有内容和所有输出将保存到文件中。 方便跟踪您的工作。
2.  当前窗格“屏幕捕获”当前窗格中
    所有可见的文本都保存到文件中。 就像屏幕截图一样，但文字化。
3.  保存当前窗格的完整历史记录
    可以将自创建当前窗格以来输入的所有内容和所有输出保存到文件中。
4.  使用以下命令清除窗​​格历史记录 `prefix + alt + c`

经过测试并在Linux，OSX和Cygwin上工作。

### `[](#1-logging)1. Logging`

在当前窗格中切换（开始/停止）日志记录。

*   按键绑定： `prefix + shift + p`
*   文件名格式： `tmux-#{session_name}-#{window_index}-#{pane_index}-%Y%m%dT%H%M%S.log`
*   文件路径：（ `$HOME` 用户主目录）
    *   示例文件： `~/tmux-my-session-0-1-20140527T165614.log`

### `[](#2-screen-capture)2. "Screen Capture"`

在当前窗格中保存可见文本。 等效于“文本截图”。

*   按键绑定： `prefix + alt + p`
*   文件名格式： `tmux-screen-capture-#{session_name}-#{window_index}-#{pane_index}-%Y%m%dT%H%M%S.log`
*   文件路径：（ `$HOME` 用户主目录）
    *   示例文件： `tmux-screen-capture-my-session-0-1-20140527T165614.log`

### `[](#3-save-complete-history)3. Save complete history`

将完整的窗格历史记录保存到文件。 如果您回想起来很方便，则需要记录/保存所有工作。

*   按键绑定： `prefix + alt + shift + p`
*   文件名格式： `tmux-history-#{session_name}-#{window_index}-#{pane_index}-%Y%m%dT%H%M%S.log`
*   文件路径：（ `$HOME` 用户主目录）
    *   示例文件： `tmux-history-my-session-0-1-20140527T165614.log`

**注意** ：此功能取决于 `history-limit` \- 值 Tmux在回滚缓冲区中保留的行数。 Tmux保留的内容也只会保存到文件中。

`set -g history-limit 50000` 在.tmux.conf中 使用 ，对于现代计算机，可以将此选项设置为高数字。

### `[](#4-clear-pane-history)4. Clear pane history`

按键绑定： `prefix + alt + c`

这只是一个便捷键绑定。

### `[](#installation-with-tmux-plugin-manager-recommended)Installation with [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) (recommended)`

将插件添加到TPM插件列表中 `.tmux.conf` ：

```
set -g @plugin 'tmux-plugins/tmux-logging'

```

点击 `prefix + I` 获取插件并将其来源。

现在，您应该已经 `tmux-logging` 定义了 所有 键绑定。

### `[](#manual-installation)Manual Installation`

克隆仓库：

```
$ git clone https://github.com/tmux-plugins/tmux-logging ~/clone/path

```

将此行添加到以下内容的底部 `.tmux.conf` ：

```
run-shell ~/clone/path/logging.tmux

```

重新加载TMUX环境：

```
# type this in terminal
$ tmux source-file ~/.tmux.conf

```

现在，您应该已经 `tmux-logging` 定义了 所有 键绑定。

### [](#installing-ansifilter-recommended-for-osx-users)安装 `ansifilter` （建议OSX用户使用）

如果您使用的是OSX，建议安装 `ansifilter` ： `$ brew install ansifilter`

[ansifilter](http://www.andre-simon.de/doku/ansifilter/en/ansifilter.php) 是专门用于删除（或使用）ANSI代码的程序。

它有助于从日志中删除ANSI代码。 如果 `ansifilter` 不存在，则使用删除ANSI代码 `sed` 。

`pipe-pane` 通过剥离ANSI代码， 此功能改进了默认 日志记录机制。 `pipe-pane` 如果您使用带颜色的终端， 这就是普通 日志输出的样子：

[![日志输出乱码](https://github.com/tmux-plugins/tmux-logging/raw/master/screenshots/garbled_log_output.png)](https://github.com/tmux-plugins/tmux-logging/blob/master/screenshots/garbled_log_output.png)

乱码称为ANSI代码。 它们在终端中启用颜色，但仅在文本日志输出中产生“噪音”。

用户可能希望从日志中过滤出ANSI代码。 这是使用此插件时与上述相同的日志：

[![正确的日志输出](https://github.com/tmux-plugins/tmux-logging/raw/master/screenshots/proper_log_output.png)](https://github.com/tmux-plugins/tmux-logging/blob/master/screenshots/proper_log_output.png)

### `[](#other-plugins)Other plugins`

这些对你也可能有用：

*   [恢复](https://github.com/tmux-plugins/tmux-resurrect) \-重新启动系统后恢复tmux环境
*   [疼痛控制](https://github.com/tmux-plugins/tmux-pain-control) \-用于控制窗格的有用的标准绑定
*   [sessionist\-](https://github.com/tmux-plugins/tmux-sessionist) 用于切换和创建会话的轻量级tmux utils

# `Tmux Pain Control`

Tmux插件，用于控制窗格。 添加标准窗格导航绑定。

到目前为止，您必须四处搜索并梳理其他人的dotfile才能找到这些文件。 该插件有望使它们更加可用和“更加标准”。

感谢Tmux社区“发明”了这些绑定。 我只是在这里复制了它们。

经过测试并在Linux，OSX和Cygwin上工作。

### `[](#bindings)Bindings`

注意，大多数绑定都模拟vim光标的移动。

[![窗格导航](https://github.com/tmux-plugins/tmux-pain-control/raw/master/screenshots/pane_navigation.gif)](https://github.com/tmux-plugins/tmux-pain-control/blob/master/screenshots/pane_navigation.gif)

**导航**

*   `prefix + h` 然后 `prefix + C-h`
    选择左侧的窗格
*   `prefix + j` 并 `prefix + C-j`
    选择当前窗格下方的窗格
*   `prefix + k` 然后 `prefix + C-k`
    选择上方的窗格
*   `prefix + l` 然后 `prefix + C-l`
    选择右侧的窗格

**注意** ：这会覆盖tmux的默认绑定，以便在最后一个活动窗口之间切换 `prefix + l` 。 [tmux\-sensible](https://github.com/tmux-plugins/tmux-sensible) 为您提供了更好的绑定 `prefix + a` （如果您的前缀为 `C-a` ）。

[![窗格大小调整](https://github.com/tmux-plugins/tmux-pain-control/raw/master/screenshots/pane_resizing.gif)](https://github.com/tmux-plugins/tmux-pain-control/blob/master/screenshots/pane_resizing.gif)

**调整窗格大小**

*   `prefix + shift + h`
    调整当前窗格左侧5个单元格的大小
*   `prefix + shift + j`
    向下调整5个单元格的大小
*   `prefix + shift + k`
    向上调整5个单元格的大小
*   `prefix + shift + l`
    在右侧调整5个单元格的大小

这些映射是 `repeatable` 。

可以使用 `@pane_resize` 选项 配置要调整大小的单元格数量 。 有关 详细信息， 请参见 [配置部分](#configuration) 。

[![窗格分割](https://github.com/tmux-plugins/tmux-pain-control/raw/master/screenshots/pane_splitting.gif)](https://github.com/tmux-plugins/tmux-pain-control/blob/master/screenshots/pane_splitting.gif)

**分割窗格**

*   `prefix + |`
    水平分割当前窗格
*   `prefix + -`
    垂直分割当前窗格
*   `prefix + \`
    水平拆分当前窗格全宽
*   `prefix + _`
    垂直拆分当前窗格全宽

新创建的窗格始终具有与原始窗格相同的路径。

**交换窗口**

*   `prefix + <` \-将当前窗口向左移动一个位置
*   `prefix + >` \-将当前窗口向右移动一个位置

### `[](#installation-with-tmux-plugin-manager-recommended)Installation with [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) (recommended)`

将插件添加到TPM插件列表中 `.tmux.conf` ：

```
set -g @plugin 'tmux-plugins/tmux-pain-control'

```

点击 `prefix + I` 获取插件并将其来源。

现在，您应该已经 `pain-control` 定义了 所有 绑定。

### `[](#manual-installation)Manual Installation`

克隆仓库：

```
$ git clone https://github.com/tmux-plugins/tmux-pain-control ~/clone/path

```

将此行添加到以下内容的底部 `.tmux.conf` ：

```
run-shell ~/clone/path/pain_control.tmux

```

重新加载TMUX环境：

```
# type this in terminal
$ tmux source-file ~/.tmux.conf

```

现在，您应该已经 `pain-control` 定义了 所有 绑定。

### `[](#configuration)Configuration`

您可以设置“ `@pane_resize` Tmux”选项来选择用于调整大小绑定的调整大小单元数。 默认值为“ 5”。

例：

```
set-option -g @pane_resize "10"
```

# `Tmux Resurrect`

[![建立状态](https://camo.githubusercontent.com/1d107683212d6cebe50bc99836b500f8da53142a/68747470733a2f2f7472617669732d63692e6f72672f746d75782d706c7567696e732f746d75782d7265737572726563742e7376673f6272616e63683d6d6173746572)](https://travis-ci.org/tmux-plugins/tmux-resurrect)

`tmux` 系统重启后 恢复 环境。

Tmux很棒，除非您必须重新启动计算机。 您会丢失所有正在运行的程序，工作目录，窗格布局等。那里有一些有用的管理工具，但是随着工作流程的发展或启动新项目，它们需要进行初始配置和不断更新。

`tmux-resurrect` 保存您的tmux环境中的所有小细节，以便在系统重新启动后（或您愿意时）可以将其完全还原。 无需配置。 您应该觉得自己永远不会退出tmux。

它甚至（可选） [恢复vim和neovim会话](https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/restoring_vim_and_neovim_sessions.md) ！

使用 [tmux\-continuum](https://github.com/tmux-plugins/tmux-continuum) 插件 也可以自动恢复和连续保存tmux env 。

### `[](#screencast)Screencast`

[![屏幕截图](https://github.com/tmux-plugins/tmux-resurrect/raw/master/video/screencast_img.png)](https://vimeo.com/104763018)

### `[](#key-bindings)Key bindings`

*   `prefix + Ctrl-s` \- 保存
*   `prefix + Ctrl-r` \-恢复

### `[](#about)About`

该插件竭尽全力来保存和还原 `tmux` 环境中的 所有详细信息 。 这里是照顾的：

*   所有会话，窗口，窗格及其顺序
*   每个窗格的当前工作目录
*   **窗口** 内**精确的窗格布局** （即使缩放）
*   活动和替代会话
*   每个会话的活动和备用窗口
*   有焦点的窗户
*   每个窗口的活动窗格
*   “分组的会话”（将tmux与多个监视器一起使用时的有用功能）
*   程序在窗格中运行！ [恢复程序doc](https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/restoring_programs.md) 中的更多详细信息 。

可选的：

*   [恢复vim和neovim会话](https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/restoring_vim_and_neovim_sessions.md)
*   [恢复窗格内容](https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/restoring_pane_contents.md)

要求/依赖项： `tmux 1.9` 或更高， `bash` 。

经过测试并在Linux，OSX和Cygwin上工作。

`tmux-resurrect` 是幂等的！ 它不会尝试还原已经存在的窗格或窗口。
唯一的例外是tmux仅用1个窗格启动以便还原以前的tmux env。 仅在这种情况下，此单个窗格才会被覆盖。

### `[](#installation-with-tmux-plugin-manager-recommended)Installation with [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) (recommended)`

将插件添加到TPM插件列表中 `.tmux.conf` ：

```
set -g @plugin 'tmux-plugins/tmux-resurrect'

```

点击 `prefix + I` 获取插件并将其来源。 您现在应该可以使用该插件了。

### `[](#manual-installation)Manual Installation`

克隆仓库：

```
$ git clone https://github.com/tmux-plugins/tmux-resurrect ~/clone/path

```

将此行添加到以下内容的底部 `.tmux.conf` ：

```
run-shell ~/clone/path/resurrect.tmux

```

刷新TMUX环境： `$ tmux source-file ~/.tmux.conf` 。 您现在应该可以使用该插件了。

### `[](#docs)Docs`

*   [从tmuxinator迁移的指南](https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/migrating_from_tmuxinator.md)

**组态**

*   [更改默认的键绑定](https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/custom_key_bindings.md) 。
*   [在保存和恢复上设置挂钩](https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/hooks.md) 。
*   默认情况下，仅还原保守的程序列表
    `vi vim nvim emacs man less more tail top htop irssi weechat mutt` 。
    [恢复程序文档](https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/restoring_programs.md) 说明了如何恢复其他程序。
*   [修改文件夹](https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/save_dir.md) ，其中 `tmux-resurrect` 保存TMUX环境。

**可选功能**

*   [](https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/restoring_vim_and_neovim_sessions.md)如果您是vim / neovim用户，那么 [恢复vim和neovim会话](https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/restoring_vim_and_neovim_sessions.md) 非常好。
*   [恢复窗格内容](https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/restoring_pane_contents.md) 功能。

**实验功能（也是可选的）**

*   [恢复shell历史](https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/restoring_shell_history.md)

### `[](#other-goodies)Other goodies`

*   [tmux\-copycat\-](https://github.com/tmux-plugins/tmux-copycat) 用于tmux中的正则表达式搜索和快速匹配选择的插件
*   [tmux\-yank\-](https://github.com/tmux-plugins/tmux-yank) 启用将突出显示的文本复制到系统剪贴板
*   [tmux\-open\-](https://github.com/tmux-plugins/tmux-open) 一个用于快速打开突出显示的文件或URL的插件
*   [tmux\-continuum\-](https://github.com/tmux-plugins/tmux-continuum) 自动恢复和连续保存tmux env

### `[](#reporting-bugs-and-contributing)Reporting bugs and contributing`

欢迎提供贡献报告和错误报告。 请查看 [贡献准则](https://github.com/tmux-plugins/tmux-resurrect/blob/master/CONTRIBUTING.md) 。

### `[](#credits)Credits`

[MislavMarohnić\-](https://github.com/mislav) 插件的想法来自他的 [tmux\-session脚本](https://github.com/mislav/dotfiles/blob/2036b5e03fb430bbcbc340689d63328abaa28876/bin/tmux-session) 。

# `tmux-continuum`

特征：

*   持续保存tmux环境
*   打开计算机/服务器后自动启动tmux
*   启动tmux时自动还原

这些功能共同实现了tmux使用的不间断。 无论计算机或服务器重新启动，如果计算机已打开，tmux都会在其中，您如何在上次使用它时将其关闭。

经过测试并在Linux，OSX和Cygwin上工作。

#### `[](#continuous-saving)Continuous saving`

Tmux环境将每隔15分钟保存一次。 所有节省都在后台进行，而不会影响您的工作流程。

安装插件后，此操作将自动开始。

#### `[](#automatic-tmux-start)Automatic tmux start`

打开计算机/服务器后，Tmux自动启动。

请参阅 [说明，](https://github.com/tmux-plugins/tmux-continuum/blob/master/docs/automatic_start.md) 如何为您的系统启用此功能。

#### `[](#automatic-restore)Automatic restore`

启动tmux时，将自动恢复最后保存的环境。

将 `set -g @continuum-restore 'on'` 在 `.tmux.conf` 启用它。

注意：自动还原 **仅** 在tmux服务器启动 时发生 。 没有其他动作（例如source `.tmux.conf` ）触发此操作。

#### `[](#dependencies)Dependencies`

`tmux 1.9` 或更高， `bash` ， [TMUX\-复活](https://github.com/tmux-plugins/tmux-resurrect) 插件。

### `[](#installation-with-tmux-plugin-manager-recommended)Installation with [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) (recommended)`

请确保您已 安装 [tmux\-resurrect](https://github.com/tmux-plugins/tmux-resurrect) 。

将插件添加到TPM插件列表中 `.tmux.conf` ：

```
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'

```

点击 `prefix + I` 获取插件并将其来源。 该插件将在后台自动开始“运行”，无需执行任何操作。

### `[](#manual-installation)Manual Installation`

请确保您已 安装 [tmux\-resurrect](https://github.com/tmux-plugins/tmux-resurrect) 。

克隆仓库：

```
$ git clone https://github.com/tmux-plugins/tmux-continuum ~/clone/path

```

将此行添加到以下内容的底部 `.tmux.conf` ：

```
run-shell ~/clone/path/continuum.tmux

```

使用以下命令重新加载TMUX环境： `$ tmux source-file ~/.tmux.conf`

该插件将在后台自动开始“运行”，无需执行任何操作。

### `[](#docs)Docs`

*   [经常问的问题](https://github.com/tmux-plugins/tmux-continuum/blob/master/docs/faq.md)
*   [运行多个tmux服务器时的行为](https://github.com/tmux-plugins/tmux-continuum/blob/master/docs/multiple_tmux_servers.md) \-此文档可以安全跳过，但是如果您使用带有 `-L` 或 `-S` 标志的 tmux，则可能需要阅读该文档
*   [打开计算机后自动启动tmux](https://github.com/tmux-plugins/tmux-continuum/blob/master/docs/automatic_start.md)
*   [tmux状态行中的连续体状态](https://github.com/tmux-plugins/tmux-continuum/blob/master/docs/continuum_status.md)

### `[](#other-goodies)Other goodies`

*   [tmux\-copycat\-](https://github.com/tmux-plugins/tmux-copycat) 用于tmux中的正则表达式搜索和快速匹配选择的插件
*   [tmux\-yank\-](https://github.com/tmux-plugins/tmux-yank) 启用将突出显示的文本复制到系统剪贴板
*   [tmux\-open\-](https://github.com/tmux-plugins/tmux-open) 一个用于快速打开突出显示的文件或URL的插件

# `tmux-yank`

复制到中的系统剪贴板 [`tmux`](https://tmux.github.io/) 。

支持：

*   的Linux
*   苹果系统
*   西格温
*   Windows Linux子系统（WSL）

## `[](#installing)Installing`

### `[](#via-tpm-recommended)Via TPM (recommended)`

最简单的安装方法 `tmux-yank` 是通过 [Tmux插件管理器](https://github.com/tmux-plugins/tpm) 。

1.  将插件添加到TPM插件列表中 `.tmux.conf` ：

    ```shell
    set -g @plugin 'tmux-plugins/tmux-yank'
    ```

2.  使用 prefix – I 安装 `tmux-yank` 。 您现在应该可以 `tmux-yank` 立即进行操作。

3.  当您要更新时，请 `tmux-yank` 使用 prefix – U 。

### `[](#manual-installation)Manual Installation`

1.  克隆存储库

    ```shell
    $ git clone https://github.com/tmux-plugins/tmux-yank ~/clone/path
    ```

2.  将此行添加到 `.tmux.conf`

    ```shell
    run-shell ~/clone/path/yank.tmux
    ```

3.  重新加载 `tmux` 环境

    ```shell
    # type this inside tmux
    $ tmux source-file ~/.tmux.conf
    ```

您现在应该可以 `tmux-yank` 立即 使用 。

## `[](#requirements)Requirements`

为了 `tmux-yank` 正常工作，必须有一个程序将数据存储在系统剪贴板中。

### `[](#macos)macOS`

*   [`reattach-to-user-namespace`](https://github.com/ChrisJohnsen/tmux-MacOSX-pasteboard)

**注意** ：据报道，某些版本的macOS（又名OS X）可以在不使用的情况下运行 `reattach-to-user-namespace` 。 安装它没有什么坏处。

*   OS X 10.8：Mountain Lion – *必需*
*   OS X 10.9：Mavericks – *必需*
*   OS X 10.10：优胜美地\- *不需要*
*   OS X 10.11：El Capitan – *不需要*
*   macOS 10.12：Sierra – *必需*
*   macOS 10.14：Mojave\- *必需*
*   macOS 10.15：Catalina\- *不需要*

用最简单的方式 `reattach-to-user-namespace` 与 `tmux` IS使用使用 [`tmux-sensible`](https://github.com/tmux-plugins/tmux-sensible) 插件。

要手动使用它，请使用：

```shell
# ~/.tmux.conf
set-option -g default-command "reattach-to-user-namespace -l $SHELL"
```

如果您拥有 `tmux` 1.5或更高版本，并且正在使用 [iTerm2](https://www.iterm2.com/) 版本3或更高版本，那么 y in `copy-mode` 和鼠标选择将不起作用 `tmux-yank` 。

要启用此功能：

1.  进入iTerm2的首选项。

2.  转到“常规”标签。

3.  选中“终端中的应用程序可以访问剪贴板”

4.  在中 `tmux` ，确保 `set-clipboard` 已打开：

    ```shell
    $ tmux show-options -g -s set-clipboard
    set-clipboard on
    ```

#### `[](#homebrew-recommended)[HomeBrew](https://brew.sh/) (recommended)`

```shell
$ brew install reattach-to-user-namespace
```

#### `[](#macports)MacPorts`

```shell
$ sudo port install tmux-pasteboard
```

### `[](#linux)Linux`

*   `xsel` （推荐）或 `xclip` （对于X）。
*   `wl-copy` 从 [wl\-clipboard](https://github.com/bugaevc/wl-clipboard) （用于Wayland）

如果您使用的是 `tmux` 1.5或更高版本，并且正在使用 `xterm` ，则 y in `copy-mode` 和mouse选择将不起作用 `tmux-yank` 。 有关 选项， 请参见 `tmux(1)` 手册页条目 `set-clipboard` 。

#### `[](#debian--ubuntu)Debian & Ubuntu`

```shell
$ sudo apt-get install xsel # or xclip
```

#### `[](#redhat--centos)RedHat & CentOS`

```shell
$ sudo yum install xsel # or xclip
```

### `[](#cygwin)Cygwin`

*   （ *可选* ） `putclip` ，它是 `cygutils-extra` 包装的 一部分 。

### `[](#windows-subsystem-for-linux-wsl)Windows Subsystem for Linux (WSL)`

*   `clip.exe` Windows Subsystem for Linux附带了该软件。

## `[](#configuration)Configuration`

### `[](#key-bindings)Key bindings`

*   正常模式

    *   prefix –\-将 y 文本从命令行复制到剪贴板。

        适用于所有流行的shell / repls。 经过测试：

        *   炮弹： `bash` ， `zsh` （带有 `bindkey -e` ）， `tcsh`
        *   repls： ， `irb` ， `pry` ， `node` ， `psql` ， ， `python` `php -a` `coffee`
        *   远程炮弹： `ssh` ， [莫什](http://mosh.mit.edu/)
        *   vim / neovim命令行（需要 [vim\-](https://github.com/bruno-/vim-husk) husk 或 [vim\-rsi](https://github.com/tpope/vim-rsi) 插件）
    *   prefix – Y —将当前窗格的当前工作目录复制到剪贴板。

*   复制模式

    *   y —将选择复制到系统剪贴板。
    *   Y （shift\-y）\-“放置”选择。 等效于复制选择并将其粘贴到命令行。

### `[](#default-and-preferred-clipboard-programs)Default and Preferred Clipboard Programs`

tmux\-yank竭尽全力为您的OS上的剪贴板程序检测合理的选择。

如果tmux\-yank无法检测到已知的剪贴板程序，则将 `@custom_copy_command` tmux选项用作剪贴板程序（如果已设置）。

如果您始终需要为剪贴板程序重写tmux\-yank的选择，则可以设置 `@override_copy_command` 为强制tmux\-yank使用所需的任何内容。

请注意，两个程序都 *必须* 接受 `STDIN` 要复制的文本。

设置示例 `@override_copy_command` ：

```shell
# ~/.tmux.conf

set -g @custom_copy_command 'my-clipboard-copy --some-arg'
# or
set -g @override_copy_command 'my-clipboard-copy --some-arg'
```

### `[](#linux-clipboards)Linux Clipboards`

Linux有几个剪切和粘贴剪贴板： `primary` ， `secondary` ，和 `clipboard` （默认TMUX，猛拉是 `clipboard` ）。

您可以通过设置来更改此设置 `@yank_selection` ：

```shell
# ~/.tmux.conf

set -g @yank_selection 'primary' # or 'secondary' or 'clipboard'
```

启用鼠标支持后（请参见下文），鼠标选择的默认剪贴板为 `primary` 。

您可以通过设置来更改此设置 `@yank_selection_mouse` ：

```shell
# ~/.tmux.conf

set -g @yank_selection_mouse 'clipboard' # or 'primary' or 'secondary'
```

### `[](#controlling-yank-behavior)Controlling Yank Behavior`

默认情况下， `tmux-yank` 选中文本后将退出复制模式。 如果您希望保留在复印模式下，可以设置 `@yank_action` ：

```shell
# ~/.tmux.conf

set -g @yank_action 'copy-pipe' # or 'copy-pipe-and-cancel' for the default
```

### `[](#mouse-support)Mouse Support`

`tmux-yank` 默认情况下已启用鼠标支持。 仅当 `tmux` 还启用了内置鼠标支持（ `mouse on` 从 `tmux` 2.1 `mode-mouse on` 版本 开始 ，或 在较早版本中）时，它才有效。

要用鼠标拉动，请单击并拖动主按钮以开始选择，然后松开以拉动。

如果您希望禁用此行为，或者为 `MouseDragEnd1Pane` 事件 提供自己的绑定，则 可以执行以下操作：

```shell
# ~/.tmux.conf

set -g @yank_with_mouse off # or 'on'
```

如果要在选择鼠标后保留在复印模式下，请 `@yank_action` 按上述说明进行 设置 。

### `[](#vi-mode-support)vi mode support`

如果使用 `tmux` 2.3或更早版本 *并* 使用vi键，则将添加以下配置设置：

```shell
# ~/.tmux.conf

set -g @shell_mode 'vi'
```

`tmux` 2.4或更高版本 不需要此功能 。

### `[](#screen-cast)Screen-cast`

[![屏幕截图](https://github.com/tmux-plugins/tmux-yank/raw/master/video/screencast_img.png)](https://vimeo.com/102039099)

**注意** ：截屏使用 Control – y 进行“放置选择”。 Y 在 `v2.0.0` 及以后 使用 。

### `[](#other-tmux-plugins)Other tmux plugins`

*   [tmux\-copycat\-](https://github.com/tmux-plugins/tmux-copycat) 用于在tmux中进行正则表达式搜索和快速匹配选择的插件
*   [tmux\-open\-](https://github.com/tmux-plugins/tmux-open) 一个用于快速打开突出显示的文件或URL的插件
*   [tmux\-continuum\-](https://github.com/tmux-plugins/tmux-continuum) 自动恢复并连续保存tmux环境。

# `Tmux CPU and GPU status`

允许在Tmux `status-right` 和中 显示CPU和GPU信息 `status-left` 。 可配置百分比和图标显示。

## `[](#installation)Installation`

### `[](#installation-with-tmux-plugin-manager-recommended)Installation with [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) (recommended)`

将插件添加到TPM插件列表中 `.tmux.conf` ：

```
set -g @plugin 'tmux-plugins/tmux-cpu'

```

点击 `prefix + I` 获取插件并将其来源。

如果将格式字符串添加到中 `status-right` ，则它们现在应该可见。

### `[](#manual-installation)Manual Installation`

克隆仓库：

```
$ git clone https://github.com/tmux-plugins/tmux-cpu ~/clone/path

```

将此行添加到以下内容的底部 `.tmux.conf` ：

```
run-shell ~/clone/path/cpu.tmux

```

重新加载TMUX环境：

```
# type this in terminal
$ tmux source-file ~/.tmux.conf

```

如果将格式字符串添加到中 `status-right` ，则它们现在应该可见。

### `[](#optional-requirement-linux-bsd-osx)Optional requirement (Linux, BSD, OSX)`

`iostat` 或者 `sar` 是获得准确的CPU百分比的最佳方法。 使用包含了后备广告， `ps -aux` 但可能不准确。 `free` 用于获取系统RAM状态。 `nvidia-smi` 需要GPU信息。 对于OSX， `cuda-smi` 则是必需的（但仅显示GPU内存的使用而非负载）。

如果显示“ No GPU”，则表明脚本无法找到 `nvidia-smi` / `cuda-smi` 。 请确保在PATH中安装了适当的命令。

## `[](#usage)Usage`

将任何受支持的格式字符串（请参见下文）添加到现有的 `status-right` tmux选项。 例：

```
# in .tmux.conf
set -g status-right '#{cpu_bg_color} CPU: #{cpu_icon} #{cpu_percentage} | %a %h-%d %H:%M '

```

### `[](#supported-options)Supported Options`

这可以通过引入8个新的格式字符串来完成，这些字符串可以添加到 `status-right` option中：

*   `#{cpu_icon}` \-将显示一个CPU状态图标
*   `#{cpu_percentage}` \-将显示CPU百分比（跨内核平均）
*   `#{cpu_bg_color}` \-将根据CPU百分比更改背景颜色
*   `#{cpu_fg_color}` \-将根据CPU百分比更改前景色
*   `#{ram_icon}` \-将显示RAM状态图标
*   `#{ram_percentage}` \-将显示RAM百分比（跨内核平均）
*   `#{ram_bg_color}` \-将根据RAM百分比更改背景颜色
*   `#{ram_fg_color}` \-将根据RAM百分比更改前景色

GPU等效项也存在：

*   `#{gpu_icon}` \-将显示GPU状态图标
*   `#{gpu_percentage}` \-将显示GPU百分比（跨设备平均）
*   `#{gpu_bg_color}` \-将根据GPU百分比更改背景颜色
*   `#{gpu_fg_color}` \-将根据GPU百分比更改前景色
*   `#{gram_icon}` \-将显示GPU RAM状态图标
*   `#{gram_percentage}` \-将显示GPU RAM百分比（跨设备总计）
*   `#{gram_bg_color}` \-将根据GPU RAM百分比更改背景颜色
*   `#{gram_fg_color}` \-将根据GPU RAM百分比更改前景色

## `[](#examples)Examples`

CPU使用率低于30％：
[![low_fg](https://github.com/tmux-plugins/tmux-cpu/raw/master/screenshots/low_fg.png)](https://github.com/tmux-plugins/tmux-cpu/blob/master/screenshots/low_fg.png) [![low_bg](https://github.com/tmux-plugins/tmux-cpu/raw/master/screenshots/low_bg.png)](https://github.com/tmux-plugins/tmux-cpu/blob/master/screenshots/low_bg.png) [![low_icon](https://github.com/tmux-plugins/tmux-cpu/raw/master/screenshots/low_icon.png)](https://github.com/tmux-plugins/tmux-cpu/blob/master/screenshots/low_icon.png)

30％到80％之间的CPU使用率：
[![medium_fg](https://github.com/tmux-plugins/tmux-cpu/raw/master/screenshots/medium_fg.png)](https://github.com/tmux-plugins/tmux-cpu/blob/master/screenshots/medium_fg.png) [![medium_bg](https://github.com/tmux-plugins/tmux-cpu/raw/master/screenshots/medium_bg.png)](https://github.com/tmux-plugins/tmux-cpu/blob/master/screenshots/medium_bg.png) [![medium_icon](https://github.com/tmux-plugins/tmux-cpu/raw/master/screenshots/medium_icon.png)](https://github.com/tmux-plugins/tmux-cpu/blob/master/screenshots/medium_icon.png)

CPU使用率高于80％：
[![high_fg](https://github.com/tmux-plugins/tmux-cpu/raw/master/screenshots/high_fg.png)](https://github.com/tmux-plugins/tmux-cpu/blob/master/screenshots/high_fg.png) [![high_bg](https://github.com/tmux-plugins/tmux-cpu/raw/master/screenshots/high_bg.png)](https://github.com/tmux-plugins/tmux-cpu/blob/master/screenshots/high_bg.png) [![high_icon](https://github.com/tmux-plugins/tmux-cpu/raw/master/screenshots/high_icon.png)](https://github.com/tmux-plugins/tmux-cpu/blob/master/screenshots/high_icon.png)

## `[](#customization)Customization`

以下是所有可用选项及其默认值：

```shell
@cpu_low_icon "=" # icon when cpu is low
@cpu_medium_icon "≡" # icon when cpu is medium
@cpu_high_icon "≣" # icon when cpu is high

@cpu_low_fg_color "" # foreground color when cpu is low
@cpu_medium_fg_color "" # foreground color when cpu is medium
@cpu_high_fg_color "" # foreground color when cpu is high

@cpu_low_bg_color "#[bg=green]" # background color when cpu is low
@cpu_medium_bg_color "#[bg=yellow]" # background color when cpu is medium
@cpu_high_bg_color "#[bg=red]" # background color when cpu is high

@cpu_percentage_format "%3.1f%%" # printf format to use to display percentage
```

相同的选项对 `@gpu`

请注意，这些颜色取决于您的终端/ X11配置。

您可以在中自定义以下每个选项 `.tmux.conf` ，例如：

```shell
set -g @cpu_low_fg_color "#[fg=#00ff00]"
set -g @cpu_percentage_format "%5.1f%%" # Add left padding
```

`$ tmux source-file ~/.tmux.conf` 完成此操作后，请 不要忘记重新加载tmux环境（ ）。

# `Tmux sensible`

一组所有人都应该接受的tmux选项。

受 [vim明智的](https://github.com/tpope/vim-sensible) 启发 。

经过测试并在Linux，OSX和Cygwin上工作。

### `[](#principles)Principles`

*   `tmux-sensible` 选项应为 **每个** tmux用户 所接受 ！
    如果有任何选项困扰您，请打开一个问题，它可能会被更新（或删除）。
*   如果您认为应该添加新选项，请随时打开拉取请求。
*   **不会覆盖** 用户定义的设置。
    您现有的 `.tmux.conf` 设置会得到尊重，并且不会更改。 `tmux-sensible` 如果您有一些特定选项，则 可以使用这种方式 。

### `[](#goals)Goals`

*   将标准tmux社区选项集中在一个地方
*   清除杂物 `.tmux.conf`
*   教育新的tmux用户基本选项

### `[](#options)Options`

```
# utf8 is on
set -g utf8 on
set -g status-utf8 on

# address vim mode switching delay (http://superuser.com/a/252717/65504)
set -s escape-time 0

# increase scrollback buffer size
set -g history-limit 50000

# tmux messages are displayed for 4 seconds
set -g display-time 4000

# refresh 'status-left' and 'status-right' more often
set -g status-interval 5

# set only on OS X where it's required
set -g default-command "reattach-to-user-namespace -l $SHELL"

# upgrade $TERM
set -g default-terminal "screen-256color"

# emacs key bindings in tmux command prompt (prefix + :) are better than
# vi keys, even for vim users
set -g status-keys emacs

# focus events enabled for terminals that support them
set -g focus-events on

# super useful when using "grouped sessions" and multi-monitor setup
setw -g aggressive-resize on

```

### `[](#key-bindings)Key bindings`

```
# easier and faster switching between next/prev window
bind C-p previous-window
bind C-n next-window

```

上面的绑定 通过允许您按住 并重复 / （如果您的前缀是 ） 来 增强默认设置 `prefix + p` 和 `prefix + n` 绑定 ，这要快得多。 `Ctrl` `a + p` `a + n` `C-a`

```
# source .tmux.conf as suggested in `man tmux`
bind R source-file '~/.tmux.conf'

```

基于您的 `prefix` 价值的 “适应性”键绑定 ：

```
# if prefix is 'C-a'
bind C-a send-prefix
bind a last-window

```

如果prefix是 `C-b` ，则上面的键将是 `C-b` 和 `b` 。
如果prefix是 `C-z` ，则上面的键将是 `C-z` 和 `z` ...。

### `[](#installation-with-tmux-plugin-manager-recommended)Installation with [Tmux Plugin Manager](https://github.com/tmux-plugins/tpm) (recommended)`

将插件添加到TPM插件列表中 `.tmux.conf` ：

```
set -g @plugin 'tmux-plugins/tmux-sensible'

```

点击 `prefix + I` 获取插件并将其来源。 而已！

### `[](#manual-installation)Manual Installation`

克隆仓库：

```
$ git clone https://github.com/tmux-plugins/tmux-sensible ~/clone/path

```

将此行添加到以下内容的底部 `.tmux.conf` ：

```
run-shell ~/clone/path/sensible.tmux

```

用刷新TMUX环境 `$ tmux source-file ~/.tmux.conf` ，仅此而已。

### `[](#other-goodies)Other goodies`

这些对你也可能有用：

*   [模仿者](https://github.com/tmux-plugins/tmux-copycat) 改善了tmux搜索并减少了鼠标的使用
*   [疼痛控制](https://github.com/tmux-plugins/tmux-pain-control) 用于控制窗格的有用的标准绑定
*   [](https://github.com/tmux-plugins/tmux-resurrect)在系统重新启动后， [resurrect](https://github.com/tmux-plugins/tmux-resurrect) 保留tmux环境


# `Tmux sysstat plugin`

允许在Tmux状态栏中打印CPU使用率，内存和交换，平均负载，净I / O指标

[![介绍](https://github.com/samoshkin/tmux-plugin-sysstat/raw/master/screenshots/intro.png)](https://github.com/samoshkin/tmux-plugin-sysstat/blob/master/screenshots/intro.png)

您可以签出 [tmux\-config](https://github.com/samoshkin/tmux-config) 仓库以查看此插件的运行情况。

## `[](#features)Features`

*   CPU使用率
*   可用内存/可用内存，已用内存，总计内存（KiB，MiB，GiB），可用内存/已用百分比
*   交换已使用，免费，总计，免费/已使用百分比
*   最近1,5,15分钟的平均负载
*   可自定义颜色的可配置阈值（低，中，压力）
*   使用模板调整每个指标输出（例如，“已用完16G中的10％”）
*   可配置的尺寸刻度（K，M，G）
*   OSX，Linux支持
*   [ ]  **TODO：** 网络I / O指标支持

经过测试：OS X El Capitan 10.11.5，Ubuntu 14 LTS，CentOS 7，FreeBSD 11.1。

## `[](#installation)Installation`

最好通过 [Tmux插件管理器](https://github.com/tmux-plugins/tpm) （TMP）安装。 在 `.tmux.conf` 文件中 添加以下行 ：

```
set -g @plugin 'samoshkin/tmux-plugin-sysstat'

```

`prefix + I` 从tmux内部 使用 以安装所有插件并获取它们。 如果愿意，可以 [从命令行](https://github.com/tmux-plugins/tpm/blob/master/docs/managing_plugins_via_cmd_line.md) 获得相同的效果 ：

```
$ ~.tmux/plugins/tpm/bin/install_plugins

```

## `[](#basic-usage)Basic usage`

插入后， 可以使用以下占位符配置 tmux `status-left` 或 `status-right` 选项。 每个占位符都将扩展为度量标准的默认输出。

*   `#{sysstat_cpu}` ， CPU使用率 \- `CPU:40.2%`
*   `#{sysstat_mem}` ， 内存使用情况 \- `MEM:73%`
*   `#{sysstat_swap}` ，交换使用量\- `SW:66%`
*   `#{sysstat_loadavg}` ，系统平均负载\- `0.25 0.04 0.34`

例如：

```
set -g status-right "#{sysstat_cpu} | #{sysstat_mem} | #{sysstat_swap} | #{sysstat_loadavg} | #[fg=cyan]#(echo $USER)#[default]@#H"

```

## `[](#changing-default-output)Changing default output`

如果需要显示更多字段或要提供自定义模板，则可以更改CPU和内存指标的默认输出。 在您的 `.tmux.conf` ：

例如，要获取 `Used 4.5G out of 16G` 内存指标的输出：

```
set -g @sysstat_mem_view_tmpl '#Used [fg=#{mem.color}]#{mem.used}#[default] out of #{mem.total}'

```

如果您不希望使用 `CPU:` 前缀并且不喜欢CPU指标的彩色输出：

```
set -g @sysstat_cpu_view_tmpl '#{cpu.pused}'

```

### `[](#supported-fields)Supported fields`

如您所见，每个指标都可以配置模板，其中包含固定文本（ `CPU:` ），颜色占位符（ `#[fg=#{mem.color}]` ）和字段占位符（ `#{mem.used}` ）。 这种方法使您可以最终控制每个指标的输出。 支持以下字段占位符：

| 中央处理器 |
| --- |
| `#{cpu.color}` | 主要指标颜色 |
| `#{cpu.pused}` | CPU使用率 |

| 记忆 |
| --- |
| `#{mem.color}` | 主要指标颜色 |
| `#{mem.free}` | 可用/可用内存 |
| `#{mem.pfree}` | 可用内存占总数的百分比 |
| `#{mem.used}` | 使用的内存 |
| `#{mem.pused}` | 已用内存占总内存的百分比 |
| `#{mem.total}` | 总安装内存 |

| 交换 |
| --- |
| `#{swap.color}` | 主要交换指标颜色 |
| `#{swap.free}` | 空闲交换内存 |
| `#{swap.pfree}` | 可用交换内存占总交换空间的百分比 |
| `#{swap.used}` | 用过的交换内存 |
| `#{swap.pused}` | 已用交换内存占总交换空间的百分比 |
| `#{swap.total}` | 总交换空间 |

### `[](#change-size-scale)Change size scale`

可用/已用/总内存可以绝对和相对单位显示。 对于绝对单位，您可以选择 *大小比例因子，* 以在GiB，MiB和KiB之间进行选择。 默认值为GiB。 如果您安装的内存少于3\-4G，则可以使用MiB。 KiB选项不太实用，因为它会产生很长的输出，不适合状态栏的限制。

```
set -g @sysstat_mem_size_unit "G"

```

如果选择 `G` 大小比例，则输出将具有 `%.1f` （浮点数后1位），否则大小为整数（4.5G，1024M，1232345K）。

## `[](#thresholds-and-colored-output)Thresholds and colored output`

默认情况下，每个度量标准输出都是彩色的。 颜色根据度量标准值而有所不同。

| **阈** | **中央处理器** | **记忆** | **交换** | **默认颜色** |
| 低 | x <30％ | x <75％ | x <25％ | 绿色 |
| 中 | 30％<x <80％ | 75％<x <90％ | 25％<x <75％ | 黄色 |
| 高 | x> 80％ | x> 90％ | x> 75％ | 红 |

您可以在中更改阈值 `.tmux.conf` ：

```
set -g @sysstat_cpu_medium_threshold "75"
set -g @sysstat_cpu_stress_threshold "95"

set -g @sysstat_mem_medium_threshold "85"
set -g @sysstat_mem_stress_threshold "95"

set -g @sysstat_swap_medium_threshold "80"
set -g @sysstat_swap_stress_threshold "90"

```

您可以分别更改每个阈值的颜色。 您可以使用ANSI基本颜色（红色，青色，绿色），或者如果您的终端支持256种颜色（如今大多数情况下），请使用 `colourXXX` 格式。

```
set -g @sysstat_cpu_color_low "colour076"
set -g @sysstat_cpu_color_medium "colour220"
set -g @sysstat_cpu_color_stress "colour160"
set -g @sysstat_mem_color_low "green"
set -g @sysstat_mem_color_medium "blue"
set -g @sysstat_mem_color_stress "cyan"

```

`#{(mem|cpu|swap).color}` 您的占位符 `@sysstat_(mem|cpu|swap)_view_tmpl` 将替换为相应的颜色，具体取决于指标值是否落入特定阈值。

### `[](#256-color-palette-support)256 color palette support`

对于256调色板支持，请确保 `tmux` 为父终端配置了正确的终端类型。 看 [这里](https://unix.stackexchange.com/questions/1045/getting-256-colors-to-work-in-tmux) 和 [那里](https://github.com/tmux/tmux/wiki/FAQ)

```
# ~/.tmux.conf
set -g default-terminal "screen-256color"

```

```
# parent terminal
$ echo $TERM
xterm-256color

# jump into a tmux session
$ tmux new
$ echo $TERM
screen-256color

```

### `[](#multiple-colors-for-each-threshold)Multiple colors for each threshold`

每个阈值 最多可以 配置 *3* 种颜色。 要了解为什么您可能需要这样做，请解决此任务。 注意，这是相当高级的用例。

> 我想要 `CPU: #{cpu.pused}` 度量标准输出，在“低”和“中”阈值处具有绿色和黄色的文本颜色，最后，对于“高”阈值，我想使用红色，但是使前景和背景相反，即将红色用于背景，和白色的文字。 我想要的更多信息是“ CPU：”文本用红色分隔

像这样：

[![自定义颜色的CPU阈值](https://github.com/samoshkin/tmux-plugin-sysstat/raw/master/screenshots/cpu_thresholds.png)](https://github.com/samoshkin/tmux-plugin-sysstat/blob/master/screenshots/cpu_thresholds.png)

您可以使用以下配置获得结果：

```
set -g @sysstat_cpu_view_tmpl '#[fg=#{cpu.color3}]CPU:#[default] #[fg=#{cpu.color},bg=#{cpu.color2}]#{cpu.pused}#[default]'

set -g @sysstat_cpu_color_low "$color_level_ok default default"
set -g @sysstat_cpu_color_medium "$color_level_warn default default"
set -g @sysstat_cpu_color_stress "white,bold $color_level_stress $color_level_stress"

```

## `[](#tmux-status-interval-setting)Tmux status-interval setting`

您可以配置状态刷新间隔，增加或减少 `tmux-plugin-sysstat` 命令调用的 频率 。

```
set -g status-interval 5

```

建议将其设置 `status-interval` 为合理的值，例如5\-10秒。 更频繁的更新（1秒）是无用的，因为它们分散了注意力，并导致额外的资源压力花费在指标计算本身上。

## `[](#internals-cpu-calculation)Internals: CPU calculation`

**注意：**如果您只想使用此插件而不会弄湿脚，请在此处停止。如果您是tmux的忠实用户并且对内部构造感到好奇，请继续阅读

在内部，我们 在OSX 和 Linux 上 使用 `iostat` 和 来收集度量标准值。 都不要求您安装额外的软件包。 这些命令以采样方式运行，以每N秒M次报告统计信息。 自系统启动以来，第一个样本包括平均值。 第二个是最近N秒的每秒平均CPU数（正是我们所需要的） `top` `vmstat` `top`

例如：

```
$ iostat -c 2 -w 5
          disk0       cpu     load average
    KB/t tps  MB/s  us sy id   1m   5m   15m
   44.22   6  0.26   3  2 95  1.74 1.90 2.15
    5.47   8  0.04   4  5 91  1.84 1.92 2.16  << use this row, 2nd sample

```

我们将CPU计算间隔（ `-w` ）与tmux状态栏刷新间隔（ `status-interval` 设置） 对齐 。

## `[](#internals-memory-calculation)Internals: memory calculation`

您可能会问我们将什么视为 `free` 内存以及如何计算内存。

### `[](#osx)OSX`

让我们从OSX开始。 我们使用 `vm_stat` 命令（与 `vmstat` Linux上的 命令不同 ）来报告以下数据（内存页数，而不是KB）：

```
$ vm_stat
Pages free:                               37279
Pages active:                           1514200
Pages inactive:                         1152997
Pages speculative:                         6214
Pages throttled:                              0
Pages wired down:                       1174408
Pages purgeable:                          15405
Pages stored in compressor:             1615663
Pages occupied by compressor:            306717

```

总安装内存公式为：

```
Total = free + active + inactive + speculative + occupied by compressor + wired

```

哪里

*   `free` ，系统完全未使用的内存
*   `wired` ，由系统，内核和关键应用程序存储在RAM中的重要信息。 永远不要交换到硬盘驱动器，永远不要替换为用户级数据。
*   `active` ，当前正在使用或应用程序最近使用的信息。 当这种内存长时间不使用（或应用程序关闭）时，它将移至非活动内存。
*   `inactive` ，例如Linux中的缓冲区/缓存内存。 保留了最近退出的应用程序内存，以在将来更快地启动同一应用程序。

那么问题是什么构成 `free` 和 `used` 记忆。 事实证明，OSX上的各种监视和系统统计工具对它们的计算方式都不相同。

*   htop： `used = active + wired` ， `free` \= `total - used`
*   最佳。 使用= `used = active + inactive + occupied by compressor + wired` ; 可用= `free + speculative` 居民人数（RSS）= `active`
*   OSX活动监视器。 已使用= `app memory + wired + compressor` 。 请注意，尚不清楚什么是应用程序内存。

一般来说，他们当前使用的存储器或者治疗，其可以在需要的情况下被回收（缓存，不活动，通过占用压缩机），如 `used` 或 `free` 。

谈论 `available` 内存而不是内存 是有意义的 `free` 。 可用内存是未使用的内存+可以为应用程序需求回收的任何已用内存。

因此，， `tmux-plugin-sysstat` 使用以下公式：

```
used = active + wired
available/free = free/unused + inactive + speculative + occupied by compressor

```

### `[](#linux)Linux`

同样的想法可以应用于Linux系统。

通常，诸如 `free` 报告空闲/未使用，已使用，缓冲区，高速缓存内存类型之类的命令。

```
$ free
             total       used       free     shared    buffers     cached
Mem:       1016464     900236     116228      21048      93448     241544
-/+ buffers/cache:     565244     451220
Swap:      1046524     141712     904812

```

第二行表示可用内存（空闲+缓冲区+缓存），并假设在需要时可以100％回收缓冲区和缓存。

但是，我们不使用免费，因为它的输出因系统而异。 例如，在RHEL7上没有 `-/+ buffers/cache` ，并且 `available` 以不同的方式报告内存。 我们直接从 `/proc/meminfo`

```
$ cat /proc/meminfo

MemTotal:        1016232 kB
MemFree:          152672 kB
MemAvailable:     637832 kB
Buffers:               0 kB
Cached:           529040 kB

```

`tmux-plugin-sysstat` 使用以下公式：

```
free/available = MemAvailable;  // if MemAvailable present
free/available = MemFree + Buffers + Cached;
used = MemTotal - free/avaialble

```

使用 `MemAvailable` 而不是手动计算是获取可用内存的更准确的方法 `free + buffers + cache` ，因为 `buffers + cache` 可以针对新应用程序需求100％回收 的假设 可能是错误的。 使用时 `MemAvailable` ，OS会为您计算可用内存，这显然是一种更好且准确的方法。

有关 字段的 更多推理， 请参阅 [本主题](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=34e431b0ae398fc54ea69ff85ec700722c9da773) `MemAvailable` 。