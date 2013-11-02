from django.conf.urls import patterns, include, url

import clicker.urls
import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'openclicker.views.home', name='home'),
    # url(r'^openclicker/', include('openclicker.foo.urls')),
    
    # A redirect to clicker/
    url(r'^$', views.main),
    
    # The directory to the clicker app
    url(r'^clicker/', include(clicker.urls)),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
