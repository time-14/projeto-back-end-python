from rest_framework import serializers

from addresses.models import Address


class AddressSerialiazer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    state = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)
    street = serializers.CharField(max_length=127)
    zip_code = serializers.CharField(max_length=8)
    number = serializers.IntegerField(allow_null=True, default=None)
    complement = serializers.CharField(max_length=127)

    class Meta:
        model = Address
        fields = [
            "id",
            "state",
            "city",
            "street",
            "zip_code",
            "number",
            "complement",
        ]