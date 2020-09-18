from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^index/$', views.IndexView.as_view()),
    url(r'^news/$', views.NewsView.as_view()),
    url(r'^tag/$', views.TagView.as_view()),
    url(r'^tag/(?P<pk>\d+)/$', views.TagDetailView.as_view()),
]

