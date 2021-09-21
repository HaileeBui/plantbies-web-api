from django.urls import include, path
from rest_framework import routers

from plants_api.views import PlantViewSet

router = routers.DefaultRouter()
router.register(r"plants", PlantViewSet, basename="plant")

urlpatterns = [
    path("", include(router.urls)),
]