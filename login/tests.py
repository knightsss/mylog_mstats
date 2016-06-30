#coding=utf-8
from django.test import TestCase

# Create your tests here.

#生成加密文件
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.hashers import make_password, check_password
password = '123'
sha_pwd = make_password(password,None,'pbkdf2_sha256')   #加密
print sha_pwd
result = check_password(password,sha_pwd)        #验证
print result