from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Profile, Post
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
    user = get_object_or_404(User, username=username)
    user_icon = user.user_profile.icon
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


def detail_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    return render(request, 'account/detail_post.html', {'post': post})


def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return render(request, 'account/detail_post.html', {'post': post})
