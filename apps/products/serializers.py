'''
from rest_framework import serializers
from .models import Sim

class SimSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sim
        fields = ('id',
                  'operator',
                  'number',
                  'account_number',
                  'date_receive',
                  'rate',
                  'packet_volume',
                  'rate_volume',
                  'installer',
                  'date_given',
                  )


class SimBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sim
        fields = (
                  'operator',
                  'number',
                  'account_number',
                  'date_receive',
                  'rate',
                  'packet_volume',
                  'rate_volume',
                  'installer',
                  'date_given',
                  )
'''