from django.contrib import admin
from src.apps.website.models import ContactUs, WebsiteConfig

admin.site.register(WebsiteConfig)
admin.site.register(ContactUs)
