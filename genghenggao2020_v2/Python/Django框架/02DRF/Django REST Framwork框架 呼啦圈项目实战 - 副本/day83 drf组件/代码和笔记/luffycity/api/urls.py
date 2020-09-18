from django.conf.urls import url,include
from django.contrib import admin
from api.views import account
from api.views import article

urlpatterns = [
    url(r'^login/', account.LoginView.as_view()),
    url(r'^article/', article.ArticleView.as_view()),
]