---
title: git hooks
date: 2020-10-12 12:09:51
permalink: /pages/b323dd/
categories:
  - git
  - git进阶
tags:
  - 
---
# 吉特·胡克斯

[概念概述](#conceptual-overview) [本地挂钩](#local-hooks) [服务器端挂钩](#server-side-hooks) [摘要](#summary)

Git钩子是脚本，每次在Git存储库中发生特定事件时，它们都会自动运行。 它们使您可以自定义Git的内部行为，并在开发生命周期的关键点触发可自定义的动作。

![在提交创建过程中执行的挂钩](https://wac-cdn.atlassian.com/dam/jcr:ac22adee-d740-4216-a92a-33c14b5623e5/01.svg?cdnVersion=1084)

Git钩子的常见用例包括鼓励提交策略，根据存储库的状态更改项目环境以及实施连续集成工作流。 但是，由于脚本是无限可定制的，因此您可以使用Git挂钩来自动化或优化开发工作流程的几乎任何方面。

在本文中，我们将从概念上概述Git钩子如何工作。 然后，我们将调查一些在本地和服务器端存储库中使用的最受欢迎的钩子。

## 概念概述

所有Git挂钩都是普通脚本，当存储库中发生某些事件时，Git会执行这些脚本。 这使得它们非常容易安装和配置。

挂钩可以驻留在本地或服务器端存储库中，并且仅响应该存储库中的操作而执行。 我们将在本文后面详细讨论钩子的类别。 本节其余部分讨论的配置适用于本地和服务器端挂钩。

### 安装挂钩

挂钩位于 `.git/hooks` 每个Git存储库 的 目录中。 初始化存储库时，Git会使用示例脚本自动填充此目录。 如果查看一下 `.git/hooks` ，您将找到以下文件：

```
applypatch-msg.sample pre-push.sample
commit-msg.sample pre-rebase.sample
post-update.sample prepare-commit-msg.sample
pre-applypatch.sample update.sample
pre-commit.sample
```

这些代表了大多数可用的挂钩，但是 `.sample` 扩展名阻止它们在默认情况下执行。 要“安装”挂钩，您要做的就是删除 `.sample` 扩展名。 或者，如果您是从头开始编写新脚本，则可以简单地添加一个与上述文件名之一匹配的新文件，减去 `.sample` 扩展名。

例如，尝试安装一个简单的 `prepare-commit-msg` 钩子。 `.sample` 从此脚本中 删除 扩展名，并将以下内容添加到文件中：

```
#!/bin/sh
echo "# Please include a useful commit message!" > $1
```

挂钩必须是可执行的，因此，如果要从头开始创建脚本，则可能需要更改脚本的文件权限。 例如，要确保该 `prepare-commit-msg` 文件是可执行文件，您将运行以下命令：

```
chmod +x prepare-commit-msg
```

现在，您应该在每次运行时看到此消息，而不是默认的提交消息 `git commit` 。 我们将在“准备提交消息”部分中仔细研究它的实际工作方式。 现在，让我们陶醉于我们可以自定义Git的某些内部功能这一事实。

内置的示例脚本是非常有用的参考，因为它们记录了传递给每个挂钩的参数（每个挂钩各不相同）。

### 脚本语言

内置脚本主要是Shell和PERL脚本，但是您可以使用任何喜欢的脚本语言，只要它可以作为可执行文件运行即可。 `#!/bin/sh` 每个脚本中 的shebang行（ ）定义了如何解释文件。 因此，要使用其他语言，只需将其更改为解释器的路径即可。

例如，我们可以在 `prepare-commit-msg` 文件中 编写可执行的Python脚本， 而无需使用shell命令。 以下挂钩与上一节中的shell脚本具有相同的作用。

```
#!/usr/bin/env python
import sys, os
commit_msg_filepath = sys.argv[1]
with open(commit_msg_filepath, 'w') as f:
f.write("# Please include a useful commit message!")
```

注意第一行如何更改为指向Python解释器。 而且， `$1` 我们没有使用 `sys.argv[1]` （访问稍后 传递给脚本的第一个参数），而是使用 了。

对于Git钩子来说，这是一个非常强大的功能，因为它使您可以使用最适应的任何语言进行工作。

### 钩的范围

挂钩对于任何给定的Git存储库都是本地的，并且 在运行时 它们 *不会* 复制到新的存储库中 `git clone` 。 而且，由于挂钩是本地的，因此任何有权访问该存储库的人都可以对其进行更改。

为开发人员团队配置挂钩时，这具有重要影响。 首先，您需要找到一种方法来确保挂钩在您的团队成员中保持最新状态。 其次，您不能强迫开发人员以某种方式创建提交\-您只能鼓励他们这样做。

为开发人员团队维护挂钩可能会有些棘手，因为该 `.git/hooks` 目录不会随项目的其余部分克隆，也不会受到版本控制。 解决这两个问题的简单方法是将您的钩子存储在实际项目目录中（该 `.git` 目录 之上 ）。 这使您可以像其他任何版本控制文件一样编辑它们。 要安装该挂钩，您可以在中创建指向它的符号链接，也可以在 更新挂钩时将 `.git/hooks` 其复制并粘贴到 `.git/hooks` 目录中。

![在提交创建过程中执行的挂钩](https://wac-cdn.atlassian.com/dam/jcr:e068ea71-a552-4d07-9917-49104f4d382e/02.svg?cdnVersion=1084)

作为替代，Git还提供了 [模板目录](http://git-scm.com/docs/git-init#_template_directory) 机制，使自动安装挂钩变得更加容易。 `.git` 每次使用 `git init` 或 时 ，此模板目录中包含的所有文件和 目录都会 复制到该 目录中 `git clone` 。

存储库的所有者可以更改或完全卸载以下描述的 所有 [本地挂钩](https://www.atlassian.com/git/tutorials/git-hooks/local-hooks) 。 是否实际使用挂钩完全取决于每个团队成员。 考虑到这一点，最好将Git挂钩视为方便的开发人员工具，而不是严格执行的开发策略。

也就是说，可以使用 [服务器端hook](https://www.atlassian.com/git/tutorials/git-hooks/server-side-hooks) 拒绝不符合某些标准的提交 。 我们将在本文后面详细讨论。

## 本地钩

本地挂钩仅影响它们所在的存储库。 在通读本节时，请记住，每个开发人员都可以更改自己的本地挂钩，因此不能将它们用作实施提交策略的方法。 但是，它们可以使开发人员更容易遵守某些准则。

在本节中，我们将探索6个最有用的本地钩子：

*   `pre-commit`
*   `prepare-commit-msg`
*   `commit-msg`
*   `post-commit`
*   `post-checkout`
*   `pre-rebase`

前4个挂钩可让您插入整个提交生命周期，后2个挂钩可让您 分别 对 `git checkout` 和 `git rebase` 命令 执行一些额外的操作或安全检查 。

所有的 `pre-` 挂钩都可以让您更改即将发生的操作，而 `post-` 挂钩仅用于通知。

我们还将看到一些有用的技术，这些技术可用于使用较低级别的Git命令解析钩子参数和请求有关存储库的信息。

### 提交前

`pre-commit` 每次您运行 该 脚本时 `git commit` ，Git都会向开发人员询问提交消息或生成提交对象。 您可以使用此挂钩检查将要提交的快照。 例如，您可能需要运行一些自动化测试，以确保提交不会破坏任何现有功能。

没有参数传递给 `pre-commit` 脚本，并且以非零状态退出将中止整个提交。 让我们看一下内置 `pre-commit` 钩子 的简化（和更详细）版本 。 如果该脚本发现 `git diff-index` 命令 所定义的任何空格错误，则该脚本将中止提交 （默认情况下，追踪空格，仅包含空格的行以及行的初始缩进内的空格和制表符后的空格均被视为错误）。

```
#!/bin/sh
# Check if this is the initial commit
if git rev-parse --verify HEAD >/dev/null 2>&1
then
echo "pre-commit: About to create a new commit..."
against=HEAD
else
echo "pre-commit: About to create the first commit..."
against=4b825dc642cb6eb9a060e54bf8d69288fbee4904
fi
# Use git diff-index to check for whitespace errors
echo "pre-commit: Testing for whitespace errors..."
if ! git diff-index --check --cached $against
then
echo "pre-commit: Aborting commit due to whitespace errors"
exit 1
else
echo "pre-commit: No whitespace errors :)"
exit 0
fi
```

为了使用 `git diff-index` ，我们需要找出我们将索引 与之 比较的提交引用。 通常，这是 `HEAD` ; 但是， `HEAD` 在创建初始提交时不存在，因此我们的首要任务是解决这种情况。 我们使用进行此操作 [`git rev-parse --verify`](https://www.kernel.org/pub/software/scm/git/docs/git-rev-parse.html) ，该操作仅检查参数（ `HEAD` ）是否为有效引用。 该 `>/dev/null 2>&1` 部分使来自的任何输出静音 `git rev-parse` 。 任一 `HEAD` 或空commit对象被存储在 `against` 用于在使用可变 `git diff-index` 。 所述 `4b825d...` 散列是魔提交表示一个空的提交ID。

该 [`git diff-index --cached`](https://www.kernel.org/pub/software/scm/git/docs/git-diff-index.html) 命令将提交与索引进行比较。 通过传递 `--check` 选项，我们要求它警告我们更改是否会引起空格错误。 如果是这样，我们将通过返回退出状态来中止提交 `1` ，否则将以退出， `0` 提交工作流将继续正常进行。

这只是 `pre-commit` 钩子的 一个例子 。 碰巧是使用现有的Git命令来对建议的提交所引入的更改进行测试，但是您可以做任何您想做的事情， `pre-commit` 包括执行其他脚本，运行第三方测试套件或使用Lint检查代码样式。

### 准备提交消息

在 `prepare-commit-msg` 挂钩之后调用该 `pre-commit` 挂钩，以使用提交消息填充文本编辑器。 这是更改自动生成的提交消息以压缩或合并提交的好地方。

1\-3个参数传递给 `prepare-commit-msg` 脚本：

1.  包含消息的临时文件的名称。 您可以通过就地更改此文件来更改提交消息。
2.  提交的类型。 可以是 `message` （ `-m` 或 `-F` 选项）， `template` （ `-t` 选项）， `merge` （如果提交是合并提交）或 `squash` （如果提交正在压缩其他提交）。
3.  相关提交的SHA1哈希。 只有当给予 `-c` ， `-C` 或 `--amend` 在给定的选项。

与一样 `pre-commit` ，以非零状态退出将中止提交。

我们已经看到了一个编辑提交消息的简单示例，但是让我们看一个更有用的脚本。 使用问题跟踪器时，常见的约定是在单独的分支中解决每个问题。 如果在分支名称中包含发行号，则可以编写一个 `prepare-commit-msg` 钩子，以将其自动包括在该分支的每个提交消息中。

```
#!/usr/bin/env python
import sys, os, re
from subprocess import check_output
# Collect the parameters
commit_msg_filepath = sys.argv[1]
if len(sys.argv) > 2:
commit_type = sys.argv[2]
else:
commit_type = ''
if len(sys.argv) > 3:
commit_hash = sys.argv[3]
else:
commit_hash = ''
print "prepare-commit-msg: File: %s\nType: %s\nHash: %s" % (commit_msg_filepath, commit_type, commit_hash)
# Figure out which branch we're on
branch = check_output(['git', 'symbolic-ref', '--short', 'HEAD']).strip()
print "prepare-commit-msg: On branch '%s'" % branch
# Populate the commit message with the issue #, if there is one
if branch.startswith('issue-'):
print "prepare-commit-msg: Oh hey, it's an issue branch."
result = re.match('issue-(.*)', branch)
issue_number = result.group(1)
with open(commit_msg_filepath, 'r+') as f:
content = f.read()
f.seek(0, 0)
f.write("ISSUE-%s %s" % (issue_number, content))
```

首先，上面的 `prepare-commit-msg` 钩子向您展示了如何收集传递给脚本的所有参数。 然后，它调用 `git symbolic-ref --short HEAD` 以获取与对应的分支名称 `HEAD` 。 如果此分支名称以开头 `issue-` ，它将重写提交消息文件的内容，以在第一行中包含发行号。 因此，如果您的分支名称为 `issue-224` ，这将生成以下提交消息。

```
ISSUE-224
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch issue-224
# Changes to be committed:
# modified: test.txt
```

使用时要记住的一件事 `prepare-commit-msg` 是，即使用户传递带有 `-m` 选项的 消息，它也可以运行 `git commit` 。 这意味着上述脚本将自动插入 `ISSUE-[#]` 字符串，而无需用户对其进行编辑。 您可以通过查看第二个参数（ `commit_type` ）是否等于来 处理这种情况 `message` 。

但是，如果没有该 `-m` 选项，则该 `prepare-commit-msg` 挂钩确实允许用户在生成消息后对其进行编辑，因此，与执行提交消息策略的方法相比，这实际上更是一种便捷脚本。 为此，您需要在 `commit-msg` 下一节中讨论 的 挂钩。

### 提交讯息

该 `commit-msg` 挂钩与该 `prepare-commit-msg` 挂钩 很相似 ，但是 在用户输入提交消息 *之后* 调用 该 挂钩 。 这是警告开发人员其信息不符合您团队标准的适当位置。

传递给该钩子的唯一参数是包含消息的文件的名称。 如果它不喜欢用户输入的消息，则可以就地更改此文件（就像使用一样 `prepare-commit-msg` ），也可以通过以非零状态退出来完全中止提交。

例如，以下脚本检查以确保用户没有删除 上一部分中 `ISSUE-[#]` 由 `prepare-commit-msg` 挂钩 自动生成 的 字符串 。

```
#!/usr/bin/env python
import sys, os, re
from subprocess import check_output
# Collect the parameters
commit_msg_filepath = sys.argv[1]
# Figure out which branch we're on
branch = check_output(['git', 'symbolic-ref', '--short', 'HEAD']).strip()
print "commit-msg: On branch '%s'" % branch
# Check the commit message if we're on an issue branch
if branch.startswith('issue-'):
print "commit-msg: Oh hey, it's an issue branch."
result = re.match('issue-(.*)', branch)
issue_number = result.group(1)
required_message = "ISSUE-%s" % issue_number
with open(commit_msg_filepath, 'r') as f:
content = f.read()
if not content.startswith(required_message):
print "commit-msg: ERROR! The commit message must start with '%s'" % required_message
sys.exit(1)
```

尽管每次用户创建提交都会调用此脚本，但是您应该避免在检查提交消息之外做很多事情。 如果您需要通知其他服务快照已提交，则应使用 `post-commit` 挂钩。

### 投产后

该 `post-commit` 挂钩在调用后立即 `commit-msg` 挂机。 它无法更改 `git commit` 操作 的结果 ，因此主要用于通知目的。

该脚本不带任何参数，并且其退出状态不会以任何方式影响提交。 对于大多数 `post-commit` 脚本，您需要访问刚刚创建的提交。 您可以 `git rev-parse HEAD` 用来获取新提交的SHA1哈希，或者可以 `git log -1 HEAD` 用来获取其所有信息。

例如，如果您想在每次提交快照时都向老板发送电子邮件（可能不是大多数工作流程的最佳主意），则可以添加以下 `post-commit` 挂钩。

```
#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText
from subprocess import check_output
# Get the git log --stat entry of the new commit
log = check_output(['git', 'log', '-1', '--stat', 'HEAD'])
# Create a plaintext email message
msg = MIMEText("Look, I'm actually doing some work:\n\n%s" % log)
msg['Subject'] = 'Git post-commit hook notification'
msg['From'] = 'mary@example.com'
msg['To'] = 'boss@example.com'
# Send the message
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
session.ehlo()
session.starttls()
session.ehlo()
session.login(msg['From'], 'secretPassword')
session.sendmail(msg['From'], msg['To'], msg.as_string())
session.quit()
```

可以用来 `post-commit` 触发本地连续集成系统，但是大多数情况下，您会想在 `post-receive` 挂钩中 执行此操作 。 它在服务器而不是用户的本地计算机上运行，​​并且每次 *任何* 开发人员推送他们的代码 时*都* 运行 。 这使它成为执行连续集成的更合适的地方。

### 结帐后

该 `post-checkout` 挂钩的工作原理与该 `post-commit` 挂钩 非常相似 ，但是只要您成功通过签出引用，就会调用 该 挂钩 `git checkout` 。 这很适合清除您的工作目录中的生成文件，否则会引起混淆。

该挂钩接受三个参数，并且其退出状态对 `git checkout` 命令 没有影响 。

1.  前一个HEAD的参考
2.  新HEAD的参考
3.  一个标志，告诉您它是分支检出还是文件检出。 该标志 分别 是 `1` 和 `0` 。

当 `.pyc` 切换分支后 生成的 文件仍然 存在时，Python开发人员会遇到一个常见问题 。 解释器有时会使用这些 文件 `.pyc` 而不是 `.py` 源文件。 为避免混淆， `.pyc` 每次使用以下 `post-checkout` 脚本 签出新分支时 ，都可以删除所有 文件 ：

```
#!/usr/bin/env python
import sys, os, re
from subprocess import check_output
# Collect the parameters
previous_head = sys.argv[1]
new_head = sys.argv[2]
is_branch_checkout = sys.argv[3]
if is_branch_checkout == "0":
print "post-checkout: This is a file checkout. Nothing to do."
sys.exit(0)
print "post-checkout: Deleting all '.pyc' files in working directory"
for root, dirs, files in os.walk('.'):
for filename in files:
ext = os.path.splitext(filename)[1]
if ext == '.pyc':
os.unlink(os.path.join(root, filename))
```

挂钩脚本的当前工作目录始终设置为存储库的根目录，因此该 `os.walk('.')` 调用会遍历存储库中的每个文件。 然后，我们检查其扩展名，如果它是 `.pyc` 文件 ，则将其删除 。

您还可以使用 `post-checkout` 挂钩根据已签出的分支来更改工作目录。 例如，您可以使用 `plugins` 分支将所有插件存储在核心代码库之外。 如果这些插件需要很多其他分支不需要的二进制文件，则只有在使用 `plugins` 分支 时才可以有选择地构建它们 。

### 变基前

`pre-rebase` 在 `git rebase` 更改任何内容 之前先调用 该 挂钩 ，这是确保不会发生可怕事件的好地方。

这个钩子有两个参数：系列派生自其的上游分支，以及该分支的基础。 重新建立当前分支时，第二个参数为空。 要中止变基，请以非零状态退出。

例如，如果要完全禁止在存储库中进行基础调整，则可以使用以下 `pre-rebase` 脚本：

```
#!/bin/sh
# Disallow all rebasing
echo "pre-rebase: Rebasing is dangerous. Don't do it."
exit 1
```

现在，每次运行 `git rebase` ，您都会看到以下消息：

```
pre-rebase: Rebasing is dangerous. Don't do it.
The pre-rebase hook refused to rebase.
```

有关更深入的示例，请查看其中包含的 `pre-rebase.sample` 脚本。 该脚本在何时禁止重新定级方面更为智能。 它检查您要重新确定基准的主题分支是否已经合并到该 `next` 分支（假定为主线分支）中。 如果有的话，您可能会因重新设定基准而陷入麻烦，因此脚本中止了重新设定基准。

## 服务器端挂钩

服务器端挂钩的工作方式与本地挂钩相同，不同之处在于它们位于服务器端存储库（例如，中央存储库或开发人员的公共存储库）中。 当附加到官方存储库时，其中一些可以用作通过拒绝某些提交来实施策略的方法。

在本文的其余部分中，我们将讨论3个服务器端挂钩：

*   `pre-receive`
*   `update`
*   `post-receive`

所有这些挂钩可让您对 `git push` 过程的 不同阶段做出反应 。

服务器端挂钩的输出通过管道传递到客户端的控制台，因此很容易将消息发送回开发人员。 但是，您还应该记住，这些脚本在执行完毕之前不会返回对终端的控制，因此您在执行长时间运行的操作时应格外小心。

### 预先接收

`pre-receive` 每当有人 `git push` 用来将提交推送到存储库 时，都会执行 该 挂钩 。 它应始终驻留在作为 推送目标 的 *远程* 存储库中，而不是原始存储库中。

挂钩在更新任何引用之前运行，因此是执行所需的任何类型的开发策略的好地方。 如果您不喜欢执行推送的人员，不喜欢提交消息的格式或提交中包含的更改，则可以拒绝它。 虽然您不能阻止开发人员进行格式错误的提交，但可以通过拒绝它们来阻止它们进入官方代码库 `pre-receive` 。

该脚本不带任何参数，但是要推送的每个引用都以以下格式在标准输入的单独一行中传递给脚本：

```
<old-value> <new-value> <ref-name>
```

您可以使用非常 `pre-receive` 简单的脚本 来查看此钩子的工作原理，该 脚本仅读取推入的引用并将其打印出来。

```
#!/usr/bin/env python
import sys
import fileinput
# Read in each ref that the user is trying to update
for line in fileinput.input():
print "pre-receive: Trying to push ref: %s" % line
# Abort the push
# sys.exit(1)
```

同样，这与其他挂钩略有不同，因为信息是通过标准输入而不是作为命令行参数传递给脚本的。 将上述脚本放置在 `.git/hooks` 远程存储库 的 目录中并推送 `master` 分支之后，您将在控制台中看到类似以下内容的内容：

```
b6b36c697eb2d24302f89aa22d9170dfe609855b 85baa88c22b52ddd24d71f05db31f4e46d579095 refs/heads/master
```

您可以使用这些SHA1散列以及一些较低级别的Git命令来检查将要引入的更改。 一些常见的用例包括：

*   拒绝涉及上游基础的变更
*   防止非快进合并
*   检查用户是否具有进行预期更改的正确权限（主要用于集中式Git工作流程）

如果推送了多个引用，则从其返回非零状态将 `pre-receive` 中止 *所有* 引用 。 如果要根据情况接受或拒绝分支，则需要使用 `update` 挂钩。

### 更新资料

该 `update` 钩子称为after `pre-receive` ，其工作方式大致相同。 在实际更新任何东西之前，它仍然会被调用，但是对于每个推送的引用，它都会被分别调用。 这意味着如果用户尝试推送4个分支，则将 `update` 执行4次。 不同于 `pre-receive` ，此钩子不需要从标准输入中读取。 而是，它接受以下3个参数：

1.  引用的名称正在更新
2.  存储在ref中的旧对象名称
3.  存储在ref中的新对象名称

这是传递给的相同信息 `pre-receive` ，但是由于 `update` 是分别为每个引用调用的，因此您可以拒绝某些引用，同时允许其他引用。

```
#!/usr/bin/env python
import sys
branch = sys.argv[1]
old_commit = sys.argv[2]
new_commit = sys.argv[3]
print "Moving '%s' from %s to %s" % (branch, old_commit, new_commit)
# Abort pushing only this branch
# sys.exit(1)
```

上面的 `update` 钩子仅输出分支和旧的/新的提交哈希。 当将多个分支推送到远程存储库时，您将看到 `print` 针对每个分支执行 的 语句。

### 接收后

`post-receive` 在成功执行推入操作之后，将调用 该 挂钩，这使其成为执行通知的好地方。 对于许多工作流程而言，这是触发通知的最佳场所， `post-commit` 因为更改可以在公用服务器上使用，而不是仅驻留在用户的本地计算机上，而不是在此处。 通过电子邮件向其他开发人员发送电子邮件并触发持续集成系统是的常见用例 `post-receive` 。

该脚本不带任何参数，但发送的信息与 `pre-receive` 通过标准输入 发送的信息相同 。

## 摘要

在本文中，我们学习了如何使用Git挂钩来更改内部行为，并在存储库中发生某些事件时接收通知。 挂钩是驻留在 `.git/hooks` 资源库 中的普通脚本 ，这使得它们非常易于安装和自定义。

我们还研究了一些最常见的本地和服务器端挂钩。 这些使我们能够插入整个开发生命周期。 现在，我们知道如何在提交创建过程以及该 `git push` 过程的 每个阶段执行可自定义的动作 。 有了一点脚本知识，您几乎可以使用Git存储库执行您可以想象的任何事情。