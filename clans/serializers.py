from rest_framework import serializers

from clans.models import Clan

from profiles.serializers import ClanProfileSerializer


class ClanSerializer(serializers.ModelSerializer):
    profiles = ClanProfileSerializer(
        read_only=True, many=True
    )

    class Meta:
        model = Clan
        fields = (
            'id',
            'title',
            'description',
            'date_joined',
            'total_profiles',
            'profiles'
        )
