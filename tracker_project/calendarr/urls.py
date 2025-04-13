from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendarr_view, name='calendarr_view'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
]