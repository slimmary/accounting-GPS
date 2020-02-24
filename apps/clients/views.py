from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Client, ClientPostAdress, ContactProfile, ContactPhone, ContactEmail
 
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


class ClientPostAdressList(generics.ListCreateAPIView):
      queryset = ClientPostAdress.objects.all()
      serializer_class = ClientPostAdressSerializer
      pagination_class = LimitOffsetPagination

class ClientPostAdressDetail(generics.RetrieveUpdateDestroyAPIView):
      serializer_class = ClientPostAdressSerializer

      def get_object(self):
        obj = get_object_or_404(ClientPostAdress, pk=self.kwargs.get('adress_id'))
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


class ContactPhoneList(generics.ListCreateAPIView):
      queryset = ContactPhone.objects.all()
      serializer_class = ContactPhoneSerializer
      pagination_class = LimitOffsetPagination

class ContactPhoneDetail(generics.RetrieveUpdateDestroyAPIView):
      serializer_class = ContactPhoneSerializer

      def get_object(self):
        obj = get_object_or_404(ContactPhone, pk=self.kwargs.get('phone_id'))
        return obj

      
class ContactEmailList(generics.ListCreateAPIView):
      queryset = ContactEmail.objects.all()
      serializer_class = ContactEmailSerializer
      pagination_class = LimitOffsetPagination

class ContactEmailDetail(generics.RetrieveUpdateDestroyAPIView):
      serializer_class = ContactEmailSerializer

      def get_object(self):
        obj = get_object_or_404(ContactEmail, pk=self.kwargs.get('email_id'))
        return obj
