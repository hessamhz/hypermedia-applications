import uuid

from django.db import models


class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=128)
    overview = models.CharField(max_length=512)
    description = models.TextField()

    working_time = models.CharField(max_length=128)

    picture = models.ForeignKey(
        "storage.MediaModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_picture",
    )

    manager = models.ForeignKey(
        "members.Member",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_manager",
    )

    comments = models.ManyToManyField(
        "services.ServiceComment",
        blank=True,
        related_name="%(app_label)s_%(class)s_comments",
    )

    slug = models.SlugField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
