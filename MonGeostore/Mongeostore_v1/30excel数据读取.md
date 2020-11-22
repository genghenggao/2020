# Excel数据

[TOC]
## 常用工具

| 类型   | xlrd&xlwt&xlutils | XlsxWriter | OpenPyXL | Excel开放接口 |
| :----- | :---------------- | :--------- | :------- | :------------ |
| 读取   | 支持              | 不支持     | 支持     | 支持          |
| 写入   | 支持              | 支持       | 支持     | 支持          |
| 修改   | 支持              | 不支持     | 支持     | 支持          |
| xls    | 支持              | 不支持     | 不支持   | 支持          |
| xlsx   | 高版本支持        | 支持       | 支持     | 支持          |
| 大文件 | 不支持            | 支持       | 支持     | 不支持        |
| 效率   | 快                | 快         | 快       | 超慢          |
| 功能   | 较弱              | 强大       | 一般     | 超强大        |



## 一、安装模块

### xlrd & xlwt & xlutils 介绍

xlrd&xlwt&xlutils 顾明思意是由以下三个库组成：

- xlrd：用于读取 Excel 文件；
- xlwt：用于写入 Excel 文件；
- xlutils：用于操作 Excel 文件的实用工具，比如复制、分割、筛选等；

### 安装

```
pip install xlrd xlwt xlutils
```



## 二、Excel数据写入

```python
'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-05 18:31:26
LastEditors: henggao
LastEditTime: 2020-11-05 18:37:53
'''
# 导入 xlwt 库
import xlwt

# 创建 xls 文件对象
wb = xlwt.Workbook()

# 新增两个表单页
sh1 = wb.add_sheet('成绩')
sh2 = wb.add_sheet('汇总')

# 然后按照位置来添加数据,第一个参数是行，第二个参数是列
# 写入第一个sheet
sh1.write(0, 0, '姓名')
sh1.write(0, 1, '成绩')
sh1.write(1, 0, '张三')
sh1.write(1, 1, 88)
sh1.write(2, 0, '李四')
sh1.write(2, 1, 99.5)

# 写入第二个sheet
sh2.write(0, 0, '总分')
sh2.write(1, 0, 187.5)

# 最后保存文件即可
wb.save('./mongeostore_env/upload/data_w.xls')

```



## 三、Excel数据读取

```python
'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-05 18:22:11
LastEditors: henggao
LastEditTime: 2020-11-05 18:39:09
'''
# 导入 xlrd 库
import xlrd

# 打开刚才我们写入的 test_w.xls 文件
wb = xlrd.open_workbook('./mongeostore_env/upload/data_w.xls')

# 获取并打印 sheet 数量
print("sheet 数量:", wb.nsheets)

# 获取并打印 sheet 名称
print("sheet 名称:", wb.sheet_names())

# 根据 sheet 索引获取内容
sh1 = wb.sheet_by_index(0)
# 或者
# 也可根据 sheet 名称获取内容
# sh = wb.sheet_by_name('成绩')

# 获取并打印该 sheet 行数和列数
print(u"sheet %s 共 %d 行 %d 列" % (sh1.name, sh1.nrows, sh1.ncols))

# 获取并打印某个单元格的值
print("第一行第二列的值为:", sh1.cell_value(0, 1))

# 获取整行或整列的值
rows = sh1.row_values(0)  # 获取第一行内容
cols = sh1.col_values(1)  # 获取第二列内容

# 打印获取的行列值
print("第一行的值为:", rows)
print("第二列的值为:", cols)

# 获取单元格内容的数据类型
print("第二行第一列的值类型为:", sh1.cell(1, 0).ctype)

# 遍历所有表单内容
for sh in wb.sheets():
    for r in range(sh.nrows):
        # 输出指定行
        print(sh.row(r))

```



## 四、修改 excel

- 格式转换操作

