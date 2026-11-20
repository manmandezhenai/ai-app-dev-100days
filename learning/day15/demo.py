"""Day15 Git基础命令工具脚本"""
# ====================== 知识点演示区 ======================
# 1. Git核心基础命令清单
print("\n===== 1. Git核心基础命令清单 =====")
git_command_list = [
    ("git init", "初始化本地Git仓库"),
    ("git status", "查看仓库当前状态"),
    ("git add 文件名", "将单个文件加入暂存区"),
    ("git add .", "将所有变更文件加入暂存区"),
    ("git commit -m \"描述\"", "提交暂存区内容到本地仓库"),
    ("git log", "查看完整提交日志"),
    ("git log --oneline", "查看简洁版提交日志"),
    ("git reset --hard 版本号", "硬重置回退到指定版本"),
    ("git reflog", "查看所有操作记录"),
]
for cmd, desc in git_command_list:
    print(f"  {cmd:<30} - {desc}")

# 2. 提交信息基础校验
print("\n===== 2. 提交信息基础校验 =====")


def check_commit_message(msg):
    """
    校验提交信息基础合法性
    :param msg: 提交信息字符串
    :return: (是否合法, 提示信息)
    """
    if not msg.strip():
        return False, "提交信息不能为空"
    if len(msg) < 4:
        return False, "提交信息过短，无法清晰描述变更内容"
    if len(msg) > 50:
        return False, "提交信息过长，建议精简描述"
    return True, "提交信息符合基础规范"


test_msg1 = "新增用户登录功能"
test_msg2 = ""
print(f"测试信息1：{repr(test_msg1)} → {check_commit_message(test_msg1)[1]}")
print(f"测试信息2：{repr(test_msg2)} → {check_commit_message(test_msg2)[1]}")

# 3. 版本回退命令生成
print("\n===== 3. 版本回退命令生成 =====")


def generate_reset_command(version_id, mode="hard"):
    """
    生成版本回退命令模板
    :param version_id: 目标版本哈希
    :param mode: 重置模式，默认hard
    :return: 完整命令字符串
    """
    return f"git reset --{mode} {version_id}"


demo_version = "a1b2c3d"
reset_cmd = generate_reset_command(demo_version)
print(f"目标版本：{demo_version} 回退命令：{reset_cmd}")


# ====================== 综合练习区 ======================
def daily_practice():
    """接收用户输入变更内容，生成标准提交流程命令模板"""
    print("\n===== 综合练习：Git提交命令生成工具 =====")
    file_name = input("请输入待提交的文件名（输入.代表全部文件）：")
    commit_msg = input("请输入提交描述信息：")
    is_valid, tip = check_commit_message(commit_msg)
    if not is_valid:
        print(f"提交信息不合法：{tip}")
        return

    print("\n===== 生成的提交命令模板 =====")
    print(f"1. 加入暂存区：git add {file_name}")
    print(f"2. 提交到仓库：git commit -m \"{commit_msg}\"")
    print(f"3. 查看提交记录：git log --oneline")
    print("\n请按顺序在终端执行以上命令完成提交")


if __name__ == "__main__":
    daily_practice()
