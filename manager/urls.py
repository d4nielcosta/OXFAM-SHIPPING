__author__ = 'daniel'

from django.conf.urls import *
import views

urlpatterns = patterns('',
    url(r'^$', views.manager, name='manager'),

)