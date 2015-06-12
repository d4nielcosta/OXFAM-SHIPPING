from django.conf.urls import patterns, include, url
from django.contrib import admin
from volunteer import views

urlpatterns = patterns('',
                       url(r'^volunteer/', include('volunteer.urls')),
                       url(r'^manager/', include('manager.urls')),
                       url(r'^admin/', include(admin.site.urls)),

                       (r'^accounts/', include('registration.backends.simple.urls')),

                       #Disabled to facilitate debugging
                       #url(r'^', views.index, name='index'),

                       )
