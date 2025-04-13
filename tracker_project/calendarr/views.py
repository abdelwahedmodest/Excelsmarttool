from django.shortcuts import render
from django.http import HttpResponse

def calendarr_view(request):
    return HttpResponse("Calendarr View")

def event_detail(request, event_id):
    return HttpResponse(f"Event Detail View for event {event_id}")
