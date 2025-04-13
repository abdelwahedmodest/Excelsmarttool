# tracking/serializers.py
from rest_framework import serializers
from .models import Category, Activity, CheckPoint, Resource

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['user']

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'
        read_only_fields = ['uploaded_at']

class CheckPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckPoint
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    checkpoints = CheckPointSerializer(many=True, read_only=True)
    resources = ResourceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Activity
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']