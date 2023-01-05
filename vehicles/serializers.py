from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Vehicle
from users.serializers import UserSerializer

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Vehicle
        fields = ["id", "brand", "model", "year", "owner_id" ,"unique_owner", "price", "mileage", "description", "vehicle_info"]

    def create(self, validated_data):
        vehicle_info_dict = validated_data.pop("vehicle_info")

        vehicle_info, _ = Vehicle.objects.get_object_or_404(**vehicle_info_dict)

        return Vehicle.objects.create(**validated_data, vehicle_info=vehicle_info)