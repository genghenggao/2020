# Vue页面在后端相互跳转

在项目目录下`urls.py`配置

```
from django.urls import path, re_path

re_path(r'.*', TemplateView.as_view(template_name='index.html'))
```

这样就可以愉快的在后端项目跳转了。



参考：

https://www.jianshu.com/p/9eea64371692

