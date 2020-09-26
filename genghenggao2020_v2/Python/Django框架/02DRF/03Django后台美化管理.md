

# 四大Django admin 第三方后台美化应用

[TOC]

## 1.Xadmin

Xadmin 在 Django 后台管理系统应用库中算是名声显赫。它算是一款内置功能比较丰富的框架，提供了基本的CRUD功能，还内置了丰富的插件功能；还包括数据导出、书签、图表、数据添加向导及图片相册等多种扩展功能。 最重要的是，它使用起来非常方便。我们只需要定义数据的字段等信息，即可获取一个功能全面的管理系统。

推荐指数：5 星

django1.x: https://github.com/sshwsfc/xadmin/

django2: https://github.com/sshwsfc/xadmin/tree/django2

详情参考我的这篇文章： [Django2集成xadmin](http://ertao.xyz/info/23/)

## 2.django-grappelli

django-grappelli 可以算是一个功能强大的应用。它使用网格状的形式来呈现数据，这个给人简洁大方的感觉。因此，django-grappelli 更加适合需要对数据频繁操作的场景。

推荐指数：4 星

**github 地址**： https://github.com/sehmaschine/django-grappelli/

## 3.django-material

django-material 是采用谷歌 Material Design 来设置 UI 。自己比较喜欢 MD 这种风格的界面，所以推荐给大家。

推荐指数：3 星半

**github 地址：** https://github.com/viewflow/django-material

## 4.django-admin-bootstrap

django-admin-bootstrap 是一个能自动隐藏侧面菜单栏的响应式管理后台。它跟 Xadmin 一样，都是基于 bootstrap 开发的。个人觉得比较适合初学者来学习和研究。

推荐指数：3 星

**github 地址**： https://github.com/douglasmiranda/django-admin-bootstrap



## 5.django-simpleui 

关于simpleui的使用，提供了很多主题可以使用，相对于xadmin也比较简单：

1. 安装simpleui:
   命令 ：pip install django-simpleui
2. 将simpleui注册到自己的项目中:

```
#在第一行中加入
INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'articles',
]
```

除此之外不需要改动其他代码

3. 运行项目，打开浏览器输入[后台管理 http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/):
   登录并进入后台管理界面





## 6、vue-element-admin

参考这个开发教程

## 7、富文本编辑器

- vue-quill-editor
- [几款主流好用的富文本编辑器（所见即所得常用编辑器）介绍](https://www.cnblogs.com/1175429393wljblog/p/12626157.html)

