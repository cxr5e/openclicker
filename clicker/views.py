from django.shortcuts import render_to_response

from django.views.generic import TemplateView
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render_to_response('index.html')
    