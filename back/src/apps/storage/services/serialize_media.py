from typing import Any, Dict, Optional

from src.apps.storage.models import MediaModel
from src.apps.storage.serializers import MediaModelSerializer


def serialize_media(
    media: MediaModel, context: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Serializes a media object.
    """
    if context is None:
        context = {}
    serializer = MediaModelSerializer(media, context=context)
    return serializer.data
