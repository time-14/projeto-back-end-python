from rest_framework import serializers
from .models import Vehicle_Info

class VehicleInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicle_Info
        fields=["engine", "transmission", "doors", "seats", "color", "vehicle_type", "gas_type", "revisions", "last_maintance"]

        def create(self, validated_data: dict) -> Vehicle_Info:
            return Vehicle_Info.objects.create(**validated_data)