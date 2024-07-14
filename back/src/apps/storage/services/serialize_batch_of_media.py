from typing import Any, Dict, List, Optional

from django.conf import settings
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
    data = serializer.data
    if not settings.IS_LOCAL_URL:
        for item in data:
            item["file"] = item["file"].replace("http", "https")
    return data
