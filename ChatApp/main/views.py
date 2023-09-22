from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.postgres.search import TrigramSimilarity
from .forms import SearchForm

def index(request):
    if request.user.is_authenticated:
        return render(request, 'main/index.html', {'chat_selected': True})
    
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
