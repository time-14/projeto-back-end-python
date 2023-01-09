import uuid

from django.db import models


class Address(models.Model):
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=127)
    zip_code = models.CharField(max_length=8)
    number = models.IntegerField(null=True)
    complement = models.CharField(max_length=127)