```python
# 导入 xlwt 库
import xlwt

# 设置写出格式字体红色加粗
styleBR = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')

# 设置数字型格式为小数点后保留两位
styleNum = xlwt.easyxf(num_format_str='#,##0.00')

# 设置日期型格式显示为YYYY-MM-DD
styleDate = xlwt.easyxf(num_format_str='YYYY-MM-DD')

# 创建 xls 文件对象
wb = xlwt.Workbook()

# 新增两个表单页
sh1 = wb.add_sheet('成绩')
sh2 = wb.add_sheet('汇总')

# 然后按照位置来添加数据,第一个参数是行，第二个参数是列
sh1.write(0, 0, '姓名', styleBR)   # 设置表头字体为红色加粗
sh1.write(0, 1, '日期', styleBR)   # 设置表头字体为红色加粗
sh1.write(0, 2, '成绩', styleBR)   # 设置表头字体为红色加粗

# 插入数据
sh1.write(1, 0, '张三',)
sh1.write(1, 1, '2019-01-01', styleDate)
sh1.write(1, 2, 88, styleNum)
sh1.write(2, 0, '李四')
sh1.write(2, 1, '2019-02-02')
sh1.write(2, 2, 99.5, styleNum)

# 设置单元格内容居中的格式
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
style = xlwt.XFStyle()
style.alignment = alignment

# 合并A4,B4单元格，并将内容设置为居中
sh1.write_merge(3, 3, 0, 1, '总分', style)

# 通过公式，计算C2+C3单元格的和
sh1.write(3, 2, xlwt.Formula("C2+C3"))

# 对 sheet2 写入数据
sh2.write(0, 0, '总分', styleBR)
sh2.write(1, 0, 187.5)

# 最后保存文件即可
wb.save('test_w3.xls')
```



