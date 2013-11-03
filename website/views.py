from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from api.models import User, Message
from uuid import uuid1



WELCOME_EMAIL = 'Welcome!\nYour user token is: {user_token}\n'\
                'Your access token is: {access_token}\nHave fun!'


@require_GET
def index(request):
    """index page"""
    return render(request, 'index.html')


@require_GET
def reset_user(request):
    """reset user credentials form page"""
    return render(request, 'reset.html')
    

@require_GET
def welcome(request):
    "welcome page for new users"
    return render(request, 'welcome.html')


@require_GET
def signup_error(request):
    "email used to create new account already in system"
    return render(request, 'signup-error.html')


@require_GET
def user_error(request):
    "user does not exist"
    return render(request, 'user-error.html')


@require_GET
def user_updated(request):
    "user api credentials updated. new tokens"
    return render(request, 'user-updated.html')
    
    
@require_POST
def signup(request):
    """signup a new user"""
    try:
        user = User.objects.get(email=request.POST.get('email'))
        #include error message that email is already in system
        return redirect('/error/signup/')

    except ObjectDoesNotExist:
        user = User.objects.create(
            email=request.POST.get('email')
        )
        

        send_mail(
            'Welcome to bbedy', 
            WELCOME_EMAIL.format(
            user_token=user.user_token,
            access_token=user.access_token),  
            'your@email.com', 
            ['pablo.rivera.programmer@gmail.com'])
        
        return redirect('/welcome/')
        

@require_POST
def reset(request):
    """reset api credentials for user"""
    try:
        user = User.objects.get(email=request.POST.get('email'))
        user.user_token = uuid1()
        user.access_token = uuid1()
        user.save()
        
        return redirect('/user/')
    
    except ObjectDoesNotExist:
        return redirect('/error/user/')