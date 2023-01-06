from rest_framework import serializers


from .models import Vehicle
from vehicle_info.models import Vehicle_Info
from users.serializers import UserSerializer
from vehicle_info.serializers import VehicleInfoSerializer

class VehicleSerializer(serializers.ModelSerializer):

    vehicle_info= VehicleInfoSerializer()

    class Meta:
        model= Vehicle
        fields = ["id", "brand", "model", "year", "owner_id" ,"unique_owner", "price", "mileage", "description", "vehicle_info"]

    def create(self, validated_data):
        vehicle_info_dict = validated_data.pop("vehicle_info")

        vehicle_info, _ = Vehicle_Info.objects.get_or_create(**vehicle_info_dict)

        return Vehicle.objects.create(**validated_data, vehicle_info=vehicle_info)