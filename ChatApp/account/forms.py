from django import forms
from django.contrib.auth.models import User
from .models import Post

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username')    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email']


    def clean_password2(self):
        # Password validity check
        cd = self.cleaned_data

        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match.')
        
        if len(cd['password1']) < 8:
            raise forms.ValidationError('Password must be more than 8 characters')

        return cd['password2']


    def clean_email(self):
        # Check if mail is already in use
        data = self.cleaned_data['email']

        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        
        return data


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['photo', 'description']