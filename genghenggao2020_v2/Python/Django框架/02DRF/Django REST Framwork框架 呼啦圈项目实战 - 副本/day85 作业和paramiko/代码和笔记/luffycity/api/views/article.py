from rest_framework.views import APIView
from rest_framework.response import Response

# from rest_framework.throttling import AnonRateThrottle,BaseThrottle




class ArticleView(APIView):
    # throttle_classes = [AnonRateThrottle,]

    def get(self,request,*args,**kwargs):
        # 获取用户提交的token，进行一步一步校验
        import jwt
        from rest_framework import exceptions
        from rest_framework_jwt.settings import api_settings
        jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

        jwt_value = request.query_params.get('token')
        try:
            payload = jwt_decode_handler(jwt_value)
        except jwt.ExpiredSignature:
            msg = '签名已过期'
            raise exceptions.AuthenticationFailed(msg)
        except jwt.DecodeError:
            msg = '认证失败'
            raise exceptions.AuthenticationFailed(msg)
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed()
        print(payload)

        return Response('文章列表')

class ArticleDetailView(APIView):
    def get(self,request,*args,**kwargs):

        return Response('文章列表')