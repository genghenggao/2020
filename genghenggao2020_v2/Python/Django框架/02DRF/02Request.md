# Request



## 测试工具

- postman
  - 模拟前端给后端发送数据
  
    

## Request.data

- Django中只有`request.body`和`request.POST`。

- DRF中才有`request.data`

- `x-www-form-urlencoded`

  ```
  request.body  name=alex&age=19&gender=1
  request.POST	{'name': ['alex'], 'age': ['19'], 'gender': ['12']}
  ```

- json

  ```
  request.body  b'{"ID":1,"name":"Alex","age":19}'
  request.POST 没有值
  ```

  





解析器：根据用户格式不同进行数据解析

- content-type：x-www-lenco
- 序列化
- 渲染器
  - 可以帮助   我们将json数据渲染到页面上进行友好展示



面向对象的继承



2、分页

视图

```python
class pageArticleView(APIView):
	def get(self,request,*args，**kwargs)：
		queryset = models.Artcile.objects.all()
        
        
```

系统架构

cssm vue+drf

功能实现

- APIView

- GenericAPIView，桥梁 

- ListAPIView，CreateAPIView
- RetrieveAPIView，UpdateAPIView，DestroyAPIView
- restful
- 筛选器
- drf组件

类继承关系

iniitial()在视图函数之前

request封装老的request

## 版本

- 三步使用
  - url中version
  - 在视图中应用
  - 在settings中配置
  - uuid.uuid4()
- 登录列表
- 登录视图
- 写认证类
- Login视图不应用认证



## 权限

request

BasePermission 





## 项目

- settings.py
  - "app.apps.mongeostoreConfig"
  - "rest_framework"
  - REST_FRAMEWORK={}
- 做路由分发
  - 版本
- 序列化
- 视图会越写越多，删除View，新建View目录，在View目录下新建
- 路由分发
- 登录LoginView
  - post
- 认证
- 权限
- 

- https代替http
- 在url中体线api标识
- 接口体现版本
- restful

- 跨域
- drf访问频率限制
- jwt

## 跨域

Jquery csdn

- 域不同时，永远不存在跨域
  - crm，非前后端分离，没有跨域
  - 路飞学城，前后端分离，没有跨域
- 与不同时，才会存在跨域
  - 拉勾网，前后端分离，存在跨域（设置响应头解决跨域）

### 解决跨域：CORS

```
本质在数据返回值设置响应头

from django.shortcuts import render,HttpResponse

def json(request):
    response = HttpResponse("JSONasdfasdf")
    response['Access-Control-Allow-Origin'] = "*"
    return response
    
```

### 跨越时，发送了2请求

- 在跨域时，发送一次请求

```
设置响应头就可以解决
from django.shortcuts import render,HttpResponse

def json(request):
    response = HttpResponse("JSONasdfasdf")
    response['Access-Control-Allow-Origin'] = "*"
    return response
```



- 复杂请求

  - 预检

  - 请求

    ```
    
    ```

    

## 项目部署

- crm部署
- 前后端分离



## jwt

用于用户认证