from django.conf.urls import url
from . import views 


urlpatterns = [
    url(r'^logout/$', views.auth_logout, name="logout"),
    url(r'^login/$', views.auth_login, name="login"),
    url(r'^reg/$', views.auth_registration, name="registration"),
    url(r'^verify/$', views.approve_email, name="auth-approve-email"),
]

