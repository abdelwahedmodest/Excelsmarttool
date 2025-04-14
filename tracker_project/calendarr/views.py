
# calendar/views.py
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from datetime import datetime
from .models import CalendarEvent
from .serializers import CalendarEventSerializer

class CalendarEventViewSet(viewsets.ModelViewSet):
    serializer_class = CalendarEventSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['start_datetime', 'title']
    
    def get_queryset(self):
        queryset = CalendarEvent.objects.filter(user=self.request.user)
        
        # Filter by date range
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        
        if start_date and end_date:
            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d')
                end_date = datetime.strptime(end_date, '%Y-%m-%d')
                queryset = queryset.filter(
                    Q(start_datetime__date__range=[start_date, end_date]) | 
                    Q(end_datetime__date__range=[start_date, end_date])
                )
            except ValueError:
                pass
        
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

