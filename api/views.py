#TODO: decorator for authentication.

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.core.exceptions import ObjectDoesNotExist
from models import User, Message
from utils import JsonResponse


def authenticate(user_token, access_token):
    """authenticate an user"""
    try:
        user = User.objects.get(
            user_token=user_token,
            access_token=access_token)
        return True
        
    except ObjectDoesNotExist:
        return False
            

@csrf_exempt
@require_POST
def messages(request):
    """return messages for given user"""
    
    if authenticate(
        user_token=request.POST.get('user_token'),
        access_token=request.POST.get('access_token')) == True:
        
        receiver = User.objects.get(user_token=request.POST.get('user_token'))
    
        messages = Message.objects.filter(receiver=receiver)
    
        message_list = []
    
        if messages is not None:
        
            for message in messages:
                message_list.append(
                {"body": message.body,
                "sender": message.sender.user_token,
                "date": str(message.date)}
                )
    
        return JsonResponse(content={"messages": message_list},status=200)
        
    else:
        return JsonResponse(content={"Error": "User does not exist" },status=404)



@csrf_exempt
@require_POST
def send(request):
    """send a message"""
    
    if authenticate(
        user_token=request.POST.get('user_token'),
        access_token=request.POST.get('access_token')) == True:
    
        try:
            receiver = User.objects.get(user_token=request.POST.get('receiver'))
    
        except ObjectDoesNotExist:
            return JsonResponse(content={
                "Error": "Receiving user does not exist"
                },status=404)
            

        try:
            sender = User.objects.get(user_token=request.POST.get('user_token'))
    
        except ObjectDoesNotExist:
            return JsonResponse(content={
                "Error": "Sender user does not exist"
                },status=404)

    
        message = Message.objects.create(
            sender=sender,
            receiver=receiver,
            body=request.POST.get('body')
        )
    
        return JsonResponse(content={"Message": "Sent"},status=200)
    
        
    else:
        return JsonResponse(content={"Error": "User does not exist" },status=404)