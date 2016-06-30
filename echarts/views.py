#coding=utf-8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt    #用于处理post请求出现的错误
from django.shortcuts import render_to_response
import json
import simplejson
from django.http import HttpResponse


def echarts(request):
    return render_to_response('Test_ECharts.html')

def air(request):
    return render_to_response('Test_air.html')