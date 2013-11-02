from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    # The main page
    url(r'^$', views.index, name='index_page'),
    
    # The QUnit test page
    url(r'^test/$', views.test, name='test_page'),
)
