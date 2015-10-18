from django.conf.urls import patterns, include, url
from . import views 


urlpatterns = [
    url(r'^logout/$', views.auth_logout, name="logout"),
    url(r'^login/$', views.auth_login, name="login"),
    url(r'^reg/$', views.auth_registration, name="registration"),
    url(r'^setavatar/$', views.auth_set_avatar, name="setavatar"),
]

