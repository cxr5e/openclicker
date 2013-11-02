"""

views.py

Contains the views for the clicker game pages

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
    