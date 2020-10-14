

# pymongodb 学习总结

链接：https://www.cnblogs.com/playcodes/p/6292344.html



```
老规矩，英文文档：http://api.mongodb.com/python/current/examples/authentication.html
```

## 一、mongodb

### 1、简介

> MongoDB是一种强大、灵活、追求性能、易扩展的数据存储方式。是面向文档的数据库，不是关系型数据库，是NoSQL(not only SQL)的一种。所谓的面向文档，就是将原来关系型数据库中的“行”的概念换成了更加灵活的"文档"，以文档为存储单位。文档的值可以是数组、文档等复杂的数据模型。并且文档的键不会事先定义也不会固定不变。mongoDB设计的主要思想之一就是，将能交给客户端的操作都要从服务端转移到客户端。

### 文档

> 文档是MongoDB的核心、基本数据单元，类似于JS中的JSON对象，由多个key-value构成，但是支持更多的数据类型。多个键以及相关的值有序的放置在一起便是文档。在大多数编程语言中都是使用多个key-value的形式，Java中是map，Python中是字典，JavaScript中是对象。

```
	文档中的key/value是有序的，没有相同的两个文档。
	文档中的value的数据类型没有限制，甚至可以是文档。
	文档的key一般应该是字符串。
	文档的key不能含有空字符串，不能含有.和$以及_。
	文档的key不能重复。
	mangoDB中，key和value都是区分数据类型和大小写的。
```

### 集合

> 集合就是一组文档，如果说文档类似于关系数据库中的行，那么集合就是表。集合是无模式的(模式的概念参见模式的意义)。一个集合中的文档可以是任意类型的，也就是说文档是可以任意组合的。

```
	和key一样不能有空字符串
	不能以"system."开头，不能含有"$"
	一个集合的完全限定名：数据库名.集合(子集合)名称，例如cms.blog.posts
```

### 数据库

> MangoDB中最基本的存储单元是文档，文档组成集合，集合组成数据库。一个MangoDB实例可以承载多个数据库，数据库之间完全独立。一般情况下，一个应用对应一个数据库，类似于关系数据库中的外模式。

```
	不能是空字符串
	不得含有空格、点、斜杠与反斜杠以及空字符串。
	应该全部小写
	最多64字节
```

## 2、安装

#### 平台：centos 6

#### 下载地址：https://www.mongodb.com/download-center#community

```
cd /usr/local

解压：tar -zxvf mongodb-linux-x86_64-rhel62-3.2.7.tgz

移动：mv mongodb-linux-x86_64-rhel62-3.2.7 mongodb

配置环境变量,修改/etc/profile,添加如下内容：
export MONGODB_HOME=/usr/local/mongodb
export PATH=$MONGODB_HOME/bin:$Path

执行命令：
    source /etc/profile
```

查看mongodb版本信息 mongod -v

```
[root@myvpc bin]# mongod -v
2017-01-16T20:27:59.622+0800 I CONTROL  [initandlisten] MongoDB starting : pid=23389 port=27017 dbpath=/data/db 64-bit host=myvpc
2017-01-16T20:27:59.622+0800 I CONTROL  [initandlisten] db version v3.2.7
2017-01-16T20:27:59.622+0800 I CONTROL  [initandlisten] git version: 4249c1d2b5999ebbf1fdf3bc0e0e3b3ff5c0aaf2
2017-01-16T20:27:59.622+0800 I CONTROL  [initandlisten] OpenSSL version: OpenSSL 1.0.1e-fips 11 Feb 2013
2017-01-16T20:27:59.622+0800 I CONTROL  [initandlisten] allocator: tcmalloc
2017-01-16T20:27:59.622+0800 I CONTROL  [initandlisten] modules: none
2017-01-16T20:27:59.622+0800 I CONTROL  [initandlisten] build environment:
2017-01-16T20:27:59.622+0800 I CONTROL  [initandlisten]     distmod: rhel62
2017-01-16T20:27:59.622+0800 I CONTROL  [initandlisten]     distarch: x86_64
2017-01-16T20:27:59.622+0800 I CONTROL  [initandlisten]     target_arch: x86_64
2017-01-16T20:27:59.622+0800 I CONTROL  [initandlisten] options: { systemLog: { verbosity: 1 } }
2017-01-16T20:27:59.622+0800 D NETWORK  [initandlisten] fd limit hard:4096 soft:1024 max conn: 819
2017-01-16T20:27:59.644+0800 E NETWORK  [initandlisten] listen(): bind() failed errno:98 Address already in use for socket: 0.0.0.0:27017
2017-01-16T20:27:59.644+0800 E NETWORK  [initandlisten]   addr already in use
2017-01-16T20:27:59.644+0800 E STORAGE  [initandlisten] Failed to set up sockets during startup.
2017-01-16T20:27:59.644+0800 I CONTROL  [initandlisten] dbexit:  rc: 48
```

