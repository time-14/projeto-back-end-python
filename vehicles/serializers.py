from rest_framework import serializers

from .models import Vehicle
from users.serializers import UserSerializer

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Vehicle
        fields = ["id", "brand", "model", "year", "unique_owner", "owner", "price", "mileage", "description"]

    def create(self, validated_data):
        return Vehicle.objects.create(**validated_data)