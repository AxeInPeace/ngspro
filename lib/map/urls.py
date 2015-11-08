from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('lib.mapbaloon.views',
        url(r'^tile/$', views.get_tile, name='get-tile'),
)
