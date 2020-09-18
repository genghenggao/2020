import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from rest_framework import status

from api import models



class LoginView(APIView):
    """
    登录接口
    """
    def post(self,request,*args,**kwargs):
        """"""
        # 基于Token的认证
        """
        user_object = models.UserInfo.objects.filter(**request.data).first()
        if not user_object:
            return Response('登录失败')
        random_string = str(uuid.uuid4())
        user_object.token = random_string
        user_object.save()
        data_info = {
            'code':10001,
            'data':random_string
        }
        return Response(data_info)
        """

        # 基于jwt的认证
        # 1.去数据库获取用户信息
        from rest_framework_jwt.settings import api_settings
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        user = models.UserInfo.objects.filter(**request.data).first()
        if not user:
            return Response({'code':1000,'error':'用户名或密码错误'})

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'code':1001,'data':token})

























