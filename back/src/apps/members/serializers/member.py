from rest_framework import serializers
from src.apps.members.models import Member
from src.apps.projects.models import Project
from src.apps.projects.serializers import ProjectListSerializer
from src.apps.services.models import Service
from src.apps.services.serializers import ServiceListSerializer
from src.apps.storage.services import serialize_media


class MemberSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    activities = serializers.SerializerMethodField()

    class Meta:
        model = Member
        exclude = ["id", "created_at", "updated_at"]

    def get_avatar(self, instance):
        if instance.avatar:
            avatar = serialize_media(instance.avatar, context=self.context)
            return avatar
        return None

    def get_activities(self, instance):
        services = Service.objects.filter(manager=instance)
        services_list = ServiceListSerializer(
            services, many=True, context=self.context
        ).data
        projects = Project.objects.filter(manager=instance)
        projects_list = ProjectListSerializer(
            projects, many=True, context=self.context
        ).data

        return {"services": services_list, "projects": projects_list}


class MemberListSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ["name", "avatar", "slug", "role"]

    def get_avatar(self, instance):
        if instance.avatar:
            avatar = serialize_media(instance.avatar, context=self.context)
            return avatar
        return None


class MemberAvatarListSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = Member
        fields = ["avatar"]

    def get_avatar(self, instance):
        if instance.avatar:
            avatar = serialize_media(instance.avatar, context=self.context)
            return avatar
        return None
