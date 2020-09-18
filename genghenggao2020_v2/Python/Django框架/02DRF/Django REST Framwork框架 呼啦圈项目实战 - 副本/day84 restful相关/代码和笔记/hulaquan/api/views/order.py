from rest_framework.views import APIView
from rest_framework.response import Response
from api.extensions.auth import HulaQueryParamAuthentication


class OrderView(APIView):
    """ 订单相关接口（所都需要登录才能看） """

    def get(self, request, *args, **kwargs):
        """ 订单列表接口 """
        print(request.user)
        print(request.auth)
        return Response('订单列表')

    def post(self,request,*args,**kwargs):
        """ 订单评论（需要登录才能访问）"""
        return Response('创建订单')
