import uuid

from django.db import models


class Thread(models.Model):
    # Thread ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    open_ai_thread_id = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
