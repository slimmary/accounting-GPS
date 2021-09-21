from django.shortcuts import get_object_or_404
from rest_framework import generics, serializers
from rest_framework.pagination import LimitOffsetPagination
from .models import Vehicle
from .serializers import VehicleSerializer, VehicleBriefSerializer


class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleBriefSerializer
    pagination_class = LimitOffsetPagination


class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer

    def get_object(self):
        return get_object_or_404(Vehicle, pk=self.kwargs.get('vehicle_id'))

