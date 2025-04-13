# users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserSettingsViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'settings', UserSettingsViewSet, basename='settings')

urlpatterns = [
    path('', include(router.urls)),
]