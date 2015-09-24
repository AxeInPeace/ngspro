from django.conf.urls import patterns, include, url
from django.contrib import admin
from lib.mapbaloon import views
from lib.auth import views as auth

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.map), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', views.fun_logout),
    url(r'^login/$', auth.ajax_login),
    url(r'^reg/$', auth.ajax_registration),
)
