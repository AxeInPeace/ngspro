from django.conf.urls import patterns, include, url
from django.contrib import admin
from lib.mapbaloon import views
from lib.auth import views as auth_views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.map), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', views.fun_logout),
    url(r'^login/$', auth_views.ajax_login),
    url(r'^reg/$', auth_views.ajax_registration),
)
