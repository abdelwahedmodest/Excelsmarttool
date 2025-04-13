from django.contrib import admin
from .models import *  # Replace * with specific model names if needed

# Register your models here.
admin.site.register(CalendarEvent)  # Example: Register the Event model
# Register other models from the calendarr app here
