from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from .models import Contract

from .serializers import ContractSerializer, ContractBriefSerializer


class ContractList(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractBriefSerializer
    pagination_class = LimitOffsetPagination


class ContractDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContractSerializer

    def get_object(self):
        obj = get_object_or_404(Contract, pk=self.kwargs.get('contract_id'))
        return obj
