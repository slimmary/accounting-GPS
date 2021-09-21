from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination


from .models import Contract, Additions
from .serializers import ContractSerializer, ContractBriefSerializer, AdditionsSerializer, AdditionsBriefSerializer


class ContractList(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractBriefSerializer
    pagination_class = LimitOffsetPagination


class ContractDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContractSerializer

    def get_object(self):
        return get_object_or_404(Contract, pk=self.kwargs.get('contract_id'))


class AdditionsList(generics.ListCreateAPIView):
    queryset = Additions.objects.all()
    serializer_class = AdditionsBriefSerializer
    pagination_class = LimitOffsetPagination


class AdditionsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdditionsSerializer

    def get_object(self):
        return get_object_or_404(Additions, pk=self.kwargs.get('additions_id'))