from django.conf.urls import patterns, url
from lib.main import views

urlpatterns = patterns('',
    url(r'', views.slash),
    url(r'^main/$', views.main)
)

