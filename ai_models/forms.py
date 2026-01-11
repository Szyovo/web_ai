"""
Forms for AI Model Management System
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import AIModel, ModelType


class UserRegisterForm(UserCreationForm):
    """用户注册表单"""
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'

    def clean_email(self):
        """验证邮箱是否已存在"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('该邮箱已被注册，请使用其他邮箱。')
        return email


class UserLoginForm(AuthenticationForm):
    """用户登录表单"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'
        self.fields['password'].widget.attrs['class'] = 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent'


class AIModelForm(forms.ModelForm):
    """AI模型表单"""
    class Meta:
        model = AIModel
        fields = [
            'name', 'version', 'description', 'model_type',
            'release_date', 'parameters_count', 'accuracy_score',
            'training_hours', 'is_open_source', 'is_commercial',
            'is_active', 'contact_email', 'contact_phone',
            'developer', 'website_url'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'glass-input w-full px-4 py-3 rounded-xl text-white placeholder-white/70 focus:ring-2 focus:ring-white/30',
                'placeholder': '输入模型名称'
            }),
            'version': forms.TextInput(attrs={
                'class': 'glass-input w-full px-4 py-3 rounded-xl text-white placeholder-white/70 focus:ring-2 focus:ring-white/30',
                'placeholder': 'v1.0'
            }),
            'description': forms.Textarea(attrs={
                'class': 'glass-input w-full px-4 py-3 rounded-xl text-white placeholder-white/70 focus:ring-2 focus:ring-white/30',
                'rows': 4,
                'placeholder': '输入模型描述'
            }),
            'model_type': forms.Select(attrs={
                'class': 'glass-select w-full px-4 py-3 rounded-xl text-white'
            }),
            'release_date': forms.DateInput(attrs={
                'class': 'glass-input w-full px-4 py-3 rounded-xl text-white focus:ring-2 focus:ring-white/30',
                'type': 'date'
            }),
            'parameters_count': forms.NumberInput(attrs={
                'class': 'glass-input w-full px-4 py-3 rounded-xl text-white placeholder-white/70 focus:ring-2 focus:ring-white/30',
                'placeholder': '7000000000'
            }),
            'accuracy_score': forms.NumberInput(attrs={
                'class': 'glass-input w-full px-4 py-3 rounded-xl text-white placeholder-white/70 focus:ring-2 focus:ring-white/30',
                'step': '0.01',
                'placeholder': '95.50'
            }),
            'training_hours': forms.NumberInput(attrs={
                'class': 'glass-input w-full px-4 py-3 rounded-xl text-white placeholder-white/70 focus:ring-2 focus:ring-white/30',
                'placeholder': '1000'
            }),
            'is_open_source': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 rounded focus:ring-2 focus:ring-white/30'
            }),
            'is_commercial': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 rounded focus:ring-2 focus:ring-white/30'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 rounded focus:ring-2 focus:ring-white/30'
            }),
            'contact_email': forms.EmailInput(attrs={
                'class': 'glass-input w-full px-4 py-3 rounded-xl text-white placeholder-white/70 focus:ring-2 focus:ring-white/30',
                'placeholder': 'contact@example.com'
            }),
            'contact_phone': forms.TextInput(attrs={
                'class': 'glass-input w-full px-4 py-3 rounded-xl text-white placeholder-white/70 focus:ring-2 focus:ring-white/30',
                'placeholder': '13800138000'
            }),
            'developer': forms.TextInput(attrs={
                'class': 'glass-input w-full px-4 py-3 rounded-xl text-white placeholder-white/70 focus:ring-2 focus:ring-white/30',
                'placeholder': '开发者或组织名称'
            }),
            'website_url': forms.URLInput(attrs={
                'class': 'glass-input w-full px-4 py-3 rounded-xl text-white placeholder-white/70 focus:ring-2 focus:ring-white/30',
                'placeholder': 'https://example.com'
            }),
        }


class ModelTypeForm(forms.ModelForm):
    """模型类型表单"""
    class Meta:
        model = ModelType
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'glass-input w-full px-4 py-3 rounded-xl text-white placeholder-white/70 focus:ring-2 focus:ring-white/30',
                'placeholder': '输入类型名称'
            }),
            'description': forms.Textarea(attrs={
                'class': 'glass-input w-full px-4 py-3 rounded-xl text-white placeholder-white/70 focus:ring-2 focus:ring-white/30',
                'rows': 3,
                'placeholder': '输入类型描述'
            }),
        }


class AIModelSearchForm(forms.Form):
    """模型搜索表单"""
    keyword = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
            'placeholder': '搜索模型名称、开发者...'
        })
    )
    model_type = forms.ModelChoiceField(
        queryset=ModelType.objects.all(),
        required=False,
        empty_label='全部类型',
        widget=forms.Select(attrs={
            'class': 'px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500'
        })
    )
