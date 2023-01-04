from django.db import models
import uuid

class Vehicle(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    unique_owner = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    mileage = models.CharField(max_length=8)
    description = models.CharField(max_length=256, null=True, default=None)
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="vehicles"
    )

