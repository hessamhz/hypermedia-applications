from django.db import models
from src.utils.mixins import TimeStampedUUIDMixin


class MediaType(TimeStampedUUIDMixin, models.Model):
    """
    Represents a media type
    """

    media_type = models.CharField(max_length=100, verbose_name="media type")

    def __str__(self):
        return self.media_type
