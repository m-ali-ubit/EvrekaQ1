from django.contrib import admin

from navigation.forms import VehicleForm, NavigationRecordForm
from navigation.models import NavigationRecord, Vehicle


class VehicleAdmin(admin.ModelAdmin):
    form = VehicleForm
    list_display = ["id", "plate"]


class NavigationRecordAdmin(admin.ModelAdmin):
    form = NavigationRecordForm
    list_display = ["id", "vehicle", "latitude", "longitude", "datetime"]
    readonly_fields = ["datetime"]


admin.site.register(NavigationRecord, NavigationRecordAdmin)
admin.site.register(Vehicle, VehicleAdmin)
