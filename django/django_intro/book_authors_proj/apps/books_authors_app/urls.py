from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^books/(?P<number>\d+)$', views.show),
    url(r'^add_author/(?P<number>\d+)$', views.add_author),
    url(r'^authors$', views.show_authors),
    url(r'^new_author$', views.new_author),
    url(r'^authors/(?P<number>\d+)$', views.author_info),
    url(r'^add_book/(?P<number>\d+)$', views.add_book),
]