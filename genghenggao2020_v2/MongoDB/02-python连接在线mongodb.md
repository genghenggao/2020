### 报错

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

### 报错

```
pymongo.errors.InvalidURI: Username and password must be escaped according to RFC 3986, use urllib.parse.quote_plus()
```

- 解决

  ```
  mongo_uri = 'mongodb+srv://henggao:' + \
  #     urllib.parse.quote('@Tel15351818127') + \
  #     '@mongeostore-tgjjd.mongodb.net/test?retryWrites=true&w=majority'
  ```

  

### 连接在线mongodb

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

