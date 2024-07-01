import uuid

from django.db import models


class Member(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=128)
    email = models.EmailField(null=True, blank=True)

    education = models.TextField()
    role = models.CharField(max_length=128)
    role_description = models.TextField()
    expertise = models.TextField()

    avatar = models.ForeignKey(
        "storage.MediaModel",
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_avatar",
    )

    slug = models.SlugField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
