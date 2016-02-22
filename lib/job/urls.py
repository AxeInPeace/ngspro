from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.ListJobs.as_view())
]