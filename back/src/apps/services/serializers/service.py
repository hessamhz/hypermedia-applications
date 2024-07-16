from rest_framework import serializers
from src.apps.services.models import Service
from src.apps.services.serializers.comment import ServiceCommentSerializer
from src.apps.storage.services import serialize_media


class ServiceSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()
    manager = serializers.SerializerMethodField()
    comments = ServiceCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        exclude = ["id", "created_at", "updated_at"]

    def get_picture(self, instance):
        if instance.picture:
            picture = serialize_media(instance.picture, context=self.context)
            return picture
        return None

    def get_manager(self, instance):
        manager = instance.manager
        if manager:
            dict = {
                "name": manager.name,
                "slug": manager.slug,
            }
            return dict
        return None


class ServiceListSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ["title", "picture", "slug", "overview"]

    def get_picture(self, instance):
        if instance.picture:
            picture = serialize_media(instance.picture, context=self.context)
            return picture
        return None
