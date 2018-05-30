from django.urls import path

from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^filter_by_tag/$', views.filter_by_tag, name = "filter_by_tag"),
    url(r'^filter_by_size/$', views.filter_by_size, name = "filter_by_size"),
    url(r'^query/$', views.query, name = "query"),
]
