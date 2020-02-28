from rest_framework import serializers
from apps.users.models import UserProfile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'last_login' ]


class UserProfileBriefSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = UserProfile
        fields = ('user', 'date_start_work', 'position', 'birthday', 'phone')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer

    class Meta:
        model = UserProfile
        fields = ('user', 'date_start_work', 'status', 'position', 'birthday', 'avatar', 'phone')
