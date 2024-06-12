import uuid

from django.db import models


class TimeStampedUUIDMixin(models.Model):
    """
    Mixin for models to add UUID-based primary key and timestamp fields.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated at")

    class Meta:
        abstract = True
