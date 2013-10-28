from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.core.exceptions import ObjectDoesNotExist
from models import User, Message
from utils import JsonResponse


def authenticate(request):
    """authenticate an user"""
    try:
        user = User.objects.get(
            user_token=request.POST.get('user_token'),
            access_token=request.POST.get('access_token'))
        pass
        
    except ObjectDoesNotExist:
        return JsonResponse(content={
            "Error": "Check user credentials"
            },status=404)
            

@csrf_exempt
@require_POST
def messages(request):
    """return messages for given user"""
    authenticate(request)
    return JsonResponse(content=list(Message.objects.filter(
        receiver=request.POST.get('user_token')).values),
        status=200)


@csrf_exempt
@require_POST
def send(request):
    """send a message"""
    authenticate(request)
    
    try:
        receiver = User.objects.get(user_token=request.POST.get('receiver'))
    
    except ObjectsDoesNotExist:
        return JsonResponse(content={
            "Error": "Receiving user does not exist"
            },status=404)

    sender = User.objects.get(user_token=request.POST.get('user_token'))
    
    message = Message.objects.create(
        sender=sender,
        receiver=receiver,
        body=request.POST.get('body')
    )
    
    return JsonResponse(content={"Message": "Sent"},status=200)