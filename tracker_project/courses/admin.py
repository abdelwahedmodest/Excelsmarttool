# courses/admin.py
from django.contrib import admin
from .models import CourseCategory, Course

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'progress', 'user']
    list_filter = ['category', 'user']
    search_fields = ['name', 'description', 'category__name']

