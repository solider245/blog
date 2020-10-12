---
title: git-show
date: 2020-10-12 12:09:51
permalink: /pages/c59014/
categories:
  - git
  - git进阶
tags:
  - 
---
# Git秀

### 什么是git\-show？

`git-show` 是一个命令行实用程序，用于查看有关Git对象的扩展详细信息，例如Blob，树，标签和提交。 `git-show` 每个对象类型都有特定的行为。

标签显示标签消息和标签中包含的其他对象。 树显示树中对象的名称和内容。 Blob显示Blob的直接内容。 提交显示提交日志消息和提交更改的差异输出。

Git对象全部由引用访问。 默认情况下， `git-show` 对HEAD引用起作用。 HEAD引用始终指向当前分支的最后提交。 因此，您可以 `git-show` 用来显示日志消息和最新提交的diff输出。

### Git显示选项

**`<object>…`**
到一个或多个对象的一个列表的引用可以被传递到检查那些特定的对象。 如果未传递任何显式对象，则 `git-show` 默认为HEAD引用。

**`--pretty[=<format>]`**
pretty选项采用辅助格式值，该值可以是 `oneline, short, medium, full, fuller, email, raw,` 和之一 `format:<string>` 。 如果省略，则格式默认为 `medium` 。 每个格式选项都是一个不同的模板，用于说明Git如何格式化显示输出。 <code> oneline </ code>选项对于显示提交列表非常有用。

**`--abbrev-commit`**
该选项缩短了输出提交ID的长度。 提交ID的长度为40个字符，在狭窄的终端屏幕上很难查看。 结合使用此选项 `--pretty=oneline` 可以产生非常简洁的 `git log` 输出。

**`--no-abbrev-commit`**
始终显示完整的40个字符的提交ID。 这将忽略\- `abbrev-commit` 以及其他缩写提交ID的选项，例如 `--oneline format`

**`--oneline`**
这是使用扩展命令的快捷方式 `--pretty=oneline --abbrev-commit`

**`--encoding[=<encoding>]`**
Git日志消息上的字符编码默认为UTF\-8。 编码选项可以更改为其他字符编码输出。 如果您在具有不同字符编码的环境（例如亚洲语言终端）中使用Git，这将很有用。

**`>--expand-tabs=<n>
--expand-tabs
--no-expand-tabs`**
这些选项在日志消息输出中用空格替换制表符。 `n` 可以设置 该 值以配置选项卡扩展到多少个空格字符。 没有显式的n值，制表符将扩展为8个空格。 `--no-expand-tabs` 相当于 `n=0`

**`--notes=<ref>
--no-notes`**
Git有一个便笺系统，该系统使任意“便笺”元数据都可以附加到对象上。 使用时，可以隐藏或过滤此数据 `git-show` 。

**`--show-signature`**
此选项通过将提交传递给gpg子命令来验证提交是否已使用加密签名签名。

### git\-show的漂亮格式

`--pretty` 上面讨论 的 选项接受几个辅助选项来调整 `git-show` 输出 格式 。 下面列出了这些辅助选项以及示例模板

*   **一条线**
    `<sha1> <title line>`

Oneline尝试将尽可能多的信息压缩为一行

*   **短**
    `commit <sha1>
    Author: <author>
    <title line>`

*   **中**
    `commit <sha1>
    Author: <author>
    Date: <author date>
    <title line>
    <full commit message>`

*   **充分**
    `commit <sha1>
    Author: <author>
    Commit: <committer>
    <title line>
    <full commit message>`

*   **饱满的**
    `commit <sha1>
    Author: <author>
    AuthorDate: <author date>
    Commit: <committer>
    CommitDate: <committer date>
    <title line>
    <full commit message>`

*   **电子邮件**
    `From <sha1> <date>
    From: <author>
    Date: <author date>
    Subject: [PATCH] <title line>
    <full commit message>`

*   **raw**
    **raw** format忽略传递给其他直接格式化选项， `git-show` 并完全按照存储在对象中的方式输出提交。 Raw将无视 `--abrev` 并且 `--no-abbrev` 始终显示父提交。

*   **format：**
    format启用自定义输出格式的规范。 它的工作方式类似于C语言的 `printf` 命令。 该 `--pretty=format` 选项采用模板字符串的辅助值。 模板有权访问占位符变量，这些占位符变量将被提交对象中的数据填充。 这些占位符在下面列出：

    • *％H* ：提交哈希
    • *％h* ：缩写提交哈希
    • *％T* ：树哈希
    • *％t* ：缩写树哈希
    • *％P* ：父哈希
    • *％p* ：缩写父哈希
    • *％an* ：作者名称
    • *％aN* ：作者姓名
    • *％ae* ：作者电子邮件
    • *％aE* ：作者电子邮件
    • *％ad* ：作者日期（格式方面\-\-date =选项）
    • *％aD* ：作者日期，RFC2822样式
    • *％ar* ：作者日期，相对
    • *％at* ：作者日期，UNIX时间戳
    • *％ai* ：作者日期，ISO 8601格式
    *•％cn* ：提交者名称
    • *％cN* ：提交者名称
    • *％ce* ：提交者电子邮件
    • *％cE* ：提交者电子邮件
    • *％cd* ：提交者日期
    • *％cD* ：提交者日期，RFC2822样式
    • *％cr* ：提交者日期，相对
    • *％ct* ：提交者日期，UNIX时间戳
    • *％ci* ：提交者日期，ISO 8601格式
    • *％d* ：引用名称，例如git\-log的\-\-decorate选项（1）
    • *％e* ：编码
    • *％s* ：主题
    • *％f* ：经过清理的主题行，适用于文件名
    *•％b* ：正文
    • *％N* ：提交注释
    • *％gD* ：reflog选择器，例如refs / stash @ { 1}
    • *％gd* ：缩短的引用日志选择器，例如stash @ {1}
    • *％gs* ：引用主题
    • *％Cred* ：将颜色切换为红色
    • *％Cgreen* ：将颜色切换为绿色
    • *％Cblue* ：将颜色切换为蓝色
    • *％Creset* ：重设颜色
    • *％C（...）* ：颜色规格，如color.branch。\*配置选项
    • *％m* ：左，右或边界标记
    • *％n* ：换行符
    • *%%* ：原始％
    • *％x00* ：从十六进制代码打印字节
    • *％w（\[<w> \[， <i1> \[，<i2>\]\]\]））* ：换行，如git\-shortlog的\-w选项

### git\-show的例子

```
git show --pretty="" --name-only bd61ad98
```

这将列出提交中涉及的所有文件

```
git show REVISION:path/to/file
```

这将显示文件的特定版本。 将其替换 `REVISON` 为Git sha。

```
git show v2.0.0 6ef002d74cbbc099e1063728cab14ef1fc49c783
```

这将显示v2.0.0标记，并在 `6ef002d74cbbc099e1063728cab14ef1fc49c783`

```
git show commitA...commitD
```

这将输出从 `commitA` 到 的范围内的所有提交 `commit D`

### 摘要

`git-show` 是用于检查Git存储库中对象的非常通用的命令。 它可用于将特定版本的特定文件作为目标。 使用来检查提交范围 `git-show` 将输出该范围之间的所有单个提交。 `git-show` 在创建补丁说明和跟踪存储库中的更改时可以提供帮助。