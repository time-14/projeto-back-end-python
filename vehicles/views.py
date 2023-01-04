from django.shortcuts import render
from rest_framework import generics
from .models import Vehicle
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class VehicleView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Vehicle.objects.all()
    # serializer_class = VehicleSerializer



