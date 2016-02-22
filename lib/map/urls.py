from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mapballoon_map, name='map'),
    url(r'^trg/$', views.get_trg, name='get-trg'),
    url(r'^material/$', views.MaterialsJsonList.as_view(), name='get-materials'),
    url(r'^send_balloon/$', views.mapballoon_add_balloon, name='send_balloon'),
    url(r'^send_trgpoint/$', views.mapballoon_add_trgpoint, name='send_trgpoint'),
]
