
# tracker_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/tracking/', include('tracking.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/courses/', include('courses.urls')),
    path('api/calendarr/', include('calendarr.urls')),
    path('api/token-auth/', views.obtain_auth_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)