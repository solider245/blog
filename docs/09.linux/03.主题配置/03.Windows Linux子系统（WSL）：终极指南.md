---
title: Windows Linux子系统（WSL）：终极指南
date: 2020-10-12 12:09:51
permalink: /pages/ac8767/
categories:
  - linux
  - 主题配置
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-14 08:04:57
 * @LastEditTime: 2020-07-14 08:04:58
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\主题配置\Windows Linux子系统（WSL）：终极指南.md
 * @日行一善，每日一码
--> 
*对于Linux开发者来说，Windows子系统（WSL）是一个很好的解决方案，可让开发人员直接在Windows 10版本的桌面上直接在Linux中工作。让我们在此最终指南中深入了解如何在Windows 10上开始使用WSL！*

如果您花费太多时间对硬盘驱动器进行分区，而无法在Windows上安装多个Linux发行版，那么您对本文很幸运。 微软的童话母亲决定给您另一个选择： [Linux的Windows子系统（WSL）](https://docs.microsoft.com/en-us/windows/wsl/faq) 。 WSL使与Windows一起运行Linux发行版变得更加容易和灵活。

在本教程中，您将学习如何开始使用WSL。 您将学习如何开始学习如何使用一些漂亮的工具，从而使WSL比单独使用bash或PowerShell更具通用性。

## 目录

*   [WSL：Linux作为Windows应用程序](#wsl-linux-as-a-windows-app)
*   [WSL和WSL2](#wsl-vs-wsl2)
*   [安装WSL](#installing-wsl)
*   [通过培训视频设置WSL](#setting-up-wsl-via-training-video)
*   [检查Windows 10构建](#checking-your-windows-10-build)
*   [为Windows Windows功能启用Windows子系统](#enable-the-windows-subsystem-for-linux-windows-feature)
*   [下载Linux发行版](#download-the-linux-distro-of-choice)
*   [为Linux 2更新到Windows子系统](#updating-to-windows-subsystem-for-linux-2)
*   [启动WSL](#starting-up-wsl)
*   [通过WSL共享Windows / Linux资源](#sharing-windows-linux-resources-via-wsl)
*   [共享文件系统](#sharing-file-systems)
*   [共享环境变量](#sharing-environment-variables)
*   [共享网络资源：WSL差异说明](#sharing-network-resources-wsl-differences-explained)
*   [一起使用PowerShell和Bash](#using-powershell-and-bash-together)
*   [使用Xfce4为Linux GUI安装Windows子系统](#install-a-windows-subsystem-for-linux-gui-with-xfce4)
*   [Xfce](#xfce)
*   [xRDP](#xrdp)
*   [配置](#setting-up)
*   [技巧和窍门](#tips-and-tricks)
*   [在启动时使用wsl.conf设置WSL配置项](#setting-wsl-configuration-items-at-bootup-with-wsl-conf)
*   [使用Visual Studio Code（VS Code）在WSL上进行开发](#developing-on-wsl-with-visual-studio-code-vs-code-)
*   [将适用于Linux的Windows子系统添加到Windows终端](#adding-windows-subsystem-for-linux-to-the-windows-terminal)
*   [总结思想](#closing-thoughts)
*   [进一步阅读](#further-reading)

## **WSL：Linux作为Windows应用程序**

WSL或 *C：\\ Windows \\ System32 \\ wsl.exe* 是Windows工具，允许您从Windows存储中将Linux发行版安装为应用程序。

由于WSL是简单的Windows可执行文件，因此可以从cmd命令提示符或PowerShell终端调用它。 稍后我们将更深入地讨论该主题。 现在，重要的是要多了解一些WSL在幕后所做的事情。

![](https://adamtheautomator.com/content/images/2019/09/wsl-1.png?ezimgfmt=rs:850x381/rscb14/ng:webp/ngcb14)

*wsl.exe*

## **WSL和WSL2**

有两种用于Linux的Windows子系统版本，即WSL和WSL2。 如果您拥有Windows 10内部版本18917或更高版本，则应运行WSL2。 即使您不这样做，本文中的其他所有内容也适用于这两个版本。

它们之间的主要区别在于系统调用（ *syscall* ）； 操作系统调用服务的程序方式。

Syscall可能很快变得复杂。 我不会在这里进行syscall，但是如果您想了解更多信息，请 [在此处](https://blogs.msdn.microsoft.com/wsl/2016/06/08/wsl-system-calls/) 查阅MSDN文章 。

在较高的级别上，当您通过WSL运行命令时，syscall使用驱动程序来解释Windows内核上的驱动程序。 然后，WSL2使用 [虚拟化的Linux内核](https://github.com/microsoft/WSL2-Linux-Kernel) ，该 [内核](https://github.com/microsoft/WSL2-Linux-Kernel) 在后台运行，并通过Windows更新进行更新。

WSL2的工作方式更像传统的虚拟机（VM），其中Windows将作为主机，而WSL发行版是VM来宾。

以下是这些更改如何影响WSL中的调用资源的高级摘要：

| 系统 | WSL1 | WSL2 |
| --- | --- | --- |
| 核心 | 没有Linux内核，调用是通过为WSL编写的驱动程序进行翻译的 | 有一个随WSL一起安装的Linux内核 |
| 文件系统 | 整个目录结构是Windows文件系统的一部分 | WSL文件保存在虚拟硬盘中 |
| 设备 | 设备与您的Windows操作系统使用的设备相同，调用通过pico驱动程序运行以解释它们 | 设备通过Hyper\-V虚拟化 |
| 网络 | 数据包通过Windows使用的相同接口发送 | 虚拟化接口，并通过Windows上的NAT网关路由数据包 |

> 在撰写本文时，WSL2仍未普遍可用。 要复制本文中的所有内容，您将需要Windows Insiders预览版本并深入研究 [Microsoft的Github问题列表，](https://github.com/microsoft/vscode-cpptools/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+wsl) 以使WSL2正常工作。 根据您的紧急程度，您最好等到WSL2进入GA。 您已被警告！

## **安装WSL**

为Linux设置Windows子系统包括与Windows 10一起安装Linux发行版。但是，这种方式允许两个不同的操作系统相互交互。

要在Windows上安装Linux的Windows子系统，唯一的要求是您拥有64位Windows 10设备。 不同版本的WSL需要使用不同版本的Windows，但是它们可以相互运行。 WSL和WSL2在本文中可以互换使用。

如果要继续进行，请确保您具有：

*   Windows 10内部版本16215或更高版本（WSL1）
*   Windows内部版本18917或更高版本（WSL2）

> 注意：由于WSL在编写本文时仍在积极开发中，因此其中某些功能可能需要高于16215的版本。随着您的发展，请注意您需要使用哪个版本的功能。 您可能必须自己检查版本，以了解是否需要任何Windows更新。

### 通过培训视频设置WSL

如果您更喜欢视觉学习，请随时观看此TechSnips视频，了解如何启动和运行WSL。

如果您不喜欢通过视频学习如何设置WSL，请继续阅读。

### 检查Windows 10构建

如前所述，使用WSL需要特定版本的Windows 10。 为了确保您可以使用任何给定的WSL版本，请首先检查您正在运行的Windows版本。 有几种不同的方法可以执行此操作，但是最简单的两种方法来自cmd或PowerShell。

#### 使用Cmd查找Window 10构建

在命令提示符下，运行 `systeminfo` 。 在此处，您将在结果顶部附近看到Windows 10操作系统版本，如下所示。

![](https://adamtheautomator.com/content/images/2019/09/systeminfo.png?ezimgfmt=rs:850x242/rscb14/ng:webp/ngcb14)

`systeminfo`

#### 使用PowerShell查找Windows 10构建

在PowerShell中，您可以检查Windows注册表以找到Windows 10版本。 以下是可用于此目的的代码段。

```powershell
Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion" | Select CurrentBuild
```

复制

确认您正在运行兼容的Windows 10版本后，现在就可以从Microsoft商店下载WSL Linux发行版。 您可以安装设备支持的Linux发行版，并在Windows安装中使用它们。

### 为Windows Windows功能启用Windows子系统

在管理性PowerShell控制台会话中，运行 `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux` 并重新启动。 这将安装用于Windows的Microsoft Windows子系统Windows功能。

### 下载Linux发行版

Windows 10恢复运行后，请转到Microsoft商店并通过 [搜索'WSL'](https://www.microsoft.com/en-us/search/shop/apps?q=wsl) 下载Linux发行版 。 适用于Linux的Windows子系统本身不会安装发行版，它仅允许您在设置发行版之后进行安装。

本文的其余部分将引用Ubuntu 18.04发行版。但是，在撰写本文时，还有其他可用版本，例如：

*   Ubuntu 16.04 LTS
*   Ubuntu 18.04 LTS
*   OpenSUSE飞跃15
*   OpenSUSE飞跃42
*   SUSE Linux Enterprise Server 12
*   SUSE Linux Enterprise Server 15
*   卡利Linux
*   Debian GNU / Linux
*   WSL的Fedora Remix
*   彭文
*   高山WSL

## 为Linux 2更新到Windows子系统

在2019 MS Build会议上，微软 [宣布了新版本的WSL](https://devblogs.microsoft.com/commandline/announcing-wsl-2/) （WSL2）。 对于最终用户，WSL2与WSL1基本相同，只是有一个很大的区别：WSL2运行完整的Linux内核，而不是模拟对一个内核的系统调用。

WSL2还更快并且与Linux本地应用程序（或设计为仅在Linux上运行的应用程序）更兼容。

如果您正在运行Windows内部版本18917或更高版本，并且已经安装了WSL，则可以通过 `Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform` 以管理员权限 运行来更新到WSL2 ，然后重新启动。

#### 配置Linux发行版以与WSL2一起使用

一旦设备启动备份，您就可以在现有已安装发行版上开始使用WSL2。 在下面，您将看到几个步骤，可以为WSL2配置现有的Linux发行版。 打开一个PowerShell控制台，然后：

1.  列出您通过运行 `wsl -l` 或 安装的Linux版本 `wsl --list` 。
2.  获得列表后，用WSL2复制要运行的发行版的名称，然后运行 `wsl --set-version <Distro> 2` ，将<Distro>替换为先前复制的名称。
3.  通过运行 `wsl -l -v` 或 确认命令是否成功 `wsl --list --verbose` 。 该命令将返回WSL发行版的完整列表以及每个发行版使用的版本。

![](https://adamtheautomator.com/content/images/2019/09/revert-linux-distro-wsl.png?ezimgfmt=rs:850x181/rscb14/ng:webp/ngcb14)

设置WSL Linux发行版

> *请注意，您还可以通过运行以下命令为以后安装的所有发行版设置默认的WSL版本到WSL2 `wsl --set-default-version 2`*

#### 将Linux发行版从WSL2还原到WSL1

如果要将发行版从WSL2还原回WSL1，请运行 `wsl --set-version <Distro> 1` ，用 该发行版的名称 替换 *<Distro>* 。

## **启动WSL**

要开始使用WSL，请打开PowerShell终端并输入 `wsl` 。 如果正确设置了WSL，则将输入在所选WSL发行版上运行的bash终端。 从这里，您可以运行所需的任何Linux命令。

在下面，您将找到 *wsl.exe* 启动时提供的 所有选项的*参考* 。

运行Linux二进制文件的参数

| 命令 | 说明 | 例 |
| --- | --- | --- |
| exec \-e | 将在不使用默认外壳的情况下运行命令 | wsl \-e curl google.com |
| \- | 在此参数之后将任何内容传递给默认外壳。 将操作员排除在外也将起作用。 | wsl\-curl google.com，wsl curl google.com |
| 分布，\-d | 在指定发行版的Shell中打开终端 | wsl \-d Ubuntu\-18.04 |
| 用户\-u | 只要该发行版上存在用户，就以指定用户身份运行WSL命令 | wsl \-d Ubuntu\-18.04 \-u tux\_user |
| 出口 | 将指定的发行版导出到本地系统上的tar文件中。 | wsl \-\-export Ubuntu ./Test\-Ubuntu.tar |
| 进口 \[ \- 版\] | 导入tar文件作为新的WSL发行版。 可以使用\-\-version选项指定WSL版本 | wsl\-导入Test\-Ubuntu C：\\ data \\ Test\-Ubuntu。\\ Test\-Ubuntu.tar |
| 列表，\-l \[选项\] | wsl\-列表 |  |
| 所有 | 列出所有已安装的WSL发行版 | wsl \-l \-\-all |
| 跑步 | 仅列出当前正在运行的WSL发行版 | wsl \-l\-运行 |
| 安静\-q | 仅显示WSL发行名称 | wsl \-l \-q |
| 详细\-v | 显示有关所有WSL发行版的详细信息 | wsl \-l \-v |
| 设置默认值\-s | 将指定的WSL分发设置为WSL命令的默认分发。 | wsl \-s Test\-Ubuntu |
| 设置默认版本 | 更改安装到该系统的所有新发行版的默认WSL版本 | wsl \-\-set\-default\-version 2 |
| 集版本 | 更改指定发行版的WSL版本 | wsl \-\-set\-version Test\-Ubuntu 2 |
| 关掉 | 立即终止所有正在运行的WSL发行版 | wsl\-关闭 |
| 终止\-t | 终止指定的WSL分发 | wsl \-t Test\-Ubuntu |
| 取消注册 | 注销指定的WSL发行版 | wsl \-\-unregister Test\-Ubuntu |
| 救命 | 显示有关使用WSL的信息 | wsl\-帮助 |

一旦您习惯了使用这些开关，就会发现通过WSL运行和管理应用程序要比自己管理Linux虚拟机容易得多。

> 快速提示：通过运行查找到WSL的所有标志和参数 `wsl --help` 。

完成后，键入 `exit` 以返回到PowerShell终端。

## **通过WSL共享Windows / Linux资源**

WSL最好的部分之一是，它允许您彼此无缝共享Windows和Linux资源。 目前，您可以共享文件系统，环境变量，网络资源和命令行解释器（如cmd和PowerShell）。

您将在本节中看到的所有示例均通过WSL Ubuntu Linux发行版进行。 如果您选择下载其他发行版，则里程可能会有所不同。

### 共享文件系统

文件系统是与WSL共享的最有用的东西之一。 WSL使您可以像对待两个文件系统一样使用它们。

Windows 10文件系统在Linux中作为目录安装，而Linux文件系统在Windows中作为文件夹安装。

#### 使用环境变量从Windows查找Linux文件系统

使用WSL安装Linux发行版时，有时会添加Windows环境变量。 对于WSL Ubuntu Linux发行版，它将创建一个名为 *UBUNTU\_HOME* 的环境变量*。* 此环境变量 从Windows和WSL Ubuntu都 指向Linux */ home / ubuntu* 目录。

*UBUNTU\_HOME中* 定义的路径 可用于运行脚本，该脚本使用跨它们的资源，或为Windows终端设置默认位置（稍后介绍）。

![](https://adamtheautomator.com/content/images/2019/09/default-linux-location.png?ezimgfmt=rs:850x88/rscb14/ng:webp/ngcb14)

检查WSL UBUNTU\_HOME环境变量

其他发行版可以定义类似的环境变量。 `Get-ChildItem -Path $Env:\` 安装新的Linux发行版后 ，使用PowerShell命令检查Windows环境变量， 以查看是否已添加。

如果要将所有内容都放在 */ home / ubuntu* 目录 中，则此环境变量快捷方式非常方便 。 但是，让我们更深入地了解它如何到达那里以及如何达到它。

#### 通过Microsoft Store Packages文件夹从Windows查找Linux文件系统

并非每个WSL发行版都能保证提供一种简单的引用方式。 重要的是，您必须学习如何找到另一种Linux文件系统。

由于大多数WSL Linux发行版都将从Microsoft商店安装，因此您可以在其他Windows商店应用程序的同一位置查找Linux文件系统。 导航到 *％USERPROFILE％\\ AppData \\ Local \\ Packages \\，* 以找到Windows应用商店应用所在的目录。 然后 [假定对文件夹的控制，](https://www.windowscentral.com/how-take-ownership-files-and-folders-windows-10) 因为通常默认情况下 [该文件夹](https://www.windowscentral.com/how-take-ownership-files-and-folders-windows-10) 是受保护的。

您将在packages文件夹中看到许多子文件夹，这些文件夹可能会显示您的Linux发行文件系统。 例如，WSL Ubuntu发行版 对我而言 就位于 *CanonicalGroupLimited.Ubuntu18.04onWindows\_79rhkp1fndgsc* 文件夹 下 。

如果导航到package文件夹，则会找到Linux文件系统。 对于WSL Ubuntu，它位于 *LocalState \\ rootfs* 文件夹中 *。* 这是您的Linux发行版的根目录。

![](https://adamtheautomator.com/content/images/2019/09/windows-apps.png?ezimgfmt=rs:850x579/rscb14/ng:webp/ngcb14)

％USERPROFILE％/ AppData / Local / Packages /下的Linux文件系统

#### 从Linux查找Windows文件系统

要从Linux查找Windows 10文件系统，请在Windows中打开WSL。 然后，WSL将启动一个bash终端。 默认情况下， 此bash终端将在 *UBUNTU\_HOME* 目录中 启动 。

您还可以找到Windows存储卷的根目录。 WSL Linux文件系统将每个Windows字母驱动器（C，D，E等）视为已安装的驱动器。 只要您具有 [root特权](https://www.linux.com/tutorials/how-use-sudo-and-su-commands-linux-introduction/) ，就 可以找到安装为 */ mnt / c* ， */ mnt / d* 等的 每个卷 。[](https://www.linux.com/tutorials/how-use-sudo-and-su-commands-linux-introduction/)

![](https://adamtheautomator.com/content/images/2019/09/window-file-system-from-linux.png?ezimgfmt=rs:850x217/rscb14/ng:webp/ngcb14)

Bash相当于 `Get-ChildItem C:\Windows\System32 | Select-Object -First 5` 在WSL 上 运行

#### WSL2文件系统

浏览WSL文件系统非常简单。 任何不熟悉Linux文件系统结构的人都将能够使用Windows资源管理器对其进行导航。 但是，如果您想切换到WSL2，它将变得更加复杂。

WSL2更改了共享文件系统背后一切的工作方式。 首先，文件系统现在是 *vhdx* 格式 的虚拟硬盘， 而不是目录。

您可以在 *WUSER* Ubuntu发行版的 *Windows\_79rhkp1fndgsc \\ LocalState的％USERPROFILE％\\ AppData \\ Local \\ Packages \\ CanonicalGroupLimited.Ubuntu18.04* 下 找到*vhdx* 文件 。 但是不幸的是， *rootfs* 文件夹与WSL1不同。

##### Windows资源管理器文件导航无法进行（暂时）

在撰写本文时，无法通过WSL Linux文件系统 在终端 的 `cp` or `Copy-Item` 命令 之外浏览Windows文件系统 。

您会发现可以使用 *磁盘管理器* 工具 在Windows中挂载VHDX文件 。 但是，注册WSL发行版时无法挂载虚拟磁盘。

### 共享环境变量

环境变量是任何操作系统的关键部分，因此可以轻松在应用程序中的任何位置引用二进制文件和可执行文件。

在Windows 10内部版本17063之前，Windows 10和WSL Linux之间共享的唯一环境变量是 *PATH* 变量。 从那时起，可以使用 *WSLENV* 共享 环境变量。

使用 *WSLENV* 环境变量来共享其他环境变量可能会有点*麻烦* 。 要跨平台共享环境变量，实际上您必须在另一个环境变量中设置环境变量。

#### 总览

共享环境变量是下面的三个步骤。 在Windows / Linux上共享时，唯一的主要区别是使用的switch参数（下面有完整的参考）。

1.  [在Windows](https://adamtheautomator.com/powershell-set-windows-environment-variables/) 或 [Linux中](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/) [定义环境变量](https://adamtheautomator.com/powershell-set-windows-environment-variables/) 。
2.  将 *WSLENV* 环境变量 设置为 等于先前定义的环境变量，后跟一个switch参数（用于路径转换）。
3.  在Windows或Linux中读取环境变量。

#### 共享选项

您可以使用四种不同的方式使变量可用，具体取决于您希望使用开关在哪个平台上显示环境变量（如下表所示）。

*   Windows文件系统中的路径仅可通过自身使用
*   WSL文件系统中的路径仅可从WSL获得
*   WSL Linux和Windows上都可以使用WSL文件系统中的路径
*   Windows文件系统中的路径在WSL Linux和Windows上均可用

| 旗 | 说明 |
| --- | --- |
| / p | 单路径。 与此相关的变量集将在Windows和WSL Linux之间转换并提供给两者。 |
| /升 | 路径列表。 与相似 `/p` ，不同之处 在于 它可以接受多个路径。 在Windows上，此列表将以分号分隔，而在WSL Linux上，将以冒号分隔。 |
| / u | Unix路径。 仅当从Windows调用WSL Linux时，才能访问设置有此标志的路径。 可以与 `/p` 或 `/l` 标志一起使用 |
| / w | Windows路径。 仅当从WSL Linux调用Windows时，才能访问设置有此标志的路径。 可以与 `/p` 或 `/l` 标志一起使用 |

#### 路径翻译

共享环境变量的主要原因是路径转换。 您可能已经知道，Windows具有用户配置文件文件夹，例如Linux具有用户配置文件目录。 每个用户都有一个预定的“主文件夹”，例如 Windows上的 *C：\\ Users \\ <用户名>* 和 Linux上的 */ home / <用户名>* 。

使用 `/p` 和 `/l` 开关，WSL将在平台之间转换这些文件夹路径。

#### 与Linux共享和转换Windows路径

您可以使用 `/p` 和 `/l` 开关 一次共享一个或多个路径 。

在Windows命令提示，并用一个Windows环境变量定义称为 *DESKTOP* ，分配的值 `DESKTOP/p` 到 *WSLENV* 变量。 这使您可以从WSL Linux访问它。 您可以在下面看到一个示例。

![](https://adamtheautomator.com/content/images/2019/09/windows-environment-variables.png?ezimgfmt=rs:850x458/rscb14/ng:webp/ngcb14)

在Windows中设置变量并在Linux中访问

使用 `/l` 开关 可以一次对多个路径执行完全相同的过程 。

#### 与Windows共享和翻译Linux路径

与Windows共享和转换Linux路径的过程与Windows相同，尽管使用 [特定于Linux的命令来设置环境变量](https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/) 。

要深入了解共享环境变量，请查阅 [这篇Microsoft文章](https://devblogs.microsoft.com/commandline/share-environment-vars-between-wsl-and-windows/) 。

### 共享网络资源：WSL差异说明

网络组件是Windows和WSL Linux之间共享的另一个便捷资源。 在网络上，WSL变得有些困难。 根据您使用的WSL版本，您应该了解一些信息。

#### WSL与WSL2联网

您会发现，根据所使用的WSL版本，网络将完全不同。 理解这些差异非常重要，因为它们会对您在WSL中开发应用程序的方式产生重大影响。

##### 物理与虚拟网络接口

最显着的区别是WSL如何公开Windows网络接口。 在WSL1中，WSL使用与Windows 10使用相同的物理网络接口。 使用相同的网络接口意味着WSL网络接口将与Windows 10共享相同的IP地址。

如果您可以在Windows和WSL上使用相同的IP网络，则WSL1网络很好，但是如果您需要不同的话，则必须使用WSL2。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%221600%22%20height%3D%22373%22%3E%3C%2Fsvg%3E)

Windows和WSL1 IP地址的比较

在WSL2中，网络接口已虚拟化。 虚拟化的网络接口意味着WSL2网络实例可以拥有与其Windows 10对应实例不同的IP配置。

在撰写本文时， [WSL2 Linux的IP地址使用网络地址转换](https://docs.microsoft.com/en-us/windows/wsl/wsl2-ux-changes) （NAT）来访问Windows上的网络资源，尽管Microsoft提到删除NAT在其积压的问题上很重要。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%221600%22%20height%3D%22352%22%3E%3C%2Fsvg%3E)

与之前的比较相同，但针对WSL2发行版

##### 客户端DNS解析

WSL和WSL2仍将生成 */etc/resolv.conf* 和 */ etc / hosts* 文件以允许DNS解析。 只要您没有在 */etc/wsl.conf中* 显式覆盖该行为 ，客户端DNS解析将继续按预期运行。

稍后，您将了解有关 *wsl.conf* 文件的 更多 信息。

### 一起使用PowerShell和Bash

One of the coolest features of WSL is the ability to seamlessly pass information to and from PowerShell and Bash on WSL.

#### PowerShell \-\-> Bash

Since the WSL executable accepts input from the pipeline, you can call the *wsl.exe* command inside of PowerShell and accept stdin. This allows you to use WSL to pass entire objects from PowerShell into the WSL which then get processed with the bash terminal. You can see an example below.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%221266%22%20height%3D%22671%22%3E%3C%2Fsvg%3E)

Passing PowerShell to `grep`

#### Bash \-\-> PowerShell/Cmd

You can also pass information from bash in the WSL to PowerShell and cmd just as easily. Below you can see an example of executing the Linux *ls* command and passing the output to the PowerShell `Select-Object` cmdlet via the pipeline.

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%221266%22%20height%3D%22671%22%3E%3C%2Fsvg%3E)

Passing Bash output to PowerShell

您还可以从WSL调用一些Windows cmd实用程序，并将输出传递回Linux，只要这两个命令都在系统路径中即可。

> 请记住，WSL知道两侧的系统路径，因为默认情况下它可以访问Windows PATH变量

在下面可以看到，您可以 在WSL中 运行 *ipconfig* （这是Windows命令），并将该输出传递给Linux *grep* 命令。 您还可以看到调用Linux命令相反 *它* 并通过输出到Windows *IPCONFIG* 命令。

![](data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%221266%22%20height%3D%22286%22%3E%3C%2Fsvg%3E)

在Linux中执行Windows命令

#### 翻译问题

在bash和PowerShell之间来回传递命令输出有一些警告。

一个大问题是PowerShell和bash如何返回信息。 PowerShell是一种面向对象的编程语言，而bash是一种字符串处理工具。 通过管道传递给bash的所有PowerShell对象都将扁平化为字符串。 相反，任何通过管道传递给PowerShell的bash输出都将转换为字符串对象。

您可以通过在PowerShell中转换或显式转换对象类型来某种程度上解决此问题，如以下示例所示。 但是，如果您希望在PowerShell和WSL之间传递对象而无需进行任何额外的工作，则会感到失望。

![](https://adamtheautomator.com/content/images/2019/09/bash-powershell-3.png?ezimgfmt=rs:850x457/rscb14/ng:webp/ngcb14)

问题传递对象

通过将bash日期强制转换为 `[datetime]` PowerShell中 的 类，现在我们有了一个可以在脚本中使用的有效PowerShell对象。 如果您编写的脚本需要从Windows转到WSL，然后再返回，则可以对代码进行少量按摩。

## 使用Xfce4为Linux GUI安装Windows子系统

当命令行不够用时，就该打破GUI了。 如果您需要在WSL上运行图形实用程序，浏览自定义发行版，或者您还不熟悉bash，则可以安装Linux GUI。

### Xfce

Linux有许多可用的桌面环境。 为WSL设置的最常见的设置之一称为 [Xfce](https://www.xfce.org/) 。 在撰写本文时，Xfce的版本为4。可以使用其他桌面环境，但是在本文中，您将学习如何设置Xfce4。

### xRDP

设置Linux桌面环境后，您将需要一个了解RDP协议的服务。 在本文中，我们将重点介绍 [xRDP服务器](http://xrdp.org/) 。 xRDP是Linux的开源RDP服务器，它使您可以像使用Windows主机一样使用RDP客户端连接到Linux。

### 配置

要使用Xfce4和xRDP从Windows访问Linux GUI，请按照以下说明进行操作。 在WSL终端中：

1.  **下载并安装Xfce4\-** 使用命令下载并安装Xfce4 `sudo apt-get -y install xfce4 && sudo apt-get -y install xubuntu-desktop` 。 这需要一段时间。 支持。
2.  **安装xRDP服务器\-** 通过运行下载并安装xRDP `sudo apt-get -y install xrdp` 。
3.  **为xfce4配置xRDP\-** `echo xfce4-session > ~/.xsession`
4.  **重新启动XRDP** \- `sudo service xrdp restart`
5.  **查找WSL发行版IP地址** \- `ifconfig | grep inet`

此时，您应该能够从Windows 10打开RDP会话。使用 `mstsc` 并提供在步骤＃5中找到的Linux IP地址， 打开远程桌面连接窗口 。

如果一切顺利，则可以打开与Windows操作系统上运行的Linux发行版的RDP连接，如下所示。

![](https://adamtheautomator.com/content/images/2019/09/windows-subsystem-linux-gui.png?ezimgfmt=rs:850x683/rscb14/ng:webp/ngcb14)

具有Xfce4和xRDP的Linux GUI的Windows子系统

## **技巧和窍门**

既然您已经了解了WSL的基础知识以及如何使用它，那么下一步是什么？ 幸运的是，有许多工具是为WSL构建的或可以很好地与WSL一起使用。

### **在启动时使用*wsl.conf*设置WSL配置项**

WSL中的配置文件位于 */etc/wsl.conf。* 该文件包含每次WSL发行版启动时运行的配置设置。 当 *wsl.conf* 文件存在时 *，* 每次Linux发行版启动 时*，* WSL都会在该文件中提取任何设置。

您可以配置 *wsl.conf* 文件 中的几个不同部分 。

*   **自动** 挂载\-从Windows挂载驱动器
*   **网络** \-生成 *resolv.conf* 或 *主机* 文件
*   **互操作** \-启用或禁用Windows互操作

有关 *wsl.conf* 文件的 更多详细信息 *，* 请查看 [Microsoft *Set WSL Launch Settings*](https://docs.microsoft.com/en-us/windows/wsl/wsl-config#set-wsl-launch-settings) 页面。

### **使用Visual Studio Code（VS Code）在WSL上进行开发**

VS Code似乎与所有内容集成在一起，WSL也不例外。 在VS Code中，您可以在WSL Distro上设置工作区，但可以在Windows上使用VS Code对其进行完全操作。 您甚至不需要运行终端！

要在Windows上设置VS Code以与WSL一起使用，您首先显然需要 安装 [Windows的VS Code](https://code.visualstudio.com/download) 。 另外，请确保已安装“ [*远程\-WSL* VS代码”扩展名](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) 。

安装扩展程序后，现在可以通过打开WSL终端并运行来连接到该扩展程序 `code <workspace>` 。 `<Workspace>` 是您要从中运行VS Code的目录。 然后，VS Code将检测到您在WSL发行版中，打开一个窗口，并建立与工作区的连接。

通过注意VS Code左下角的WSL连接图标来确认它是否正常工作。 您应该看到它具有您的WSL发行版的名称。

![](https://adamtheautomator.com/content/images/2019/09/visual-studio-code-wsl-2.png?ezimgfmt=rs:850x638/rscb14/ng:webp/ngcb14)

使用WSL和Visual Studio Code

您甚至可以使用内置终端直接与WSL工作区进行交互。 无需为 [git bash](https://git-scm.com/downloads) 命令 运行单独的窗口 。

### **将适用于Linux的Windows子系统添加到Windows终端**

WSL的另一个有用用例是将WSL控制台添加到 [Windows Terminal中](https://github.com/microsoft/terminal) 。

在Windows Terminal中，您可以在其自己的选项卡中添加每个WSL发行版。 您还可以自定义每个标签的外观，以免迷路。

如果使用的WSL发行版为用户目录（如 *UBUNTU\_HOME）* 设置环境变量 ，则还可以将其设置为终端的起始目录。

![](https://adamtheautomator.com/content/images/2019/09/terminal-1.gif)

如果您想获得有关设置WSL与Windows Terminal一起使用的完整视频演练，请查看下面的TechSnips入门视频。

## **总结思想**

微软发布了WSL，使Linux开发人员能够在Windows上进行开发。 到目前为止，WSL已经朝着正确的方向迈出了一步。

WSL似乎将成为Microsoft新的开源友好战略的重要组成部分。 如果微软要取代苹果成为开发人员在其上编写代码的设备，那将是一场艰苦的战斗。 但是WSL是发挥作用的强牌。

WSL为开发人员带来了许多可喜的好处，例如：

*   比运行本地Linux VM轻得多
*   消除了安装和管理虚拟机监控程序的开销
*   不再需要多分区硬盘
*   不再需要复杂的grub引导程序

WSL只是打开并运行，因此我们以后都可以快乐地进行编码。

## **进一步阅读**

*   [***适用于Linux的Windows子系统文档（Microsoft）***](https://docs.microsoft.com/en-us/windows/wsl/about)
*   ***[WSL GitHub存储库](https://github.com/microsoft/WSL)***