from django.conf.urls import patterns, url
from lib.landing import views

urlpatterns = [
    url(r'^$', views.LandingView.as_view(), name='landing'),
]
