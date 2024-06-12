from typing import Any, Dict, List, Optional

from src.apps.storage.models import MediaModel
from src.apps.storage.serializers import MediaModelSerializer


def serialize_batch_of_media(
    media: List[MediaModel], context: Optional[Dict[str, Any]] = None
) -> List[Dict[str, Any]]:
    """
    Serializes a batch of media objects.
    """
    if context is None:
        context = {}
    serializer = MediaModelSerializer(media, context=context, many=True)
    serializer_data = serializer.data
    return serializer_data
