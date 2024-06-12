import magic
from django.db.models.signals import pre_save
from django.dispatch import receiver
from src.apps.storage.models import MediaType


@receiver(pre_save, sender="storage.MediaModel")
def create_media_type(sender, instance, **kwargs) -> None:
    """
    Pre-save signal handler to determine the MIME type of the media file.
    """
    try:
        mim = magic.from_buffer(instance.file.read(), mime=True)
        media_type_object, _ = MediaType.objects.get_or_create(media_type=mim)
        instance.mime_type = media_type_object
    except Exception as e:
        print(f"Error determining mime type: {e}")
