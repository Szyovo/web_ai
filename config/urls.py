"""
URL configuration for AI Model Management System project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ai_models.urls')),
]
