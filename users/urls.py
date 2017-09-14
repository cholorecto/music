from django.conf.urls import url

from .views import UserLogin, Dashboard

urlpatterns = [
    url(r'^login/$', UserLogin.as_view(), name='UserLogin'),
    url(r'^dashboard/$', Dashboard.as_view(), name='Dashboard')
]