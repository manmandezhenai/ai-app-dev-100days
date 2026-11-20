"""Day16 Git分支管理工具脚本"""
# ====================== 知识点演示区 ======================
# 1. 分支核心命令清单
print("\n===== 1. 分支核心命令清单 =====")
branch_commands = [
    ("git branch", "查看本地所有分支"),
    ("git branch 分支名", "创建新分支"),
    ("git checkout 分支名", "切换到指定分支"),
    ("git checkout -b 分支名", "创建并切换到新分支"),
    ("git merge 分支名", "将指定分支合并到当前分支"),
    ("git branch -d 分支名", "删除已合并的本地分支"),
    ("git branch -D 分支名", "强制删除本地分支")
]

for cmd, desc in branch_commands:
    print(f"  {cmd:<28} - {desc}")

# 2. 分支操作命令生成
print("\n===== 2. 分支操作命令生成 =====")


def generate_feature_flow(branch_name, feature_desc):
    """
    生成功能分支开发全流程命令
    :param branch_name: 功能分支名
    :param feature_desc: 功能描述
    :return: 命令列表
    """
    return [
        f"git checkout -b {branch_name}",
        f"# 开发{feature_desc}，完成后执行以下命令",
        "git add .",
        f"git commit -m \"feat：完成{feature_desc}\"",
        "git checkout main",
        f"git merge {branch_name}",
        f"git branch -d {branch_name}"
    ]


flow_cmds = generate_feature_flow("feature-user-login", "用户登录功能")
print("功能分支开发流程命令：")
for cmd in flow_cmds:
    print(f"    {cmd}")

# 3. 冲突处理步骤校验
print("\n===== 3. 冲突处理步骤校验 =====")
conflict_steps = [
    "查看冲突文件",
    "编辑冲突内容",
    "删除冲突标记",
    "暂存已解决文件",
    "完成合并提交"
]

print("标准冲突处理5步流程：")
for idx, step in enumerate(conflict_steps, 1):
    print(f"    {idx}. {step}")


# ====================== 综合练习区 ======================
def daily_practice():
    """接收用户输入分支信息，生成完整分支开发合并流程命令模板"""
    print("\n===== 综合练习：分支开发流程命令生成器 =====")
    branch_name = input("请输入功能分支名称：")
    feature_name = input("请输入功能描述：")

    if not branch_name.strip():
        print("分支名称不能为空")
        return

    flow = generate_feature_flow(branch_name, feature_name)
    print("\n===== 生成的完整操作流程 =====")
    for i, cmd in enumerate(flow, 1):
        if cmd.startswith("#"):
            print(f"  {cmd}")
        else:
            print(f"{i}. {cmd}")
    print("\n请按顺序在终端执行以上命令完成功能开发与合并")


if __name__ == "__main__":
    daily_practice()
