from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from .models import Post


class AsyncChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name = "blog"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):


        await  self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        ret_message = await self.save_message(message)

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat_message",
                "message": f"{ret_message.pub_date} - {ret_message.text}"
            }
        )

    async def chat_message(self, event):

        message = event["message"]

        await self.send(text_data=json.dumps(
            {"message": message}
        ))

    @database_sync_to_async
    def save_message(self, message):
        return Post.objects.create(text=message)

