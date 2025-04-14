# courses/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseCategoryViewSet, CourseViewSet

router = DefaultRouter()
router.register(r'categories', CourseCategoryViewSet, basename='course-category')
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router.urls)),
]
