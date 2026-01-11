# AI大模型管理系统

基于 Django 开发的 Web 信息管理系统，用于管理 AI 大模型信息。

## 功能特性

### 1. 用户认证系统
- 用户注册功能
- 用户登录/登出功能
- 使用 Session 保持登录状态
- 未登录用户可查看模型，但无法编辑

### 2. AI 模型管理（主题信息）
- **增删改查功能**：支持对 AI 模型的完整 CRUD 操作
- **多种数据类型字段**：
  - 字符串：模型名称、版本号、描述、开发者等
  - 日期：发布日期、创建时间、更新时间
  - 整数：参数量、训练时长
  - 小数：准确率（Decimal）
  - 布尔：是否开源、是否商用、是否启用
  - Email：联系邮箱（带验证）
  - 手机：联系电话（带中国大陆手机号验证）
  - URL：官网地址
- **分页功能**：列表页面每页显示 10 条记录
- **导出 CSV**：支持导出模型数据为 CSV 文件
- **搜索功能**：
  - 关键字模糊搜索（模型名称、开发者、描述）
  - 通过外键（模型类型）精确查询

### 3. 模型类型管理（外键表）
- 支持模型类型的增删改查
- 级联删除：删除类型时，关联的所有模型也会被删除
- 类型包括：语言模型、音频模型、视频模型等

### 4. 技术实现
- **Django 装饰器**：
  - `@login_required_with_message`：自定义登录验证装饰器
  - `@admin_required`：管理员权限装饰器
  - `@check_model_ownership`：所有权检查装饰器
- **状态保持**：使用 Django Session 保持用户登录状态
- **UI 美化**：使用 Tailwind CSS 实现现代化响应式界面

## 项目结构

```
out_web/
├── config/                 # 项目配置
│   ├── __init__.py
│   ├── settings.py        # Django 设置
│   ├── urls.py            # 根 URL 配置
│   ├── wsgi.py
│   └── asgi.py
├── ai_models/             # AI 模型应用
│   ├── __init__.py
│   ├── models.py          # 数据模型
│   ├── views.py           # 视图函数
│   ├── forms.py           # 表单
│   ├── urls.py            # URL 路由
│   ├── admin.py           # Admin 配置
│   ├── apps.py
│   └── decorators.py      # 自定义装饰器
├── templates/             # 模板文件
│   ├── base.html
│   └── ai_models/
│       ├── register.html
│       ├── login.html
│       ├── ai_model_list.html
│       ├── ai_model_detail.html
│       ├── ai_model_form.html
│       ├── ai_model_confirm_delete.html
│       ├── model_type_list.html
│       ├── model_type_form.html
│       └── model_type_confirm_delete.html
├── manage.py
└── requirements.txt
```

## 快速开始

### 方法一：一键初始化（推荐）

项目已包含初始化脚本和测试数据，只需一条命令即可启动：

```bash
# Windows系统
py init_and_run.py

# 然后启动服务器
py run_server.py
```

初始化脚本会自动：
- 创建数据库和表结构
- 创建5个模型类型（语言模型、音频模型、视频模型、图像模型、多模态模型）
- 创建6个示例AI模型（GPT-4、Claude 3、Whisper等）
- 创建2个测试用户账户

**测试账户：**
- 用户名: `admin` / 密码: `admin123456`
- 用户名: `testuser` / 密码: `test123456`

访问 http://127.0.0.1:8000/ 即可使用系统。

### 方法二：手动安装

#### 1. 环境准备

确保已安装 Python 3.8 或更高版本。

#### 2. 安装依赖

```bash
# Windows系统
py -m pip install -r requirements.txt

# Linux/Mac系统
pip install -r requirements.txt
```

#### 3. 数据库迁移

```bash
# Windows系统
py manage.py makemigrations
py manage.py migrate

# Linux/Mac系统
python manage.py makemigrations
python manage.py migrate
```

#### 4. 创建超级管理员（可选）

```bash
# Windows系统
py manage.py createsuperuser

# Linux/Mac系统
python manage.py createsuperuser
```

#### 5. 运行开发服务器

```bash
# Windows系统
py manage.py runserver

# Linux/Mac系统
python manage.py runserver
```

访问 http://127.0.0.1:8000/ 即可使用系统。

## 使用说明

### 首次使用

1. **注册账户**：访问首页点击"注册"按钮创建新账户
2. **登录系统**：使用注册的账户登录
3. **创建模型类型**：
   - 点击"模型类型"菜单
   - 点击"创建新类型"
   - 添加类型如：语言模型、音频模型、视频模型等
4. **创建 AI 模型**：
   - 返回"模型列表"
   - 点击"创建新模型"
   - 填写模型信息并保存

### 主要功能说明

#### 模型列表
- **搜索**：在搜索框输入关键字，或选择模型类型进行过滤
- **查看**：点击"查看"按钮查看模型详情
- **编辑**：登录后可点击"编辑"修改模型信息
- **删除**：登录后可点击"删除"删除模型
- **导出**：点击"导出 CSV"按钮下载当前搜索结果

#### 模型类型管理
- **查看类型**：显示所有模型类型及关联模型数量
- **创建类型**：登录后可创建新的模型类型
- **编辑类型**：修改类型名称和描述
- **删除类型**：删除类型时会级联删除所有关联的模型（会有警告提示）

#### 权限说明
- **未登录用户**：只能查看模型和类型信息
- **已登录用户**：可以进行所有增删改查操作

## 数据模型说明

### ModelType（模型类型）
- name：类型名称（唯一）
- description：类型描述
- created_at：创建时间

### AIModel（AI 模型）
- name：模型名称
- version：版本号
- description：模型描述
- model_type：模型类型（外键，级联删除）
- release_date：发布日期
- parameters_count：参数量（大整数）
- accuracy_score：准确率（小数，0-100）
- training_hours：训练时长（小时）
- is_open_source：是否开源
- is_commercial：是否商用
- is_active：是否启用
- contact_email：联系邮箱
- contact_phone：联系电话
- developer：开发者/组织
- website_url：官网地址
- created_at：创建时间
- updated_at：更新时间

## 技术栈

- **后端框架**：Django 5.0.1
- **数据库**：SQLite（开发环境）
- **前端框架**：Tailwind CSS
- **模板引擎**：Django Template
- **认证系统**：Django Auth

## 特色功能

1. **装饰器使用**：自定义装饰器控制访问权限和消息提示
2. **Session 状态保持**：用户登录信息保存在 Session 中，24 小时有效
3. **级联删除**：删除模型类型时自动删除关联模型
4. **数据验证**：Email 和手机号格式验证
5. **响应式设计**：使用 Tailwind CSS 实现美观的响应式界面
6. **分页导航**：完整的分页功能，支持首页/上一页/下一页/末页
7. **CSV 导出**：支持导出搜索结果为 CSV 文件

## Admin 后台

访问 http://127.0.0.1:8000/admin/ 可使用 Django Admin 后台管理系统。

需要先创建超级管理员账户：
```bash
python manage.py createsuperuser
```

## 注意事项

1. 本项目使用 SQLite 数据库，适合开发和小型应用
2. 生产环境建议更换为 PostgreSQL 或 MySQL
3. 请修改 `settings.py` 中的 `SECRET_KEY`
4. 生产环境请将 `DEBUG` 设置为 `False`
5. 删除模型类型会级联删除所有关联模型，操作需谨慎

## 开发者

基于 Django 框架开发，使用 Tailwind CSS 美化界面。

## 许可证

MIT License
