from django.conf.urls import patterns, include, url
from . import views 


urlpatterns = [
    url(r'^logout/$', views.fun_logout, name="logout"),
    url(r'^login/$', views.ajax_login, name="login"),
    url(r'^reg/$', views.ajax_registration, name="registration"),
    url(r'^setavatar/$', views.setavatar, name="setavatar"),
]

