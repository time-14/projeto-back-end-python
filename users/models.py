import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from addresses.serializers import AddressSerialiazer


class User(AbstractUser):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    username = models.CharField(max_length=250, unique=True)
    firts_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=127, unique=True) 

    address = models.OneToOneField(
        "addresses.Address",
        on_delete=models.CASCADE,
        related_name="users",
        )

