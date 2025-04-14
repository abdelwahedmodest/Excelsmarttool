# courses/serializers.py
from rest_framework import serializers
from .models import CourseCategory, Course

class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name', read_only=True)
    
    class Meta:
        model = Course
        fields = ['id', 'name', 'category', 'category_name', 'progress', 'description', 'user']
        read_only_fields = ['user']
