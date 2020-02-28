from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Vehicle

from .serializers import VehicleSerializer


class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    pagination_class = LimitOffsetPagination


class ContractDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer

    def get_object(self):
        obj = get_object_or_404(Vehicle, pk=self.kwargs.get('vehicle_id'))
        return obj
