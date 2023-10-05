from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import Profile, Post
from main.models import Chat, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ('user', 'icon')


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    likes = UserSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)

    class Meta:
        model = Chat
        fields = '__all__'

    
class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer()

    class Meta:
        model = Message
        fields = '__all__'


class ChatMessageSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)
    messages = MessageSerializer(many=True)

    class Meta:
        model = Chat
        fields = ('id', 'participants', 'messages')
