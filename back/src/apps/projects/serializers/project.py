from rest_framework import serializers
from src.apps.projects.models import Project
from src.apps.storage.services import serialize_batch_of_media, serialize_media


class ProjectSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()
    manager = serializers.SerializerMethodField()
    album = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"
        # TODO: exclude email if not needed

    def get_picture(self, instance):
        if instance.picture:
            picture = serialize_media(instance.picture, context=self.context)
            return picture
        return None

    def get_album(self, instance):
        if instance.album:
            album = serialize_batch_of_media(instance.album, context=self.context)
            return album
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


class ProjectListSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["title", "picture", "slug", "overview"]

    def get_picture(self, instance):
        if instance.picture:
            picture = serialize_media(instance.picture, context=self.context)
            return picture
        return None
