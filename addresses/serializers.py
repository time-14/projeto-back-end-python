from rest_framework import serializers

from addresses.models import Address


class AddressSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"