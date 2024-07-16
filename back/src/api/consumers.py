import json
from urllib.parse import parse_qs

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    """
    A consumer class for handling WebSocket connections and messages for the chatbot.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the ChatConsumer class and sets up the assistant client.
        """
        super().__init__(*args, **kwargs)
        from src.apps.chatbot.clients import Assistant

        self.assistant = Assistant()

    async def _get_query_params(self) -> str:
        """
        Retrieves the thread ID from the WebSocket connection's query parameters.

        Returns:
            str: The thread ID, or None if not present.
        """
        # Decode and parse the query string to get thread_id
        query_params = self.scope["query_string"].decode()
        query_params = parse_qs(query_params)
        thread_id = query_params.get("id", [None])[0]
        return thread_id

    async def _get_or_create_thread(self):
        """
        Retrieves or creates a new thread based on the thread ID from query parameters.

        Returns:
            Thread: The retrieved or newly created Thread object.
        """
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
        """
        Retrieves a thread based on the thread ID from query parameters.

        Returns:
            Thread or str: The retrieved Thread object, or an error message
                if not found.
        """
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
        """
        Handles a new WebSocket connection by retrieving or creating a thread
        and accepting the connection.
        """
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
        """
        Handles the WebSocket disconnection.

        Args:
            close_code: The close code for the WebSocket connection.
        """
        pass

    async def receive(self, text_data: str):
        """
        Handles incoming messages from the WebSocket.

        Args:
            text_data (str): The received message data in JSON format.
        """
        thread = await self._get_thread()

        # If no valid thread, send error message and close the connection
        if thread is None:
            await self.send(text_data=json.dumps({"error": "Thread not found"}))
            await self.close()
            return

        try:
            # Parse the received message data
            text_data_json = json.loads(text_data)
            query = text_data_json.get("query")

            # Send the query to the assistant and get the response
            response_message = await self.assistant.send_prompt(
                thread.open_ai_thread_id, query
            )

            # Send the response message back to the client
            await self.send(text_data=json.dumps({"message": response_message}))
        except Exception as e:
            # Send error message back to the client in case of an exception
            await self.send(text_data=json.dumps({"error": str(e)}))
