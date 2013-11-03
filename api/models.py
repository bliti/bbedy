from django.db import models
from uuid import uuid1


class User(models.Model):


    email = models.EmailField(unique=True)
    user_token = models.TextField(default=uuid1())
    access_token = models.TextField(default=uuid1())


class Message(models.Model):


    sender = models.ForeignKey('User', related_name="sender")
    receiver = models.ForeignKey('User', related_name='receiver')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)