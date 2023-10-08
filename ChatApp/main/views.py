from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Max
from .forms import SearchForm
from .models import Chat, Message

def index(request):
    if request.user.is_authenticated:
        chats = Chat.objects.filter(participants=request.user).annotate(
            last_message=Max('messages__created')).order_by('-last_message')
        
        context = {
            'chat_selected': True,
            'chats': chats,
        }

        return render(request, 'main/index.html', context)
    return redirect('account:login')


def search(request):
    ''' searching for users using trigram similarity '''
    
    form = SearchForm()
    query = None
    result = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        
        if form.is_valid():
            query = form.cleaned_data['query']

            result = User.objects.annotate(
                similarity=TrigramSimilarity('username', query),
            ).filter(similarity__gt=0.1).order_by('-similarity')
    
    context = {
        'search_selected': True,
        'form': form,
        'result': result
    }

    return render(request, 'main/search.html', context)


def chat(request, user_id):
    ''' Creates a new chat if it already exists shows all messages in this chat
    and the number of 'unread' messages '''

    chat = Chat.objects.filter(participants=request.user).filter(participants=user_id).first()

    if not chat:
        chat = Chat.objects.create()
        chat.participants.add(request.user.pk, user_id)
        chat.save()
    
    chat.messages.all().filter(is_read=False).exclude(sender=request.user).update(is_read=True)
    
    context = {
        'chat_selected': True,
        'chat': chat
    }

    return render(request, 'main/chat.html', context)
