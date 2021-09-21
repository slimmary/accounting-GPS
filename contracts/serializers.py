from rest_framework import serializers
from .models import Contract, Additions


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class ContractBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('number', 'contract_date', 'status', 'type', 'provider', 'client')


class AdditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additions
        fields = '__all__'


class AdditionsBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Additions
        fields = ('number', 'contract_date', 'status', 'type', 'contract_to', 'client')