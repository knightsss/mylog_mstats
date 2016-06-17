#coding=utf-8
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt    #用于处理post请求出现的错误
from django.shortcuts import render_to_response
import json
import simplejson
from django.http import HttpResponse
from login.models import User    #导入模型
from django.contrib.auth.hashers import make_password, check_password  #导入加密解密库
# Create your views here.
@csrf_exempt   #处理Post请求出错的情况
def login(request):
     error1 = False
     if 'username' in request.POST:
          name = request.POST['username']
          password = request.POST['password']
          if (not name) or (not password):
               error1 = True            #用户名或密码输入不完整错误
          else:
               try:
                    login = User.objects.get(login_name=name)       #通过get获取对象--在这里用户名唯一
               except:
                    error3 = True
                    return render_to_response('login.html',{"error3":error3})
               sha_pwd = login.pwd           #获取数据库的密文
               if check_password(password,sha_pwd):           #登陆成功
                    request.session['login_name'] = name
                    return render_to_response('main.html')
               else:
                    error2 = True
                    return render_to_response('login.html',{"error2":error2})      #密码胡账户名错误
     return render_to_response('login.html',{"error1":error1})

@csrf_exempt   #处理Post请求出错的情况
def login_ajax(request):
     error1 = False
     if 'username' in request.POST:
          name = request.POST['username']
          if User.objects.filter(login_name=name):      #通过get获取对象--在这里用户名唯一:
               login = User.objects.get(login_name=name)
               password = request.POST['password']
               sha_pwd = login.pwd           #获取数据库的密文
               if check_password(password,sha_pwd):           #登陆成功
                    request.session['login_name'] = name
                    data = {'message':'sucess',
                            'flag':1,
                            'redirect':'main.html'}
               else:
                    data = {'message':'密码错误！',
                            'flag':0,
                            'redirect':'login_error.html'}
               return HttpResponse(json.dumps(data),content_type="application/json")
          else:
               data = {'message':'用户名不存在！',
                       'flag':0,
                       'redirect':'login_error.html'}
               return HttpResponse(json.dumps(data),content_type="application/json")
     return render(request,'login_ajax.html')

def main(request):
     return render_to_response('main.html')