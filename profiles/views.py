from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser

from profiles.serializers import (
    UserSerializer, ProfileSerializer
)
from profiles.models import (
    User, Profile
)
from profiles.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        print(f"\n\n\n\n\n\n\n {self.request.user} \n\n\n\n\n\n\n")
        return serializer.save(user=self.request.user)


class ProfileViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
