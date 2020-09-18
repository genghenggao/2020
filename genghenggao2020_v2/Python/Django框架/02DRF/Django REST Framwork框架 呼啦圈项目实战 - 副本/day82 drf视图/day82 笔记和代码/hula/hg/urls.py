from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    # 登录
    url(r'^login/$', views.LoginView.as_view()),
    # 文章
    url(r'^article/$', views.ArticleView.as_view()),
    url(r'^article/(?P<pk>\d+)/$', views.OneArticleView.as_view()),
    # 评论
    url(r'^comment/$', views.CommentView.as_view()),
]