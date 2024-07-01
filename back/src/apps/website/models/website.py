import uuid

from django.db import models


# Singletone model for django settings
class WebsiteConfig(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=512)
    overview = models.CharField(max_length=512)
    about_us = models.TextField()

    donations = models.PositiveIntegerField(default=0)
    volunteers = models.PositiveIntegerField(default=0)
    womens_assisted = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
