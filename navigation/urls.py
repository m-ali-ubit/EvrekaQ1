from django.urls import path, include
from rest_framework.routers import DefaultRouter

from navigation.views import VehicleViewSet, NavigationRecordViewSet

router = DefaultRouter()
router.register(r"vehicles", VehicleViewSet, basename="vehicles")
router.register(
    r"navigation_records", NavigationRecordViewSet, basename="navigation_records"
)

urlpatterns = [
    path("", include(router.urls)),
]
