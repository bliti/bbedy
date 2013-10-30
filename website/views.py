from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.core.exceptions import ObjectDoesNotExist
from api.models import User, Message
from uuid import uuid1
#from utils import error messages! 


@require_GET
def index(request):
    """index page"""
    return render(request, 'index.html')


@require_GET
def message(request):
    """generic message page."""
    return render(request, 'message.html', {"message": "Hello, world."})


@require_POST
def signup(request):
    """signup a new user"""
    try:
        user = User.objects.get(email=request.POST.get('email'))
        #include error message that email is already in system
        return redirect('/message/', {"message": USER_EXISTS_ERROR})

    except ObjectDoesNotExist:
        user = User.objects.create(
            email=request.POST.get('email')
        )
        
        #code to send welcome email goes here.
        
        return redirect('/message/',  {"message": WELCOME})
        

@require_POST
def reset(request):
    """reset api credentials for user"""
    try:
        user = User.objects.get(email=request.POST.get('email'))
        user.user_token = uuid1()
        user.access_token = uuid1()
        user.save()
        
        return redirect('/message/',  {"message": ACCOUNT_RESET})
    
    except ObjectDoesNotExist:
        return redirect('/message/',  {"message": USER_NOT_FOUND})