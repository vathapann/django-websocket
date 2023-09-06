# consumers.py
import json
from channels.generic.websocket import (
    AsyncWebsocketConsumer,
    AsyncJsonWebsocketConsumer,
)


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("--> connect(): ", self.scope["user"])
        # if self.scope["user"].is_anonymous:
        #     await self.close()  # Close the WebSocket connection for unauthenticated users
        # else:
            # await self.accept()
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        sender = self.scope["user"].username
        recipient = text_data_json["recipient"]
        print("---> receive()'s para: ", sender, recipient)

        await self.send_message_to_user(sender, recipient, message)

    async def send_message_to_user(self, sender, recipient, message):
        if recipient != sender:
            await self.send(
                text_data=json.dumps(
                    {
                        "sender": sender,
                        "message": message,
                    }
                )
            )


# class PracticeConsumer(AsyncJsonWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def receive(self, text_data=None, bytes_data=None, **kwargs):
#         if text_data == "PING":
#             await self.send("PONG")
