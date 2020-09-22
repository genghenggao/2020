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

- 删除View，新建View目录，在View目录下新建
- 路由分发