"""
Data models for AI Model Management System
"""
from django.db import models
from django.core.validators import EmailValidator, RegexValidator


class ModelType(models.Model):
    """
    大模型类型表（外键表）
    """
    name = models.CharField(max_length=100, unique=True, verbose_name='类型名称')
    description = models.TextField(blank=True, verbose_name='类型描述')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '大模型类型'
        verbose_name_plural = '大模型类型'
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class AIModel(models.Model):
    """
    AI大模型信息表（主题表）
    包含各种数据类型字段
    """
    # 字符串类型
    name = models.CharField(max_length=200, verbose_name='模型名称')
    version = models.CharField(max_length=50, verbose_name='版本号')
    description = models.TextField(verbose_name='模型描述')

    # 外键关系 - 级联删除
    model_type = models.ForeignKey(
        ModelType,
        on_delete=models.CASCADE,  # 删除类型时，关联的模型也被删除
        related_name='ai_models',
        verbose_name='模型类型'
    )

    # 日期类型
    release_date = models.DateField(verbose_name='发布日期')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    # 数字类型
    parameters_count = models.BigIntegerField(verbose_name='参数量（整数）', help_text='模型参数数量')
    accuracy_score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='准确率（小数）',
        help_text='0-100之间的准确率分数'
    )
    training_hours = models.IntegerField(verbose_name='训练时长（小时）')

    # 布尔类型
    is_open_source = models.BooleanField(default=False, verbose_name='是否开源')
    is_commercial = models.BooleanField(default=False, verbose_name='是否商用')
    is_active = models.BooleanField(default=True, verbose_name='是否启用')

    # Email类型
    phone_validator = RegexValidator(
        regex=r'^1[3-9]\d{9}$',
        message='请输入有效的中国大陆手机号码'
    )

    contact_email = models.EmailField(
        validators=[EmailValidator(message='请输入有效的电子邮件地址')],
        verbose_name='联系邮箱'
    )

    # 手机号类型
    contact_phone = models.CharField(
        max_length=11,
        validators=[phone_validator],
        verbose_name='联系电话'
    )

    # 其他字段
    developer = models.CharField(max_length=200, verbose_name='开发者/组织')
    website_url = models.URLField(blank=True, verbose_name='官网地址')

    class Meta:
        verbose_name = 'AI大模型'
        verbose_name_plural = 'AI大模型'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['model_type']),
        ]

    def __str__(self):
        return f"{self.name} ({self.version})"
