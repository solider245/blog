---
title: git diff
date: 2020-10-12 12:09:51
permalink: /pages/a78059/
categories:
  - git入门
  - git保存更改
tags:
  - 
---
# it差异

[git添加](https://www.atlassian.com/git/tutorials/saving-changes) [git commit](https://www.atlassian.com/git/tutorials/saving-changes/git-commit) [git diff](https://www.atlassian.com/git/tutorials/saving-changes/git-diff) [git stash](https://www.atlassian.com/git/tutorials/saving-changes/git-stash) [.gitignore](https://www.atlassian.com/git/tutorials/saving-changes/gitignore)

## 用git diff比较更改

区分是一项功能，它接受两个输入数据集并输出它们之间的变化。 `git diff` 是一种多用途Git命令，在执行时会在Git数据源上运行diff函数。 这些数据源可以是提交，分支，文件等。 本文档将讨论 `git diff` 工作流程模式的 常见调用 和不同模式。 该 `git diff` 命令通常与一起使用 `git status` 并 `git log`  分析Git存储库的当前状态。

## 读取差异：输出

### 原始输出格式

以下示例将在一个简单的仓库中执行。 使用以下命令创建存储库：

```
$:> mkdir diff_test_repo
$:> cd diff_test_repo
$:> touch diff_test.txt
$:> echo "this is a git diff test example" > diff_test.txt
$:> git init .
Initialized empty Git repository in /Users/kev/code/test/.git/
$:> git add diff_test.txt
$:> git commit -am"add diff test file"
[master (root-commit) 6f77fc3] add diff test file
1 file changed, 1 insertion(+)
create mode 100644 diff_test.txt
```

如果我们 `git diff` 在这一点 执行 ，将没有输出。 这是预期的行为，因为diff的回购没有变化。 创建存储库并添加 `diff_test.txt` 文件后，我们可以更改文件内容以开始尝试diff输出。

```
$:> echo "this is a diff example" > diff_test.txt
```

执行此命令将更改 `diff_test.txt` 文件 的内容 。 修改后，我们可以查看差异并分析输出。 现在执行 `git diff` 将产生以下输出：

```
diff --git a/diff_test.txt b/diff_test.txt
index 6b0c6cf..b37e70a 100644
--- a/diff_test.txt
+++ b/diff_test.txt
@@ -1 +1 @@
-this is a git diff test example
+this is a diff example
```

现在让我们检查一下diff输出的更详细的细分。

### 1.比较输入

```
diff --git a/diff_test.txt b/diff_test.txt
```

此行显示差异的输入源。 我们可以看到 `a/diff_test.txt` 并 `b/diff_test.txt` 已传递给差异。

### 2.元数据

```
index 6b0c6cf..b37e70a 100644
```

此行显示一些内部Git元数据。 您很可能不需要此信息。 此输出中的数字对应于Git对象版本哈希标识符。

### 3.变更标记

```
--- a/diff_test.txt
+++ b/diff_test.txt
```

这些行是为每个diff输入源分配符号的图例。 在这种情况下，from `a/diff_test.txt` 标记为 `---` ，而from `b/diff_test.txt` 标记 `+++` 为。

### 4.差异块

其余差异输出是差异“块”的列表。 差异仅显示文件中具有更改的部分。 在当前示例中，我们只有一个块，因为我们正在处理一个简单的场景。 块具有自己的粒度输出语义。

```
@@ -1 +1 @@
-this is a git diff test example
+this is a diff example
```

第一行是块头。 每个块之前都带有一个封闭在 `@@` 符号 内的标题 。 标头的内容是对该文件所做的更改的摘要。 在我们的简化示例中，我们有\-1 +1表示第一行发生了变化。 在比较现实的差异中，您会看到类似以下内容的标题：

```
@@ -34,6 +34,8 @@
```

在此标题示例中，从行号34开始提取了6行。此外，从行号34开始添加了8行。

差异块的其余内容显示最近的更改。 每条更改的行前都带有 `+` 或 `-` 符号，指示更改来自哪个差异输入版本。 正如我们之前所讨论的， `-` 表示从更改， `a/diff_test.txt` 而+表示从更改 `b/diff_test.txt` 。

## 突出变化

### 1。 `git diff --color-words`

`git diff` 还具有一种特殊模式，用于以更好的粒度突出显示更改： `‐‐color-words` 。 此模式通过空格标记添加和删除的行，然后对它们进行比较。

```
$:> git diff --color-words
diff --git a/diff_test.txt b/diff_test.txt
index 6b0c6cf..b37e70a 100644
--- a/diff_test.txt
+++ b/diff_test.txt
@@ -1 +1 @@
this is agit difftest example
```

现在，输出仅显示已更改的颜色编码单词。

### 2。 `git diff-highlight`

如果克隆git源，则会找到一个名为contrib的子目录。 它包含了一堆与git相关的工具以及尚未升级到git core的其他有趣的点点滴滴。 其中之一是一个称为diff\-highlight的Perl脚本。 差异突出显示将差异输出的匹配行配对，并突出显示已更改的子词片段。

```
$:> git diff | /your/local/path/to/git-core/contrib/diff-highlight/diff-highlight
diff --git a/diff_test.txt b/diff_test.txt
index 6b0c6cf..b37e70a 100644
--- a/diff_test.txt
+++ b/diff_test.txt
@@ -1 +1 @@
-this is a git diff test example
+this is a diff example
```

现在，我们已将差异缩小到最小的变化。

## 差异二进制文件

到目前为止，我们已经展示了除文本文件实用程序外， `git diff` 还可以在二进制文件上运行。 不幸的是，默认输出不是很有帮助。

```
$:> git diff
Binary files a/script.pdf and b/script.pdf differ
```

Git确实具有一项功能，可让您指定shell命令以在执行diff之前将二进制文件的内容转换为文本。 确实需要一些设置。 首先，您需要指定一个textconv过滤器来描述如何将某种类型的二进制文件转换为文本。 我们正在使用一个名为pdftohtml的简单实用程序（可通过自制程序获得）将我的PDF转换为人类可读的HTML。 您可以通过编辑 `.git/config` 文件 来为单个存储库进行设置，也可以通过编辑来进行 全局设置 `~ /.gitconfig`

```
[diff "pdfconv"]
textconv=pdftohtml -stdout
```

然后，您需要做的就是将一个或多个文件模式与我们的pdfconv过滤器相关联。 您可以通过 `.gitattributes` 在资源库的根目录中 创建一个 文件来实现。

```
*.pdf diff=pdfconv
```

一旦配置， `git diff` 将首先通过配置的转换器脚本运行二进制文件，并比较转换器的输出。 可以使用相同的技术从各种二进制文件中获取有用的差异，例如：zip，jar和其他归档文件：使用 `unzip -l` （或类似方法）代替pdf2html将向您显示在提交图像之间添加或删除的路径： exiv2可用于显示元数据更改，例如图像尺寸文档：存在转换工具，可用于将.odf，.doc和其他文档格式转换为纯文本。 有时，字符串通常适用于不存在正式转换器的二进制文件。

## 比较文件：git diff文件

该 `git diff` 命令可以传递一个明确的文件路径选项。 当文件路径传递给 `git diff` diff操作时，范围将限于指定的文件。 以下示例演示了此用法。

```
git diff HEAD ./path/to/file
```

此示例的作用域是 `./path/to/file` 调用时，它将比较工作目录中的特定更改和索引，以显示尚未暂存的更改。 默认情况下， `git diff` 将对进行比较 `HEAD` 。 `HEAD` 在上面的示例中 省略 `git diff ./path/to/file` 具有相同的效果。

```
git diff --cached ./path/to/file
```

当 `git diff` 使用 `--cached` 选项 调用时， diff将比较已执行的更改与本地存储库。 该 `--cached` 选项与相同 `--staged` 。

## 比较所有变化

`git diff` 没有文件路径的 调用 将比较整个存储库中的更改。 上面的文件特定示例可以在不带 `./path/to/file` 参数的 情况下调用， 并且在本地存储库中的所有文件中都具有相同的输出结果。

## 自上次提交以来的更改

默认情况下， `git diff` 将显示自上次提交以来所有未提交的更改。

```
git diff
```

## 比较两个不同提交之间的文件

`git diff` 可以通过Git ref传递给diff。 某些参考示例是， `HEAD` 标记和分支名称。 Git中的每个提交都有一个提交ID，您可以在执行时获得该ID `GIT LOG` 。 您也可以将此提交ID传递给 `git diff` 。

```
git log --prety=oneline
957fbc92b123030c389bf8b4b874522bdf2db72c add feature
ce489262a1ee34340440e55a0b99ea6918e19e7a rename some classes
6b539f280d8b0ec4874671bae9c6bed80b788006 refactor some code for feature
646e7863348a427e1ed9163a9a96fa759112f102 add some copy to body
$:> git diff 957fbc92b123030c389bf8b4b874522bdf2db72c ce489262a1ee34340440e55a0b99ea6918e19e7a
```

## 比较分支

### 比较两个分支

像所有其他ref输入一样对分支进行比较 `git diff`

```
git diff branch1..other-feature-branch
```

本示例介绍了点运算符。 此示例中的两个点表示差异输入是两个分支的尖端。 如果省略点并在分支之间使用空格，则会发生相同的效果。 此外，还有一个三点运算符：

```
git diff branch1...other-feature-branch
```

三点运算符通过更改第一个输入参数来启动差异 `branch1` 。 它变为 `branch1` 两个diff输入，的共享祖先 `branch1` 和其他功能分支 之间的共享公共祖先提交的引用 。 最后一个参数输入参数保持不变，成为其他功能分支的提示。

## 比较两个分支的文件

要跨分支比较特定文件，请将文件路径作为第三个参数传递给 `git diff`

```
git diff master new_branch ./diff_test.txt
```

## 摘要

本页讨论了Git差异化过程和 `git diff` 命令。 我们讨论了如何读取 `git diff` 输出以及输出中包含的各种数据。 提供了有关如何 `git diff` 使用突出显示和颜色 更改 输出的 示例 。 我们讨论了不同的差异化策略，例如如何差异化分支和特定提交中的文件。 除了 `git diff` 命令外，我们还使用 `git log` 和 `git checkout` 。