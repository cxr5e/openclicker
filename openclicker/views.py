# Create your views here.

from django.shortcuts import redirect

def main(request):
    ''' If you do not supply a directory to the server, just redirect
    to url/clicker
    '''
    return redirect('index_page')
    