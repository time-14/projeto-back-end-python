from django.urls import path
from .views import VehicleView, VehicleDetailView

urlpatterns = [
    path('vehicles', VehicleView.as_view()),
    path('vehicles/<int:pk>/', VehicleDetailView.as_view()),
]