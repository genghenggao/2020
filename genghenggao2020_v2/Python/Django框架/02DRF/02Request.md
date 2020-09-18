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

  