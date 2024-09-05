import json
import asyncio
import datetime

from channels.generic.websocket import AsyncWebsocketConsumer

class TimerConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        pass

    async def disconnect(self):
        pass