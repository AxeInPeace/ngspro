from django.conf.urls import patterns, include, url
from django.contrib import admin
from lib.mapbaloon import views
from lib.auth import views as auth_views
from django.conf import settings

admin.autodiscover()

urlpatterns = [
    url(r'^', include('lib.mapbaloon.urls')),
    url(r'^auth/', include('lib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^landing/', include('lib.landing.urls')),
]


