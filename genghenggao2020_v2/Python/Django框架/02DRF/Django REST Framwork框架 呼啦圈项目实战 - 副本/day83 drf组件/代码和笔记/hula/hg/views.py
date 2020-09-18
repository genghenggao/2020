from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
from . import models

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        # fields = "__all__"
        exclude = ['author',]


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleDetail
        # fields = "__all__"
        exclude = ['article',]

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = "__all__"


class PageArticleSerializer(serializers.ModelSerializer):
    content = serializers.CharField(source="articledetail.content")
    author = serializers.CharField(source="author.username")
    category = serializers.CharField(source="get_category_display")
    date = serializers.SerializerMethodField()
    class Meta:
        model = models.Article
        fields = "__all__"

    def get_date(self,obj):
        # print(obj.date,type(obj.date))
        # from datetime import datetime
        return obj.date.strftime('%Y-%m-%d %H:%M')

class ArticleView(APIView):
    """ 文章视图类 """

    def get(self,request,*args,**kwargs):
        """ 获取文章列表 """
        pk = kwargs.get('pk')
        if not pk:
            condition = {}
            category = request.query_params.get('category')
            if category:
                condition['category'] = category
            queryset = models.Article.objects.filter(**condition).order_by('-date')
            pager = PageNumberPagination()
            result = pager.paginate_queryset(queryset,request,self)
            ser = ArticleListSerializer(instance=result,many=True)
            return Response(ser.data)
        article_object = models.Article.objects.filter(id=pk).first()
        ser = PageArticleSerializer(instance=article_object,many=False)
        return Response(ser.data)

    def post(self,request,*args,**kwargs):
        """ 新增文章（应该在后台管理开发）"""
        ser = ArticleSerializer(data=request.data)
        ser_detail = ArticleDetailSerializer(data=request.data)
        if ser.is_valid() and ser_detail.is_valid():
            # 增加文章
            article_object = ser.save(author_id=1)
            ser_detail.save(article=article_object)
            return Response('添加成功')
        return Response('错误')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = "__all__"

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        exclude = ['user']

class CommentView(APIView):
    """ 评论接口 """

    def get(self,request,*args,**kwargs):
        """ 评论列表 """
        article_id = request.query_params.get('article')
        queryset = models.Comment.objects.filter(article_id=article_id)
        ser = CommentSerializer(instance=queryset,many=True)
        return Response(ser.data)

    def post(self,request,*args,**kwargs):
        """ 添加评论 """
        ser = PostCommentSerializer(data=request.data)
        if ser.is_valid():
            ser.save(user_id=2)
            return Response('成功')
        return Response('失败')



