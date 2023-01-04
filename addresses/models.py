# Create your models here.
import uuid

from django.db import models

from addresses.serializers import AddressSerialiazer


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=127)
    zip_code = models.CharField(max_length=8)
    number = models.IntegerField(null=True)
    complement = models.CharField(max_length=127)

    address = AddressSerialiazer()

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="address",
        )