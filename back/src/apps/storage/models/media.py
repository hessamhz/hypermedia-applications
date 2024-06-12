import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from src.utils.mixins import TimeStampedUUIDMixin


class MediaModel(TimeStampedUUIDMixin, models.Model):
    """
    Media object wrapper model
    """

    def file_path(instance, filename):
        """
        Defines the upload path for the media file.
        """
        file_name = filename.split(".")[-1]
        return "{}/{}.{}".format(instance.mime_type, str(uuid.uuid4()), file_name)

    file = models.FileField(
        upload_to=file_path,
        verbose_name=_("file"),
    )
    mime_type = models.ForeignKey(
        "storage.MediaType",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("mime type"),
    )
