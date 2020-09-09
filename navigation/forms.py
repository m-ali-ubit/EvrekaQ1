from django import forms

from navigation.models import Vehicle, NavigationRecord


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"


class NavigationRecordForm(forms.ModelForm):
    class Meta:
        model = NavigationRecord
        fields = "__all__"
