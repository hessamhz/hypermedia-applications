from rest_framework import generics
from src.apps.website.models import ContactUs
from src.apps.website.serializers import ContactUsSerializer


class ContactUsCreateView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
