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
    status_choices = (
        (1,'发布'),
        (2,'删除'),
    )
    status = models.IntegerField(verbose_name='状态',choices=status_choices,default=1)
    title = models.CharField(verbose_name='标题',max_length=32)
    summary = models.CharField(verbose_name='简介',max_length=255)
    content = models.TextField(verbose_name='文章内容')
    category = models.ForeignKey(verbose_name='分类',to='Category')

    tag = models.ManyToManyField(verbose_name='标签',to='Tag',null=True,blank=True)

class Tag(models.Model):
    """标签"""
    title = models.CharField(verbose_name='标签',max_length=32)

