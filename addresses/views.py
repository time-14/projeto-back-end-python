from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from addresses.models import Address
from addresses.serializers import AddressSerialiazer
from users.models import User


class AddressView(ListCreateAPIView):
    serializer_class = AddressSerialiazer

    queryset = Address.objects.all()

    def perform_create(self, serializer):
        address_obj = get_object_or_404(Address, pk=self.kwargs.get("pk"))
        serializer.save(address=address_obj)