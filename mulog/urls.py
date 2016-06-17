#coding=utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
from login.views import login,login_ajax,main
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',login),
    url(r'^login_ajax/$',login_ajax),   #不加上$符号，所有以login_ajax开头的都能匹配到
    url(r'^login_ajax/main.html/$',main),
)
