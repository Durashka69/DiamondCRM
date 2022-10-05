from rest_framework.routers import DefaultRouter

from clans.views import ClanViewSet


router = DefaultRouter()

router.register('clans', ClanViewSet, basename='clans')

urlpatterns = []

urlpatterns += router.urls
