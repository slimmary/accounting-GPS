from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Client, ClientPostAddress, ContactProfile

from .serializers import ClientSerializer, ClientPostAddressSerializer, ContactProfileSerializer, \
    ClientPostAddressBriefSerializer


# Create your views here.
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = LimitOffsetPagination


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientSerializer

    def get_object(self):
        obj = get_object_or_404(Client, pk=self.kwargs.get('client_id'))
        return obj


class ClientPostAddressList(generics.ListCreateAPIView):
    queryset = ClientPostAddress.objects.all()
    serializer_class = ClientPostAddressBriefSerializer
    pagination_class = LimitOffsetPagination


class ClientPostAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClientPostAddressSerializer

    def get_object(self):
        obj = get_object_or_404(ClientPostAddress, pk=self.kwargs.get('address_id'))
        return obj


class ContactProfileList(generics.ListCreateAPIView):
    queryset = ContactProfile.objects.all()
    serializer_class = ContactProfileSerializer
    pagination_class = LimitOffsetPagination


class ContactProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactProfileSerializer

    def get_object(self):
        obj = get_object_or_404(ContactProfile, pk=self.kwargs.get('profile_id'))
        return obj
