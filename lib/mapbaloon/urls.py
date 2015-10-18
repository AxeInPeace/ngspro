from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('lib.mapbaloon.views',
    url(r'^$', views.mapballoon_map),
    url(r'^send_balloon/$', views.mapballoon_add_balloon, name='send_balloon'),
    url(r'^send_trgpoint/$', views.mapballoon_add_trgpoint, name='send_trgpoint'),
    url(r'^filter_years/$', views.mapballoon_filter_for_years, name='filter_years'),
)
