# 目录

[TOC]

## 一、python下上传/下载各种格式文件到MongoDB数据库中

python中，支持通过GridFS使用MongoDB数据库提供的大文件存储功能，本文中通过这种方法将各种格式文件以二进制格式(测试了.pdf、.py格式文件)存入GridFS集合中。

```python
#-*-coding:utf-8-*-
import os
import sys
from gridfs import *
from pymongo import MongoClient
from datetime import datetime

path = sys.path[0] + os.sep  # 获取当前文件所在文件夹目录
client = MongoClient('127.0.0.1', 27017)  # 连接MongoDB数据库
db = client.file  # 选定数据库，设定数据库名称为file
fs = GridFS(db, collection='pdf')  # 连接GridFS集合，名称为pdf

def upload():
    # 上传文件到GridFS集合中
    for filename in os.listdir(path):  # 遍历文件
        dic = dict()
        dic['文件名'] = filename
        dic['上传时间'] = datetime.now()
        content = open(path + filename, 'rb').read()  # 二进制格式读取文件内容
        fs.put(content, **dic)  # 上传文件

def download():
    # 下载文件
    for cursor in fs.find():
        filename = cursor.文件名
        content = cursor.read()
        with open(path + 'temp/' + filename, 'wb') as f:
            f.write(content)

if __name__ == '__main__':
    # upload()
    download()
```



## 二、本地上传

```python
'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-13 21:39:22
LastEditors: henggao
LastEditTime: 2020-10-14 11:19:33
'''
#  上传文件到gridfs
import pymongo
import gridfs
from bson import ObjectId
from pymongo.mongo_client import MongoClient
import datetime
client = MongoClient("192.168.55.110", 20000)  # 连接MongoDB数据库
db = client.segyfile  # 选定数据库，设定数据库名称为segyfile
# db = client['segyfile']
# @require_http_methods(['GET'])

# 上传文件到GridFS集合中
# 存储文件到mongo

# file = ".\mongeostore_env\mytest\AWS.png"
file = ".\mongeostore_env\mytest\mytest.SGY"
# file = ".\mongeostore_env\mytest\LX_SEGY2.segy"


def upload():
    with open(file, 'rb') as f:

        file_type = file.split(".")[-1]
        # print(file_type)   #类型

        file_name = file.split("\\")[-1]
        # print(file_name)
        dic = {
            "filename": file_name,
            "contentType": file_type,
            "metadata":"test_name",
        }
        data = f.read()
        fs = gridfs.GridFS(db, 'mysegy')  # 连接GridFS集合，名称位mysegy
        # dic['上传时间'] = datetime.now()
        # content = open(path + filename, 'rb').read()  # 二进制格式读取文件内容
        fs.put(data, **dic)


if __name__ == '__main__':
    upload()

```

## 三、数据库下载+segyio分析

```python
'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-10-11 16:39:26
LastEditors: henggao
LastEditTime: 2020-10-14 20:38:04
'''
import segyio
from gridfs import GridFS
from bson.objectid import ObjectId
import pymongo
from pymongo import MongoClient
import gridfs

######example 查询数据库下所有collection名称########
client = MongoClient("192.168.55.110", 20000)
db = client['segyfile']
coll_names = db.list_collection_names(session=None)
# print(coll_names)  # ['LX_SEGY', 'LX_SEGY2', 'fs.files', 'fs.chunks', 'User']


# 使用segyio读取segy文件
fs = client.segyfile.mysegy.chunks
filename = client.segyfile.mysegy.files
# print(fs.find())  # <pymongo.cursor.Cursor object at 0x00000143A18F0CC8>

# print(filename.find())  # <pymongo.cursor.Cursor object at 0x00000143A18F0CC8>

db = client.grid
fs_gridfs = gridfs.GridFS(db)
files = fs_gridfs.find()
files_segy = fs_gridfs.find_one({"md5": "2105ca42eba2041fa4bca6030944ae89"})
# print(files)  # <gridfs.grid_file.GridOutCursor object at 0x000002633B4983C8>
# print(files_segy)  # None

db2 = client.segyfile
filename2 = GridFS(db2, collection="mysegy")

# print(filename2)
# print(filename2.find({"filename": "AWS.png"}))
for cursor in filename2.find({"filename": "mytest.SGY"}):
    print(cursor.filename)
    # filenname = cursor.LX_SEGY2.segy
    if cursor.filename == "mytest.SGY":
        filename = cursor.filename
        # content = cursor.read()
        with open(filename, "wb") as f:
            content = cursor.read()
            f.write(content)
   
    # file = ".\mongeostore_env\mytest\mytest.SGY"
    with segyio.open(cursor.filename, mode="rb", strict=False, ignore_geometry=False, endian='big') as f:
        print(f.tracecount)

        f.close()

```

