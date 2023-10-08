from .models import Chat, Message


def new_messages(request):
    ''' The context processor must return the number of unread messages
    sent by other users to the current user in all chats with that user '''

    if request.user.is_authenticated:
        chats = Chat.objects.filter(participants=request.user)
        messages = Message.objects.filter(chat__in=chats).exclude(
            sender=request.user).filter(is_read=False).count()

        return {'new_messages_length': messages}
    
    return {}
