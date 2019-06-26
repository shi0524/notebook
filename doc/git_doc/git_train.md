
## Git简介
### Why：版本库的需求

- 备份
- 集成
- 合并

### 其它版本库

- cvs
- svn
- git

### git的特点
- 基于diff
- 分布式版本库
    - 所有操作不依赖中心库
    - 每个人的本地都有一个完整的版本库

## 如何使用git
### 获取帮助
- man git

    示例:输入命令`man git-commit`，出来的内容是详细的git帮助，常见类型如下：
    ```bash
    NAME            # 名字
    SYNOPSIS        # 参数
    DESCRIPTION     # 描述
    OPTIONS         # 选项
    DATE FORMATS
    EXAMPLES        # 示例，可做参考
    DISCUSSION
    SEE ALSO        # 相关命令
    ```

- git help
- [pro git](http://git-scm.com/book/zh/v1)，权威git书
- [git 简易指南](http://www.bootcss.com/p/git-guide/)，git常用简单命令，木有高深内容

### 常用命令
#### 全局
- `git config`: 用来指定git配置，分全局配置和项目配置。建议在工作项目中使用公司的名称和邮箱作为项目配置。
- `.gitignore`: 用来指定不放入版本库的文件，用正则表达式在`.gitignore指定`

#### 版本库提交
- `git add/git add -p`: 添加文件, `-p`选项参数说明`-p, --patch           select hunks interactively`，交互式的选择添加区块，示例：
    ![git add -p](http://7o4zqy.com1.z0.glb.clouddn.com/e8a2009587347feeb357e2dcc6d2be1a.png)
- `git commit/git commit -m`:提交代码
- `git push/git push origin master`: 将改动提交到服务器。origin为远端服务器名称，master为提交的分支。

#### 版本库更新
`git pull`

#### 检查工具（自省）
- `git log/git log -p`: 提交历史，`-p`选项可以查看全面的信息，包括提交时间，做的改动等，不加参数默认显示提交的sha1，提交信息，提交者，提交日期等简单信息。下图为`git log -p`示例
    ![git log -p示例](http://7o4zqy.com1.z0.glb.clouddn.com/2927ef783e29effdc03316c9d5f514b4.png)
- `git diff`
- `git blame`：查看某个文件各行的最后提交者
    ![git blame](http://7o4zqy.com1.z0.glb.clouddn.com/50671c388521cb2e923002944d287c19.png)

#### 分支
分支之间可以理解为物理隔离，避免频繁的合并分支
主分支：master

创建分支
```
git branch      # 查看所有分支，后跟名字可以新建分支, -a选项可以显示所有分支（包括远程分支）
git branch -D   # 删除分支，即使该分支未被合并
git branch -d   # 删除已经被完全合并到其他分支的分支
```

> 分支的本质是指向某个历史提交的指针，详细原理可以参考：
> - [git pro——分支章节](http://git-scm.com/book/zh/v1/Git-%E5%88%86%E6%94%AF-%E4%BD%95%E8%B0%93%E5%88%86%E6%94%AF)
> - [git分支管理策略——阮一峰](http://www.ruanyifeng.com/blog/2012/07/git.html)

使用命令`git log --graph`或者sourcetree等图形工具可以查看分支的逻辑流
![git log graph](http://7o4zqy.com1.z0.glb.clouddn.com/fe7f133f246f917c9c9a91539e71440c.png)

![sourcetree graph](http://7o4zqy.com1.z0.glb.clouddn.com/785786f133c550a2f21f8f70ce6ddc2c.png)

切换分支
- `git checkout`:切换到某个分支，`-b`选项可以创建并切换

合并分支
- `git merge`: 合并分支，示例`git merge test`是将test分支合并到当前分支
- `git pull`: 合并分支，建议使用，示例：`git pull . test`，将test分支合并到当前分支

> 关于pull，fetch，merge，rebase的区别和联系参考链接
> - [pull和fetch](http://stackoverflow.com/questions/292357/what-are-the-differences-between-git-pull-and-git-fetch)
> - [rebase、fetch、pull](http://stackoverflow.com/questions/14894768/git-fetch-vs-pull-merge-vs-rebase)
> - [pull和merge](http://stackoverflow.com/questions/17339091/difference-between-git-pull-master-vs-git-merge-master)

> 关于牛牛说的`merge`的`squash`参数：官方说明为`--squash              create a single commit instead of doing a merge`，若不加该参数，merge规则为将该分支所有的提交均汇入当前分支，加该参数后抛弃要汇入当前分支的所有的历史提交记录，将其所有改变作为一次提交汇入主分支。

分支工具
- `git stash`:暂存未提交的更改
- `git rebase`: 效果参考下图
    ![rebase和merge](http://7o4zqy.com1.z0.glb.clouddn.com/93461d7ab4b6e9986cd7a3e317c29f34.png)

#### 回滚
- `git checkout`: `git checkout file`可以将某个文件回复到HEAD中的文件状态
- `git reset`: 官方文档解释

    ```
    --mixed               reset HEAD and index
    --soft                reset only HEAD
    --hard                reset HEAD, index and working tree
    ```

#### 发布
- `git tag`: 将某个commit取一个别名
- `git push --tag`: 将tag推到远端
- `git achieve`: 打包工具，导出某个版本的git库位tar，默认输出到标准输出

