from rest_framework import serializers
from src.apps.services.models import ServiceComment
from src.apps.storage.services import serialize_media


class ServiceCommentSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = ServiceComment
        fields = "__all__"

    def get_picture(self, instance):
        if instance.picture:
            picture = serialize_media(instance.picture, context=self.context)
            return picture
        return None
