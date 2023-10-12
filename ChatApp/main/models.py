from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='chats')


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False, blank=True)

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id'])
        ]
    