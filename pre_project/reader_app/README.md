# 悬浮阅读器

## 环境配置

### 1. 创建虚拟环境
```bash
python -m venv venv
```

### 2. 激活虚拟环境

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

### 4. 运行项目
```bash
python main.py
```

> **注意**：全局快捷键功能需要以管理员权限运行

## 项目结构
```
reader_app/
├── config/          # 配置管理
├── core/            # 核心业务逻辑
├── overlay/         # 阅读器窗口
├── storage/data/    # 数据存储
├── ui/              # 界面组件
└── utils/           # 工具函数
```
