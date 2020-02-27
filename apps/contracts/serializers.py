from rest_framework import serializers
from .models import Contract


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ('form', 'provider', 'client', 'number', 'contract_date', 'status', 'status_date', 'contract_image')


class ContractBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ('form', 'provider', 'number', 'contract_date', 'status')