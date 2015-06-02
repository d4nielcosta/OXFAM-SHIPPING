from django.conf.urls import patterns, include, url
from django.contrib import admin
import general.views

urlpatterns = patterns('',

    url(r'^index/$', general.views.index, name='index'),
    url(r'^manager/', include('manager.urls')),
    url(r'^admin/', include(admin.site.urls)),


    url(r'^', general.views.index, name='index'),

)


# handler400 = 'general.views.index'
# handler404 = 'general.views.index'
# handler500 = 'general.views.index'
