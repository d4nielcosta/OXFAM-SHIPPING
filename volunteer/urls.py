from django.conf.urls import patterns, url
from volunteer import views

__author__ = 'daniel'

urlpatterns = patterns('',

                       url(r'^index/$', views.index, name='index'),
                       url(r'^app/$', views.app, name='app'),

                       )
