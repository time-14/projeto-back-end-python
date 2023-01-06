from django.shortcuts import render
from rest_framework import generics
from .models import Vehicle
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import VehicleSerializer
from .permisions import IsVehicleOwner

class VehicleView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsVehicleOwner]

    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

    lookup_url_kwarg = "vehicle_id"

