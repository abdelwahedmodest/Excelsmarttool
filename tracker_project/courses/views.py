# courses/views.py
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CourseCategory, Course
from .serializers import CourseCategorySerializer, CourseSerializer

class CourseCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CourseCategorySerializer
    queryset = CourseCategory.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name']

class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['name', 'progress']
    
    def get_queryset(self):
        queryset = Course.objects.filter(user=self.request.user)
        
        # Filter by category
        category_id = self.request.query_params.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        
        # Filter by progress range
        min_progress = self.request.query_params.get('min_progress')
        max_progress = self.request.query_params.get('max_progress')
        
        if min_progress is not None:
            queryset = queryset.filter(progress__gte=float(min_progress))
        
        if max_progress is not None:
            queryset = queryset.filter(progress__lte=float(max_progress))
        
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def progress_stats(self, request):
        """Get statistics about course progress."""
        total_courses = Course.objects.filter(user=request.user).count()
        completed_courses = Course.objects.filter(user=request.user, progress=1.0).count()
        in_progress_courses = Course.objects.filter(user=request.user, progress__gt=0, progress__lt=1.0).count()
        not_started_courses = Course.objects.filter(user=request.user, progress=0).count()
        
        avg_progress = 0
        if total_courses > 0:
            avg_progress = Course.objects.filter(user=request.user).aggregate(
                avg_progress=models.Avg('progress')
            )['avg_progress'] or 0
        
        return Response({
            'total_courses': total_courses,
            'completed_courses': completed_courses,
            'in_progress_courses': in_progress_courses,
            'not_started_courses': not_started_courses,
            'avg_progress': avg_progress
        })

