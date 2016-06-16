#coding=utf-8
from django.db import models

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)                 #主键
    login_name = models.CharField(max_length=20)    #登录名
    pwd = models.CharField(max_length=100)      #密码
    user_name = models.CharField(max_length=20)     #真是姓名
    email = models.CharField(max_length=20)         #邮件
    def __unicode__(self):
        return self.user_name

class Right(models.Model):
    right_id = models.IntegerField(primary_key=True)    #权限ID 主键
    right_name = models.CharField(max_length=20)        #权限名称
    description = models.CharField(max_length=200)      #权限描述
    def __unicode__(self):
        return u'%s %s' % (self.right_id, self.right_name)

class UserPrivilege(models.Model):
    user_right_id = models.IntegerField(primary_key=True)     #用户权限表主键
    user_id = models.ForeignKey('User')                      #用户id，外键
    right_id = models.ForeignKey('Right')                    #权限id,外键
    right_type = models.IntegerField()                        #是否可以访问
    def __unicode__(self):
        return self.user_id

