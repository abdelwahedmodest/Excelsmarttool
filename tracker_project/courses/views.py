from django.shortcuts import render
from django.http import HttpResponse

def course_list(request):
    return HttpResponse("List of courses")

def course_detail(request, pk):
    return HttpResponse(f"Details for course with id {pk}")
