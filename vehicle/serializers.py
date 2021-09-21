from rest_framework import serializers
from .models import Vehicle


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


class VehicleBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('number', 'owner', 'rate_client',)
