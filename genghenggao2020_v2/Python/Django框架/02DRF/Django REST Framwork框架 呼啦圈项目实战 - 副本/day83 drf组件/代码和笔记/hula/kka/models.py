from django.db import models


class UserInfo(models.Model):
    """用户表"""
    username = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)
    token = models.CharField(verbose_name='用户Token',max_length=64,null=True,blank=True)