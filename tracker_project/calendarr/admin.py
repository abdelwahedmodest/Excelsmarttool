
# calendar/admin.py
from django.contrib import admin
from .models import CalendarEvent

@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_datetime', 'end_datetime', 'user']
    list_filter = ['start_datetime', 'all_day', 'user']
    search_fields = ['title', 'description', 'location']

