from django.db import models

class Tag(models.Model):
    title = models.CharField(max_length=32)


class News(models.Model):
    """ 新闻表 """
    category_choices = (
        (1,'咨询'),
        (2,'公司动态'),
        (3,'分享'),
        (4,'答疑'),
        (5,'其他'),
    )
    category = models.IntegerField(verbose_name='分类',choices=category_choices)
    title = models.CharField(verbose_name='标题',max_length=32)
    image = models.CharField(verbose_name='图片路径',max_length=128)
    summary = models.CharField(verbose_name='简介',max_length=255)