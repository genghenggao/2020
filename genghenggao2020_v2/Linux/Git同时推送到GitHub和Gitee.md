# Git将一个项目同时推送到GitHub和Gitee

1.先完成在github上管理

2.更改.git下的config文件的\**remote\**为下面的内容，有多少个远程仓库地址就加多少个url

```
[core]
	repositoryformatversion = 0
	filemode = false
	bare = false
	logallrefupdates = true
	symlinks = false
	ignorecase = true
[remote "origin"]
	url = https://github.com/xxxxx.git
	url = https://gitee.com/xxxxx.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
```



3.保存执行命令就可以完成一次提交到多个远程仓库上了。

```
git push
```



[参考](https://blog.csdn.net/zhuzbYR/article/details/99708449?utm_medium=distribute.pc_relevant.none-task-blog-title-7&spm=1001.2101.3001.4242)

