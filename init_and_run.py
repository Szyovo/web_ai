"""
初始化和运行Django项目的脚本
"""
import os
import sys
import django

# 设置Django设置模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 初始化Django
django.setup()

from django.core.management import execute_from_command_line

print("=" * 60)
print("AI大模型管理系统 - 初始化脚本")
print("=" * 60)

# 步骤1: 创建迁移文件
print("\n[步骤1] 创建数据库迁移文件...")
execute_from_command_line(['manage.py', 'makemigrations'])

# 步骤2: 执行迁移
print("\n[步骤2] 执行数据库迁移...")
execute_from_command_line(['manage.py', 'migrate'])

# 步骤3: 创建测试数据
print("\n[步骤3] 创建测试数据...")
from ai_models.models import ModelType, AIModel
from django.contrib.auth.models import User
from datetime import date
from decimal import Decimal

# 创建模型类型
types_data = [
    {'name': '语言模型', 'description': '基于自然语言处理的大模型，如GPT、BERT等'},
    {'name': '音频模型', 'description': '处理音频数据的AI模型，如语音识别、语音合成等'},
    {'name': '视频模型', 'description': '处理视频内容的AI模型，如视频生成、视频理解等'},
    {'name': '图像模型', 'description': '处理图像数据的AI模型，如图像识别、图像生成等'},
    {'name': '多模态模型', 'description': '能够处理多种数据类型的综合AI模型'},
]

created_types = []
for type_data in types_data:
    model_type, created = ModelType.objects.get_or_create(
        name=type_data['name'],
        defaults={'description': type_data['description']}
    )
    created_types.append(model_type)
    if created:
        print(f"  [OK] 创建模型类型: {model_type.name}")
    else:
        print(f"  [SKIP] 模型类型已存在: {model_type.name}")

