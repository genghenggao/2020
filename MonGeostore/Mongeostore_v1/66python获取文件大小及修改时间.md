# Python获取文件大小、修改时间

[TOC]

## 1. Python文件操作

- 在Python中，文件操作主要来自os模块，主要方法如下：

- os.listdir(dirname)：列出dirname下的目录和文件
  os.getcwd()：获得当前工作目录
  os.curdir:返回当前目录（'.')
  os.chdir(dirname):改变工作目录到dirname

  os.path.isdir(name):判断name是不是一个目录，name不是目录就返回false
  os.path.isfile(name):判断name是不是一个文件，不存在name也返回false
  os.path.exists(name):判断是否存在文件或目录name
  os.path.getsize(name):获得文件大小，如果name是目录返回0L

  os.path.abspath(name):获得绝对路径
  os.path.normpath(path):规范path字符串形式
  os.path.split(name):分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
  os.path.splitext():分离文件名与扩展名
  os.path.join(path,name):连接目录与文件名或目录
  os.path.basename(path):返回文件名
  os.path.dirname(path):返回文件路径

  os.remove(dir) #dir为要删除的文件夹或者文件路径
  os.rmdir(path) #path要删除的目录的路径。需要说明的是，使用os.rmdir删除的目录必须为空目录，否则函数出错。

  os.path.getmtime(name) ＃获取文件的修改时间 

  os.stat(path).st_mtime＃获取文件的修改时间

  os.stat(path).st_ctime #获取文件修改时间

  os.path.getctime(name)#获取文件的创建时间

## 2. 文件大小及修改时间代码

- python遍历文件夹.py

```python
import os
import datetime

# base_dir = 'c:/'
base_dir = "./mongeostore_env/pic/"
list = os.listdir(base_dir)

filelist = []
for i in range(0, len(list)):
    path = os.path.join(base_dir, list[i])
    if os.path.isfile(path):
        filelist.append(list[i])

for i in range(0, len(filelist)):
    path = os.path.join(base_dir, filelist[i])
    if os.path.isdir(path):
        continue
    # 获取文件的修改时间
    timestamp = os.path.getmtime(path)
    print(timestamp)
    # 获取文件的修改时间
    ts1 = os.stat(path).st_mtime
    print(ts1)
    # 获取文件的大小,结果保留两位小数，单位为MB
    filesize = os.path.getsize(path)
    fsize = filesize/float(1024*1024)
    size =  round(fsize,2)
    print(size)

    date=datetime.datetime.fromtimestamp(timestamp)
    print(list[i], ' 最近修改时间是: ', date.strftime('%Y-%m-%d %H:%M:%S'))
```



- [ref](https://blog.csdn.net/weixin_41738417/article/details/103126467?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-2&spm=1001.2101.3001.4242)

