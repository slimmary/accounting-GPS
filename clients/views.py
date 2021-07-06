from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from .models import ClientAddress, Client, ClientLegalDetail, ContactProfile
from .serializers import ClientAddressSerializer, ContactProfileSerializer, ClientLegalDetailSerializer, ClientSerializer


class ClientAddressList(generics.ListCreateAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressSerializer
    pagination_class = LimitOffsetPagination


class ClientAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientAddressSerializer

    def get_object(self):
        return get_object_or_404(ClientAddress, pk=self.kwargs.get('clientaddress_id'))


class ContactProfileList(generics.ListCreateAPIView):
    queryset = ContactProfile.objects.all()
    serializer_class = ContactProfileSerializer
    pagination_class = LimitOffsetPagination


class ContactProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactProfileSerializer

    def get_object(self):
        return get_object_or_404(ContactProfile, pk=self.kwargs.get('contactprofile_id'))


class ClientLegalDetailList(generics.ListCreateAPIView):
    queryset = ClientLegalDetail.objects.all()
    serializer_class = ClientLegalDetailSerializer
    pagination_class = LimitOffsetPagination


class ClientLegalDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientLegalDetailSerializer

    def get_object(self):
        return get_object_or_404(ClientLegalDetail, pk=self.kwargs.get('clientlegaldetail_id'))


class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = LimitOffsetPagination


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer

    def get_object(self):
        return get_object_or_404(Client, pk=self.kwargs.get('client_id'))

