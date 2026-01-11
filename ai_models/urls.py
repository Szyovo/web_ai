"""
URL configuration for AI Models app
"""
from django.urls import path
from . import views

urlpatterns = [
    # 用户认证
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # AI模型管理
    path('', views.ai_model_list, name='ai_model_list'),
    path('models/', views.ai_model_list, name='ai_model_list'),
    path('models/create/', views.ai_model_create, name='ai_model_create'),
    path('models/<int:pk>/', views.ai_model_detail, name='ai_model_detail'),
    path('models/<int:pk>/edit/', views.ai_model_edit, name='ai_model_edit'),
    path('models/<int:pk>/delete/', views.ai_model_delete, name='ai_model_delete'),
    path('models/export/', views.export_models_csv, name='export_models_csv'),

    # 模型类型管理
    path('types/', views.model_type_list, name='model_type_list'),
    path('types/create/', views.model_type_create, name='model_type_create'),
    path('types/<int:pk>/edit/', views.model_type_edit, name='model_type_edit'),
    path('types/<int:pk>/delete/', views.model_type_delete, name='model_type_delete'),
]
