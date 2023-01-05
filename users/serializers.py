import ipdb
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from addresses.models import Address
from addresses.serializers import AddressSerialiazer

from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators = [UniqueValidator(queryset=User.objects.all(), message = "This field must be unique.")])

    address = AddressSerialiazer()

    class Meta: 
        model = User
        fields = ["id", "email", "password", "first_name", "last_name", "is_superuser", "username", "address"]
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validated_data: dict) -> User:
        address_dict = validated_data.pop("address")

        address, _ = Address.objects.get_or_create(**address_dict)
        
        user = User.objects.create_user(**validated_data, address=address)

        return user