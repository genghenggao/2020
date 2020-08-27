# Python基础

[TOC]



## 列表



## 元组

- 不能修改元组的元素，但可以给存储元组的变量赋值。

  ```python
  >>> dimensions = (10,23)
  >>> print("Original dimensions:")
  Original dimensions:
  >>> for dimension in dimensions:
  ...  print(dimension)
  ...
  10
  23
  >>> dimensions = (10,28)
  >>> for dimension in dimensions:
  ...      print(dimension)
  ...
  10
  28
  ```

  

## 格式

- PEP 8建议每级缩进都使用四个空格。
- 很多Python程序员都建议每行不超过80字符。
- PEP 8还建议 注释的行长都不超过72字符



## 检查特定值是否包含在列表中

- 要判断特定的值是否已包含在列表中，可使用关键字in。
- 要判断特定的值不包含在列表中，使用关键字not in。



## if语句

- PEP 8提供的唯一 建议是，在诸如==、>=和<=等比较运算符两边各添加一个空格。

```python
if conditional_test:
 do something 
```



## if-else 语句



## if-elif-else 结构



- 如果你只想执行一个代码块，就使用if-elif-else结构；如果要运行多个代码块，就 使用一系列独立的if语句。



## 字典

- Python不关心键—值对的添加顺序， 而只关心键和值之间的关联关系。

- 使用del语句时， 必须指定字典名和要删除的键。

  ```python
  for key,value in favorite_languages.keys.items(): 
  ```

  ```python
  for name in favorite_languages.keys(): 
  ```

  

- 为剔除重复项，可使用集合（set）。



## input

- 有时候，提示可能超过一行，例如，你可能需要指出获取特定输入的原因。在这种情况下， 可将提示存储在一个变量中，再将该变量传递给函数input()。这样，即便提示超过一行，input() 语句也非常清晰。
- 使用函数input()时，Python将用户输入解读为字符串。



## 函数

- 要将列表的副本传递给函数，可以像下面这样做： 

  ```
  function_name(list_name[:])
  ```

- 切片表示法[:]创建列表的副本。

- 形参**user_info中的两个星号让Python创建一个名为user_info的空字典，

## Random

```python
import random

n = random.randint(0, 100)

user_guess = int(input("input your guess : "))

if user_guess > n:
    print("try smaller")
elif user_guess < n:
    print("try bigger")
else:
    print("Bingo ,you get it")

print(n)

```

## Type



## Format

```python
s = "Welcome {name} , You're a {job} "
print(s.format(name = "Eva", job = "Student")) 
#输出 Welcome Eva , You're a Student 
```

