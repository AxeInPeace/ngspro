from django.conf.urls import patterns, url
from lib.main import views

urlpatterns = patterns('',
    url(r'^$', views.landing),
)

