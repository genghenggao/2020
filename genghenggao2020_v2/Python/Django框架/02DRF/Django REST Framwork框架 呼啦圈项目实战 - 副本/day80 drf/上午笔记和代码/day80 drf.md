# day80 drf

drf，django rest framewok

## 第一部分 问题

1. 前后端分离？

   - vue.js
   - 后端给前段返回json数据

2. 移动端盛行。

   - app
   - 后端给app返回json数据

3. PC端应用？

   ```
   crm项目，前段后端一起写，运行在浏览器上。 一般情况下都是PC端使用。 
   ```

   

## 第二部分 任务

以前的我们 ：

```
http://127.0.0.1:8000/info/get/
http://127.0.0.1:8000/info/add/
http://127.0.0.1:8000/info/update/
http://127.0.0.1:8000/info/delete/
```

现在的我们：要遵循restful规范

```
http://127.0.0.1:8000/info/
	get,获取数据
	post，添加
	put，更新
	delete，删除
```

基于django可以实现遵循restful规范的接口开发：

- FBV，可以实现比较麻烦。
- CBV，相比较简答根据method做的了不同的区分。

## 第三部分  初识drf

### 3.1 安装

```
pip3 install djangorestframework
```

### 3.2 使用

- 注册app

  ```
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'rest_framework'
  ]
  ```

- 写路由

  ```
  from django.conf.urls import url
  from django.contrib import admin
  from api import views
  
  urlpatterns = [
      url(r'^drf/info/', views.DrfInfoView.as_view()),
  ]
  
  ```

- 写视图

  ```
  from rest_framework.views import APIView
  from rest_framework.response import Response
  
  class DrfInfoView(APIView):
  
      def get(self,request,*args,**kwargs):
          data = [
              {'id': 1, 'title': '震惊了...王阳居然...', 'content': '...'},
              {'id': 2, 'title': '震惊了...王阳居然...', 'content': '...'},
              {'id': 3, 'title': '震惊了...王阳居然...', 'content': '...'},
              {'id': 4, 'title': '震惊了...王阳居然...', 'content': '...'},
          ]
          return Response(data)
  ```

### DRF的应用场景

```
以后在公司参与前后端分离项目、参与为app写接口时，用drf会比较方便。
```



## 总结

- restful规范

  ```
  1.给别人提供一个URL，根据URL请求方式的不同，做不同操作。
  	get,获取
  	post,增加
  	put，全部更新
  	patch,局部更新
  	delete,删除
  2.数据传输基于json格式。
  ```

- drf框架

  ```
  不基于drf也可以实现restful规范来开发接口程序。
  
  使用了drf之后，可以快速帮我们开发restful规范来开发接口。
  ```

  



## 第四部分 

### 4.1 创建程序并初始化数据库

### 4.2 接口：实现访问接口时，创建一个文章类型

```python
from django.conf.urls import url
from django.contrib import admin
from api import views
urlpatterns = [
    url(r'^drf/category/', views.DrfCategoryView.as_view()),
]

```

```python
from rest_framework.views import APIView
from rest_framework.response import Response
class DrfCategoryView(APIView):
	pass
```

假设：我是前段，你是后端。

开发完毕之后告诉前端：

```
http://127.0.0.1:8000/drf/category/
```

用工具模拟前端发请求：postman



x-www-urlencoded

```
request.body: name=alex&age=19&gender=12
request.POST: {'name': ['alex'], 'age': ['19'], 'gender': ['12']}
```

json

```
request.body: b'{"ID":1,"name":"Alex","age":19}'
request.POST: 没有值
```

#### 参考答案

```
from django.conf.urls import url
from django.contrib import admin
from api import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^info/', views.InfoView.as_view()),
    url(r'^drf/info/', views.DrfInfoView.as_view()),
    url(r'^drf/category/', views.DrfCategoryView.as_view()),
]

```

```
from api import models
class DrfCategoryView(APIView):

    def post(self,request,*args,**kwargs):
        """增加一条分类信息"""
        models.Category.objects.create(**request.data)
        return Response('成功')

```

![1572921773684](C:\Users\Administrator\Desktop\1572921773684.png)

### 4.3 接口：获取所有文章类型

```
from api import models
class DrfCategoryView(APIView):
    def get(self,request,*args,**kwargs):
        """获取所有文章分类"""
        queryset = models.Category.objects.all().values('id','name')
        data_list = list(queryset)
        return Response(data_list)

    def post(self,request,*args,**kwargs):
        """增加一条分类信息"""
        models.Category.objects.create(**request.data)
        return Response('成功')
```

