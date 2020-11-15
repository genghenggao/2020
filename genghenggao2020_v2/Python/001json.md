# Python与JSON

[TOC]

## 1、对应关系

### 1.1 编码时

| Python数据类型                          | JSON数据类型 |
| --------------------------------------- | ------------ |
| dict                                    | object       |
| list、tuple                             | array        |
| str                                     | string       |
| int、float、int、派生的int和float的Enum | number       |
| True                                    | true         |
| False                                   | false        |
| None                                    | null         |
|                                         |              |



### 1.2 解码时

| JSON类型       | Python类型 |
| :------------- | :--------- |
| object         | dict       |
| array          | list       |
| string         | str        |
| number（int）  | int        |
| number（real） | float      |
| true           | True       |
| false          | False      |
| null           | None       |



## 2、转换

Python中，json数据与dict字典以及对象之间的转化，是必不可少的操作。

Python中自带json库。通过`import json`导入。

在json模块有如下方法，

1. `loads()`：将json数据转化成dict数据
2. `dumps()`：将dict数据转化成json数据
3. `load()`：读取json文件数据，转成dict数据
4. `dump()`：将dict数据转化成json数据后写入json文件

`dump()`将dict转成json字符串，然后存入文件中；而`dumps()`直接将字典dict转为json字符串

------

dict字典转json字符串：

```python
import json

def dict_to_json():

    dict = {}
    dict['name'] = 'many'
    dict['age'] = 10
    dict['sex'] = 'male'
    print type(dict),dict  
    # 输出：<type 'dict'> {'age': 10, 'name': 'many', 'sex': 'male'}

    json_data = json.dumps(dict)
    print type(json_data),json_data 
    # 输出：<type 'str'> {"age": 10, "name": "many", "sex": "male"}
    
if __name__ == '__main__':
    dict_to_json()
```

json字符串转成dict字典

```python
import json
def json_to_dict():
    j = '{"id": "007", "name": "007", "age": 28, "sex": "male", "phone": "13000000000", "email": "123@qq.com"}'

    dict = json.loads(j)
    print type(dict),dict 
#<type 'dict'> {u'name': u'007', u'age': 28, u'sex': u'male', u'phone': u'13000000000', u'email': u'123@qq.com', u'id': u'007'}

if __name__ == '__main__':
    json_to_dict()
```

 json的`load()`与`dump()`方法的使用:

`dump()`方法将dict数据转化成json数据后写入json文件

```python
import json

def dict_to_json_write_file():
    dict = {}
    dict['name'] = 'many'
    dict['age'] = 10
    dict['sex'] = 'male'
    print(dict)  # 输出：{'age': 10, 'name': 'many', 'sex': 'male'}

    with open('1.json', 'w') as f:
        json.dump(dict, f)  # 会在目录下生成一个1.json的文件，文件内容是dict数据转成的json字符串

if __name__ == '__main__':

    dict_to_json_write_file()
```

`load()`读取json文件数据，转成dict数据

```python
import json

def json_file_to_dict():

    with open('1.json', 'r') as f:
        dict = json.load(f)
        print(dict)  # {'name': 'many', 'age': 10, 'sex': 'male'}

if __name__ == '__main__':

    json_file_to_dict()
```