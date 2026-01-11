"""
Views for AI Model Management System
"""
import csv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q

from .models import AIModel, ModelType
from .forms import (
    UserRegisterForm, UserLoginForm, AIModelForm,
    ModelTypeForm, AIModelSearchForm
)
from .decorators import login_required_with_message


def register_view(request):
    """用户注册视图"""
    if request.user.is_authenticated:
        return redirect('ai_model_list')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'欢迎 {user.username}！注册成功！')
            return redirect('ai_model_list')
    else:
        form = UserRegisterForm()

    return render(request, 'ai_models/register.html', {'form': form})


def login_view(request):
    """用户登录视图"""
    if request.user.is_authenticated:
        return redirect('ai_model_list')

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # 使用session保存用户信息
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                messages.success(request, f'欢迎回来，{username}！')
                next_url = request.GET.get('next', 'ai_model_list')
                return redirect(next_url)
    else:
        form = UserLoginForm()

    return render(request, 'ai_models/login.html', {'form': form})


@login_required
def logout_view(request):
    """用户登出视图"""
    username = request.user.username
    logout(request)
    # 清除session
    request.session.flush()
    messages.info(request, f'再见，{username}！')
    return redirect('login')


def ai_model_list(request):
    """
    AI模型列表视图 - 带搜索、过滤、分页功能
    未登录用户也可以查看
    """
    # 初始化查询集
    models = AIModel.objects.select_related('model_type').all()

    # 搜索和过滤
    search_form = AIModelSearchForm(request.GET)
    if search_form.is_valid():
        keyword = search_form.cleaned_data.get('keyword')
        model_type = search_form.cleaned_data.get('model_type')

        # 关键字模糊搜索
        if keyword:
            models = models.filter(
                Q(name__icontains=keyword) |
                Q(developer__icontains=keyword) |
                Q(description__icontains=keyword)
            )

        # 通过外键表查询
        if model_type:
            models = models.filter(model_type=model_type)

    # 分页功能
    paginator = Paginator(models, 10)  # 每页显示10条
    page = request.GET.get('page', 1)

    try:
        models_page = paginator.page(page)
    except PageNotAnInteger:
        models_page = paginator.page(1)
    except EmptyPage:
        models_page = paginator.page(paginator.num_pages)

    context = {
        'models': models_page,
        'search_form': search_form,
        'is_authenticated': request.user.is_authenticated,
    }
    return render(request, 'ai_models/ai_model_list.html', context)


@login_required_with_message
def ai_model_create(request):
    """创建AI模型视图 - 需要登录"""
    if request.method == 'POST':
        form = AIModelForm(request.POST)
        if form.is_valid():
            model = form.save()
            messages.success(request, f'模型 "{model.name}" 创建成功！')
            return redirect('ai_model_detail', pk=model.pk)
    else:
        form = AIModelForm()

    return render(request, 'ai_models/ai_model_form.html', {
        'form': form,
        'title': '创建AI模型'
    })


def ai_model_detail(request, pk):
    """AI模型详情视图 - 所有人可查看"""
    model = get_object_or_404(AIModel, pk=pk)
    return render(request, 'ai_models/ai_model_detail.html', {
        'model': model,
        'is_authenticated': request.user.is_authenticated
    })


@login_required_with_message
def ai_model_edit(request, pk):
    """编辑AI模型视图 - 需要登录"""
    model = get_object_or_404(AIModel, pk=pk)

    if request.method == 'POST':
        form = AIModelForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            messages.success(request, f'模型 "{model.name}" 更新成功！')
            return redirect('ai_model_detail', pk=model.pk)
    else:
        form = AIModelForm(instance=model)

    return render(request, 'ai_models/ai_model_form.html', {
        'form': form,
        'title': '编辑AI模型',
        'model': model
    })