如有以上提示，即表明安装成功。

## 3、启动

### 3.1 创建数据库目录

#### Mongodb 需要自建数据库文件夹

```
mkdir -p /data/mongodb
mkdir -p /data/mongodb/log
touch /data/mongodb/log/mongodb.log
```

#### 添加配置文件

新建配置文件：mongodb.conf，通过其进行启动

```
vim /etc/mongodb.conf
```

配置文件参数说明：

```
mongodb的参数说明：
 --dbpath 数据库路径(数据文件)
 --logpath 日志文件路径
 --master 指定为主机器
 --slave 指定为从机器
 --source 指定主机器的IP地址
 --pologSize 指定日志文件大小不超过64M.因为resync是非常操作量大且耗时，最好通过设置一个足够大的oplogSize来避免resync(默认的 oplog大小是空闲磁盘大小的5%)。
 --logappend 日志文件末尾添加
 --port 启用端口号
 --fork 在后台运行
 --only 指定只复制哪一个数据库
 --slavedelay 指从复制检测的时间间隔
 --auth 是否需要验证权限登录(用户名和密码)

注：mongodb配置文件里面的参数很多，定制特定的需求，请参考官方文档
```

配置文件内容：

```
dbpath=/data/mongodb
logpath=/data/mongodb/log/mongodb.log
logappend=true
port=27017
fork=true
##auth = true # 先关闭, 创建好用户在启动
```

#### 通过配置文件启动

```
mongod -f /etc/mongodb.conf
about to fork child process, waiting until server is ready for connections.
forked process: 2814
child process started successfully, parent exiting
```

若出现上述信息，则表示启动成功了。

## 4、进入mongodb-shell

#### 方法：

```
cd /usr/local/mongodb/bin
./mongo
```

#### 创建数据库

```
[IN] use test
[OUT] switched to db test
```

#### 创建用户，设置权限

```
db.createUser(
    {
        user: "test",
        pwd: "test",
        roles: [ { role: "readWrite", db: "test" } ]
    }
)
```

