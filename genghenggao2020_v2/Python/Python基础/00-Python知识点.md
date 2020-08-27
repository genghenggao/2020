# Python知识点

[TOC]

## 一、知识点

### 1、变量的命名和使用

- 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打 头。

- 使用符合标准 Python 约定的文件名：使用小写字母和下划线，

## 二、注意点

`input` 方法接收到的所有数据都是字符串形式。可以通过int将字符串转换为数字类型。

```python
print("Welcome to use your first programme")
name = input("your name :")
age = int(input("your age :"))
sex = input("your sex :")

msg = '''
--------Personal Info --------
your name : %s
your age : %d
your sex : %s
-------------End--------------
''' %(name, age, sex)

print(msg)
if age > 20:
    print("you need to learn more")
else:
    print("Yes, you can pass")
```

## 三、pip安装

1、pip install *** 安装路径查看：

```shell
python -m site
```

参考：https://blog.csdn.net/mukvintt/article/details/80908951

2、pip install ***安装报错

- 问题：

```
socket.timeout: The read operation timed out
```

- 分析原因：

  pip安装python包，一般是由于网速不稳定，下载过慢，超出默认时间，所以只要修改一下响应时间就好了。

- 解决方法一:

  ```shell
  #windows下输入 
  pip --default-timeout=100 install 包名
  #linux下输入 
  pip --default-timeout=100 install -U 包名
  ```

- 解决方法二：（建议使用）

- 1、可以使用清华源

  ```shell
  pip --default-timeout=100 install -i https://pypi.tuna.tsinghua.edu.cn/simple some-packages
  ```

- 2、可以使用豆瓣源

  ```shell
  pip install -i https://pypi.douban.com/simple some-packages
  ```

  