from django.contrib import admin
from django.db import models
from src.apps.projects.models import Project
from tinymce.widgets import TinyMCE


class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE(attrs={"cols": 80, "rows": 30})},
    }


admin.site.register(Project, ProjectAdmin)
