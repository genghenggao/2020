# 数据库在Setting中配置

[TOC]

## 1.测试

- 在`mytest/settings.py`添加数据库配置

```python
## MongoDB数据库设置 ##
import pymongo
MongoDB_client = pymongo.MongoClient("192.168.55.110", 20000)

### MongoDB Atlas ###
# MONGODB_URL = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net/mongoestore?retryWrites=true&w=majority"
MONGODB_URL = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net"
MongoDB_Atlas_client = pymongo.MongoClient(MONGODB_URL)

### mongoengine 连接Atlas ###
MONGODB_Atlas_URL = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net"
```



## 2. MongoEngine

- mongoengine连接

  ```python
  from mongoengine import connect
  from mongoengine.context_managers import switch_collection
  from mongoengine.document import Document
  from mongoengine.fields import IntField, StringField
  
  import settings
  from mongoengine import *
  # connect('钻孔数据管理子系统', host='192.168.55.110', port=20000)
  
  # url = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net/用户信息管理子系统?retryWrites=true&w=majority"
  # connect(host=url, port=20000)
  
  # url = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net"
  # connect(db='用户信息管理子系统', host=url, port=20000)
  connect(db='用户信息管理子系统', host=settings.MONGODB_Atlas_URL, port=20000)
  
  class Users(Document):
      name = StringField(required=True, max_length=200)
      age = IntField(required=True)
  
  # user1 = Users(
  #     name='zz',
  #     age=112
  # )
  
  # user1.save()
  # print(user1.name)
  # user1.name = 'zz11'
  # user1.save()
  # print(user1.name)
  
  with switch_collection(Users, '用户') as user:
      user(name='henggao',age=28).save()  # 将数据保存至 用户 集合
  ```



## 3. Pymongo

- pymongo连接

  ```python
  '''
  Description: henggao_learning
  version: v1.0.0
  Author: henggao
  Date: 2021-01-20 09:06:06
  LastEditors: henggao
  LastEditTime: 2021-01-21 10:34:06
  '''
  #!/usr/bin/python3
  # coding=utf-8
  # import pymongo
  # import urllib
  # from urllib import parse
  
  # mongo_uri = 'mongodb+srv://henggao:tel123456@cluster0-nnssa.mongodb.net/test?retryWrites=true&w=majority'
  # mongo_uri = 'mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net/mongeostore?retryWrites=true&w=majority'
  # mongo_uri = 'mongodb+srv://henggao:@Tell5351818127@mongeostore.tgjjd.mongodb.net/mongeostore?retryWrites=true&w=majority'
  # 转义用户名和密码
  # mongo_uri = 'mongodb+srv://henggao:' + urllib.parse.quote(
  #     '@Tel15351818127') + '@mongeostore-tgjjd.mongodb.net/mongeostore?retryWrites=true&w=majority'
  
  # myclient = pymongo.MongoClient(mongo_uri)
  # dblist = myclient.list_database_names()
  # print(dblist)
  # if "gridfs" in dblist:
  #     print("数据库已存在！")
  
  
  # client = pymongo.MongoClient("mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net/mongeostore?retryWrites=true&w=majority")
  # db = client.test
  
  # print(db)
  
  
  import pymongo
  from pymongo import MongoClient
  import urllib.parse
  import settings
  
  # username = urllib.parse.quote_plus('henggao')
  # password = urllib.parse.quote_plus("tel123456")
  
  # url = "mongodb+srv://henggao:<password>@mongeostore.tgjjd.mongodb.net/<dbname>?retryWrites=true&w=majority".format(username, password)
  # url = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net/mongoestore?retryWrites=true&w=majority"
  url = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net"
  # url is just an example (your url will be different)
  
  cluster = MongoClient(url)
  db = cluster['demo01']
  collection = db['test01']
  
  ### Demo1 插入数据 #######
  # data = {
  #     "mobile": 15518501828,
  #     "code": 123456,
  # }
  # collection.insert_one(document=data)
  
  # print(db)
  # print(collection)
  
  
  ### Demo2 查询数据库 #######
  # dblist = cluster.list_database_names()
  # print(dblist)
  
  
  ###    使用配置文件连接MongoDB （当前目录下settings.py）     ###
  # client = settings.MongoDB_client   
  client = settings.MongoDB_Atlas_client
  # dblist = client.list_database_names()
  # print(dblist)
  db  = client['钻孔数据管理子系统']
  collection = db['定位表']
  print(db)
  print(collection)
  
  ```

  

  ## 4. MonGeoStore实例

- 在`Mongeostore_v1/local_settings.py`添加数据库配置

  - 配置MongoDB数据库

  ```python
  ## MongoDB数据库设置 ##
  ### 1. MongoDB CentOS ###
  # MongoDB_client = pymongo.MongoClient("192.168.55.110", 20000)
  # MONGODB_URL = "192.168.55.110:20000"
  # MONGODB_URL = "192.168.55.110:27017"
  ### 2. MongoDB Atlas ###
  MONGODB_URL = "mongodb+srv://henggao:tel123456@mongeostore.tgjjd.mongodb.net"
  
  MongoDB_client = pymongo.MongoClient(MONGODB_URL)
  
  
  # 默认数据库重写
  DATABASES = {
      'default': {
          # 'ENGINE': 'django.db.backends.sqlite3',
          # 'NAME': BASE_DIR / 'db.sqlite3',
  
          # 使用djongo设置mongodb
          'ENGINE': 'djongo',
          'NAME': 'django_example',
          'CLIENT': {
              'host': MONGODB_URL,
              # 'host': '192.168.55.110:27017',
              # 'host': '192.168.55.110:20000',
          }
      },
  }
  ```

  - 🔔上述DATABASES主要针对使用Djongo时models.py配置，如果使用mongoengine，这里可以不需要。

  

- mongeostore_app/views.py修改

  - 将2处mongodb数据库调整为

  ```
          # client = MongoClient("192.168.55.110", 27017)
          # collection = client.mobilecode.expire
          client = settings.MongoDB_client
          db  = client['用户数据管理子系统']
          collection = db['用户手机注册']
  ```

  