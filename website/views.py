# Create your views here.
from django.shortcuts import render


def index(request):
    """index page"""
    return render(request, 'index.html')


def signup(request):
    """process signup"""
    pass
    

def reset(request):
    """reset api credentials"""
    pass