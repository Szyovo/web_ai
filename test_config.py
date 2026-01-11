import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from ai_models.models import AIModel, ModelType

print("Django配置成功！")
print(f"模型类: {AIModel.__name__}, {ModelType.__name__}")
