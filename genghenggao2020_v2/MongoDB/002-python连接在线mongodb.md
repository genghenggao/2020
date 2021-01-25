# MongoDB

[TOC]



## 1. MongoDB Atlas

### 1.1 报错

#### 1.1.1 报错001

```
pymongo.errors.ConfigurationError: The "dnspython" module must be installed to use mongodb+srv:// URIs
```

- 解决

  In order to use **mongo+srv** protocol, you need to install **pymongo-srv** Launch this command to do it with python 3:

  ```
  pip3 install pymongo[srv]
  ```

  or this one for other versions:

  ```
  pip install pymongo[srv]
  ```



#### 1.1.2 报错002

```
pymongo.errors.InvalidURI: Username and password must be escaped according to RFC 3986, use urllib.parse.quote_plus()
```

- 解决

  ```
  mongo_uri = 'mongodb+srv://henggao:' + \
  #     urllib.parse.quote('@Tel15351818127') + \
  #     '@mongeostore-tgjjd.mongodb.net/test?retryWrites=true&w=majority'
  ```

  

### 1.2 连接在线MongoDB

```python
'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-05-18 17:52:35
@LastEditors: Henggao
@LastEditTime: 2020-05-18 18:53:52
'''

#!/usr/bin/python3
# coding=utf-8
import pymongo
import urllib
# from urllib import parse

mongo_uri = 'mongodb+srv://henggao:tel123456@cluster0-nnssa.mongodb.net/test?retryWrites=true&w=majority'
myclient = pymongo.MongoClient(mongo_uri)

dblist = myclient.list_database_names()
print(dblist)
if "gridfs" in dblist:
    print("数据库已存在！")

```



### 1.3 实例测试

- 写入数据

  ```python
  import pymongo
  from pymongo import MongoClient
  import urllib.parse
  
  # username = urllib.parse.quote_plus('henggao')
  # password = urllib.parse.quote_plus("tel123456")
  
  # url = "mongodb+srv://henggao:<password>@mongeostore.tgjjd.mongodb.net/<dbname>?retryWrites=true&w=majority".format(username, password)
  url = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net/mongoestore?retryWrites=true&w=majority"
  # url is just an example (your url will be different)
  
  cluster = MongoClient(url)
  db = cluster['demo01']
  collection = db['test01']
  
  data = {
      "mobile": 15518501828,
      "code": 123456,
  }
  collection.insert_one(document=data)
  
  print(db)
  print(collection)
  ```

- 查看

  ![](IMG/微信截图_20210120101842.png)

## 2. CentOS

### pymongo连接MongoDB

```python
import datetime
import pymongo
from pymongo import MongoClient

client = MongoClient("192.168.55.110", 27017)
collection = client.test.expire
collection.create_index(
    [("time", pymongo.ASCENDING)], expireAfterSeconds=66)
data = {
    "mobile":15351818127,
    "code": 123456,
}
# collection.insert(data)
dblist = client.list_database_names()
code = collection.find_one()
mobilecode = collection.find_one({"mobile":15351818127})
# print(dblist)
# print(code)
print(mobilecode)
print(mobilecode['code'])
# print(type(mobilecode))
# print(collection)
```

