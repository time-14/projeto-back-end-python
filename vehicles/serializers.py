import ipdb
from rest_framework import serializers

from users.serializers import UserSerializer
from vehicle_info.models import Vehicle_Info
from vehicle_info.serializers import VehicleInfoSerializer

from .models import StatusVehicleOrder, Vehicle, VehicleOrder


class VehicleSerializer(serializers.ModelSerializer):

    vehicle_info= VehicleInfoSerializer()

    class Meta:
        model= Vehicle
        fields = ["id", "brand", "model", "year", "owner_id" ,"unique_owner", "price", "mileage", "description", "vehicle_info"]

    def create(self, validated_data):
        vehicle_info_dict = validated_data.pop("vehicle_info")

        vehicle_info, _ = Vehicle_Info.objects.get_or_create(**vehicle_info_dict)

        return Vehicle.objects.create(**validated_data, vehicle_info=vehicle_info)


class VehicleOrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    createdAt = serializers.DateTimeField(read_only=True)
    status = serializers.ChoiceField(
        choices=StatusVehicleOrder.choices, 
        default=StatusVehicleOrder.pendente)

    buyer = serializers.SerializerMethodField()

    owner = serializers.SerializerMethodField()


    def get_buyer(self, obj):
        return obj.buyer.first_name

    def get_owner(self, obj):

        return obj.owner.owner_id


    def create(self, validated_data):
        return VehicleOrder.objects.create(**validated_data)


    class Meta:
        model = Vehicle
        fields = [
            "id",
            "createdAt",
            "status",
            "buyer",
            "owner",
        ]
        read_only_fields = ["createdAt", "buyer", "owner",]
