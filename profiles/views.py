from rest_framework import viewsets, permissions

from profiles.serializers import (
    UserSerializer, ProfileSerializer, GuildSerializer
)
from profiles.models import (
    User, Profile, Guild
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        print(f"\n\n\n\n\n\n\n {self.request.user} \n\n\n\n\n\n\n")
        return serializer.save(user=self.request.user)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class GuildViewSet(viewsets.ModelViewSet):
    queryset = Guild.objects.all()
    serializer_class = GuildSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)
