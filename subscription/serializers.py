from rest_framework import serializers
from .models import Subscription, Letters
from django.utils.html import format_html


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class SubscriptionBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('client', 'quarter', 'year', 'status', 'price_quarter', 'sum_payment')


class LettersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letters
        fields = '__all__'


class LettersBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letters
        fields = ('date_letter', 'client', 'action', 'vehicle', 'status',)


class SubLettersLinkSerializer(serializers.Serializer):
    subscription = format_html("<a href='../../subscriptions/subscriptions/'>Абонплата</a>")
    letters = format_html("<a href='../../subscriptions/letters/'>Звернення</a>")
