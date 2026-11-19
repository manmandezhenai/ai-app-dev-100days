"""Day00 开发环境验证脚本"""
import sys
import os
import subprocess

# ====================== 知识点演示区 ======================
# 1. Python版本与基础环境校验
print("\n===== 1. Python环境校验 =====")
print(f"Python版本：{sys.version}")
print(f"当前工作路径：{os.getcwd()}")
print(f"虚拟环境标识：{'venv' in sys.executable}")

# 2. 第三方依赖导入校验
print("\n===== 2. 基础依赖校验 =====")
try:
    import requests

    print(f"requests 安装成功，版本：{requests.__version__}")
except ImportError:
    print("requests 未安装，请执行 pip install requests")

try:
    from dotenv import load_dotenv

    print("python-dotenv 安装成功")
except ImportError:
    print("python-dotenv 未安装，请执行 pip install python-dotenv")


# ====================== 综合练习区 ======================
def env_full_check():
    """全量环境自检，输出校验结果"""
    print("\n===== 全量环境自检 =====")
    check_pass = 0
    check_total = 4

    # 校验Python版本
    if sys.version_info.major == 3 and sys.version_info.minor == 10:
        print(f"[✅] Python 3.10 版本校验通过")
        check_pass += 1
    else:
        print(f"[❌] Python版本不符合要求，需使用 3.10.x")

    # 校验虚拟环境
    if "venv" in sys.executable:
        print("[✅] 虚拟环境激活状态正常")
        check_pass += 1
    else:
        print("[❌]未检测到虚拟环境，请先激活 venv")

    # 校验pip可用性
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "--version"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"[✅] pip 可用：{result.stdout.strip()}")
            check_pass += 1
    except Exception:
        print("[❌] pip 不可用")

    # 校验基础依赖
    try:
        import requests
        from dotenv import load_dotenv
        print("[✅] 基础依赖包全部导入成功")
        check_pass += 1
    except ImportError:
        print("[❌] 存在未安装的基础依赖包")

    print(f"\n自检结果：{check_pass}/{check_total} 项通过")
    if check_pass == check_total:
        print("开发环境配置完成，可进入正式学习")
    else:
        print("存在未通过项，请排查后重新验证")


if __name__ == "__main__":
    env_full_check()
