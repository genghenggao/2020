# MongoEngine

[TOC]

## 一、安装

```
python -m pip install mongoengine
```



## 二、实例

### 2.1简单实用

- 这里的Users即是collections名，与pymongo、djongo有所不同

```python
from mongoengine import connect
from mongoengine.document import Document
from mongoengine.fields import IntField, StringField


from mongoengine import *
connect('钻孔数据管理子系统', host='192.168.55.110', port=20000)

class Users(Document):
    name = StringField(required=True, max_length=200)
    age = IntField(required=True)

user1 = Users(
    name='zz',
    age=112
)
user1.save()
print(user1.name)
user1.name = 'zz11'
user1.save()
print(user1.name)

```



### 2.2使用指定数据库

- alias字段指定数据库

```python
from mongoengine import connect
from mongoengine.document import Document
from mongoengine.fields import IntField, StringField


from mongoengine import *
connect(alias='drill_system',db='钻孔数据管理子系统', host='192.168.55.110', port=20000)
connect(alias='rs_system',db='遥感数据管理子系统', host='192.168.55.110', port=20000)


class Users(Document):
    name = StringField(required=True, max_length=200)
    age = IntField(required=True)
    meta = {'db_alias': 'rs_system'}

user1 = Users(
    name='zz',
    age=112
)
user1.save()
print(user1.name)
user1.name = 'zz11'
user1.save()
print(user1.name)

```



### 2.3 切换数据库和集合

- 数据库

  ```
  with switch_db(User, 'archive-user-db') as User:
      User(name='Ross').save()  #  ===》 这时会将数据保存至 'archive-user-db'
  ```

- 集合

  ```
  with switch_collection(Group, 'group2000') as Group:
      Group(name='hello Group 2000 collection!').save()  # 将数据保存至 group2000 集合
  ```

  

- [ref](https://cloud.tencent.com/developer/article/1406578)

- [ref](https://www.cnblogs.com/zhenyauntg/p/13201826.html)



## 三、序列化

- 序列化需要专门的`django-rest-framework-mongoengine`

### 3.1、安装

```
pip install django-rest-framework-mongoengine
```



### 3.2、配置

- settings.py

  ```python
  INSTALLED_APPS = (
      ...
      'rest_framework',
      'rest_framework_mongoengine',
      ...
  )
  ```

  

- 参见[github](https://github.com/umutbozkurt/django-rest-framework-mongoengine)

- 使用参见文档：[API](http://umutbozkurt.github.io/django-rest-framework-mongoengine/)



### 3.3、实例

- models.py

    ```python
    class DrillLocation(Document):
        '''钻孔定位表'''
        name = StringField(required=True)
        locaton = ListField(required=True)
        meta = {'db_alias': 'drill_system'}
    ```

- serializers.py

  ```python
  from rest_framework_mongoengine.serializers import DocumentSerializer
  class DrillLocationSerializer(DocumentSerializer):
    '''钻孔数据管理子系统定位表数据'''
      class Meta:
          model = DrillLocation
          fields = "__all__"
  ```
  
- views.py

    ```python
            with switch_collection(DrillLocation, 'GeoJSON') as DrillLocationTest:
                docstest = DrillLocationTest.objects.all()
                print(docstest)
            ser = DrillLocationSerializer(instance=docstest, many=True)
                print(ser)   
    ```

    

### 四、空间查询