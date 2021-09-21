from django.shortcuts import get_object_or_404
from rest_framework import generics, serializers

from django.urls import reverse
from rest_framework.pagination import LimitOffsetPagination
from .models import Equipment, Service, Sim, Gps, FuelSensor
from .serializers import \
    EquipmentSerializer, EquipmentBriefSerializer, \
    ServiceSerializer, ServiceBriefSerializer, \
    SimSerializer, SimBriefSerializer, \
    GpsSerializer, GpsBriefSerializer, \
    FuelSensorSerializer, FuelSensorBriefSerializer,\
    ProductsLinkSerializer


class EquipmentList(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentBriefSerializer
    pagination_class = LimitOffsetPagination


class EquipmentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EquipmentSerializer

    def get_object(self):
        return get_object_or_404(Equipment, pk=self.kwargs.get('equipment_id'))


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceBriefSerializer
    pagination_class = LimitOffsetPagination


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceSerializer

    def get_object(self):
        return get_object_or_404(Service, pk=self.kwargs.get('service_id'))


class SimList(generics.ListCreateAPIView):
    queryset = Sim.objects.all()
    serializer_class = SimBriefSerializer
    pagination_class = LimitOffsetPagination


class SimDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SimSerializer

    def get_object(self):
        return get_object_or_404(Sim, pk=self.kwargs.get('sim_id'))


class GpsList(generics.ListCreateAPIView):
    queryset = Gps.objects.all()
    serializer_class = GpsBriefSerializer
    pagination_class = LimitOffsetPagination


class GpsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GpsSerializer

    def get_object(self):
        return get_object_or_404(Gps, pk=self.kwargs.get('gps_id'))


class FuelSensorList(generics.ListCreateAPIView):
    queryset = FuelSensor.objects.all()
    serializer_class = FuelSensorBriefSerializer
    pagination_class = LimitOffsetPagination


class FuelSensorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FuelSensorSerializer

    def get_object(self):
        return get_object_or_404(FuelSensor, pk=self.kwargs.get('fuelsensor_id'))


class ProductsList(generics.ListAPIView):
    serializer_class = ProductsLinkSerializer
    pagination_class = LimitOffsetPagination


