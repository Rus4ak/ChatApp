import json
from django.contrib.auth.models import User
from django.utils import timezone
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message, Chat


class ChatConsumer(AsyncWebsocketConsumer):
    ''' This class defines the WebSocket consumer class responsible for managing real-time chat interactions
    between users using Django Channels. It uses asynchronous features to handle WebSocket connections,
    receive and send messages in real-time, and interact with the database '''

    async def connect(self):
        ''' Initializes chat group, adds the client to the group, and accepts the connection '''

        self.chat = self.scope['url_route']['kwargs']['chat']
        self.chat_group = f'chat_{self.chat}'
        
        self.current_chat = await sync_to_async(Chat.objects.get)(id=self.chat)

        await self.channel_layer.group_add(
            self.chat_group,
            self.channel_name
        )

        await self.accept()

    
    async def disconnect(self, code):
        ''' Removes the client from the chat group '''

        await self.channel_layer.group_discard(
            self.chat_group,
            self.channel_name
        )


    async def receive(self, text_data=None, bytes_data=None):
        ''' Parses the received JSON data to extract the message and sends it to the chat group '''

        data = json.loads(text_data)
        message = data['message']
        sender_id = self.scope['user'].id
        sender = self.scope['user'].username
        datetime = timezone.now()

        await self.channel_layer.group_send(
            self.chat_group,
            {
                'type': 'chat_message',
                'message': message,
                'sender_id': sender_id,
                'sender': sender,
                'datetime': datetime.strftime('%Y-%m-%dT%H:%M:%S')
            }
        )

    
    async def chat_message(self, event):
        ''' Retrieves the message and sender information from the event, saves the message to the database,
        and sends the message back to the sender's WebSocket client '''

        message = event['message']
        sender_id = event['sender_id']
        sender = event['sender']
        datetime = event['datetime']

        current_user = await sync_to_async(User.objects.get)(pk=sender_id)

        new_message = await sync_to_async(Message.objects.create)(
            chat=self.current_chat,
            sender=current_user,
            content=message
        )

        await self.send(text_data=json.dumps({
            'message': message,
            'sender_id': sender_id,
            'sender': sender,
            'datetime': datetime
        }))
