from rest_framework.views import APIView

class ArticleView(APIView):
    """ 文章相关接口，无需登录就可以查看 """
    authentication_classes = []
    def get(self,request,*args,**kwargs):
        """ 文章列表接口 & 文章详细接口 """
        pass