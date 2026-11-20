"""Day17 Git远程仓库与提交规范工具脚本"""
# ====================== 知识点演示区 ======================
# 1. 远程仓库常用命令清单
print("\n===== 1. 远程仓库常用命令清单 =====")
remote_commands = [
    ("git remote add origin 地址", "关联远程仓库"),
    ("git remote -v", "查看远程仓库地址"),
    ("git push origin 分支名", "推送本地提交到远程"),
    ("git push -u origin 分支名", "首次推送并建立追踪关系"),
    ("git pull origin 分支名", "拉取并合并远程最新代码"),
    ("git clone 仓库地址", "克隆远程仓库到本地"),
]

for cmd, desc in remote_commands:
    print(f"  {cmd:<32} - {desc}")

# 2. 约定式提交类型校验
print("\n===== 2. 约定式提交类型校验 =====")
VALID_COMMIT_TYPES = ["feat", "fix", "docs", "style", "refactor", "chore"]


def check_commit_type(commit_type):
    """
    校验提交类型是否符合规范
    :param commit_type: 提交类型字符串
    :return: (是否合法, 提示信息)
    """
    if commit_type in VALID_COMMIT_TYPES:
        return True, "提交类型符合规范"
    return False, f"非法提交类型，支持的类型：{','.join(VALID_COMMIT_TYPES)}"


test_types = ["feat", "update", "docs"]
for t in test_types:
    valid, tip = check_commit_type(t)
    print(f"类型：{repr(t)}：{tip}")

# 3. 标准提交信息生成
print("\n===== 3. 标准提交信息生成 =====")


def generate_commit_msg(commit_type, scope, description):
    """
    生成符合约定式提交规范的提交信息
    :param commit_type: 提交类型
    :param scope: 作用范围
    :param description: 提交描述
    :return: 完成提交信息字符串
    """
    if scope:
        return f"{commit_type}（{scope}）：{description}"
    return f"{commit_type}：{description}"


demo_msg = generate_commit_msg("feat", "day17", "完成远程仓库与提交规范学习")
print(f"生成示例：{demo_msg}")


# ====================== 综合练习区 ======================
def daily_practice():
    """接收用户输入提交信息，生成规范提交命令与推送命令"""
    print("\n===== 综合练习：提交命令生成工具 =====")
    commit_type = input("请输入提交类型（feat/fix/docs等）：").strip()
    scope = input("请输入作用范围（可留空）：").strip()
    desc = input("请输入提交描述：").strip()

    valid, tip = check_commit_type(commit_type)
    if not valid:
        print(f"错误：{tip}")
        return

    if not desc.strip():
        print("错误：提交描述不能为空")
        return

    commit_msg = generate_commit_msg(commit_type, scope, desc)
    print("\n===== 生成的操作命令 =====")
    print("1. 暂存文件：git add .")
    print(f"2. 提交代码：git commit -m \"{commit_msg}\"")
    print("3. 拉取最新代码：git pull origin main")
    print("4. 推送到远程：git push origin main")
    print("\n请按顺序在终端执行以上命令完成同步")


if __name__ == "__main__":
    daily_practice()
