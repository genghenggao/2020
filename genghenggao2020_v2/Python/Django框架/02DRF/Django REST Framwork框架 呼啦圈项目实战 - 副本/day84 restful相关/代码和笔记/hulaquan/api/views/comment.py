from rest_framework.views import APIView
from rest_framework.response import Response

class CommentView(APIView):
    """ 评论相关接口 """

    def get(self, request, *args, **kwargs):
        """ 评论列表接口 """
        return Response('所有评论')

    def post(self,request,*args,**kwargs):
        """ 新增评论（需要登录才能访问）"""
        return Response('添加评论')

    def get_authenticators(self):
        if self.request.method == "GET":
            return []
        elif self.request.method == 'POST':
            return super().get_authenticators()