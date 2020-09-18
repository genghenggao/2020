from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework.throttling import AnonRateThrottle
from api import models


class LoginView(APIView):
    authentication_classes = []
    def post(self,request,*args,**kwargs):
        # 1.根据用户名和密码检测用户是否可以登录
        user = models.UserInfo.objects.filter(username=request.data.get('username'),password=request.data.get('password')).first()
        if not user:
            return Response({'code':10001,'error':'用户名或密码错误'})

        # 2. 根据user对象生成payload（中间值的数据）
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        payload = jwt_payload_handler(user)

        # 3. 构造前面数据，base64加密；中间数据base64加密；前两段拼接然后做hs256加密（加盐），再做base64加密。生成token
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        token = jwt_encode_handler(payload)
        return Response({'code': 10000, 'data': token})

