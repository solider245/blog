---
title: 适用于Linux初学者的16个有用的'cp'命令示例
date: 2020-10-12 12:09:51
permalink: /pages/9c7e64/
categories:
  - 常用命令
  - cp命令
tags:
  - 
---
作为Linux用户，复制文件和目录是最常见的日常操作task.cp命令，用于使用命令行将文件和目录从一个本地复制到另一个本地。 cp命令在几乎所有的Unix和Linux操作系统中都可用

[![cp-command-examples-linux-beginners](https://www.linuxtechi.com/wp-content/uploads/2019/02/cp-command-examples-linux-beginners.jpg)](https://www.linuxtechi.com/wp-content/uploads/2019/02/cp-command-examples-linux-beginners.jpg)

在本文中，我们将为Linux初学者演示16个有用的cp命令示例。 以下是cp命令的基本语法，

**将一个文件复制到另一个文件**

＃cp {options} source\_file target\_file

**将文件复制到另一个目录或文件夹**

＃cp {options} source\_file target\_directory

**将目录复制到目录**

＃cp {options} source\_directory target\_directory

让我们跳入cp命令的实际示例，

#### 示例：1）将文件复制到目标目录

假设我们出于某些备份目的将/ etc / passwd文件复制到/ mnt / backup目录，因此在cp命令下运行，

root@linuxtechi:~# cp /etc/passwd /mnt/backup/
root@linuxtechi:~#

使用以下命令来验证它是否已被复制。

root@linuxtechi:~# ls \-l /mnt/backup/
total 4
\-rw\-r\-\-r\-\- 1 root root 2410 Feb  3 17:10 passwd
root@linuxtechi:~#

#### 示例：2同时复制多个文件

假设我们要同时将多个副本（/ etc / passwd，/ etc / group和/ etc / shadow）复制到目标目录（/ mnt / backup）

root@linuxtechi:~# cp /etc/passwd /etc/group /etc/shadow /mnt/backup/
root@linuxtechi:~#

#### 示例：3）交互复制文件（\-i）

如果您希望以交互方式将文件从一个位置复制到另一位置，然后在cp命令中使用“ \-i”选项，则仅当目标目录已经具有相同文件时，交互选项才有效，示例如下所示，

root@linuxtechi:~# cp \-i /etc/passwd /mnt/backup/
cp: overwrite '/mnt/backup/passwd'? y
root@linuxtechi:~#

在上面的命令中，必须手动键入“ y”以允许复制操作

#### 示例：4）复制命令（\-v）期间的详细输出

如果要cp命令的详细输出，请使用“ \-v”选项，示例如下所示

root@linuxtechi:~# cp \-v /etc/fstab  /mnt/backup/
'/etc/fstab' \-> '/mnt/backup/fstab'
root@linuxtechi:~#

如果要同时使用交互模式和详细模式，请使用选项“ \-iv”

root@linuxtechi:~# cp \-iv /etc/fstab  /mnt/backup/
cp: overwrite '/mnt/backup/fstab'? y
'/etc/fstab' \-> '/mnt/backup/fstab'
root@linuxtechi:~#

#### 示例：5）复制目录或文件夹（\-r或\-R）

要将目录从一个位置复制到另一位置，请 在cp命令中 使用 **\-r** 或 **\-R** 选项。 假设我们要将linuxtechi用户的主目录复制到“ / mn / backup”，

root@linuxtechi:~# cp \-r /home/linuxtechi /mnt/backup/
root@linuxtechi:~#

在上面的命令中，\-r选项将递归复制文件和目录。

现在，在目标位置验证linuxtechi目录的内容，

root@linuxtechi:~# ls \-l /mnt/backup/linuxtechi/
total 24
drwxr\-xr\-x 2 root root 4096 Feb  3 17:41 data
\-rw\-r\-\-r\-\- 1 root root    7 Feb  3 17:41 file\_1.txt
\-rw\-r\-\-r\-\- 1 root root    7 Feb  3 17:41 file\_2.txt
\-rw\-r\-\-r\-\- 1 root root    7 Feb  3 17:41 file\_3.txt
\-rw\-r\-\-r\-\- 1 root root    7 Feb  3 17:41 file\_4.txt
\-rw\-r\-\-r\-\- 1 root root    7 Feb  3 17:41 file\_5txt
\-rw\-r\-\-r\-\- 1 root root    0 Feb  3 17:41 file\_5.txt
root@linuxtechi:~#

#### 示例：6）复制期间归档文件和目录（\-a）

在使用cp命令复制目录时，我们通常使用\-r或\-R选项，但是代替\-r选项，我们可以使用'\-a'，它将在复制期间存档文件和目录，示例如下所示，

root@linuxtechi:~# cp \-a /home/linuxtechi /mnt/backup/
root@linuxtechi:~# ls \-l /mnt/backup/linuxtechi/
total 24
drwxr\-xr\-x 2 root root 4096 Feb  3 17:41 data
\-rw\-r\-\-r\-\- 1 root root    7 Feb  3 17:39 file\_1.txt
\-rw\-r\-\-r\-\- 1 root root    7 Feb  3 17:39 file\_2.txt
\-rw\-r\-\-r\-\- 1 root root    7 Feb  3 17:39 file\_3.txt
\-rw\-r\-\-r\-\- 1 root root    7 Feb  3 17:39 file\_4.txt
\-rw\-r\-\-r\-\- 1 root root    7 Feb  3 17:40 file\_5txt
\-rw\-r\-\-r\-\- 1 root root    0 Feb  3 17:39 file\_5.txt
root@linuxtechi:~#

#### 示例：7）仅在源文件比目标文件（\-u）更新时复制

在某些情况下，仅当源文件比目标文件新时，才需要复制文件。 使用 cp命令中的 “ **\-u** ”选项 可以轻松实现 。

在Example：6中，我们已将linuxtechi主目录复制到/ mnt / backup文件夹，在linuxtechi主目录中，我们有5个txt文件，让我们编辑其中的几个，然后使用“ cp \-u”复制所有txt文件。

root@linuxtechi:~# cd /home/linuxtechi/
root@linuxtechi:/home/linuxtechi# echo "LinuxRocks" >> file\_1.txt
root@linuxtechi:/home/linuxtechi# echo "LinuxRocks" >> file\_4.txt
root@linuxtechi:/home/linuxtechi# cp \-v \-u  file\_\*.txt /mnt/backup/linuxtechi/
'file\_1.txt' \-> '/mnt/backup/linuxtechi/file\_1.txt'
'file\_4.txt' \-> '/mnt/backup/linuxtechi/file\_4.txt'
root@linuxtechi:/home/linuxtechi#

**另请参阅**：  **[14个用于在Linux中安全传输文件的SCP命令示例](https://www.linuxtechi.com/scp-command-examples-in-linux/)**

#### 示例：8）复制（\-n）时不要覆盖现有文件

在某些情况下，您不想在复制时覆盖现有的目标文件。 这可以通过在“ cp”命令中使用选项“ \-n”来完成

root@linuxtechi:~# cp \-i /etc/passwd /mnt/backup/
cp: overwrite '/mnt/backup/passwd'?

如您在上面的命令中看到的，它正在提示我们覆盖现有文件，如果您使用\-n，则它不会提示您进行覆盖，也不会覆盖现有文件。

root@linuxtechi:~# cp \-n /etc/passwd /mnt/backup/
root@linuxtechi:~#

#### 示例：9）使用cp命令（\-s）创建符号链接

假设我们要创建文件的符号链接，而不是使用cp命令进行复制，对于这种情况，请在cp命令中使用'\-s'选项，示例如下所示

root@linuxtechi:~# cp \-s /home/linuxtechi/file\_1.txt /mnt/backup/
root@linuxtechi:~# cd /mnt/backup/
root@linuxtechi:/mnt/backup# ls \-l file\_1.txt
lrwxrwxrwx 1 root root 27 Feb  5 18:37 file\_1.txt \-> /home/linuxtechi/file\_1.txt
root@linuxtechi:/mnt/backup#

#### 示例：10）使用cp命令创建硬链接（\-l）

如果要创建文件的硬链接，而不是使用cp命令进行复制，请使用'\-l'选项。 示例如下所示，

root@linuxtechi:~# cp \-l /home/linuxtechi/devops.txt /mnt/backup/
root@linuxtechi:~#

如我们所知，在硬链接中，源文件和链接文件将具有相同的inode编号，让我们使用以下命令进行验证，

root@linuxtechi:~# ls \-li /mnt/backup/devops.txt
918196 \-rw\-r\-\-r\-\- 2 root root 37 Feb  5 20:02 /mnt/backup/devops.txt
root@linuxtechi:~# ls \-li /home/linuxtechi/devops.txt
918196 \-rw\-r\-\-r\-\- 2 root root 37 Feb  5 20:02 /home/linuxtechi/devops.txt
root@linuxtechi:

#### 示例：11）将属性从源复制到目标（–attributes\-only）

如果要使用cp命令仅将属性从源复制到目标，请使用选项“ **–attributes\-only** ”

root@linuxtechi:/home/linuxtechi# cp \-\-attributes\-only /home/linuxtechi/distributions.txt /mnt/backup/
root@linuxtechi:/home/linuxtechi# ls \-l /home/linuxtechi/distributions.txt
\-rw\-r\-\-r\-\- 1 root root 41 Feb  5 19:31 /home/linuxtechi/distributions.txt
root@linuxtechi:/home/linuxtechi# ls \-l /mnt/backup/distributions.txt
\-rw\-r\-\-r\-\- 1 root root 0 Feb  5 19:34 /mnt/backup/distributions.txt
root@linuxtechi:/home/linuxtechi#

在上面的命令中，我们已将distribution.txt文件从linuxtechi主目录复制到/ mnt / backup文件夹中，如果您注意到，则仅复制属性，并跳过内容。 / mn / backup文件夹下的distribution.txt的大小为零字节。

#### 示例：12）在复制时创建现有目标文件的备份（\-backup）

cp命令的默认行为是在存在相同文件的情况下覆盖目标文件，如果要在复制操作期间对现有目标文件进行备份，则使用“ **\-backup** ”选项，示例如下所示，

root@linuxtechi:~# cp \-\-backup=simple \-v /home/linuxtechi/distributions.txt /mnt/backup/distributions.txt
'/home/linuxtechi/distributions.txt' \-> '/mnt/backup/distributions.txt' (backup: '/mnt/backup/distributions.txt~')
root@linuxtechi:~#

如果您已经注意到，备份已创建，并且在文件末尾附加了代字号。 备份选项接受以下参数

*   **无，关闭**   –永不备份
*   **编号，t** –编号备份
*   **现有，为零** –如果存在编号的备份，则编号，否则为简单
*   **简单，从不** \-始终进行简单的备份

#### 示例：13）复制时保留模式，所有权和时间戳记（\-p）

如果要在复制时保留文件属性，如模式，所有权和时间戳，请在cp命令中使用\-p选项，示例如下所示，

root@linuxtechi:~# cd /home/linuxtechi/
root@linuxtechi:/home/linuxtechi# cp \-p devops.txt /mnt/backup/
root@linuxtechi:/home/linuxtechi# ls \-l devops.txt
\-rw\-r\-\-r\-\- 1 root root 37 Feb  5 20:02 devops.txt
root@linuxtechi:/home/linuxtechi# ls \-l /mnt/backup/devops.txt
\-rw\-r\-\-r\-\- 1 root root 37 Feb  5 20:02 /mnt/backup/devops.txt
root@linuxtechi:/home/linuxtechi#

#### 示例：14）复制（\-P）时不要跟随Source中的符号链接

如果您不想在复制时跟随源代码的符号链接，请在cp命令中使用\-P选项，示例如下所示

root@linuxtechi:~# cd /home/linuxtechi/
root@linuxtechi:/home/linuxtechi# ls \-l /opt/nix\-release.txt
lrwxrwxrwx 1 root root 14 Feb  9 12:28 /opt/nix\-release.txt \-> os\-release.txt
root@linuxtechi:/home/linuxtechi#
root@linuxtechi:/home/linuxtechi# cp \-P os\-release.txt /mnt/backup/
root@linuxtechi:/home/linuxtechi# ls \-l /mnt/backup/os\-release.txt
\-rw\-r\-\-r\-\- 1 root root 35 Feb  9 12:29 /mnt/backup/os\-release.txt
root@linuxtechi:/home/linuxtechi#

**注意：** cp命令的默认行为是在复制时跟随源中的符号链接。

#### 示例：15）使用\-f选项强制复制文件和目录

在某些情况下，无法打开和删除现有目标文件。 并且，如果您有可以复制的健康文件来代替现有目标文件，则使用cp命令和\-f选项

root@linuxtechi:/home/linuxtechi# cp \-f distributions.txt  /mnt/backup/
root@linuxtechi:/home/linuxtechi#

#### 示例：16）使用cp命令中的sparse选项复制稀疏文件

稀疏文件是一个常规文件，包含长序列的零字节，不占用任何物理磁盘块。 稀疏文件的好处之一是它不会占用太多磁盘空间，并且对该文件的读取操作将非常快。

假设我们有一个稀疏的云映像，名为“ ubuntu\-cloud.img”

root@linuxtechi:/home/linuxtechi# du \-sh ubuntu\-cloud.img
12M     ubuntu\-cloud.img
root@linuxtechi:/home/linuxtechi# cp \-\-sparse=always ubuntu\-cloud.img /mnt/backup/
root@linuxtechi:/home/linuxtechi# du \-sh /mnt/backup/ubuntu\-cloud.img
0       /mnt/backup/ubuntu\-cloud.img
root@linuxtechi:/home/linuxtechi#

在cp命令中使用sparse参数时，可以使用不同的选项，

*   sparse = auto
*   总是稀疏
*   稀疏=从不

这就是本文的全部内容，希望它可以帮助您更有效地理解cp命令。 请分享您的反馈和评论

**另请参阅**： **[Linux中的17个有用的rsync（远程同步）命令示例](https://www.linuxtechi.com/rsync-command-examples-linux/)**