# 整合Django和Vue.js

[TOC]

目前,我们已经分别完成了Django后端和Vue.js前端工程的创建和编写，但实际上它们是运行在各自的服务器上，和我们的要求是不一致的。因此我们须要把Django的TemplateView指向我们刚才生成的前端dist文件即可。



1、 找到mongoestore_v1目录的urls.py，使用通用视图创建最简单的模板控制器，访问 『/』时直接返回 index.html:



2、 上一步使用了Django的模板系统，所以需要配置一下模板使Django知道从哪里找到index.html。在mongoestore_v1目录的settings.py下：



3、我们还需要配置一下静态文件的搜索路径。同样是project目录的settings.py下：





4、 配置完成，我们在project目录下输入命令`python manage.py runserver`，就能够看到我们的前端页面在浏览器上展现：





参考：

https://my.oschina.net/sunwenhao/blog/3197518