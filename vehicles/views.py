import ipdb
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Vehicle
from .permisions import IsVehicleOwner
from .serializers import VehicleOrderSerializer, VehicleSerializer


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


class VehicleOrderView(generics.ListCreateAPIView):
    
    authentication_classes = [JWTAuthentication]

    serializer_class = VehicleOrderSerializer

    queryset = Vehicle.objects.all()

    def perform_create(self, serializer):
        
        vehicle_obj = get_object_or_404(Vehicle, id=self.kwargs.get("vehicle_id"))

        serializer.save(owner=vehicle_obj, buyer=self.request.user)
    


class VehicleOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    pass