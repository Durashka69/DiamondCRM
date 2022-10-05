from rest_framework import serializers

from profiles.models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'is_staff'
        )


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(
        read_only=True
    )
    clan = serializers.ReadOnlyField(
        source='clan.title'
    )

    class Meta:
        model = Profile
        fields = (
            'id',
            'user',
            'profile_photo',
            'rang',
            'clan'
        )


class ClanProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.username'
    )

    class Meta:
        model = Profile
        fields = (
            'id',
            'user',
            'rang'
        )
