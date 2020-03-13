from rest_framework import serializers
from .models import Contract, ContractSupplementary


class ContractSupplementarySerializer(serializers.ModelSerializer):
    model = ContractSupplementary
    fields = ('number', 'date',)


class ContractSerializer(serializers.ModelSerializer):
    supplementary = ContractSupplementarySerializer

    class Meta:
        model = Contract
        fields = (
            'form',
            'provider',
            'client',
            'number',
            'contract_date',
            'status',
            'status_date',
            'contract_image',
            'supplementary',
        )


class ContractBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ('form', 'provider', 'number', 'contract_date', 'status')

