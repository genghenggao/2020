# jQuery_Demo1

1）、区别

- `$(document).ready(function(){});`初始化函数，当网页中dom元素（不包括图片、视频、资源）全部加载完毕后，立即执行；简化写法:`    $(function(){})`
- `window.onload`初始化函数，当网页中dom元素（关联图片、视频、资源）全部加载完毕后，立即执行；

2）、表单校验

- 可以减轻对服务端的访问次数。
  - 获取要检验的元素(选择器)  用户名、密码
  - 通过字符串处理方法或者正则表达式等手段，进行校验 
    - “genghenggao@outlook.com” .indexOf ("@") != -1
  - 触发校验的方法或事件(校验时机)
    - blur():失去焦点时触发
    - submit(): 当点击表单"submit"按钮时触发
    - onbiur = "xx()"  
    - onsubmit ="xxx()"