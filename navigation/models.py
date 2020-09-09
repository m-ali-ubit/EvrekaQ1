from django.db import models


class Vehicle(models.Model):
    plate = models.CharField(max_length=15)

    def __str__(self):
        return self.plate


class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(to="Vehicle", on_delete=models.DO_NOTHING)
    latitude = models.FloatField()
    longitude = models.FloatField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vehicle.plate} | {self.latitude} | {self.longitude}"
