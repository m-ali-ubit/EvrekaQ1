from rest_framework.viewsets import ModelViewSet

from navigation.models import Vehicle, NavigationRecord
from navigation.serializer import VehicleSerializer, NavigationRecordSerializer


class VehicleViewSet(ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    lookup_field = "plate"


class NavigationRecordViewSet(ModelViewSet):
    serializer_class = NavigationRecordSerializer
    queryset = NavigationRecord.objects.all()
