from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import UserRegisterForm, PostForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password2'])
            new_user.save()

            Profile.objects.create(user=new_user)
            return render(request, 'account/register_done.html')
    else:
        user_form = UserRegisterForm()
        
    return render(request, 'account/register.html', {'form': user_form})


def profile(request, username):
    user = User.objects.get(username=username)
    user_icon = user.user_profile.first().icon
    user_posts = user.posts.all()

    context = {
        'profile_selected': True,
        'user': user,
        'user_icon': user_icon,
        'user_posts': user_posts
    }

    return render(request, 'account/profile.html', context)


def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.save()

            return redirect('account:profile', username=request.user)
    else:
        post_form = PostForm()
    
    return render(request, 'account/create_post.html', {'form': post_form})
