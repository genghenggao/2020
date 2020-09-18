"""hula URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
# from api import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^info/$', views.InfoView.as_view()),
    # url(r'^drf/info/$', views.DrfInfoView.as_view()),
    # url(r'^drf/category/$', views.DrfCategoryView.as_view()),
    # url(r'^drf/category/(?P<pk>\d+)/$', views.DrfCategoryView.as_view()),
    # url(r'^new/category/$', views.NewCategoryView.as_view()),
    # url(r'^new/category/(?P<pk>\d+)/$', views.NewCategoryView.as_view()),
    #
    # # get获取列表
    # # post增加数据
    # url(r'^drf/article/$', views.ArticleView.as_view()),
    # url(r'^drf/article/(?P<pk>\d+)/$', views.ArticleView.as_view()),
    #
    # url(r'^new/article/$', views.NewArticleView.as_view()),
    # url(r'^new/article/(?P<pk>\d+)/$', views.NewArticleView.as_view()),
    #
    # # 分页
    # url(r'^page/article/$', views.PageArticleView.as_view()),
    # url(r'^page/view/article/$', views.PageViewArticleView.as_view()),
]

urlpatterns += [
    url(r'^hg/', include('hg.urls')),
]

urlpatterns += [
    url(r'^cx/', include('cx.urls')),
]
