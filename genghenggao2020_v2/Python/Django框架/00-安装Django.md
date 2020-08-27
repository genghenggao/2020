# 安装Django

- 方法一:（比较慢）

  最简单的，但汇报超时错误

  ```shell
  pip install Django
  ```

  加上下面，可以解决，但也比较慢。

  ```shell
  #windows下输入 
  pip --default-timeout=100 install Django
  #linux下输入 
  pip --default-timeout=100 install -U Django
  ```

- 解决方法二：（建议使用）

- 1、可以使用清华源

  ```shell
  pip --default-timeout=100 install -i https://pypi.tuna.tsinghua.edu.cn/simple Django
  ```

- 2、可以使用豆瓣源

```shell
pip install -i https://pypi.douban.com/simple Django
```

