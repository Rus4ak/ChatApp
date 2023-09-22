from django import forms
from django.contrib.auth.models import User
from .models import Post, Profile

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


class UserForm(forms.ModelForm):
    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        # Get current user
        current_user = kwargs.pop('current_user', None)
        super(UserForm, self).__init__(*args, **kwargs)

        self.current_user = current_user

        self.fields['username'].initial = self.current_user.username
        self.fields['email'].initial = self.current_user.email

    def clean_username(self):
        # Check if username is already in use
        data = self.cleaned_data['username']

        if data:
            if User.objects.filter(username=data).exclude(pk=self.current_user.pk).exists():
                raise forms.ValidationError('Username already in use.')
        
        return data
    
    def clean_email(self):
        # Check if mail is already in use
        data = self.cleaned_data['email']

        if data:
            if User.objects.filter(email=data).exclude(pk=self.current_user.pk).exists():
                raise forms.ValidationError('Email already in use.')
        
        return data
    

class ProfileForm(forms.ModelForm):
    icon = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['icon']
