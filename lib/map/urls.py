from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns('lib.mapbaloon.views',
        url(r'^trg/$', views.get_trg, name='get-trg'),
        url(r'^material/$', views.get_materials, name='get-materials'),
)
