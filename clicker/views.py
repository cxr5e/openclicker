"""
Openclicker - an open source clicker game.
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

from django.shortcuts import render_to_response

from django.views.generic import TemplateView
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    ''' The main page with the computer clicking game '''
    return render_to_response('index.html')
    
def test(request):
    ''' The QUnit test page '''
    return render_to_response('qunit.html')
    