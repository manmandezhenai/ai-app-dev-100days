"""Day18 Linux基础命令工具脚本"""

# ====================== 知识点演示区 ======================
# 1. 目录导航命令清单
print("\n===== 1. 目录导航命令清单 =====")
dir_commands = [
    ("pwd", "查看当前目录绝对路径"),
    ("cd 目标路径", "切换到指定目录"),
    ("ls", "列出当前目录文件与目录"),
    ("ls -l", "长格式显示文件详情信息"),
    ("ls -a", "显示所有文件，包含隐藏文件")
]

for cmd, desc in dir_commands:
    print(f"  {cmd:<18} - {desc}")

# 2. 文件查看命令清单
print("\n===== 2. 文件查看命令清单 =====")
view_commands = [
    ("cat 文件名", "查看小文件全部内容"),
    ("head -n 5 文件名", "查看文件前5行内容"),
    ("tail -n 10 文件名", "查看文件后10行内容"),
    ("more 文件名", "分页查看大体积文件")
]

for cmd, desc in view_commands:
    print(f"  {cmd:<22} - {desc}")

# 3. 文件操作命令清单
print("\n===== 3. 文件操作命令清单 =====")
file_commands = [
    ("touch 文件名", "创建空文件"),
    ("mkdir 目录名", "创建单层目录"),
    ("mkdir -p a/b/c", "递归创建多层目录"),
    ("rm 文件名", "删除指定文件"),
    ("rm -r 目录名", "删除指定目录"),
    ("cp 源 目标", "复制文件到目标位置"),
    ("mv 源 目标", "移动/重命名文件"),
]

for cmd, desc in file_commands:
    print(f"  {cmd:<22} - {desc}")


# ====================== 综合练习区 ======================
def generate_linux_cmd(operation, target, target_type="file"):
    """
    根据操作类型生成对应的Linux操作命令
    :param operation: 操作类型，支持create/delete/copy/move
    :param target: 目标文件或目录名称
    :param target_type: 目标类型，file/dir，默认file
    :return: 生成的命令字符串
    """
    if operation == "create":
        if target_type == "dir":
            return f"mkdir -p {target}"
        return f"touch {target}"
    elif operation == "delete":
        if target_type == "dir":
            return f"rm -r {target}"
        return f"rm  {target}"
    elif operation == "copy":
        dir_flag = "-r " if target_type == "dir" else ""
        return f"cp {dir_flag}{target} 目标路径"
    elif operation == "move":
        return f"mv {target} 目标路径"
    else:
        return "不支持的操作类型，请输入create/delete/copy/move"


def daily_practice():
    """接收用户输入操作信息，生成对应的Linux操作命令模板"""
    print("\n===== 综合练习：Linux命令生成工具 =====")
    print("支持操作：create（创建）、delete（删除）、copy（复制）、move（移动）")
    op_type = input("请输入操作类型：").strip()
    target_name = input("请输入目标名称：").strip()
    type_input = input("目标类型（file/dir，默认file）：").strip()
    target_type = type_input if type_input in ["file", "dir"] else "file"

    result_cmd = generate_linux_cmd(op_type, target_name, target_type)
    print(f"\n生成的操作命令：{result_cmd}")
    print("请在Linux终端执行对应命令")


if __name__ == "__main__":
    daily_practice()
