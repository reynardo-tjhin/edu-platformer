import json
import asyncio
import datetime

from channels.generic.websocket import AsyncWebsocketConsumer
from .models import PlayerDoes
from asgiref import sync
from asgiref.sync import sync_to_async
from datetime import timezone

@sync_to_async
def get_start_time(user_id: int, quiz_id: int):
    """
    Get the time based on the username and the quiz
    """
    return PlayerDoes.objects.get(username=user_id, quiz_id=quiz_id).start_time


class TimerConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        """
        Connect the client to the WebSocket server.
        Client will try to send a connectiton request.
        """
        # instantly accept the client's request for connection
        await self.accept()

        self.stop = False
        self.task = None

    async def action(self, user_id: int, quiz_id: int):
        """
        Count down the timer (asynchronously).
        """
        # get the starting time
        start_time = await get_start_time(user_id, quiz_id)

        # send timer update every second
        time = 10
        for _ in range(time): # assuming a 60-second timer currently

            # when client sends a 'disconnect' request to the WebSocket
            if (self.stop):
                break
        
            # get the current time
            curr_time = datetime.datetime.now(timezone.utc)

            # get the time difference in seconds
            diff = (curr_time - start_time).seconds

            # send the text data (the time left) to the client
            await self.send(text_data=json.dumps({
                'time': time - diff,
            }))

            # sleep for 1 second
            await asyncio.sleep(1)

        # disconnect with the client
        await self.send(text_data=json.dumps({
            'message': 'timer expires',
        }))
        await self.close()

    async def disconnect(self, close_code):
        """
        Upon receiving a disconnect request from the client.
        """
        self.stop = True
        await self.task
        sync.async_to_sync(print("WebSocket Disconnected..."))
        await self.close()

    async def receive(self, text_data):
        """
        Receiving data
        """
        text_data_json = json.loads(text_data)
        
        # count the time
        user_id = text_data_json['user_id']
        quiz_id = text_data_json['quiz_id']

        # create another asynchronous task
        # this task will count down the timer
        self.task = asyncio.create_task(self.action(user_id, quiz_id))