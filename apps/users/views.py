from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from apps.users.models import UserProfile
from apps.users.serializers import UserProfileSerializer, UserProfileBriefSerializer

# Create your views here.


class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileBriefSerializer
    pagination_class = LimitOffsetPagination


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        obj = get_object_or_404(UserProfile, pk=self.kwargs.get('user_profile_id'))
        return obj
