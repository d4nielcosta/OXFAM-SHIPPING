from django.conf.urls import patterns, include, url
from django.contrib import admin
import general.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'oxfam_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^oxfam/', include('shipping.urls')),
    url(r'^index/$', general.views.index, name='index'),
)
