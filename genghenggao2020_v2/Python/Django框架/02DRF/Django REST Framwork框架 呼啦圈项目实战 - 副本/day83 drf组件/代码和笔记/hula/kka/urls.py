from django.conf.urls import url,include
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^order/$', views.OrderView.as_view()),
    url(r'^user/$', views.UserView.as_view()),
]

