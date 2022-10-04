from rest_framework.routers import DefaultRouter

from profiles.views import (
    UserViewSet, ProfileViewSet, GuildViewSet
)


router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('profiles', ProfileViewSet, basename='profiles')
router.register('guilds', GuildViewSet, basename='guilds')

urlpatterns = []

urlpatterns += router.urls
