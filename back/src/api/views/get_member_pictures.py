from rest_framework import generics
from src.apps.members.models import Member
from src.apps.members.serializers import MemberAvatarListSerializer


class MemberAvatarListView(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberAvatarListSerializer
