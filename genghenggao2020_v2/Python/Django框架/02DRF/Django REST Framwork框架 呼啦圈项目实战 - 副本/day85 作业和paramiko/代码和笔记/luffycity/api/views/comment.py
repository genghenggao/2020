from rest_framework.views import APIView
from rest_framework.response import Response
from api.extension.permission import LuffyPermission
from api.extension.auth import LuffyAuthentication
class CommentView(APIView):
    authentication_classes = [LuffyAuthentication,]
    permission_classes = [LuffyPermission,]

    def get(self, request, *args, **kwargs):
        return Response('获取所有评论')

    def post(self,request,*args,**kwargs):
        if request.user:
            pass # 可以评论
        # 不可以评论


