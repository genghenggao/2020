# -*- coding:utf-8 -*-
# Author:cqk
# Data:2019/11/8 15:13
from rest_framework.authentication import BaseAuthentication
from . import models


class LoginAuth:
    def authenticate(self, request):
        token = request.query_params.get("token")
        user_obj = models.UserInfo.objects.filter(token=token).first()
        if user_obj:
            return user_obj, token
        else:
            return None, None
