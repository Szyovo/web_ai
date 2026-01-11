"""
Django Admin configuration for AI Model Management System
"""
from django.contrib import admin
from .models import ModelType, AIModel


@admin.register(ModelType)
class ModelTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name', 'description']


@admin.register(AIModel)
class AIModelAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'version', 'model_type', 'developer',
        'is_open_source', 'is_active', 'release_date'
    ]
    list_filter = ['model_type', 'is_open_source', 'is_commercial', 'is_active']
    search_fields = ['name', 'developer', 'description']
    date_hierarchy = 'release_date'
