# Generated by Django 4.2 on 2024-07-16 17:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="member",
            name="email",
        ),
    ]
