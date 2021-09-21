from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('number', 'date_start', 'project_status', 'client')

