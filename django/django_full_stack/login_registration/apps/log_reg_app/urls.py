from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.register_user),
    url(r'^success$', views.success),
    url(r'^logout$', views.logout),
    url(r'^login$', views.login)
]