# projects/views.py
from rest_framework import viewsets, filters
from .models import Project, ProjectTask
from .serializers import ProjectSerializer, ProjectTaskSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'category']
    ordering_fields = ['name', 'start_date', 'end_date']
    
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProjectTaskViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectTaskSerializer
    
    def get_queryset(self):
        project_id = self.request.query_params.get('project_id')
        if project_id:
            return ProjectTask.objects.filter(project_id=project_id, project__user=self.request.user)
        return ProjectTask.objects.filter(project__user=self.request.user)
