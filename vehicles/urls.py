from django.urls import path

from .views import (VehicleDetailView, VehicleOrderDetailView,
                    VehicleOrderView, VehicleView)

urlpatterns = [
    path('vehicles/', VehicleView.as_view()),
    path('vehicles/<int:pk>/', VehicleDetailView.as_view()),
    path('vehicles/<uuid:vehicle_id>/orders/', VehicleOrderView.as_view()),
    path('vehicles/<int:order_id>/orders/', VehicleOrderDetailView.as_view()),
]