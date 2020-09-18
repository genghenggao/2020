from django.db import models

class Category(models.Model):
    """
    文章分类
    """
    name = models.CharField(verbose_name='分类',max_length=32)


class Article(models.Model):
    """
    文章表
    """
    title = models.CharField(verbose_name='标题',max_length=32)
    summary = models.CharField(verbose_name='简介',max_length=255)
    content = models.TextField(verbose_name='文章内容')
    category = models.ForeignKey(verbose_name='分类',to='Category')