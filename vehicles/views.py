from django.shortcuts import render
from rest_framework import generics
from .models import Vehicle

class VehicleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
