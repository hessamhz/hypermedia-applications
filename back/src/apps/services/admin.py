from django.contrib import admin
from src.apps.services.models import Service, ServiceComment

admin.site.register(Service)
admin.site.register(ServiceComment)
