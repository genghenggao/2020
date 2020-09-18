# DRF

[TOC]



## 1、初识DRF

基于django可以实现遵循restful规范的接口开发：

- FBV，可以实现比较麻烦。
- CBV，相比较简答根据method做的了不同的区分。

### 1.1 安装

```
pip install djangorestframework
```



### 1.2 使用

- 注册app,`settings.py`

  ```python
  # Application definition
  
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  
      # myapp
      'rest_framework',
      'mongeostore_app',
      'captcha',
  ]
  ```

- 写路由`urls.py`

  ```
  from mongeostore_app import views
  from django.urls import path
  urlpatterns = [
      path('register/', views.RegisterView.as_view(), name='register'),
  ]
  ```

- 写视图`views.py`

  - Django	--> View
  - DRF        -->  APIView

  ```
  
  ```

  

## 2、DRF的应用场景

前后端分离项目、参与app写接口，用drf比较方便。

- restful规范

  ```
  1、根据url请求方式的不同，做不同操作
  	get 
  	post
  	put
  	patch
  	delete
  2、数据传输基于json格式
  ```

  

- drf框架

  - 不基于drf也可以实现restful规范来开发接口
  - 使用drf，可以快速帮助开发restful规范开发接口

  