@login_required_with_message
def ai_model_delete(request, pk):
    """删除AI模型视图 - 需要登录"""
    model = get_object_or_404(AIModel, pk=pk)

    if request.method == 'POST':
        model_name = model.name
        model.delete()
        messages.success(request, f'模型 "{model_name}" 已删除！')
        return redirect('ai_model_list')

    return render(request, 'ai_models/ai_model_confirm_delete.html', {
        'model': model
    })


def export_models_csv(request):
    """导出CSV功能"""
    # 创建HttpResponse对象，设置CSV格式
    response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
    response['Content-Disposition'] = 'attachment; filename="ai_models.csv"'

    # 创建CSV writer
    writer = csv.writer(response)

    # 写入标题行
    writer.writerow([
        '模型名称', '版本号', '模型类型', '发布日期', '参数量',
        '准确率', '训练时长', '是否开源', '是否商用', '开发者',
        '联系邮箱', '联系电话', '创建时间'
    ])

    # 获取数据并应用搜索过滤
    models = AIModel.objects.select_related('model_type').all()

    search_form = AIModelSearchForm(request.GET)
    if search_form.is_valid():
        keyword = search_form.cleaned_data.get('keyword')
        model_type = search_form.cleaned_data.get('model_type')

        if keyword:
            models = models.filter(
                Q(name__icontains=keyword) |
                Q(developer__icontains=keyword) |
                Q(description__icontains=keyword)
            )

        if model_type:
            models = models.filter(model_type=model_type)

    # 写入数据行
    for model in models:
        writer.writerow([
            model.name,
            model.version,
            model.model_type.name,
            model.release_date.strftime('%Y-%m-%d'),
            model.parameters_count,
            f'{model.accuracy_score}',
            model.training_hours,
            '是' if model.is_open_source else '否',
            '是' if model.is_commercial else '否',
            model.developer,
            model.contact_email,
            model.contact_phone,
            model.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        ])

    return response


# ==================== 模型类型管理 ====================

def model_type_list(request):
    """模型类型列表 - 所有人可查看"""
    types = ModelType.objects.all()
    return render(request, 'ai_models/model_type_list.html', {
        'types': types,
        'is_authenticated': request.user.is_authenticated
    })


@login_required_with_message
def model_type_create(request):
    """创建模型类型 - 需要登录"""
    if request.method == 'POST':
        form = ModelTypeForm(request.POST)
        if form.is_valid():
            model_type = form.save()
            messages.success(request, f'类型 "{model_type.name}" 创建成功！')
            return redirect('model_type_list')
    else:
        form = ModelTypeForm()

    return render(request, 'ai_models/model_type_form.html', {
        'form': form,
        'title': '创建模型类型'
    })


@login_required_with_message
def model_type_edit(request, pk):
    """编辑模型类型 - 需要登录"""
    model_type = get_object_or_404(ModelType, pk=pk)

    if request.method == 'POST':
        form = ModelTypeForm(request.POST, instance=model_type)
        if form.is_valid():
            form.save()
            messages.success(request, f'类型 "{model_type.name}" 更新成功！')
            return redirect('model_type_list')
    else:
        form = ModelTypeForm(instance=model_type)

    return render(request, 'ai_models/model_type_form.html', {
        'form': form,
        'title': '编辑模型类型',
        'model_type': model_type
    })


@login_required_with_message
def model_type_delete(request, pk):
    """
    删除模型类型 - 需要登录
    级联删除：删除类型时，关联的所有模型也会被删除
    """
    model_type = get_object_or_404(ModelType, pk=pk)
    related_models_count = model_type.ai_models.count()

    if request.method == 'POST':
        type_name = model_type.name
        model_type.delete()  # 级联删除相关的AI模型
        messages.success(
            request,
            f'类型 "{type_name}" 及其关联的 {related_models_count} 个模型已删除！'
        )
        return redirect('model_type_list')

    return render(request, 'ai_models/model_type_confirm_delete.html', {
        'model_type': model_type,
        'related_models_count': related_models_count
    })
