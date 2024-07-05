import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            context = text_data_json.get("context")
            query = text_data_json.get("query")

            response_message = f"Context is: {context} and query is {query}"

            await self.send(text_data=json.dumps({"message": response_message}))
        except Exception as e:
            await self.send(text_data=json.dumps({"error": str(e)}))
