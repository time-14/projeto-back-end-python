from django.db import models

class Vehicle_Info(models.Model):
    engine = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    doors = models.IntegerField()
    seats = models.IntegerField()
    color = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=50)
    gas_type = models.CharField(max_length=50)
    revisions = models.BooleanField(default=False)
    last_maintance = models.DateField(null=True)

    vehicle = models.OneToOneField(
        "vehicles.Vehicle", 
        on_delete=models.CASCADE
    ) 