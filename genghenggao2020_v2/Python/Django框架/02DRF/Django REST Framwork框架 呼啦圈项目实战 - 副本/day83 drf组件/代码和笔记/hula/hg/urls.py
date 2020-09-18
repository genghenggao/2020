from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^article/$', views.ArticleView.as_view()),
    url(r'^article/(?P<pk>\d+)/$', views.ArticleView.as_view()),

    url(r'^comment/$', views.CommentView.as_view()),
]