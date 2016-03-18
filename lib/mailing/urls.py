from django.conf.urls import url

from lib.mailing import views

urlpatterns = [
    url('^$', views.response, name='ngspro-confirm'),
]