# Day00：开发环境全量配置与验证

## 【核心知识点】

### 1. Python 3.10 安装与 venv 虚拟环境配置

1. 下载 Python 3.10 安装包，安装时勾选 `Add Python to PATH`，完成安装
2. 打开终端，执行 `python --version`，确认输出版本为 `3.10.x`
3. 进入项目根目录，执行 `python -m venv venv` 创建虚拟环境
4. Windows 系统执行 `venv\Scripts\activate` 激活虚拟环境；Mac / Linux 执行 `source venv/bin/activate`
5. 激活后终端前缀出现 `(venv)` 标识，执行 `pip --version` 确认 pip 对应虚拟环境

### 2. PyCharm 项目关联与基础配置

1. 打开 PyCharm，选择 `open`，选中项目根目录打开
2. 进入 `File → Settings → Project → Python Interpreter`
3. 选择 `Add Interpreter → Virtualenv Environment → Existing`，指定本地 `venv/Scripts/python.exe` 路径
4. 安装代码规范插件，重启 PyCharm 生效
5. 配置全局编码为 UTF-8，设置自动格式化快捷键

### 3. Git 安装与 SSH 密钥配置

1. 下载 Git 安装包，默认选项完成安装，终端执行 `git --version` 验证安装
2. 执行 `git config --global user.name "你的用户名"` 配置全局用户名
3. 执行 `git config --global user.email "你的GitHub邮箱"` 配置全局邮箱
4. 执行 `ssh-keygen -t ed25519 -C "你的GitHub邮箱"`，连续回车生成 SSH 密钥
5. 打开 `~/.ssh/id_ed25519.pub` 文件，复制全部内容，添加到 GitHub 账号的 SSH Keys 中
6. 执行 `ssh -T git@github.com` 验证密钥关联成功

### 4. 仓库初始化与目录结构创建

1. 在项目根目录执行 `git init` 初始化本地 Git 仓库
2. 按规范创建目录：`learning/day00`、`projects`、`interview/questions`、`interview/resume`
3. 根目录新建 `README.md`、`requirement.txt` 空白文件
4. 核对目录结构与规范一致，无多余层级与命名错误

### 5. 基础依赖安装与环境验证

1. 激活虚拟环境，执行 `pip install --upgrade pip` 升级 pip 到最新版本
2. 执行 `pip install requests python-dotenv` 安装基础依赖包
3. 执行 `pip list` 查看已安装依赖，确认版本与安装状态
4. 运行环境验证脚本，确认全部校验项通过

## 【今日易错点】

1. 未勾选 Python 环境变量会导致终端无法识别 `python` 命令，需手动添加 PATH
2. 虚拟环境未激活时安装依赖，会将包安装到系统 Python 而非项目环境
3. SSH 密钥复制遗漏首尾字符，会导致 GitHub 验证失败，需完整复制 `.pub` 内容
4. PyCharm 解释器选错为系统 Python，会导致代码运行依赖与虚拟环境不一致
5. `git init` 需在项目根目录执行，避免上层目录初始化导致仓库层级错误