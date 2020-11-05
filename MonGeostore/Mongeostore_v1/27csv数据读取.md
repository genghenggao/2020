

# CSV数据读取

[TOC]

## 1、通过URL读取

```python
'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-04 08:52:02
LastEditors: henggao
LastEditTime: 2020-11-04 08:59:04
'''
import requests
import csv
from contextlib import closing

'''
通过url读取csv
'''
# 文件地址
url = "http://snk-gm.hz.37.com.cn/downloads/rankshow/20191205/snk_Rugal_1006_44_1575532733_COST_MONEY_20191204050000.csv"

# 读取数据
with closing(requests.get(url, stream=True)) as r:
    f = (line.decode('gbk') for line in r.iter_lines())
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        print(row)
```



- with contextlib.closing()与with open()

  - closing 适用于提供了 close() 实现的对象，比如网络连接、数据库连接等，
  - [ref](https://blog.csdn.net/emaste_r/article/details/78105713)



## 2、使用Pandas进行CSV读取

- [ref](https://blog.csdn.net/lucky_shi/article/details/105321149?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight)



## 3、读取cvs文件并写入mongodb

```python
'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-04 10:47:36
LastEditors: henggao
LastEditTime: 2020-11-04 11:05:55
'''
from pymongo import MongoClient
import csv
# 创建连接MongoDB数据库函数


def connection():
    # 1:连接MongoDB数据库
    conn = MongoClient("192.168.55.110", 20000)
    # 2:连接数据库(segyfile)。没有时会自动创建
    db = conn.segyfile
    # 3:创建集合
    set1 = db.data
    # 4:看情况是否选择清空(两种清空方式，第一种不行的情况下，选择第二种)
    # 第一种直接remove
    set1.remove(None)
    # 第二种remove不好用的时候
    # set1.delete_many({})
    return set1


def insertToMongoDB(set1):
    # 打开文件guazi.csv
    with open('./mongeostore_env/upload/test.csv', 'r', encoding='utf-8')as csvfile:
        # 调用csv中的DictReader函数直接获取数据为字典形式
        reader = csv.DictReader(csvfile)
        # 创建一个counts计数一下 看自己一共添加了了多少条数据
        counts = 0
        for each in reader:
            # 将数据中需要转换类型的数据转换类型。原本全是字符串（string）。
            each['?rank'] = int(each['?rank'])
            each['costMoney'] = float(each['costMoney'])
            each['combat'] = float(each['combat'])
            each['topHeroesCombat'] = int(each['topHeroesCombat'])
            # each['表显里程'] = float(each['表显里程'])
            # each['排量'] = float(each['排量'])
            # each['过户数量'] = int(each['过户数量'])
            set1.insert(each)
            # set1.insert_one(each)
            counts += 1
            print('成功添加了'+str(counts)+'条数据 ')
# 创建主函数


def main():
    set1 = connection()
    insertToMongoDB(set1)


# 判断是不是调用的main函数。这样以后调用的时候就可以防止不会多次调用 或者函数调用错误
if __name__ == '__main__':
    main()

```

- [ref1](https://blog.csdn.net/qq_43389959/article/details/83240988)
- [ref2](https://blog.csdn.net/xiaoQL520/article/details/77246902?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight)



## 4、如何改变CSV文件的编码

- 读取含有中文的csv文件的时候常常遇到编码错误，因此就想把csv文件编码改为utf-8编码方式，用excel打开另存为utf-8格式没法解决问题：

  首先，将.csv文件保存一下，然后鼠标右击打开方式记事本。然后，以记事本的方式打开了。文件-另存为 这时弹出一个窗口，右下方，编码，这时候你就可以选择自己想要的编码格式，然后保存，就可以了。



## 5、读取mongoDB写入csv文件

```python
'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-04 11:16:50
LastEditors: henggao
LastEditTime: 2020-11-04 14:28:30
'''
import pymongo
import codecs
import csv

client = pymongo.MongoClient("192.168.55.110", 20000)
database = "segyfile"
db = client[database]
collection = "data"
db_coll = db[collection]
with codecs.open('./mongeostore_env/upload/data.csv', 'w', 'utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # 这里我就给了2个字段名，如果你要输出更多的字段，继续后面添加
    writer.writerow(['rid', 'vip'])
    # 第一个{}实际上是筛选数据的若干条件，我这里没给条件，所以直接给的一个空的大括号
    # 后面的字典则是mongo中的字段名，你想筛选的字段
    for d in db_coll.find({}, {'rid': True, 'vip': True}):
        writer.writerows([[d['rid'], d['vip']]])
```



## 六、可序列化的格式

Djanggo支持三种序列化格式，其中的一些可能需要安装第三方库支持：

- xml
- json
- yaml