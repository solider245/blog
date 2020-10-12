---
title: git最佳实践建议
date: 2020-10-12 12:09:51
permalink: /pages/d2f66a/
categories:
  - git
  - git文章转载
tags:
  - 
---
# Git最佳实践建议

#### `COMMIT相关的修改`

一个commit应该对应一次相关的修改内容。比如说，修复两个不一样的bug应该使用两次不同的commit。越小（修改内容）的commit能使开发人员更容易理解代码的修改或者在回退版本的时候更容易回退。

#### `经常commit`

经常使用commit能够使你的commit（里的修改内容）越小，并且能使你**commit相关的修改**，多次commit允许你推送自己代码到远程分支上的频率增加，能有效的减少merge代码时出现的代码冲突问题，因为多次 commit能使你的同事的代码库得到及时的更新。

#### `不要commit一半的工作`

 当开发任务没有完整的完成的时候，不要commit。这不是说每次commit都需要开发完成一个非常完整的大功能，而是当把功能切分成许多小的但仍然具备完整性的功能点的时候，开发人员需要完整完成这个功能点之后才能commit。必要时可以使用stash命令对修改进行记录。

#### `commit之前的测试`

保证你所开发的功能是完整无误的。在commit代码之前的对代码充分测试是非常重要的，可以避免有问题的代码被其他开发人员使用。

#### `使用commit message`

commit message的开头应该简要说明该次修改。然后换行详细描述一下两个问题的细节：

*   该次修改的目的？
*   这次修改和之前的实现有何不同之处？

#### `版本控制不是备份系统`

版本控制系统虽然具备了备份的功能，但开发人员不能把VCS当成一个备份系统。开发应该多关系每次commit；使用版本控制，目的是为了使每次修改有迹可循，而不是当成备份系统直接更新文件的内容。

#### `使用分支`

分支是git中一个很强大的功能。使用分支能够很好的帮助开发避免混淆不同的开发直线。开发应该在开发流程中广泛使用分支，对应不同的开发任务（比如新功能，bug修改，想法……）

#### `协同工作基于某个工作流程`

git的特性给开发人员提供了许多不同的开发流程：主分支、主题分支、merge/rebase、git\-flow……。使用什么样的工作流程取决于你的项目、你的开发任务、部署流程和（更重要的）你的或者你同事的个人喜好。但只要你开始进行开发的时候，团队要统一使用一个公用的工作流程，确保每个开发能够遵守。

\# Git最佳实践建议(for English)

#### `COMMIT RELATED CHANGES`

A commit should be a wrapper for related changes. For example, fixing two different bugs should produce two separate commits. Small commits make it easier for other developers to understand the changes and roll them back if something went wrong. With tools like the staging area and the ability to stage only parts of a file, Git makes it easy to create very granular commits.

#### `COMMIT OFTEN`

Committing often keeps your commits small and, again, helps you commit only related changes. Moreover, it allows you to share your code more frequently with others. That way it‘s easier for everyone to integrate changes regularly and avoid having merge conflicts. Having few large commits and sharing them rarely, in contrast, makes it hard to solve conflicts.

#### `DON‘T COMMIT HALF-DONE WORK`

You should only commit code when it‘s completed. This doesn‘t mean you have to complete a whole, large feature before committing. Quite the contrary: split the feature‘s implementation into logical chunks and remember to commit early and often. But don‘t commit just to have something in the repository before leaving the office at the end of the day. If you‘re tempted to commit just because you need a clean working copy (to check out a branch, pull in changes, etc.) consider using Git‘s «Stash» feature instead.

#### `TEST CODE BEFORE YOU COMMIT`

Resist the temptation to commit something that you «think» is completed. Test it thoroughly to make sure it really is completed and has no side effects (as far as one can tell). While committing half\-baked things in your local repository only requires you to forgive yourself, having your code tested is even more important when it comes to pushing/sharing your code with others.

#### `WRITE GOOD COMMIT MESSAGES`

Begin your message with a short summary of your changes (up to 50 characters as a guideline). Separate it from the following body by including a blank line. The body of your message should provide detailed answers to the following questions:

*   What was the motivation for the change?
*   How does it differ from the previous implementation? Use the imperative, present tense («change», not «changed» or «changes») to be consistent with generated messages from commands like git merge.

#### `VERSION CONTROL IS NOT A BACKUP SYSTEM`

Having your files backed up on a remote server is a nice side effect of having a version control system. But you should not use your VCS like it was a backup system. When doing version control, you should pay attention to committing semantically (see «related changes») \- you shouldn‘t just cram in files.

#### `USE BRANCHES`

Branching is one of Git‘s most powerful features \- and this is not by accident: quick and easy branching was a central requirement from day one. Branches are the perfect tool to help you avoid mixing up different lines of development. You should use branches extensively in your development workflows: for new features, bug fixes, ideas…

#### `AGREE ON A WORKFLOW`

Git lets you pick from a lot of different workflows: long\-running branches, topic branches, merge or rebase, git\-flow… Which one you choose depends on a couple of factors: your project, your overall development and deployment workflows and (maybe most importantly) on your and your teammates‘ personal preferences. However you choose to work, just make sure to agree on a common workflow that everyone follows.