from rest_framework import viewsets

from clans.serializers import ClanSerializer
from clans.models import Clan


class ClanViewSet(viewsets.ModelViewSet):
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer
