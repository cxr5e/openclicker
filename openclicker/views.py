# Create your views here.

from django.shortcuts import redirect

def main(request):
    return redirect('index_page')
    