# 创建AI模型示例数据
models_data = [
    {
        'name': 'GPT-4',
        'version': 'v4.0',
        'description': 'OpenAI开发的第四代大型语言模型，具有强大的理解和生成能力',
        'model_type': created_types[0],  # 语言模型
        'release_date': date(2023, 3, 14),
        'parameters_count': 1000000000000,  # 1万亿参数
        'accuracy_score': Decimal('96.50'),
        'training_hours': 10000,
        'is_open_source': False,
        'is_commercial': True,
        'is_active': True,
        'contact_email': 'contact@openai.com',
        'contact_phone': '13800138001',
        'developer': 'OpenAI',
        'website_url': 'https://openai.com'
    },
    {
        'name': 'Claude 3',
        'version': 'v3.5',
        'description': 'Anthropic开发的对话式AI助手，注重安全性和有用性',
        'model_type': created_types[0],  # 语言模型
        'release_date': date(2024, 6, 20),
        'parameters_count': 500000000000,  # 5000亿参数
        'accuracy_score': Decimal('95.80'),
        'training_hours': 8000,
        'is_open_source': False,
        'is_commercial': True,
        'is_active': True,
        'contact_email': 'contact@anthropic.com',
        'contact_phone': '13800138002',
        'developer': 'Anthropic',
        'website_url': 'https://anthropic.com'
    },
    {
        'name': 'Whisper',
        'version': 'v3',
        'description': 'OpenAI开发的自动语音识别（ASR）系统',
        'model_type': created_types[1],  # 音频模型
        'release_date': date(2023, 11, 15),
        'parameters_count': 1550000000,  # 15.5亿参数
        'accuracy_score': Decimal('94.20'),
        'training_hours': 2000,
        'is_open_source': True,
        'is_commercial': False,
        'is_active': True,
        'contact_email': 'whisper@openai.com',
        'contact_phone': '13800138003',
        'developer': 'OpenAI',
        'website_url': 'https://github.com/openai/whisper'
    },
    {
        'name': 'Stable Video Diffusion',
        'version': 'v1.1',
        'description': 'Stability AI开发的视频生成模型',
        'model_type': created_types[2],  # 视频模型
        'release_date': date(2023, 11, 21),
        'parameters_count': 2000000000,  # 20亿参数
        'accuracy_score': Decimal('88.50'),
        'training_hours': 5000,
        'is_open_source': True,
        'is_commercial': False,
        'is_active': True,
        'contact_email': 'contact@stability.ai',
        'contact_phone': '13800138004',
        'developer': 'Stability AI',
        'website_url': 'https://stability.ai'
    },
    {
        'name': 'DALL-E 3',
        'version': 'v3.0',
        'description': 'OpenAI开发的文本到图像生成模型',
        'model_type': created_types[3],  # 图像模型
        'release_date': date(2023, 10, 5),
        'parameters_count': 3500000000,  # 35亿参数
        'accuracy_score': Decimal('92.30'),
        'training_hours': 6000,
        'is_open_source': False,
        'is_commercial': True,
        'is_active': True,
        'contact_email': 'dalle@openai.com',
        'contact_phone': '13800138005',
        'developer': 'OpenAI',
        'website_url': 'https://openai.com/dall-e-3'
    },
    {
        'name': 'GPT-4V',
        'version': 'v4.0-vision',
        'description': '具有视觉理解能力的GPT-4多模态版本',
        'model_type': created_types[4],  # 多模态模型
        'release_date': date(2023, 9, 25),
        'parameters_count': 1000000000000,  # 1万亿参数
        'accuracy_score': Decimal('94.70'),
        'training_hours': 12000,
        'is_open_source': False,
        'is_commercial': True,
        'is_active': True,
        'contact_email': 'gpt4v@openai.com',
        'contact_phone': '13800138006',
        'developer': 'OpenAI',
        'website_url': 'https://openai.com'
    },
    # 新增更多语言模型
    {
        'name': 'LLaMA 3',
        'version': 'v3.1',
        'description': 'Meta开发的开源大语言模型，性能卓越',
        'model_type': created_types[0],
        'release_date': date(2024, 4, 18),
        'parameters_count': 70000000000,
        'accuracy_score': Decimal('93.80'),
        'training_hours': 5500,
        'is_open_source': True,
        'is_commercial': False,
        'is_active': True,
        'contact_email': 'llama@meta.com',
        'contact_phone': '13800138007',
        'developer': 'Meta AI',
        'website_url': 'https://ai.meta.com/llama'
    },
    {
        'name': 'Gemini Pro',
        'version': 'v1.5',
        'description': 'Google开发的多模态AI模型，支持超长上下文',
        'model_type': created_types[4],
        'release_date': date(2024, 2, 15),
        'parameters_count': 800000000000,
        'accuracy_score': Decimal('95.20'),
        'training_hours': 9000,
        'is_open_source': False,
        'is_commercial': True,
        'is_active': True,
        'contact_email': 'gemini@google.com',
        'contact_phone': '13800138008',
        'developer': 'Google DeepMind',
        'website_url': 'https://deepmind.google/gemini'
    },
    {
        'name': 'Mistral Large',
        'version': 'v2.0',
        'description': '欧洲开发的高性能语言模型',
        'model_type': created_types[0],
        'release_date': date(2024, 3, 10),
        'parameters_count': 123000000000,
        'accuracy_score': Decimal('92.50'),
        'training_hours': 4000,
        'is_open_source': True,
        'is_commercial': False,
        'is_active': True,
        'contact_email': 'contact@mistral.ai',
        'contact_phone': '13800138009',
        'developer': 'Mistral AI',
        'website_url': 'https://mistral.ai'
    },
    {
        'name': 'Qwen',
        'version': 'v2.5',
        'description': '阿里巴巴通义千问大模型，中文表现优异',
        'model_type': created_types[0],
        'release_date': date(2024, 5, 20),
        'parameters_count': 72000000000,
        'accuracy_score': Decimal('94.10'),
        'training_hours': 4500,
        'is_open_source': True,
        'is_commercial': False,
        'is_active': True,
        'contact_email': 'qwen@alibaba.com',
        'contact_phone': '13800138010',
        'developer': '阿里巴巴',
        'website_url': 'https://tongyi.aliyun.com'
    },
    # 新增音频模型
    {
        'name': 'AudioLM',
        'version': 'v2.0',
        'description': 'Google开发的音频语言模型',
        'model_type': created_types[1],
        'release_date': date(2023, 8, 12),
        'parameters_count': 2000000000,
        'accuracy_score': Decimal('91.50'),
        'training_hours': 3000,
        'is_open_source': False,
        'is_commercial': True,
        'is_active': True,
        'contact_email': 'audiolm@google.com',
        'contact_phone': '13800138011',
        'developer': 'Google Research',
        'website_url': 'https://google-research.github.io/seanet/audiolm'
    },
    {
        'name': 'WavLM',
        'version': 'v1.0',
        'description': 'Microsoft的大型自监督语音预训练模型',
        'model_type': created_types[1],
        'release_date': date(2023, 6, 5),
        'parameters_count': 1800000000,
        'accuracy_score': Decimal('93.20'),
        'training_hours': 2500,
        'is_open_source': True,
        'is_commercial': False,
        'is_active': True,
        'contact_email': 'wavlm@microsoft.com',
        'contact_phone': '13800138012',
        'developer': 'Microsoft',
        'website_url': 'https://github.com/microsoft/unilm/tree/master/wavlm'
    },
    {
        'name': 'AudioCraft',
        'version': 'v1.3',
        'description': 'Meta的音频生成工具套件',
        'model_type': created_types[1],
        'release_date': date(2023, 9, 8),
        'parameters_count': 2500000000,
        'accuracy_score': Decimal('89.80'),
        'training_hours': 3500,
        'is_open_source': True,
        'is_commercial': False,
        'is_active': True,
        'contact_email': 'audiocraft@meta.com',
        'contact_phone': '13800138013',
        'developer': 'Meta AI',
        'website_url': 'https://audiocraft.metademolab.com'
    },
    # 新增图像模型
    {
        'name': 'Midjourney',
        'version': 'v6.0',
        'description': '顶级AI艺术图像生成平台',
        'model_type': created_types[3],
        'release_date': date(2023, 12, 21),
        'parameters_count': 5000000000,
        'accuracy_score': Decimal('96.00'),
        'training_hours': 8000,
        'is_open_source': False,
        'is_commercial': True,
        'is_active': True,
        'contact_email': 'support@midjourney.com',
        'contact_phone': '13800138014',
        'developer': 'Midjourney Inc',
        'website_url': 'https://midjourney.com'
    },
    {
        'name': 'Stable Diffusion XL',
        'version': 'v1.0',
        'description': 'Stability AI的旗舰图像生成模型',
        'model_type': created_types[3],
        'release_date': date(2023, 7, 26),
        'parameters_count': 6600000000,
        'accuracy_score': Decimal('93.50'),
        'training_hours': 7000,
        'is_open_source': True,
        'is_commercial': False,
        'is_active': True,
        'contact_email': 'sdxl@stability.ai',
        'contact_phone': '13800138015',
        'developer': 'Stability AI',
        'website_url': 'https://stability.ai/stable-diffusion'
    },
    {
        'name': 'Imagen',
        'version': 'v2.0',
        'description': 'Google的文本到图像扩散模型',
        'model_type': created_types[3],
        'release_date': date(2023, 5, 10),
        'parameters_count': 4500000000,
        'accuracy_score': Decimal('94.20'),
        'training_hours': 6500,
        'is_open_source': False,
        'is_commercial': True,
        'is_active': True,
        'contact_email': 'imagen@google.com',
        'contact_phone': '13800138016',
        'developer': 'Google Research',
        'website_url': 'https://imagen.research.google'
    },
    {
        'name': 'FLUX',
        'version': 'v1.0',
        'description': 'Black Forest Labs的新一代图像生成模型',
        'model_type': created_types[3],
        'release_date': date(2024, 8, 1),
        'parameters_count': 12000000000,
        'accuracy_score': Decimal('95.80'),
        'training_hours': 9000,
        'is_open_source': True,
        'is_commercial': False,
        'is_active': True,
        'contact_email': 'info@blackforestlabs.ai',
        'contact_phone': '13800138017',
        'developer': 'Black Forest Labs',
        'website_url': 'https://blackforestlabs.ai'
    },
    # 新增视频模型
    {
        'name': 'Sora',
        'version': 'v1.0',
        'description': 'OpenAI的革命性文本到视频生成模型',
        'model_type': created_types[2],
        'release_date': date(2024, 2, 15),
        'parameters_count': 10000000000,
        'accuracy_score': Decimal('90.50'),
        'training_hours': 15000,
        'is_open_source': False,
        'is_commercial': True,
        'is_active': True,
        'contact_email': 'sora@openai.com',
        'contact_phone': '13800138018',
        'developer': 'OpenAI',
        'website_url': 'https://openai.com/sora'
    },
    {
        'name': 'Runway Gen-3',
        'version': 'v3.0',
        'description': 'Runway的专业级视频生成AI',
        'model_type': created_types[2],
        'release_date': date(2024, 6, 10),
        'parameters_count': 8000000000,
        'accuracy_score': Decimal('92.30'),
        'training_hours': 10000,
        'is_open_source': False,
        'is_commercial': True,
        'is_active': True,
        'contact_email': 'gen3@runwayml.com',
        'contact_phone': '13800138019',
        'developer': 'Runway',
        'website_url': 'https://runwayml.com'
    },
    {
        'name': 'Pika',
        'version': 'v1.5',
        'description': '简单易用的AI视频生成工具',
        'model_type': created_types[2],
        'release_date': date(2024, 4, 3),
        'parameters_count': 5000000000,
        'accuracy_score': Decimal('88.90'),
        'training_hours': 7000,
        'is_open_source': False,
        'is_commercial': True,
        'is_active': True,
        'contact_email': 'support@pika.art',
        'contact_phone': '13800138020',
        'developer': 'Pika Labs',
        'website_url': 'https://pika.art'
    },
    # 新增多模态模型
    {
        'name': 'GPT-4o',
        'version': 'v1.0',
        'description': 'OpenAI的全模态GPT-4 Omni模型',
        'model_type': created_types[4],
        'release_date': date(2024, 5, 13),
        'parameters_count': 1000000000000,
        'accuracy_score': Decimal('97.20'),
        'training_hours': 13000,
        'is_open_source': False,
        'is_commercial': True,
        'is_active': True,
        'contact_email': 'gpt4o@openai.com',
        'contact_phone': '13800138021',
        'developer': 'OpenAI',
        'website_url': 'https://openai.com/gpt-4o'
    },
    {
        'name': 'Claude 3 Opus',
        'version': 'v3.0',
        'description': 'Anthropic最强大的多模态模型',
        'model_type': created_types[4],
        'release_date': date(2024, 3, 4),
        'parameters_count': 600000000000,
        'accuracy_score': Decimal('96.80'),
        'training_hours': 11000,
        'is_open_source': False,
        'is_commercial': True,
        'is_active': True,
        'contact_email': 'opus@anthropic.com',
        'contact_phone': '13800138022',
        'developer': 'Anthropic',
        'website_url': 'https://anthropic.com/claude'
    },
    {
        'name': 'Gemini Ultra',
        'version': 'v1.0',
        'description': 'Google最先进的多模态AI模型',
        'model_type': created_types[4],
        'release_date': date(2023, 12, 6),
        'parameters_count': 900000000000,
        'accuracy_score': Decimal('96.50'),
        'training_hours': 12000,
        'is_open_source': False,
        'is_commercial': True,
        'is_active': True,
        'contact_email': 'ultra@google.com',
        'contact_phone': '13800138023',
        'developer': 'Google DeepMind',
        'website_url': 'https://deepmind.google/gemini'
    },
    # 更多语言模型
    {
        'name': 'ChatGLM',
        'version': 'v4.0',
        'description': '智谱AI的中英双语对话模型',
        'model_type': created_types[0],
        'release_date': date(2024, 1, 15),
        'parameters_count': 130000000000,
        'accuracy_score': Decimal('93.60'),
        'training_hours': 5000,
        'is_open_source': True,
        'is_commercial': False,
        'is_active': True,
        'contact_email': 'chatglm@zhipuai.cn',
        'contact_phone': '13800138024',
        'developer': '智谱AI',
        'website_url': 'https://chatglm.cn'
    },
    {
        'name': 'Baichuan',
        'version': 'v3.0',
        'description': '百川智能的开源中文大模型',
        'model_type': created_types[0],
        'release_date': date(2024, 2, 8),
        'parameters_count': 53000000000,
        'accuracy_score': Decimal('92.80'),
        'training_hours': 4200,
        'is_open_source': True,
        'is_commercial': False,
        'is_active': True,
        'contact_email': 'support@baichuan-ai.com',
        'contact_phone': '13800138025',
        'developer': '百川智能',
        'website_url': 'https://www.baichuan-ai.com'
    },
    {
        'name': 'ERNIE',
        'version': 'v4.0',
        'description': '百度文心大模型，中文理解能力强',
        'model_type': created_types[0],
        'release_date': date(2023, 10, 17),
        'parameters_count': 260000000000,
        'accuracy_score': Decimal('94.50'),
        'training_hours': 7000,
        'is_open_source': False,
        'is_commercial': True,
        'is_active': True,
        'contact_email': 'ernie@baidu.com',
        'contact_phone': '13800138026',
        'developer': '百度',
        'website_url': 'https://wenxin.baidu.com'
    },
    {
        'name': 'DeepSeek',
        'version': 'v2.5',
        'description': '深度求索的高性能开源模型',
        'model_type': created_types[0],
        'release_date': date(2024, 7, 4),
        'parameters_count': 236000000000,
        'accuracy_score': Decimal('95.10'),
        'training_hours': 6500,
        'is_open_source': True,
        'is_commercial': False,
        'is_active': True,
        'contact_email': 'contact@deepseek.com',
        'contact_phone': '13800138027',
        'developer': 'DeepSeek',
        'website_url': 'https://www.deepseek.com'
    },
    {
        'name': 'Yi',
        'version': 'v1.5',
        'description': '零一万物的高性能双语模型',
        'model_type': created_types[0],
        'release_date': date(2024, 5, 13),
        'parameters_count': 34000000000,
        'accuracy_score': Decimal('93.20'),
        'training_hours': 3800,
        'is_open_source': True,
        'is_commercial': False,
        'is_active': True,
        'contact_email': 'yi@01.ai',
        'contact_phone': '13800138028',
        'developer': '零一万物',
        'website_url': 'https://www.01.ai'
    },
]

