import jwt
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework_jwt.settings import api_settings
from api import models

class HulaQueryParamAuthentication(BaseAuthentication):
    def authenticate(self, request):
        """
        # raise Exception(), 不在继续往下执行，直接返回给用户。
        # return None ,本次认证完成，执行下一个认证
        # return ('x',"x")，认证成功，不需要再继续执行其他认证了，继续往后权限、节流、视图函数
        """
        token = request.query_params.get('token')
        if not token:
            raise exceptions.AuthenticationFailed({'code':10002,'error':"登录成功之后才能操作"})

        jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            raise exceptions.AuthenticationFailed({'code':10003,'error':"token已过期"})
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed({'code':10004,'error':"token格式错误"})
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed({'code':10005,'error':"认证失败"})

        jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER
        username = jwt_get_username_from_payload(payload)
        user_object = models.UserInfo.objects.filter(username=username).first()
        return (user_object,token)