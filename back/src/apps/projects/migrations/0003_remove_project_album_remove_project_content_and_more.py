# Generated by Django 4.2 on 2024-07-16 17:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_project_content"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="album",
        ),
        migrations.RemoveField(
            model_name="project",
            name="content",
        ),
        migrations.RemoveField(
            model_name="project",
            name="is_new",
        ),
        migrations.RemoveField(
            model_name="project",
            name="responsible",
        ),
        migrations.RemoveField(
            model_name="project",
            name="status",
        ),
    ]
