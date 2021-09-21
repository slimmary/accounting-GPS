from django.shortcuts import get_object_or_404
from rest_framework import generics, serializers
from rest_framework.pagination import LimitOffsetPagination
from .models import Project
from .serializers import ProjectSerializer, ProjectBriefSerializer


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectBriefSerializer
    pagination_class = LimitOffsetPagination


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer

    def get_object(self):
        return get_object_or_404(Project, pk=self.kwargs.get('project_id'))
