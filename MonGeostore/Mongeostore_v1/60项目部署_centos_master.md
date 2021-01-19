# CentOS部署

[TOC]

## 1. 如何一键安装所有第三方库文件？

### 1.1 pip freeze

在查看Python 项目时，经常会看到一个 `requirements.txt` 文件，里面记录了当前程序的所有依赖包及其精确版本号。这个文件有点类似与 Rails 的 Gemfile。其作用是用来在另一台 PC 上重新构建项目所需要的运行环境依赖。

`requirements.txt` 用来记录项目所有的依赖包和版本号，只需要一个简单的 pip 命令就能完成。

进入到需要导出所有 Python 库的那个环境，然后使用那个环境下的 pip ：

```
pip freeze > requirements.txt
```

> requirement.txt 文件默认输出在桌面

然后就可以用：

```
pip install -r requirements.txt
```

来一次性安装 `requirements.txt` 里面所有的依赖包，真是非常方便。

- [ref](https://github.com/tgz0514/DeepLearning_Notes_CV/blob/master/other/Python/Python%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%E6%89%80%E6%9C%89%E7%AC%AC%E4%B8%89%E6%96%B9%E5%BA%93.md)



## 二、Vue+Django+Nginx+uWSGI部署生产环境 前后端分离

- MongoDB在CentOS中部署
- 前后端以后可以采取Docker容器模式开发（）