from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('lib.mapbaloon.views',
    url(r'^$', views.map),
    url(r'^send_balloon/$', views.addBalloon, name='send_balloon'),
    url(r'^filter_years/$', views.filterForYears, name='filter_years'),
)
