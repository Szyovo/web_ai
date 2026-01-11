"""
Custom decorators for AI Model Management System
"""
from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def login_required_with_message(function):
    """
    自定义登录装饰器，未登录时显示消息并重定向
    """
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, '请先登录才能执行此操作')
            return redirect('login')
        return function(request, *args, **kwargs)
    return wrap


def admin_required(function):
    """
    管理员权限装饰器
    """
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, '请先登录')
            return redirect('login')
        if not request.user.is_staff:
            messages.error(request, '需要管理员权限')
            return redirect('ai_model_list')
        return function(request, *args, **kwargs)
    return wrap


def check_model_ownership(function):
    """
    检查模型所有权（示例装饰器）
    """
    @wraps(function)
    @login_required
    def wrap(request, *args, **kwargs):
        # 这里可以添加所有权检查逻辑
        return function(request, *args, **kwargs)
    return wrap
