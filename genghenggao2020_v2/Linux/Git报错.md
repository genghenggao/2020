# Git报错

[TOC]



## 1、modified: (modified content, untracked content)

### 1、报错提示

![](IMG/微信截图_20200902083347.png)

- xxx目录没有被跟踪，那自然push上去的时候是空的了。

- 分析：项目目录创建了一个`.git`目录，但创建的vue项目mongeostore_ui会自动再创建一个`.git`目录。

  ![](IMG/微信截图_20200902083512.png)

### 2、解决方法

目录下有一个.git 目录，删除.git目录

重新git add .就可。

## 2、[rejected] master -> master (fetch first)问题

![](IMG/微信截图_20200902082857.png)

### 方案1：

- 我们只需加上 -f 参数即可push成功。它会忽略版本不一致等问题，强制将本地库上传的远程库，但是一定要谨慎使用，因为-f会用本地库覆盖掉远程库，如果远程库上有重要更新，或者有其他同伴做的修改，也都会被覆盖，所以一定要在确定无严重后果的前提下使用此操作。

```
git push -f  
```

### 方案2

- 我们只需加上 --rebase 参数，将github修改的文件更新到本地。然后再重新 push 一次即可。

```
git pull --rebase origin master 

git push -u origin master
```



## 3、Github或Gitee中有空文件夹

修改文件夹名称，上传是否成功？成功在修改回来即可!