import uuid
from typing import Optional, Union

from src.apps.storage.models import MediaModel


def get_media_by_id(media_id: Union[str, uuid.UUID]) -> Optional[MediaModel]:
    """
    Retrieves a media object from the database by its ID.
    """
    try:
        return MediaModel.objects.get(id=media_id)
    except MediaModel.DoesNotExist:
        return None
