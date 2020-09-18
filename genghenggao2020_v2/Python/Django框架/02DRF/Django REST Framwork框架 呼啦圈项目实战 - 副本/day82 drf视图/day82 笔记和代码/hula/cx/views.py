from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models

from rest_framework.filters import BaseFilterBackend
class MyFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        val = request.query_params.get('cagetory')
        return queryset.filter(category_id=val)
class IndexView(APIView):

    def get(self,request,*args,**kwargs):
        # http://www.xx.com/cx/index/
        # models.News.objects.all()

        # http://www.xx.com/cx/index/?category=1
        # models.News.objects.filter(category=1)

        # http://www.xx.com/cx/index/?category=1
        # queryset = models.News.objects.all()
        # obj = MyFilterBackend()
        # result = obj.filter_queryset(request,queryset,self)
        # print(result)

        return Response('...')

from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.filters import BaseFilterBackend
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination
class NewFilterBackend(BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        val = request.query_params.get('cagetory')
        return queryset.filter(category_id=val)

class NewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = "__all__"

"""
class NewsView(GenericAPIView):
    queryset = models.News.objects.all()
    filter_backends = [NewFilterBackend,]
    serializer_class = NewSerializers
    pagination_class = PageNumberPagination
    
    def get(self,request,*args,**kwargs):
        v = self.get_queryset()
        queryset = self.filter_queryset(v)
        data = self.paginate_queryset(queryset)
        ser = self.get_serializer(instance=data,many=True)
        return Response(ser.data)
"""


class NewsView(ListAPIView):
    queryset = models.News.objects.all()
    filter_backends = [NewFilterBackend, ]
    serializer_class = NewSerializers
    pagination_class = PageNumberPagination


# #########################################################
class TagSer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = "__all__"

class TagView(ListAPIView,CreateAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = TagSer

    # def get_serializer_class(self):
    #     # self.request
    #     # self.args
    #     # self.kwargs
    #     if self.request.method == 'GET':
    #         return TagSer
    #     elif self.request.method == 'POST':
    #         return OtherTagSer
    # def perform_create(self,serializer):
    #     serializer.save(author=1)

class TagDetailView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset = models.Tag.objects.all()
    serializer_class = TagSer