from rest_framework import generics
from src.apps.members.models import Member
from src.apps.members.serializers import MemberListSerializer, MemberSerializer


class MemberListView(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberListSerializer


class MemberDetailView(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_field = "slug"
