# Generated by Django 4.2 on 2024-07-05 16:51

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="content",
            field=tinymce.models.HTMLField(default="nth"),
            preserve_default=False,
        ),
    ]
