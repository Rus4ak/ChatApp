from django import template
from main.models import Message

register = template.Library()

@register.filter()
def new_messages_count(chat_id, request_user):
    ''' The context processor should return the number of unread messages
    sent by other users to the current user in a particular chat '''
    
    new_messages = Message.objects.filter(chat=chat_id).exclude(
        sender=request_user).filter(is_read=False).count()

    return new_messages
