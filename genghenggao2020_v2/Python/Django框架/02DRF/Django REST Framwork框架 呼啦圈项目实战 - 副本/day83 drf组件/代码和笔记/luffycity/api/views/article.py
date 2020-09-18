from rest_framework.views import APIView
from rest_framework.response import Response

class ArticleView(APIView):
    def get(self,request,*args,**kwargs):
        return Response('文章列表')

class ArticleDetailView(APIView):
    def get(self,request,*args,**kwargs):
        return Response('文章列表')