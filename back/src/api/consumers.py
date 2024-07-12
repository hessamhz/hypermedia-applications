import json
from urllib.parse import parse_qs

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        from src.apps.chatbot.clients import Assistant

        self.assistant = Assistant()

    async def _get_query_params(self):
        # Decode and parse the query string to get room_id
        query_params = self.scope["query_string"].decode()
        query_params = parse_qs(query_params)
        thread_id = query_params.get("id", [None])[0]

        return thread_id

    async def _get_or_create_thread(self):
        thread_id = await self._get_query_params()

        from src.apps.chatbot.models.thread import Thread

        # Attempt to retrieve the Thread by ID, or create a new one if it doesn't exist
        if thread_id:
            try:
                thread = await Thread.objects.aget(id=thread_id)
            except Thread.DoesNotExist:
                thread_id = await self.assistant.create_thread()
                thread = await Thread.objects.acreate(open_ai_thread_id=thread_id)
        else:
            thread_id = await self.assistant.create_thread()
            thread = await Thread.objects.acreate(open_ai_thread_id=thread_id)

        return thread

    async def _get_thread(self):
        thread_id = await self._get_query_params()

        from src.apps.chatbot.models.thread import Thread

        # If thread id is invalid return None
        if thread_id:
            try:
                thread = await Thread.objects.aget(id=thread_id)
            except Thread.DoesNotExist:
                thread = None
        else:
            thread = "Empty thread ID provided"

        return thread

    async def connect(self):
        thread = await self._get_or_create_thread()

        # Accept the WebSocket connection
        await self.accept()

        # Optionally, send back the thread ID or some confirmation message
        await self.send(
            text_data=json.dumps(
                {
                    "thread_id": str(thread.id),
                }
            )
        )

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        thread = await self._get_thread()

        # if no valid queryset => drop the connection
        if thread is None:
            await self.send(text_data=json.dumps({"error": "Thread not found"}))
            await self.close()

        try:
            text_data_json = json.loads(text_data)
            # if we needed the context = text_data_json.get("context")
            query = text_data_json.get("query")

            response_message = await self.assistant.send_prompt(
                thread.open_ai_thread_id, query
            )
            # response_message = f"Context is: {context} and query is {query}"

            await self.send(text_data=json.dumps({"message": response_message}))
        except Exception as e:
            await self.send(text_data=json.dumps({"error": str(e)}))
