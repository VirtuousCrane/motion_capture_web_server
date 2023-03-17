import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from time import sleep

class WebSocketTestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data="Hello, World!")

    async def receive(self, text_data=None, bytes_data=None):
        await self.send(text_data="Hello, World!")

    async def disconnect(self, close_code):
        pass
