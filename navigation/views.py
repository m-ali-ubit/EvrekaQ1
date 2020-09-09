from datetime import datetime, timedelta

from django.utils import timezone
from rest_framework.viewsets import ModelViewSet

from navigation.models import Vehicle, NavigationRecord
from navigation.serializer import VehicleSerializer, NavigationRecordSerializer


class VehicleViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    lookup_field = "plate"


class NavigationRecordViewSet(ModelViewSet):
    serializer_class = NavigationRecordSerializer
    delta_time_48_hours = timezone.now() - timedelta(hours=48)
    queryset = NavigationRecord.objects.filter(datetime__gte=delta_time_48_hours)
