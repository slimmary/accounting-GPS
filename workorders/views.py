# from django.shortcuts import get_object_or_404
# from rest_framework import generics, serializers
# from rest_framework.pagination import LimitOffsetPagination
# from .models import Subscription, Letters
# from .serializers import SubscriptionSerializer, SubscriptionBriefSerializer, LettersSerializer, LettersBriefSerializer,\
# SubLettersLinkSerializer
#
#
# class SubscriptionList(generics.ListCreateAPIView):
#     queryset = Subscription.objects.all()
#     serializer_class = SubscriptionBriefSerializer
#     pagination_class = LimitOffsetPagination
#
#
# class SubscriptionDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = SubscriptionSerializer
#
#     def get_object(self):
#         return get_object_or_404(Subscription, pk=self.kwargs.get('subscription_id'))
#
#
# class LettersList(generics.ListCreateAPIView):
#     queryset = Letters.objects.all()
#     serializer_class = LettersBriefSerializer
#     pagination_class = LimitOffsetPagination
#
#
# class LettersDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = LettersSerializer
#
#     def get_object(self):
#         return get_object_or_404(Letters, pk=self.kwargs.get('letters_id'))
#
#
# class SubLettersList(generics.ListAPIView):
#     serializer_class = SubLettersLinkSerializer
#     pagination_class = LimitOffsetPagination
#
