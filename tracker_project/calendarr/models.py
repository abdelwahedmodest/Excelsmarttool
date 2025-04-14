# calendar/models.py
from django.db import models
from users.models import User

class CalendarEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField(null=True, blank=True)
    all_day = models.BooleanField(default=False)
    location = models.CharField(max_length=255, blank=True)
    repeat = models.CharField(max_length=20, blank=True)  # daily, weekly, monthly, yearly
    color = models.CharField(max_length=7, default="#3788d8")  # Hex color code
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calendar_events')
    
    def __str__(self):
        return self.title
