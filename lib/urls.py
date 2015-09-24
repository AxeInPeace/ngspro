from django.conf.urls import patterns, include, url
from django.contrib import admin
from lib.mapbaloon import views

admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', views.map), 
    url(r'^registration/$', views.registration),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^design/$', views.design),
    url(r'^logout/$', views.fun_logout),
)
