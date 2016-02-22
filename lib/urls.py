from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^auth/', include('lib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^landing/', include('lib.landing.urls')),
    url(r'^', include('lib.main.urls')),
    url(r'^', include('lib.photo.urls')),
    url(r'^map/', include('lib.map.urls')),
    url(r'^job/', include('lib.job.urls')),
]
