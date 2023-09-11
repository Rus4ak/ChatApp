from django.shortcuts import render
from .models import Profile
from .forms import UserRegisterForm


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

