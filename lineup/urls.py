from django.conf.urls import patterns, url
from lineup import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^view/(?P<lineup_id>\d)$', views.view, name='view'),
                       url(r'^edit/(?P<lineup_id>\d)$', views.edit, name='edit'))
