"""
运行Django开发服务器
"""
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

from django.core.management import execute_from_command_line

print("=" * 60)
print("启动 AI大模型管理系统 开发服务器")
print("=" * 60)
print("\n访问地址: http://127.0.0.1:8000/")
print("按 Ctrl+C 停止服务器\n")
print("=" * 60)

execute_from_command_line(['manage.py', 'runserver'])
