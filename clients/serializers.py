from rest_framework import serializers
from .models import ClientAddress, Client, ClientLegalDetail, ContactProfile


class ClientAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAddress
        fields = '__all__'


class ContactProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactProfile
        fields = '__all__'


class ContactProfileBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactProfile
        fields = ('firstname', 'surname', 'phone', 'email')


class ClientLegalDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientLegalDetail
        fields = '__all__'


class ClientLegalDetailBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientLegalDetail
        fields = ('IPN', 'director', 'IBAN', 'bank', 'legal_address', 'post_address')


class ClientSerializer(serializers.ModelSerializer):
    client_legal_detail = ClientLegalDetailBriefSerializer()
    contacts = ContactProfileBriefSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ('name', 'login', 'day_start', 'contacts', 'client_legal_detail', 'status', 'edrpou',)


class ClientBriefSerializer(serializers.ModelSerializer):
    contacts = ContactProfileBriefSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ('name', 'login', 'contacts')