for model_data in models_data:
    model, created = AIModel.objects.get_or_create(
        name=model_data['name'],
        version=model_data['version'],
        defaults=model_data
    )
    if created:
        print(f"  [OK] 创建AI模型: {model.name} {model.version}")
    else:
        print(f"  [SKIP] AI模型已存在: {model.name} {model.version}")

# 创建测试用户
print("\n[步骤4] 创建测试用户...")
test_users = [
    {'username': 'admin', 'email': 'admin@example.com', 'password': 'admin123456'},
    {'username': 'testuser', 'email': 'test@example.com', 'password': 'test123456'},
]

for user_data in test_users:
    user, created = User.objects.get_or_create(
        username=user_data['username'],
        defaults={'email': user_data['email']}
    )
    if created:
        user.set_password(user_data['password'])
        user.save()
        print(f"  [OK] 创建用户: {user.username} (密码: {user_data['password']})")
    else:
        print(f"  [SKIP] 用户已存在: {user.username}")

print("\n" + "=" * 60)
print("初始化完成！")
print("=" * 60)
print("\n测试账户信息:")
print("  用户名: admin")
print("  密码: admin123456")
print("\n  用户名: testuser")
print("  密码: test123456")
print("\n现在可以运行开发服务器:")
print("  py manage.py runserver")
print("\n或使用:")
print("  py run_server.py")
print("=" * 60)
