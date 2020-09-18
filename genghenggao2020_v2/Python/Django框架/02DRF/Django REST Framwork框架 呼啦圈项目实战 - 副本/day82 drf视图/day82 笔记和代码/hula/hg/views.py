from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.pagination import PageNumberPagination
import uuid
from rest_framework import serializers
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, \
    ListCreateAPIView
from rest_framework.filters import BaseFilterBackend
from . import models
from django.db.models import F

from hg.myauth import LoginAuth
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        # fields = "__all__"
        exclude = ['author', ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ArticleDetail
        # fields = "__all__"
        exclude = ['article', ]


class ArticleListSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = models.Article
        fields = "__all__"

    def get_date(self, obj):
        return obj.date.strftime('%Y-%m-%d %H:%M')


class PageArticleSerializer(serializers.ModelSerializer):
    content = serializers.CharField(source="articledetail.content")
    author = serializers.CharField(source="author.username")
    category = serializers.CharField(source="get_category_display")
    date = serializers.SerializerMethodField()

    class Meta:
        model = models.Article
        fields = "__all__"

    def get_date(self, obj):
        print(obj.date, type(obj.date))
        # from datetime import datetime
        return obj.date.strftime('%Y-%m-%d %H:%M')


# class ArticleView(APIView):
#     """ 文章视图类 """
#
#     def get(self,request,*args,**kwargs):
#         """ 获取文章列表 """
#         pk = kwargs.get('pk')
#         if not pk:
#             condition = {}
#             category = request.query_params.get('category')
#             if category:
#                 condition['category'] = category
#             queryset = models.Article.objects.filter(**condition).order_by('-date')
#             pager = PageNumberPagination()
#             result = pager.paginate_queryset(queryset,request,self)
#             ser = ArticleListSerializer(instance=result,many=True)
#             return Response(ser.data)
#         article_object = models.Article.objects.filter(id=pk).first()
#         ser = PageArticleSerializer(instance=article_object,many=False)
#         return Response(ser.data)
#
#     def post(self,request,*args,**kwargs):
#         """ 新增文章（应该在后台管理开发）"""
#         ser = ArticleSerializer(data=request.data)
#         ser_detail = ArticleDetailSerializer(data=request.data)
#         if ser.is_valid() and ser_detail.is_valid():
#             # 增加文章
#             article_object = ser.save(author_id=1)
#             ser_detail.save(article=article_object)
#             return Response('添加成功')
#         return Response('错误')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = "__all__"


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        exclude = ['user', "article"]


# class CommentView(APIView):
#     """ 评论接口 """
#
#     def get(self,request,*args,**kwargs):
#         """ 评论列表 """
#         article_id = request.query_params.get('article')
#         queryset = models.Comment.objects.filter(article_id=article_id)
#         ser = CommentSerializer(instance=queryset,many=True)
#         return Response(ser.data)
#
#     def post(self,request,*args,**kwargs):
#         """ 添加评论 """
#         ser = PostCommentSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save(user_id=2)
#             return Response('成功')
#         return Response('失败')




class LoginView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):

        user_obj = models.UserInfo.objects.filter(**request.data)
        if user_obj:
            token = str(uuid.uuid4())
            user_obj.update(token=token)
            Response(token)
        else:
            return Response("用户名或密码错误")


class ArticleBaseFilterBackend(BaseFilterBackend):  # 文章筛选类
    def filter_queryset(self, request, queryset, view):
        val = {}
        if request.query_params.get("category"):
            val = {"category": request.query_params.get("category")}
        return queryset.filter(**val).order_by("-date")


class ArticleView(ListAPIView, CreateAPIView):
    queryset = models.Article.objects.all()  # 获取全部文章
    serializer_class = ArticleListSerializer  # 展示全部文章信息
    filter_backends = [ArticleBaseFilterBackend]  # 筛选某一类别的文章

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ArticleSerializer
        elif self.request.method == "GET":
            return self.serializer_class

    def perform_create(self, serializer):  # 重构数据存储方法
        ser_detail = ArticleDetailSerializer(data=self.request.data)  # 文章的内容校验
        if ser_detail.is_valid():
            article_object = serializer.save(author_id=1)  # 文章新增  添加作者id 并返回当前对象
            print(article_object, type(article_object))  # Article object <class 'hg.models.Article'>
            ser_detail.save(article=article_object)


class OneArticleView(RetrieveAPIView):
    queryset = models.Article.objects
    serializer_class = PageArticleSerializer

    def get(self, request, *args, **kwargs):
        models.Article.objects.filter(pk=kwargs.get("pk")).update(read_count=F("read_count") + 1)
        return super().get(request, *args, **kwargs)


class CommentFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        val = {}
        if request.query_params.get("article"):
            val = {"article": request.query_params.get("article")}
        return queryset.filter(**val).order_by("-id")


class CommentView(ListCreateAPIView):
    queryset = models.Comment.objects
    serializer_class = CommentSerializer
    filter_backends = [CommentFilter]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PostCommentSerializer
        elif self.request.method == "GET":
            return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=2, article=self.request.query_params.get("article"))
