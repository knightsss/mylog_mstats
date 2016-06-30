#coding=utf-8
from django.conf.urls import patterns, include, url
import settings
from django.contrib import admin
from login.views import login,login_ajax,main
from echarts.views import echarts,air
from log_management.views import log_management
from partition_management.views import partition_management
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',login),
    url(r'^login_ajax/$',login_ajax),   #不加上$符号，所有以login_ajax开头的都能匹配到
    url(r'^login_ajax/main.html/$',main),
    url(r'^echarts/$',echarts),
    url(r'^air/$',air),
    url(r'^log_management/$',log_management),
    url(r'^partition_management/$',partition_management),


    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_URL }),
)
