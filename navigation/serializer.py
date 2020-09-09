from rest_framework import serializers

from navigation.models import Vehicle, NavigationRecord


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"


class NavigationRecordSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.SerializerMethodField(required=False)
    datetime = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S", required=False)

    @staticmethod
    def get_vehicle_plate(instance):
        return instance.vehicle.plate

    class Meta:
        model = NavigationRecord
        exclude = ("id", "vehicle",)
