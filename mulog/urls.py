from django.conf.urls import patterns, include, url

from django.contrib import admin
from login.views import login,login_auth
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/',login),
    url(r'^login_auth/',login_auth)
)
