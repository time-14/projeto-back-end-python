from rest_framework import permissions
from rest_framework.views import Request, View
from vehicles.models import Vehicle


class IsVehicleOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Vehicle):
        return request.user.is_authenticated and request.user == obj