from django.contrib.auth.models import User
from rest_framework import generics
from .serializer import UserSerializer, ProfileSerializer, PostSerializer, ChatSerializer, ChatMessageSerializer
from .permissions import IsAuthorOrReadOnly
from account.models import Profile, Post
from main.models import Chat


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, )


class ChatList(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatDetail(generics.RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatMessageSerializer

