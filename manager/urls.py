__author__ = 'daniel'

from django.conf.urls import *
import views

urlpatterns = patterns('',
    url(r'^$', views.manager, name='manager'),
    url(r'^storerank/$', views.storerank, name='storerank'),
)