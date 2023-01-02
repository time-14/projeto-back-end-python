from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    firts_name = models.CharField(max_length=50)
    last_name = models.EmailField(max_length=50)
    email = models.CharField(max_length=127, unique=True)
    
    # Quando criado o app de vehicles criar a model com a foreingkey relacionando a model de user
    