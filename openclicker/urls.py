"""
Openclicker -1.0 | an open source clicker game.
Copyright (C) 2013  Cheryl Yang and Ryan Lam
Contact: cheriexryan@hellokitty.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

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
