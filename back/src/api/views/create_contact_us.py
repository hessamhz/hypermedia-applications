from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from src.apps.website.models import ContactUs
from src.apps.website.serializers import ContactUsSerializer


@method_decorator(csrf_exempt, name="dispatch")
class ContactUsCreateView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
