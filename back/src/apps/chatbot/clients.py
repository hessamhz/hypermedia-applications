from django.conf import settings
from openai import OpenAI


class Assistant:

    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_KEY)
        self.assistant_id = settings.OPENAI_ASSISTANT_ID

    async def create_thread(self):
        thread = self.client.beta.threads.create()
        return thread.id

    async def send_prompt(self, thread_id, message):
        thread_id = str(thread_id)

        await self._add_message_to_thread(thread_id, message)

        run = self.client.beta.threads.runs.create_and_poll(
            thread_id=thread_id,
            assistant_id=self.assistant_id,
        )

        if run.status == "completed":
            messages = self.client.beta.threads.messages.list(thread_id=thread_id)

        return messages.data[0].content[0].text.value

    async def _add_message_to_thread(self, thread_id, message):
        self.client.beta.threads.messages.create(
            thread_id=thread_id, role="user", content=message
        )
