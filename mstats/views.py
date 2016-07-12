#coding=utf-8
from django.shortcuts import render

# Create your views here.
import time,datetime
import json
import simplejson
from json import loads, dumps
from django.shortcuts import render_to_response,HttpResponse
from mstats.models import Info
def mstats(request):
    return render_to_response('mstats.html')

def get_mstats(request):
    #根据时间戳的范围来获取数据
    # 时间过滤，获取集合
    current_time = int(time.time())
    start_time = 1467964810
    mid_time = 1467966310
    end_time = 1467968398
    static_s =  348595
    f_time = current_time - static_s
    l_time = f_time - 600
    data_set = Info.objects.filter(mtime__range=(l_time,f_time))
    data = {}
    list_data = []
    old_minutes = 66
    flag = 1
    #遍历集合
    for row in data_set:
        # flag = 0
        #row.time获取时间戳字段，在转换成时间，获取分
        new_minutes = int(time.strftime("%M", time.localtime(row.mtime)))
        if new_minutes == old_minutes:
            flag = 0
        else:
            flag = 1
        # if new_minutes%3 == 0 and flag == 1:
        if flag == 1:
            pid = row.pid
            agent_id = row.agent_id
            server_id = row.server_id
            mtime = row.mtime
            timeArray = time.localtime(mtime)
            new_time = time.strftime("%H:%M", timeArray)
            stats = row.stats

            #转换成json格式,将数据转换成dict
            dict_row = simplejson.loads(stats)
            # dict_row = {}
            dict_row['mtime'] = new_time
            #将json追加到list中
            list_data.append(dict_row)
            # dict_row['number'] = stats['time']['run']
            # data['info'] = data['info'] + dict_row
        old_minutes = new_minutes

    data['info'] = list_data
    # data = Info.objects.get(mtime=1467968348)
    #转换成json字符串
    json_str = dumps(data)
    # 以json格式的字符串传递,js可直接读取
    return HttpResponse(json_str,content_type='application/json')
    # return HttpResponse(json.dumps(stats),content_type="application/json")