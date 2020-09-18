from django.conf.urls import url,include
from django.contrib import admin
from .views import account
from .views import order
from .views import comment

urlpatterns = [
    url(r'^login/$',account.LoginView.as_view()),
    url(r'^order/$',order.OrderView.as_view()),
    url(r'^comment/$',comment.CommentView.as_view()),
]