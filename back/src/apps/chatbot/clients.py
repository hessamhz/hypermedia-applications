from django.conf import settings
from openai import OpenAI


class Assistant:
    """
    General class for handling the OpenAI assistant.
    """

    def __init__(self):
        """
        Initializes the Assistant class with an OpenAI client and assistant ID.
        """
        self.client = OpenAI(api_key=settings.OPENAI_KEY)
        self.assistant_id = settings.OPENAI_ASSISTANT_ID

    async def create_thread(self) -> str:
        """
        Creates a new thread using the OpenAI client.

        Returns:
            str: The ID of the created thread.
        """
        # Create a new thread
        thread = self.client.beta.threads.create()
        # Return the thread ID
        return thread.id

    async def send_prompt(self, thread_id: str, message: str) -> str:
        """
        Sends a prompt message to a specified thread and waits for a response.

        Args:
            thread_id (str): The ID of the thread to send the message to.
            message (str): The message content to be sent.

        Returns:
            str: The response message from the assistant.
        """
        thread_id = str(thread_id)  # Ensure thread_id is a string

        # Add the user's message to the thread
        await self._add_message_to_thread(thread_id, message)

        # Create and poll a new run for the thread
        run = self.client.beta.threads.runs.create_and_poll(
            thread_id=thread_id,
            assistant_id=self.assistant_id,
        )

        # If the run is completed, get the messages from the thread
        if run.status == "completed":
            messages = self.client.beta.threads.messages.list(thread_id=thread_id)

        # Return the last message content from the assistant
        return messages.data[0].content[0].text.value

    async def _add_message_to_thread(self, thread_id: str, message: str) -> None:
        """
        Adds a message to a specified thread.

        Args:
            thread_id (str): The ID of the thread to add the message to.
            message (str): The message content to be added.
        """
        # Create a new message in the thread with the role of "user"
        self.client.beta.threads.messages.create(
            thread_id=thread_id, role="user", content=message
        )
