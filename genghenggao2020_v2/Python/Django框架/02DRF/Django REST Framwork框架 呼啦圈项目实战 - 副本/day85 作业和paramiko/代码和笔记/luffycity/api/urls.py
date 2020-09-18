from django.conf.urls import url,include
from django.contrib import admin
from api.views import account
from api.views import article

from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    url(r'^login/', account.LoginView.as_view()),
    url(r'^jwt/login/',obtain_jwt_token), # ObtainJSONWebToken.as_view()


    url(r'^article/', article.ArticleView.as_view()),
]