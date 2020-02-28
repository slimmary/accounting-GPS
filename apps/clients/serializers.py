from rest_framework import serializers
from .models import Client, ClientPostAddress, ContactProfile
from apps.contracts.serializers import ContractBriefSerializer
from apps.contracts.models import Contract


class ClientPostAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientPostAddress
        fields = ('id', 'index', 'region', 'district',
                  'city', 'street', 'house', 'office', 'client')


class ClientPostAddressBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientPostAddress
        fields = ('id', 'index', 'region', 'district',
                  'city', 'street', 'house', 'office')


class ContactProfileBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactProfile
        fields = ('id', 'firstname', 'surname', 'patronymic',
                  'position', 'phone', 'phone_2', 'email')


class ContactProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactProfile
        fields = ('id', 'firstname', 'surname', 'patronymic',
                  'position', 'phone', 'phone_2', 'email', 'client_field')


class ClientSerializer(serializers.ModelSerializer):
    address = ClientPostAddressBriefSerializer
    contacts = ContactProfileBriefSerializer
    contracts = ContractBriefSerializer

    class Meta:
        model = Client
        fields = ('id', 'name', 'status', 'pay_form', 'login',
                  'address', 'contacts', 'contracts')

    
class ClientBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'name', 'status', 'login')
