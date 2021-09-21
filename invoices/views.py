from django.shortcuts import get_object_or_404
from rest_framework import generics, serializers
from rest_framework.pagination import LimitOffsetPagination
from .models import ServiceInvoice, SubInvoice, ProjectInvoice, SaleInvoice
from .serializers import \
    SaleInvoiceSerializer, SaleInvoiceBriefSerializer, \
    ServiceInvoiceSerializer, ServiceInvoiceBriefSerializer, \
    SubInvoiceSerializer, SubInvoiceBriefSerializer, \
    ProjectInvoiceSerializer, ProjectInvoiceBriefSerializer, \
    InvoicesLinkSerializer


class SaleInvoicesList(generics.ListCreateAPIView):
    queryset = SaleInvoice.objects.all()
    serializer_class = SaleInvoiceBriefSerializer
    pagination_class = LimitOffsetPagination


class SaleInvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SaleInvoiceSerializer

    def get_object(self):
        return get_object_or_404(SaleInvoice, pk=self.kwargs.get('serviceinvoice_id'))


class ServiceInvoicesList(generics.ListCreateAPIView):
    queryset = ServiceInvoice.objects.all()
    serializer_class = ServiceInvoiceBriefSerializer
    pagination_class = LimitOffsetPagination


class ServiceInvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ServiceInvoiceSerializer

    def get_object(self):
        return get_object_or_404(ServiceInvoice, pk=self.kwargs.get('serviceinvoice_id'))


class SubInvoicesList(generics.ListCreateAPIView):
    queryset = SubInvoice.objects.all()
    serializer_class = SubInvoiceBriefSerializer
    pagination_class = LimitOffsetPagination


class SubInvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubInvoiceSerializer

    def get_object(self):
        return get_object_or_404(SubInvoice, pk=self.kwargs.get('subinvoice_id'))


class ProjectInvoiceList(generics.ListCreateAPIView):
    queryset = ProjectInvoice.objects.all()
    serializer_class = ProjectInvoiceBriefSerializer
    pagination_class = LimitOffsetPagination


class ProjectInvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectInvoiceSerializer

    def get_object(self):
        return get_object_or_404(ProjectInvoice, pk=self.kwargs.get('projectinvoice_id'))


class InvoicesList(generics.ListAPIView):
    serializer_class = InvoicesLinkSerializer
    pagination_class = LimitOffsetPagination

