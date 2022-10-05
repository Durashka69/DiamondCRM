from rest_framework.routers import DefaultRouter

from profiles.views import (
    UserViewSet, ProfileViewSet
)


router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('profiles', ProfileViewSet, basename='profiles')

urlpatterns = []

urlpatterns += router.urls