更多权限配置请参考：[点我](http://www.cnblogs.com/zhoujinyi/p/4610050.html)

注：在设置好权限后，到/etc/mongodb.conf 将auth改为true，下次在使用对应的数据库时，则需要进行验证：db.auth(user,passwd)

## 5、配置防火墙

将27017端口添加到防火墙中

```
vi /etc/sysconfig/iptables
    -A INPUT -m state --state NEW -m tcp -p tcp --dport 27017 -j ACCEPT
/etc/init.d/iptables reload
```

## 二、PyMongo

### 1、安装

```
pip install pymongo
```

### 2、使用

#### 2.1 连接

```
 (1) 导入
from pymongo import MongoClient

 (2) 连接mongodb
host = localhost
port = 27017

client = MongoClient(host,port)

 (3) 连接数据库

db = client.test_database

or 

db = client[test_database]

注：当连接的数据库设置了auth之后，需要这样连接，不同版本，不同平台都不一样，具体见官方文档

client[test_database].authenticate("user","passwd",mechanism="SCRAM-SHA-1")

(4) 连接数据库中的某个集合
## 获取该数据库中的非系统集合
db.collection_names(include_system_collections=False)

## 连接集合
collection = db[collection_name]
or 
collection = db.collection_name
```

#### 2.2 增删改查

很好的一点就是，数据库不需要先建立，在连接后，如果进行插入数据操作，系统可以自己创建，上面提到过，mongodb的数据，使用的是类似json风格的文档，在python中即为字典，形如下例：

```
         insert_data = {
         "author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()
          }
```

#### collection = db[collection_name]

##### (1)增

在插入一个文档时，MongoDB会自动给每个文档增加一个”_id”的键，这个键是通过复杂计算出来的，不会重复，类似于下面这样的：

```
ObjectId('4ea02dfdd483050fe8000001')
```

那么如何利用ObjectId查询，这里有一个坑

```
>>> import pymongo
>>> import time
>>> db = pymongo.Connection("192.168.xx.xx",27017).linuxyan
>>> posts = db.posts
>>> post = {"id": "1",
...         "author": "Mike",
...         "text": "My first blog post!",
...         "tags": ["mongodb", "python", "pymongo"],
...         "date": time.strftime('%Y-%m-%d %H:%M:%S')}
>>> posts.insert(post)
ObjectId('53bd5a5fe138235f74b67563')

#//插入数据成功
#//利用{'author':'Mike'} 测试查询正常
>>> posts.find_one({'author':'Mike'})
{u'_id': ObjectId('53bd5a5fe138235f74b67563'), u'author': u'Mike',....}

#//利用{'_id':"ObjectId('53bd5a5fe138235f74b67563')"}查询为空
>>>posts.find_one({'_id':"ObjectId('53bd5a5fe138235f74b67563')"})	

#//如何利用ObjectId来查询？
>>> from bson import ObjectId
>>> posts.find_one({'_id':ObjectId('53bd5a5fe138235f74b67563')})  
{ u'_id': ObjectId('53bd5a5fe138235f74b67563'), u'author': u'Mike',....}
#//原来ObjectId是一个对象，而不是一个字符串，此时我只能"呵呵"，折腾两个多小时。
```

增加数据不需要事先定义文档的机构，每个文档的结构也可以不一样

###### 单条插入

```
result = collection.insert_one(insert_data)
```

###### 多条插入

```
result = collection.insert_many(insert_datas)
```

##### 返回插入id

```
result.insert_id [单]    
result.insert_ids [多]
```

##### (2)查 参考[here](http://www.cnblogs.com/similarface/p/5608987.html)

###### 无条件查询

```
collection.find_one() [单]    
collection.find() [多]
```

###### 条件查询

```
collection.find({"author": "Mike"})    
collection.find_one({"author": "Mike"})
cursor = collection.find({
"$or":[{"cuisine": "Italian", "address.zipcode": "10075"}]
}
)    
[仅显示cuisine为Italian和address.zipcode为10075的数据。两个条件只要满足一个就可以]
```

###### 区间查询

```
d = datetime.datetime(2009, 11, 12, 12)
for post in collection.find({"date": {"$lt": d}}).sort("author"):    
    print post
 $lt 小于
```

###### 文档记录数

```
collection.count()
```

###### 数据排序

调用 pymongo.ASCENDING()和pymongo.DESCENDING()来指定是按升降序进行排序

```
cursor = collection.find().sort([
    ("borough", pymongo.ASCENDING),
    ("address.zipcode", pymongo.ASCENDING)
])
```

###### 从第几行开始读取(SLICE)，读取多少行(LIMIT)

```
for u in collection.find().skip(2).limit(3): 
    print u
```

###### IN

```
for u in db.users.find({"age":{"$in":(23, 26, 32)}}): print u
for u in db.users.find({"age":{"$nin":(23, 26, 32)}}): print u
```

###### 是否存在

```
db.users.find({'sex':{'$exists':True}})  # select * from 集合名 where exists 键1
db.users.find({'sex':{'$exists':False}}) # select * from 集合名 where not exists 键1
```

###### 正则表达式查询

```
for u in db.users.find({"name" : {"$regex" : r"(?i)user[135]"}}, ["name"]): print u # 查询出 name 为 user1, user3, user5 的
```

###### 多级路径的元素值匹配

```
Document 采取 JSON-like 这种层级结构，因此我们可以直接用嵌入(Embed)代替传统关系型数据库的关联引用(Reference)。
    MongoDB 支持以 "." 分割的 namespace 路径，条件表达式中的多级路径须用引号

# 条件表达式中的多级路径须用引号,以 "." 分割
    u = 集合名.find_one({"im.qq":12345678})
    # 查询结果如：{"_id" : ObjectId("4c479885089df9b53474170a"), "name" : "user1", "im" : {"msn" : "user1@hotmail.com", "qq" : 12345678}}
```

##### (3)改

```
origin_data = {"title":"Python and MongoDB",
     "slug":"python-mongodb",
     "author":"SErHo",
     "content":"Python and MongoDB....",
     "tags":["Python","MongoDB"],
     "time":datetime.datetime.now()}
>>> post = posts.find_one({"slug":"python-mongodb"})
>>> post["author"]
u'SErHo'
>>> post["author"] = "HaHa Lu"
>>> post["title"] = "Test Update"
>>> post["title"] = "Test Update"
>>> post["_id"]
ObjectId('4ea0207dd483050fe8000001')
>>> posts.update({"_id":post["_id"]},post)
>>> post = posts.find_one({"_id":post["_id"]})
>>> print post
{u'author': u'HaHa Lu', u'title': u'Test Update',
 u'tags': [u'Python', u'MongoDB'],
 u'content': u'Python and MongoDB....',
 u'time': datetime.datetime(2011, 10, 20, 21, 21, 52, 818000),
 u'_id': ObjectId('4ea0207dd483050fe8000001'),
 u'slug': u'python-mongodb'}
```

> 首先我们根据slug来获得一篇文章，然后可以通过Python字典访问方法得到键的值，然后重新设置，再对post集合进行更新，在对整个集合进行更新时，你得先匹配要更改的文档，利用_id这个属性来更新是比较常用的方法，因为你其他改了，这个可改不了。在执行update中最常见的错误就是限制的条件找到了多个文档，如果这样，数据库就不会更新这个集合，所有最好使用_id来匹配。

如果只更新一个键呢，那就不用这么大费周折了，可以使用”$set”这个修改器，指定一个键，如果不存在，就可以创建。比如我要继续更新上面那篇文章的content，可以这样做（记住，修改它，必须先找到它，这里我利用上面查询到的_id值来找）：

```
>>> posts.update({"_id":post["_id"]},{"$set": {"content":"Test Update SET...."}})
```

MongoDB的修改是很强大的，你可以把数据类型也给改了，比如把tags的数组改成普通的字符串。”$set”过后又想删除这个键，可以使用”$unset”。如果我的这个post里面有一个键是views，即文章访问的次数，我想在每次访问这个文章后给它的值增加1，这该怎么办？于是”$inc”修改器出场了，这个可以用来增加已有键的值，如果没有，则创建它，类似的用法是：

```
>>> posts.update({"_id":post["_id"]},{"$inc":  {"views":1}})
```

如果想修改tags这个数组里面的内容怎么办？有一个办法就是用$set整体修改，但只是改里面的一些元素呢，MongoDB准备好了用于数组的修改器。比如，想要在tags里面加一个”Test”，这需要使用”$push”，它可以在数组末尾添加一个元素：

```
>>> posts.update({"_id":post["_id"]},{"$push":{"tags":"Test"}})
```

为了避免加入了重复的，可以将”$push”改为使用”$addToSet”，如果需要添加多个值，可以配合”$each”来使用，这样就可以添加不重复的进去，如下面：

```
>>> posts.update({"_id":post["_id"]},{"$addToSet": {"tags":{"$each":["Python","Each"]}}})
```

##### (4) 删

可以把数组看成栈和队列，使用”$pop”来操作，比如上面的：

```
>>> posts.update({"_id":post["_id"]},{"$pop":{"tags":1}})
```

这个会删除tags里面最后一个，改成-1则删除第一个。可以使用”$pull”来删除数组中指定的值，它会删除数组中所有匹配的值。如何修改其中的一个值呢？可以先删除掉，再增加一个进去，还有就是直接定位修改。比如tags数组中，”Python”是第一个，想把它改成”python”，可以通过下标直接选择,就是tags[0]，然后使用上面的”$set”等修改器，如果不确定可以使用$来定位：

```
>>> posts.update({"tags":"MongoDB"},{"$set":{"tags.$":"Hello"}})
```

这个将先搜索tags中满足”MongoDB”的，如果找到，就把它修改为”Hello”。可以看到上面的update这个函数已经有两个参数了，它还有第3个参数upsert，如果设为”True”，则如果没有找到匹配的文档，就会在匹配的基础上新建一个文档

### 3、相关操作

```
注：collection:user
(1) $all: 判断数组属性是否包含全部条件。
    db.users.insert({'name':"user3", 'data':[1,2,3,4,5,6,7]})
    db.users.insert({'name':"user4", 'data':[1,2,3]})

    for u in db.users.find({'data':{'$all':[2,3,4]}}): print u
    # 显示： { "_id" : ObjectId("4c47a133b48cde79c6780df0"), "name" : "user3", "data" : [ 1, 2, 3, 4, 5, 6, 7 ] }
    注意和 $in 的区别。$in 是检查目标属性值是条件表达式中的一员，而 $all 则要求属性值包含全部条件元素。

  (2) $size: 匹配数组属性元素数量。
    for u in db.users.find({'data':{'$size':3}}): print u
    # 只显示匹配此数组数量的： { "_id" : ObjectId("4c47a13bb48cde79c6780df1"), "name" : "user4", "data" : [ 1, 2, 3 ] }

  (3) $type: 判断属性类型。
    for u in db.users.find({'t':{'$type':1}}): print u  # 查询数字类型的
    for u in db.users.find({'t':{'$type':2}}): print u  # 查询字符串类型的

    类型值:
        double:1
        string: 2
        object: 3
        array: 4
        binary data: 5
        object id: 7
        boolean: 8
        date: 9
        null: 10
        regular expression: 11
        javascript code: 13
        symbol: 14
        javascript code with scope: 15
        32-bit integer: 16
        timestamp: 17
        64-bit integer: 18
        min key: 255
        max key: 127

  (4) $not: 取反，表示返回条件不成立的文档。
    似乎只能跟正则和 $mod 一起使用？？？？
    # 还不知如何使用

  (5) $unset: 和 $set 相反，表示移除文档属性。
    for u in db.users.find({'name':"user1"}): print u
    # 显示如： { "_id" : ObjectId("4c479885089df9b53474170a"), "name" : "user1", "age" : 15, "address" : [ "address1", "address2" ] }

    db.users.update({'name':"user1"}, {'$unset':{'address':1, 'age':1}})
    for u in db.users.find({'name':"user1"}): print u
    # 显示如： { "_id" : ObjectId("4c479885089df9b53474170a"), "name" : "user1" }

  (6) $push: 和 $ pushAll 都是向数组属性添加元素。# 好像两者没啥区别
    for u in db.users.find({'name':"user1"}): print u
    # 显示如： { "_id" : ObjectId("4c479885089df9b53474170a"), "age" : 15, "name" : "user1" }

    db.users.update({'name':"user1"}, {'$push':{'data':1}})
    for u in db.users.find({'name':"user1"}): print u
    # 显示如： { "_id" : ObjectId("4c479885089df9b53474170a"), "age" : 15, "data" : [ 1 ], "name" : "user1" }

    db.users.update({'name':"user1"}, {'$pushAll':{'data':[2,3,4,5]}})
    for u in db.users.find({'name':"user1"}): print u
    # 显示如： { "_id" : ObjectId("4c479885089df9b53474170a"), "age" : 15, "data" : [ 1, 2, 3, 4, 5 ], "name" : "user1" }

  (7) $addToSet: 和 $push 类似，不过仅在该元素不存在时才添加 (Set 表示不重复元素集合)。
    db.users.update({'name':"user2"}, {'$unset':{'data':1}})
    db.users.update({'name':"user2"}, {'$addToSet':{'data':1}})
    db.users.update({'name':"user2"}, {'$addToSet':{'data':1}})
    for u in db.users.find({'name':"user2"}): print u
    # 显示： { "_id" : ObjectId("4c479896089df9b53474170b"), "data" : [ 1 ], "name" : "user2" }

    db.users.update({'name':"user2"}, {'$push':{'data':1}})
    for u in db.users.find({'name':"user2"}): print u
    # 显示： { "_id" : ObjectId("4c479896089df9b53474170b"), "data" : [ 1, 1 ], "name" : "user2" }

    要添加多个元素，使用 $each。
    db.users.update({'name':"user2"}, {'$addToSet':{'data':{'$each':[1,2,3,4]}}})
    for u in db.users.find({'name':"user2"}): print u
    # 显示： {u'age': 12, u'_id': ObjectId('4c479896089df9b53474170b'), u'data': [1, 1, 2, 3, 4], u'name': u'user2'}
    # 貌似不会自动删除重复

  (8) $each 添加多个元素用。
    db.users.update({'name':"user2"}, {'$unset':{'data':1}})
    db.users.update({'name':"user2"}, {'$addToSet':{'data':1}})
    for u in db.users.find({'name':"user2"}): print u
    # 显示： { "_id" : ObjectId("4c479896089df9b53474170b"), "data" : [ 1 ], "name" : "user2" }

    db.users.update({'name':"user2"}, {'$addToSet':{'data':{'$each':[1,2,3,4]}}})
    for u in db.users.find({'name':"user2"}): print u
    # 显示： {u'age': 12, u'_id': ObjectId('4c479896089df9b53474170b'), u'data': [1, 2, 3, 4], u'name': u'user2'}

    db.users.update({'name':"user2"}, {'$addToSet':{'data':[1,2,3,4]}})
    for u in db.users.find({'name':"user2"}): print u
    # 显示： { "_id" : ObjectId("4c479896089df9b53474170b"), "data" : [ 1, 2, 3, 4, [ 1, 2, 3, 4 ] ], "name" : "user2" }

    db.users.update({'name':"user2"}, {'$unset':{'data':1}})
    db.users.update({'name':"user2"}, {'$addToSet':{'data':[1,2,3,4]}})
    for u in db.users.find({'name':"user2"}): print u
    # 显示： { "_id" : ObjectId("4c47a133b48cde79c6780df0"), "data" : [ [1, 2, 3, 4] ], "name" : "user2" }

  (9) $pop: 移除数组属性的元素(按数组下标移除)，$pull 按值移除，$pullAll 移除所有符合提交的元素。
    db.users.update({'name':"user2"}, {'$unset':{'data':1}})
    db.users.update({'name':"user2"}, {'$addToSet':{'data':{'$each':[1, 2, 3, 4, 5, 6, 7, 2, 3 ]}}})
    for u in db.users.find({'name':"user2"}): print u
    # 显示： { "_id" : ObjectId("4c47a133b48cde79c6780df0"), "data" : [ 1, 2, 3, 4, 5, 6, 7, 2, 3 ], "name" : "user2" }

    db.users.update({'name':"user2"}, {'$pop':{'data':1}}) # 移除最后一个元素
    for u in db.users.find({'name':"user2"}): print u
    # 显示： { "_id" : ObjectId("4c47a133b48cde79c6780df0"), "data" : [ 1, 2, 3, 4, 5, 6, 7, 2 ], "name" : "user2" }

    db.users.update({'name':"user2"}, {'$pop':{'data':-1}}) # 移除第一个元素
    for u in db.users.find({'name':"user2"}): print u
    # 显示： { "_id" : ObjectId("4c47a133b48cde79c6780df0"), "data" : [ 2, 3, 4, 5, 6, 7, 2 ], "name" : "user2" }

    db.users.update({'name':"user2"}, {'$pull':{'data':2}}) # 移除全部 2
    for u in db.users.find({'name':"user2"}): print u
    # 显示： { "_id" : ObjectId("4c47a133b48cde79c6780df0"), "data" : [ 3, 4, 5, 6, 7 ], "name" : "user2" }

    db.users.update({'name':"user2"}, {'$pullAll':{'data':[3,5,6]}}) # 移除 3,5,6
    for u in db.users.find({'name':"user2"}): print u
    # 显示： { "_id" : ObjectId("4c47a133b48cde79c6780df0"), "data" : [ 4, 7 ], "name" : "user2" }

  (10) $where: 用 JS 代码来代替有些丑陋的 $lt、$gt。
    MongoDB 内置了 Javascript Engine (SpiderMonkey)。可直接使用 JS Expression，甚至使用 JS Function 写更复杂的 Code Block。

    db.users.remove() # 删除集合里的所有记录
    for i in range(10):
        db.users.insert({'name':"user" + str(i), 'age':i})
    for u in db.users.find(): print u
    # 显示如下：
    { "_id" : ObjectId("4c47b3372a9b2be866da226e"), "name" : "user0", "age" : 0 }
    { "_id" : ObjectId("4c47b3372a9b2be866da226f"), "name" : "user1", "age" : 1 }
    { "_id" : ObjectId("4c47b3372a9b2be866da2270"), "name" : "user2", "age" : 2 }
    { "_id" : ObjectId("4c47b3372a9b2be866da2271"), "name" : "user3", "age" : 3 }
    { "_id" : ObjectId("4c47b3372a9b2be866da2272"), "name" : "user4", "age" : 4 }
    { "_id" : ObjectId("4c47b3372a9b2be866da2273"), "name" : "user5", "age" : 5 }
    { "_id" : ObjectId("4c47b3372a9b2be866da2274"), "name" : "user6", "age" : 6 }
    { "_id" : ObjectId("4c47b3372a9b2be866da2275"), "name" : "user7", "age" : 7 }
    { "_id" : ObjectId("4c47b3372a9b2be866da2276"), "name" : "user8", "age" : 8 }
    { "_id" : ObjectId("4c47b3372a9b2be866da2277"), "name" : "user9", "age" : 9 }

    for u in db.users.find({"$where":"this.age > 7 || this.age < 3"}): print u
    # 显示如下：
    {u'age': 0.0, u'_id': ObjectId('4c47b3372a9b2be866da226e'), u'name': u'user0'}
    {u'age': 1.0, u'_id': ObjectId('4c47b3372a9b2be866da226f'), u'name': u'user1'}
    {u'age': 2.0, u'_id': ObjectId('4c47b3372a9b2be866da2270'), u'name': u'user2'}
    {u'age': 8.0, u'_id': ObjectId('4c47b3372a9b2be866da2276'), u'name': u'user8'}
    {u'age': 9.0, u'_id': ObjectId('4c47b3372a9b2be866da2277'), u'name': u'user9'}

    for u in db.users.find().where("this.age > 7 || this.age < 3"): print u
    # 显示如下：
    {u'age': 0.0, u'_id': ObjectId('4c47b3372a9b2be866da226e'), u'name': u'user0'}
    {u'age': 1.0, u'_id': ObjectId('4c47b3372a9b2be866da226f'), u'name': u'user1'}
    {u'age': 2.0, u'_id': ObjectId('4c47b3372a9b2be866da2270'), u'name': u'user2'}
    {u'age': 8.0, u'_id': ObjectId('4c47b3372a9b2be866da2276'), u'name': u'user8'}
    {u'age': 9.0, u'_id': ObjectId('4c47b3372a9b2be866da2277'), u'name': u'user9'}

    # 使用自定义的 function, javascript语法的
    for u in db.users.find().where("function() { return this.age > 7 || this.age < 3;}"): print u
    # 显示如下：
    {u'age': 0.0, u'_id': ObjectId('4c47b3372a9b2be866da226e'), u'name': u'user0'}
    {u'age': 1.0, u'_id': ObjectId('4c47b3372a9b2be866da226f'), u'name': u'user1'}
    {u'age': 2.0, u'_id': ObjectId('4c47b3372a9b2be866da2270'), u'name': u'user2'}
    {u'age': 8.0, u'_id': ObjectId('4c47b3372a9b2be866da2276'), u'name': u'user8'}
    {u'age': 9.0, u'_id': ObjectId('4c47b3372a9b2be866da2277'), u'name': u'user9'}
```