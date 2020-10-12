---
title: 如何在Ubuntu上创建Sudo用户[快速入门]
date: 2020-10-12 12:09:51
permalink: /pages/1d76d4/
categories:
  - linux用户管理
  - 常见问题
tags:
  - 
---
<!--
 * @Author: 中箭的吴起
 * @Date: 2020-07-17 08:55:37
 * @LastEditTime: 2020-07-17 08:55:37
 * @LastEditors: 中箭的吴起
 * @Description: 
 * @FilePath: \科技文章c:\Users\admin\OneDrive\studybook\linux\linux用户管理\常见问题\如何在Ubuntu上创建Sudo用户[快速入门].md
 * @日行一善，每日一码
--> 
该 `sudo` 命令提供了一种向普通用户授予管理员特权的机制， 该 特权通常仅对root用户可用。 本指南将向您展示在Ubuntu上创建具有sudo访问权限的新用户的最简单方法，而无需修改服务器 `sudoers` 文件。 如果要为现有用户配置sudo，只需跳至步骤3。

## 创建新的Sudo用户的步骤

1.  以 `root` 用户 身份登录到服务器 。

    ```
    ssh root@server_ip_address

    ```

2.  使用 `adduser` 命令将新用户添加到您的系统。

    请务必更换 用户名 与您要创建的用户。

    ```
    adduser username

    ```

    *   在提示符下设置并确认新用户的密码。 强烈建议您使用强密码！

        ```
        Set password prompts:Enter new UNIX password:
        Retype new UNIX password:
        passwd: password updated successfully

        ```

    *   按照提示设置新用户的信息。 可以接受默认值，将所有这些信息留空。

        ```
        User information prompts:Changing the user information for username
        Enter the new value, or press ENTER for the default
            Full Name []:
            Room Number []:
            Work Phone []:
            Home Phone []:
            Other []:
        Is the information correct? [Y/n]

        ```

3.  使用 `usermod` 命令将用户添加到 `sudo` 组中。

    ```
    usermod -aG sudo username

    ```

    默认情况下，在Ubuntu上，该 `sudo` 组的 成员 具有sudo特权。

4.  在新用户帐户上测试sudo访问

    *   使用 `su` 命令切换到新的用户帐户。

        ```
        su - username

        ```

    *   作为新用户，通过在要使用超级用户特权运行的命令前添加“ sudo”，验证您可以使用sudo。

        ```
        sudo command_to_run

        ```

    *   例如，您可以列出目录的内容，该 `/root` 目录通常只能由root用户访问。

        ```
        sudo ls -la /root

        ```

    *   第一次 `sudo` 在会话中 使用 时，系统将提示您输入用户帐户的密码。 输入密码以继续。

        ```
        Output:[sudo] password for username:

        ```

        如果您的用户在适当的组中，并且您正确输入了密码，则使用sudo发出的命令应以root特权运行。

## 相关教程

这是更详细的用户管理教程的链接：

*   [如何在Ubuntu服务器上添加和删除用户](https://www.digitalocean.com/community/tutorials/how-to-add-and-delete-users-on-an-ubuntu-14-04-vps)