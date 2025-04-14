
# calendar/serializers.py
from rest_framework import serializers
from .models import CalendarEvent

class CalendarEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarEvent
        fields = ['id', 'title', 'description', 'start_datetime', 'end_datetime', 
                  'all_day', 'location', 'repeat', 'color', 'user']
        read_only_fields = ['user']
