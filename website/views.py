from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST
from django.core.exceptions import ObjectDoesNotExist
from api.models import User, Message


@require_GET
def index(request):
    """index page"""
    return render(request, 'index.html')


@require_POST
def signup(request):
    """signup a new user"""
    try:
        user = User.objects.get(email=request.POST.get('email'))
        #include error message that email is already in system
        return HttpResponseRedirect('/error/')

    except ObjectDoesNotExist:
        user = User.objects.create(
            email=request.POST.get('email')
        )
        
        #code to send welcome email goes here.
        
        return HttpResponseRedirect('/welcome/')
        

@require_POST
def reset(request):
    """reset api credentials for user"""
    pass