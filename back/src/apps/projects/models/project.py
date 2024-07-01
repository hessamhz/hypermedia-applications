import uuid

from django.db import models


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=128)
    overview = models.CharField(max_length=512)
    description = models.TextField()

    picture = models.ForeignKey(
        "storage.MediaModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_picture",
    )
    is_new = models.BooleanField(default=True)

    album = models.ManyToManyField(
        "storage.MediaModel",
        related_name="%(app_label)s_%(class)s_album",
    )

    start_date = models.DateField()
    responsible = models.CharField(max_length=128)
    status_choices = [
        ("C", "Completed"),
        ("I", "Ongoing"),
        ("P", "Planned"),
        ("S", "Stalled"),
    ]
    status = models.CharField(max_length=1, choices=status_choices, default="P")

    manager = models.ForeignKey(
        "members.Member",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(app_label)s_%(class)s_manager",
    )
    is_new = models.BooleanField(default=True)

    slug = models.SlugField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
