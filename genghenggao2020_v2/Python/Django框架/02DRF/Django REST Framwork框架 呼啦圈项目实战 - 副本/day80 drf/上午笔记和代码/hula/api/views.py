from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views import View

class InfoView(View):
    """
    咨询先关接口
    """
    def get(self,request,*args,**kwargs):
        data = [
            {'id': 1, 'title': '震惊了...王阳居然...', 'content': '...'},
            {'id': 2, 'title': '震惊了...王阳居然...', 'content': '...'},
            {'id': 3, 'title': '震惊了...王阳居然...', 'content': '...'},
            {'id': 4, 'title': '震惊了...王阳居然...', 'content': '...'},
        ]

        return JsonResponse(data, safe=False)

    def post(self, request, *args, **kwargs):
        pass
    def put(self, request, *args, **kwargs):
        pass
    def delete(self, request, *args, **kwargs):
        pass

from rest_framework.views import APIView
from rest_framework.response import Response
class DrfInfoView(APIView):
    def get(self,request,*args,**kwargs):
        data = [
            {'id': 1, 'title': '震惊了...王阳居然...', 'content': '...'},
            {'id': 2, 'title': '震惊了...王阳居然...', 'content': '...'},
            {'id': 3, 'title': '震惊了...王阳居然...', 'content': '...'},
            {'id': 4, 'title': '震惊了...王阳居然...', 'content': '...'},
        ]
        return Response(data)

from api import models
from django.forms.models import model_to_dict
class DrfCategoryView(APIView):
    def get(self,request,*args,**kwargs):
        """获取所有文章分类/单个文章分类"""
        pk = kwargs.get('pk')
        if not pk:
            queryset = models.Category.objects.all().values('id','name')
            data_list = list(queryset)
            return Response(data_list)
        else:
            category_object = models.Category.objects.filter(id=pk).first()
            data = model_to_dict(category_object)
            return Response(data)

    def post(self,request,*args,**kwargs):
        """增加一条分类信息"""
        models.Category.objects.create(**request.data)
        return Response('成功')

    def delete(self,request,*args,**kwargs):
        """删除"""
        pk = kwargs.get('pk')
        models.Category.objects.filter(id=pk).delete()
        return Response('删除成功')

    def put(self,request,*args,**kwargs):
        """更新"""
        pk = kwargs.get('pk')
        models.Category.objects.filter(id=pk).update(**request.data)
        return Response('更新成功')


# #################################################
from rest_framework import serializers
class NewCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        # fields = "__all__"
        fields = ['id','name']

class NewCategoryView(APIView):
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        if not pk:
            queryset = models.Category.objects.all()
            ser = NewCategorySerializer(instance=queryset,many=True)
            return Response(ser.data)
        else:
            model_object = models.Category.objects.filter(id=pk).first()
            ser = NewCategorySerializer(instance=model_object, many=False)
            return Response(ser.data)

    def post(self,request,*args,**kwargs):
        ser = NewCategorySerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def put(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        category_object = models.Category.objects.filter(id=pk).first()
        ser = NewCategorySerializer(instance=category_object,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def delete(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        models.Category.objects.filter(id=pk).delete()
        return Response('删除成功')