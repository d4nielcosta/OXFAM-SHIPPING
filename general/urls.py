from django.conf.urls import *
import views

__author__ = 'daniel'

urlpatterns = patterns('',

    url(r'^index/$', views.index, name='index'),
    url(r'^manager/$', views.manager, name='manager'),

)