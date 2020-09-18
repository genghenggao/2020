import uuid
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.versioning import URLPathVersioning
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from .auth import TokenAuthentication


class LoginView(APIView):
    authentication_classes = []
    def post(self,request,*args,**kwargs):
        user_object = models.UserInfo.objects.filter(**request.data).first()
        if not user_object:
            return Response('登录失败')
        random_string = str(uuid.uuid4())
        user_object.token = random_string
        user_object.save()
        return Response(random_string)

from rest_framework.permissions import BasePermission
from rest_framework import exceptions

class MyPermission(BasePermission):
    message = {'code': 10001, 'error': '你没权限'}
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.user:
            return True

        # raise exceptions.PermissionDenied({'code': 10001, 'error': '你没权限'})
        return False

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return False

class OrderView(APIView):
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [MyPermission,]
    def get(self,request,*args,**kwargs):
        return Response('order')


class UserView(APIView):
    # authentication_classes = [TokenAuthentication,]
    permission_classes = [MyPermission, ]
    def get(self,request,*args,**kwargs):
        return Response('user')