- [ref](http://www.ityouknow.com/python/2019/12/29/python-excel-103.html)



## 五、Excel转Json

```

```

- [ref](https://blog.csdn.net/hhl_work/article/details/105518367?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-8.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-8.edu_weight)



## 六、Excel导入MongoDB

```python
'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-11-05 19:25:23
LastEditors: henggao
LastEditTime: 2020-11-05 20:09:37
'''
import xlrd
import json
import pymongo

# 连接数据库

client = pymongo.MongoClient("192.168.55.110", 20000)
mydb = client['segyfile']
info = mydb['excel_data']
# 读取Excel文件
data = xlrd.open_workbook('./mongeostore_env/upload/data_w.xls')
# 选择上传的sheet，注意字段
table = data.sheets()[2]
# 读取excel第一行数据作为存入mongodb的字段名
rowstag = table.row_values(0)
nrows = table.nrows
returnData = {}


for i in range(1, nrows):
    # 将字段名和excel数据存储为字典形式，并转换为json格式
    returnData[i] = json.dumps(dict(zip(rowstag, table.row_values(i))))
    # 通过编解码还原数据
    returnData[i] = json.loads(returnData[i])
    print(returnData[i])
    info.insert(returnData[i])

```

- [ref1](https://blog.csdn.net/stormdony/article/details/80785408)

- [ref2](https://blog.csdn.net/weixin_34218890/article/details/94183181?utm_medium=distribute.pc_relevant.none-task-blog-title-3&spm=1001.2101.3001.4242)



## 七、MongoDB数据下载到Excel

### 1、安装`openpyxl` 

```
pip install openpyxl 
```

### 2、MongoDB数据下载到Excel

```python
from openpyxl import Workbook
import pymongo


# 读取mongoDB数据库相应的表，每条数据取出数个字段存入一个dict，再将所有的dict存入一个list
def read_mongoDB():
    # 连接mongoDB数据库，读取 db 库 table 表中的数据
    client = pymongo.MongoClient("192.168.55.110", 20000)
    db = client['segyfile']
    table = db['excel_data']

    # 创建list用于存储从mongoDB中读取到的数据
    mongo_data_list = []
    # 从table中读取的数据为整个documents内容
    documents = table.find()
    # 遍历 documents 表中的每一个document
    for document in documents:
        # 创建dict用于存储各条数据的各个字段名称及内容
        mongo_data_dict = {}
        rid = document.get("rid")
        vip = document.get("vip")
        rank = document.get("?rank")
        costMoney = document.get("costMoney")
        # 将查询到的的数据字段内容以更新添加的方式添加到每个dict中
        mongo_data_dict.update({"rid": rid})
        mongo_data_dict.update({"vip": vip})
        mongo_data_dict.update({"rank": rank})
        mongo_data_dict.update({"costMoney": costMoney})
        print("mongo_data_dict:", mongo_data_dict)
        mongo_data_list.append(mongo_data_dict)
        # print("mongo_data_dict:", mongo_data_list)
    return mongo_data_list


# 保存至本地excel表格
def save_to_excel(mongoDB_data):
    outwb = Workbook()
    outws = outwb.worksheets[0]
    # 字段写入
    header_list = ["rid", "vip", "rank", "costMoney"]
    outws.append(header_list)
    # 遍历外层列表
    for new_dict in mongoDB_data:
        a_list = []
        # 遍历内层每一个字典dict，把dict每一个值存入list
        for item in new_dict.values():
            print(item)
            a_list.append(item)
            print(a_list)
        # sheet直接append list即可
        outws.append(a_list)

    outwb.save(r'./mongeostore_env/upload/excel_data.xlsx')
    print('数据存入excel成功')


def main():
    mongoDB_data = read_mongoDB()
    # print(mongoDB_data)
    save_to_excel(mongoDB_data)


if __name__ == '__main__':
    main()

```

- [ref](https://blog.csdn.net/xiabocs/article/details/102498417?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-3.edu_weight)

### 3、优化版

- 可以写个循环，获取数据库中所有关键字。优化版

```python
from openpyxl import Workbook
import pymongo


# 读取mongoDB数据库相应的表，每条数据取出数个字段存入一个dict，再将所有的dict存入一个list
# def read_mongoDB():
    # 连接mongoDB数据库，读取 db 库 table 表中的数据
client = pymongo.MongoClient("192.168.55.110", 20000)
db = client['segyfile']
table = db['excel_data']

# 创建list用于存储从mongoDB中读取到的数据
mongo_data_list = []
# 从table中读取的数据为整个documents内容
documents = table.find()
# print(documents[1].keys())
list_keys = documents[1].keys()
# print(list_keys)
# 遍历 documents 表中的每一个document
for document in documents:
    # 创建dict用于存储各条数据的各个字段名称及内容
    # print(document.keys())
    mongo_data_dict = {}
    for list_key in list_keys:
        print(list_key)
        list_key_tmp = document.get(str(list_key))
        # 为了处理ObjectId
        if list_key == "_id":
            list_key_tmp = str(list_key_tmp)
        mongo_data_dict.update({str(list_key): list_key_tmp})
    # rid = document.get("rid")
    # vip = document.get("vip")
    # rank = document.get("?rank")
    # costMoney = document.get("costMoney")
    # 将查询到的的数据字段内容以更新添加的方式添加到每个dict中
    # mongo_data_dict.update({"rid": rid})
    # mongo_data_dict.update({"vip": vip})
    # mongo_data_dict.update({"rank": rank})
    # mongo_data_dict.update({"costMoney": costMoney})
    print("mongo_data_dict:", mongo_data_dict)
    mongo_data_list.append(mongo_data_dict)
    # print("mongo_data_dict:", mongo_data_list)
    # return mongo_data_list


# 保存至本地excel表格
# def save_to_excel(mongoDB_data):
outwb = Workbook()
outws = outwb.worksheets[0]
# 字段写入
# header_list = ["rid", "vip", "rank", "costMoney"]
header_list = list(list_keys)
# print(type(header_list))
outws.append(header_list)
# 遍历外层列表
for new_dict in mongo_data_list:
    a_list = []
    # 遍历内层每一个字典dict，把dict每一个值存入list
    for item in new_dict.values():
        # print(item)
        a_list.append(item)
        # print(a_list)
    # sheet直接append list即可
    outws.append(a_list)

outwb.save(r'./mongeostore_env/upload/excel_data.xlsx')
print('数据存入excel成功')


# def main():
#     mongoDB_data = read_mongoDB()
#     # print(mongoDB_data)
#     save_to_excel(mongoDB_data)


# if __name__ == '__main__':
#     main()

```

- **注意点**

  - 字典(Dictionary) keys() 函数以列表返回一个字典所有的键

    ```
    list_keys = documents[1].keys()
    ```

    

  - ObjectId

    ```
     # 为了处理ObjectId
            if list_key == "_id":
                list_key_tmp = str(list_key_tmp)
    ```

    

  - dict.keys()转换成list类型

    ```
    header_list = list(list_keys)
    ```

    