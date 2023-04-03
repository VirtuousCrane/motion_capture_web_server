import asyncio
import json
import redis
from channels.generic.websocket import AsyncWebsocketConsumer
from time import sleep
from asgiref.sync import async_to_sync

def redis_handler(msg):
    print(msg["data"])

class WebSocketTestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data="Hello, World!")

        self.redis_client = redis.Redis()
        self.pubsub = self.redis_client.pubsub()
        self.pubsub.subscribe(**{"MOTIONCAPTURE": self.redis_handler })
        thread = self.pubsub.run_in_thread(sleep_time=0.001)
        
    async def receive(self, text_data=None, bytes_data=None):
        await self.send(text_data="Hello, World!")

    async def disconnect(self, close_code):
        pass

    def redis_handler(self, message):
        async_to_sync(self.send)(text_data=message["data"].decode("utf-8"))
