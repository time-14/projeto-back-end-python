from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators = [UniqueValidator(queryset=User.objects.all(), message = "This field must be unique.")])
    class Meta: 
        model = User
        fields = ["id", "email", "password", "first_name", "last_name", "is_superuser", "username", "address"]
        extra_kwargs = {"password":{"write_only":True}}

    def create(self, validated_data: dict) -> User:
        return User.objects.create_superuser(**validated_data)