from rest_framework import serializers
from api import models
class ArticleSerializer(serializers.ModelSerializer):
    category_txt = serializers.CharField(source='category.name',required=False)
    x1 = serializers.SerializerMethodField()

    status_txt = serializers.CharField(source='get_status_display',required=False)

    x2 = serializers.SerializerMethodField()
    class Meta:
        model = models.Article
        # fields = "__all__"
        fields = ['id','title','summary','content','category','category_txt','x1','status','status_txt','x2']
        # depth = 1

    def get_x1(self,obj):
        return obj.category.name

    def get_x2(self,obj):
        return obj.get_status_display()

class NewArticleSerializer(serializers.ModelSerializer):
    tag_info = serializers.SerializerMethodField()
    class Meta:
        model = models.Article
        fields = ['title','summary','tag_info']

    def get_tag_info(self,obj):
        return [row for row in obj.tag.all().values('id','title')]

class FormNewArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'