### 4.4 接口：获取一条文章类型的详细信息

```
from django.conf.urls import url
from django.contrib import admin
from api import views
urlpatterns = [
    url(r'^drf/category/$', views.DrfCategoryView.as_view()),
    url(r'^drf/category/(?P<pk>\d+)/$', views.DrfCategoryView.as_view()),
]

```

```python
from api import models
from django.forms.models import model_to_dict
class DrfCategoryView(APIView):
    def get(self,request,*args,**kwargs):
        """获取所有文章分类/单个文章分类"""
        pk = kwargs.get('pk')
        if not pk:
            queryset = models.Category.objects.all().values('id','name')
            data_list = list(queryset)
            return Response(data_list)
        else:
            category_object = models.Category.objects.filter(id=pk).first()
            data = model_to_dict(category_object)
            return Response(data)

    def post(self,request,*args,**kwargs):
        """增加一条分类信息"""
        models.Category.objects.create(**request.data)
        return Response('成功')

```

![1572923696692](C:\Users\Administrator\Desktop\1572923696692.png)



### 4.5 接口：文章分类的更新和删除

```
from django.conf.urls import url
from django.contrib import admin
from api import views
urlpatterns = [
    url(r'^drf/category/$', views.DrfCategoryView.as_view()),
    url(r'^drf/category/(?P<pk>\d+)/$', views.DrfCategoryView.as_view()),
]

```

```
from api import models
from django.forms.models import model_to_dict
class DrfCategoryView(APIView):
    def get(self,request,*args,**kwargs):
        """获取所有文章分类/单个文章分类"""
        pk = kwargs.get('pk')
        if not pk:
            queryset = models.Category.objects.all().values('id','name')
            data_list = list(queryset)
            return Response(data_list)
        else:
            category_object = models.Category.objects.filter(id=pk).first()
            data = model_to_dict(category_object)
            return Response(data)

    def post(self,request,*args,**kwargs):
        """增加一条分类信息"""
        models.Category.objects.create(**request.data)
        return Response('成功')

    def delete(self,request,*args,**kwargs):
        """删除"""
        pk = kwargs.get('pk')
        models.Category.objects.filter(id=pk).delete()
        return Response('删除成功')

    def put(self,request,*args,**kwargs):
        """更新"""
        pk = kwargs.get('pk')
        models.Category.objects.filter(id=pk).update(**request.data)
        return Response('更新成功')
```



## 第五部分 drf的序列化

drf的 serializers帮助我们提供了

- 数据校验
- 序列化

```
from django.conf.urls import url
from django.contrib import admin
from api import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^info/$', views.InfoView.as_view()),
    url(r'^drf/info/$', views.DrfInfoView.as_view()),
    url(r'^drf/category/$', views.DrfCategoryView.as_view()),
    url(r'^drf/category/(?P<pk>\d+)/$', views.DrfCategoryView.as_view()),


    url(r'^new/category/$', views.NewCategoryView.as_view()),
    url(r'^new/category/(?P<pk>\d+)/$', views.NewCategoryView.as_view()),
]

```

```python
from rest_framework import serializers

class NewCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        # fields = "__all__"
        fields = ['id','name']

class NewCategoryView(APIView):
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        if not pk:
            queryset = models.Category.objects.all()
            ser = NewCategorySerializer(instance=queryset,many=True)
            return Response(ser.data)
        else:
            model_object = models.Category.objects.filter(id=pk).first()
            ser = NewCategorySerializer(instance=model_object, many=False)
            return Response(ser.data)

    def post(self,request,*args,**kwargs):
        ser = NewCategorySerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def put(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        category_object = models.Category.objects.filter(id=pk).first()
        ser = NewCategorySerializer(instance=category_object,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def delete(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        models.Category.objects.filter(id=pk).delete()
        return Response('删除成功')
```





## 总结



1. 什么是前后端分离？

2. drf组件

   ```
   帮助们在django框架基础上快速搭建遵循restful规范接口的程序。
   ```

3. drf组件的功能

   - 解析器，解析请求体中的数据，将其变成我们想要的格式。request.data
   - 序列化，对对象或对象列表（queryset）进行序列化操作以及表单验证的功能。
   - 视图，继承APIView（在内部apiview继承了django的View）

4. postman

   ```
   模拟浏览器进行发送请求
   ```

5. 查找模板的顺序

   ```
   优先根目录下：templates
   根据app的注册顺序去每个app的templates目录中找。
   ```

6. 在URL的最后添加终止符



## 作业：对文章表做增删改查



























































