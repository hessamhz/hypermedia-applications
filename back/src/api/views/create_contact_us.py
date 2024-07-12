from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from src.apps.website.models import ContactUs
from src.apps.website.serializers import ContactUsSerializer


class ContactUsCreateView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ContactUsCreateView, self).dispatch(*args, **kwargs)
