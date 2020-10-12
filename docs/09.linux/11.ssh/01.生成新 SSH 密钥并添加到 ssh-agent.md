---
title: 生成新 SSH 密钥并添加到 ssh-agent
date: 2020-10-12 12:09:51
permalink: /pages/7f60b6/
categories:
  - linux
  - ssh
tags:
  - 
---
# 生成新 SSH 密钥并添加到 ssh\-agent

检查现有 SSH 密钥后，您可以生成新 SSH 密钥以用于身份验证，然后将其添加到 ssh\-agent。

[Mac](#) [Windows](#) [Linux](#) [All](#)

### [本文内容](#in-this-article)

*   [生成新 SSH 密钥](#generating-a-new-ssh-key)
*   [将 SSH 密钥添加到 ssh\-agent](#adding-your-ssh-key-to-the-ssh-agent)
*   [延伸阅读](#further-reading)

#### Were you able to find what you were looking for?

*    Yes, easily
*    Yes, eventually
*    No

 Send

*Thank you! Your feedback has been submitted.*

如果您还没有 SSH 密钥，则必须[生成新 SSH 密钥](#generating-a-new-ssh-key)。 如果您不确定是否已有 SSH 密钥，请检查[现有密钥](https://help.github.com/cn/articles/checking-for-existing-ssh-keys)。

如果不想在每次使用 SSH 密钥时重新输入密码，您可以[将密钥添加到 SSH 代理](#adding-your-ssh-key-to-the-ssh-agent)，让它管理您的 SSH 密钥并记住您的密码。

### [生成新 SSH 密钥](#generating-a-new-ssh-key)

1.  打开 Terminal（终端）Terminal（终端）Git Bash。

2.  粘贴下面的文本（替换为您的 GitHub 电子邮件地址）。

    ```shell
    $ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ```

    这将创建以所提供的电子邮件地址为标签的新 SSH 密钥。

    ```shell
    > Generating public/private rsa key pair.
    ```

3.  提示您“Enter a file in which to save the key（输入要保存密钥的文件）”时，按 Enter 键。 这将接受默认文件位置。

    ```shell
    > Enter a file in which to save the key (/Users/you/.ssh/id_rsa): [Press enter]
    ```

    ```shell
    > Enter a file in which to save the key (/c/Users/you/.ssh/id_rsa):[Press enter]
    ```

    ```shell
    > Enter a file in which to save the key (/home/you/.ssh/id_rsa): [Press enter]
    ```

4.  在提示时输入安全密码。 更多信息请参阅[“使用 SSH 密钥密码”](https://help.github.com/cn/articles/working-with-ssh-key-passphrases)。

    ```shell
    > Enter passphrase (empty for no passphrase): [Type a passphrase]
    > Enter same passphrase again: [Type passphrase again]
    ```

### [将 SSH 密钥添加到 ssh\-agent](#adding-your-ssh-key-to-the-ssh-agent)

将新 SSH 密钥添加到 ssh\-agent 以管理密钥之前，应[检查现有 SSH 密钥](https://help.github.com/cn/articles/checking-for-existing-ssh-keys)并[生成新 SSH 密钥](https://help.github.com/cn/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key)。 将 SSH 密钥添加到该代理时，应使用默认的 macOS `ssh-add` 命令，而不是使用通过 [macports](https://www.macports.org/), [homebrew](http://brew.sh/) 或某些其他外部来源安装的应用程序。

1.  在后台启动 ssh 代理。

    ```shell
    $ eval "$(ssh-agent -s)"
    > Agent pid 59566
    ```

2.  如果您使用的是 macOS Sierra 10.12.2 或更高版本，则需要修改 `~/.ssh/config` 文件以自动将密钥加载到 ssh\-agent 中并在密钥链中存储密码。

    *   首先，检查您的 `~/.ssh/config` 文件是否在默认位置。

        ```shell
        $ open ~/.ssh/config
        > The file /Users/you/.ssh/config does not exist.
        ```

    *   如果文件不存在，请创建该文件。

        ```shell
        $ touch ~/.ssh/config
        ```

    *   打开 `~/.ssh/config` 文件，然后修改该文件，如果未使用 `id_rsa` 键的默认位置和名称，则替换 `~/.ssh/id_rsa`。

        ```properties
        Host *
          AddKeysToAgent yes
          UseKeychain yes
          IdentityFile ~/.ssh/id_rsa

        ```

3.  将 SSH 私钥添加到 ssh\-agent 并将密码存储在密钥链中。 如果您创建了不同名称的密钥，或者您要添加不同名称的现有密钥，请将命令中的 *id\_rsa* 替换为您的私钥文件的名称。

    ```shell
    $ ssh-add -K ~/.ssh/id_rsa
    ```

    **注：**`-K` 选项位于 Apple 的 `ssh-add` 标准版本中，当您将 ssh 密钥添加到 ssh\-agent 时，它会将密码存储在您的密钥链中。

    如果您没有安装 Apple 的标准版本，可能会收到错误消息。 有关解决此错误的详细信息，请参阅“[错误：ssh\-add：非法选项 \-\- K](https://help.github.com/cn/articles/error-ssh-add-illegal-option-k)”。

4.  [将 SSH 密钥添加到 GitHub 帐户](https://help.github.com/cn/articles/adding-a-new-ssh-key-to-your-github-account)。

如果已安装 [GitHub Desktop](https://desktop.github.com/)，可使用它克隆仓库，而无需处理 SSH 密钥。 它还附带 Git Bash 工具，这是在 Windows 上运行 `git` 命令的首选方法。

1.  确保 ssh\-agent 正在运行：

    *   如果您使用随 GitHub Desktop 一起安装的 Git Shell，则 ssh\-agent 应该正在运行。
    *   如果您使用的是其他终端提示符，例如 Git for Windows，您可以根据“[使用 SSH 密钥密码](https://help.github.com/cn/articles/working-with-ssh-key-passphrases)”中的“自动启动 ssh\-agent”说明进行操作，或者手动启动它：

        ```shell
        # 在后台启动 ssh-agent
        $ eval $(ssh-agent -s)
        > Agent pid 59566
        ```

2.  将 SSH 私钥添加到 ssh\-agent。 如果您创建了不同名称的密钥，或者您要添加不同名称的现有密钥，请将命令中的 *id\_rsa* 替换为您的私钥文件的名称。

    ```shell
    $ ssh-add ~/.ssh/id_rsa
    ```

3.  [将 SSH 密钥添加到 GitHub 帐户](https://help.github.com/cn/articles/adding-a-new-ssh-key-to-your-github-account)。

1.  在后台启动 ssh 代理。

    ```shell
    $ eval "$(ssh-agent -s)"
    > Agent pid 59566
    ```

2.  将 SSH 私钥添加到 ssh\-agent。 如果您创建了不同名称的密钥，或者您要添加不同名称的现有密钥，请将命令中的 *id\_rsa* 替换为您的私钥文件的名称。

    ```shell
    $ ssh-add ~/.ssh/id_rsa
    ```

3.  [将 SSH 密钥添加到 GitHub 帐户](https://help.github.com/cn/articles/adding-a-new-ssh-key-to-your-github-account)。