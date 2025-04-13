# tracking/views.py
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Q
from .models import Category, Activity, CheckPoint, Resource
from .serializers import CategorySerializer, ActivitySerializer, CheckPointSerializer, ResourceSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name']
    
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'status', 'category__name']
    ordering_fields = ['name', 'start_date', 'end_date', 'created_at', 'updated_at', 'progress']
    
    def get_queryset(self):
        queryset = Activity.objects.filter(user=self.request.user)
        
        # Filter by category
        category_id = self.request.query_params.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        
        # Filter by status
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        
        # Filter by date range
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if start_date and end_date:
            queryset = queryset.filter(
                Q(start_date__range=[start_date, end_date]) | 
                Q(end_date__range=[start_date, end_date])
            )
        
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CheckPointViewSet(viewsets.ModelViewSet):
    serializer_class = CheckPointSerializer
    
    def get_queryset(self):
        activity_id = self.request.query_params.get('activity_id')
        if activity_id:
            return CheckPoint.objects.filter(activity_id=activity_id, activity__user=self.request.user)
        return CheckPoint.objects.filter(activity__user=self.request.user)

class ResourceViewSet(viewsets.ModelViewSet):
    serializer_class = ResourceSerializer
    parser_classes = [MultiPartParser, FormParser]
    
    def get_queryset(self):
        activity_id = self.request.query_params.get('activity_id')
        if activity_id:
            return Resource.objects.filter(activity_id=activity_id, activity__user=self.request.user)
        return Resource.objects.filter(activity__user=self.request.user)
