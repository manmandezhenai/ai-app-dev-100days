"""Day19 Linux权限与压缩工具脚本"""

# ====================== 知识点演示区 ======================
# 1. 权限数字对应表
print("\n===== 1. 权限数字对应表 =====")
permission_map = {
    "rwx": 7,
    "rw-": 6,
    "r-x": 5,
    "r--": 4,
    "-wx": 3,
    "-w-": 2,
    "--x": 1,
    "---": 0
}

for perm, num in permission_map.items():
    print(f"  {perm} → {num}")

# 2. 权限修改命令清单
print("\n===== 2. 权限修改命令清单 =====")
perm_commands = {
    ("chmod 755 文件", "设置所有者读写执行，组和其他读执行"),
    ("chmod 644 文件", "设置所有者读写，组和其他仅可读"),
    ("chmod u+x 文件", "给所有者添加执行权限"),
    ("chown 用户 文件", "修改文件所有者"),
    ("chgrp 组名 文件", "修改文件所属组")
}

for cmd, desc in perm_commands:
    print(f"  {cmd:<22} - {desc}")

# 3. 压缩解压命令清单
print("\n===== 3. 压缩解压命令清单 =====")
compress_commands = [
    ("tar -zcvf a.tar.gz 目录", "gzip格式压缩目录"),
    ("tar -zxvf a.tar.gz", "解压tar.gz压缩包"),
    ("tar -zxvf a.tar.gz -C 目录", "解压到指定目录"),
    ("zip -r a.zip 目录", "zip格式压缩目录"),
    ("unzip a.zip", "解压zip压缩包")
]

for cmd, desc in compress_commands:
    print(f"  {cmd:<28} - {desc}")


# ====================== 综合练习区 ======================
def calc_permission_num(user_perm, group_perm, other_perm):
    """
    根据三组权限字符串计算数字权限值
    :param user_perm: 所有者权限字符串
    :param group_perm: 所属组权限字符串
    :param other_perm: 其他用户权限字符串
    :return: 三位数字权限字符串
    """
    perm_map = {"r": 4, "w": 2, "x": 1, "-": 0}

    def calc_single(perm_str):
        total = 0
        for char in perm_str:
            total += perm_map.get(char, 0)
        return str(total)

    return calc_single(user_perm) + calc_single(group_perm) + calc_single(other_perm)


def daily_practice():
    """接收用户输入，生成对应权限设置命令与压缩命令"""
    print("\n===== 综合练习：Linux命令生成工具 =====")
    print("1. 权限数字计算与命令生成")
    print("2. 压缩命令生成")
    choice = input("请选择功能（输入1或2）：")

    if choice == "1":
        user_p = input("请输入所有者权限（如rwx）：").strip()
        group_p = input("请输入所属组权限（如r-x）：").strip()
        other_p = input("请输入其他用户权限（如r--）：").strip()
        file_name = input("请输入目标文件名：")
        perm_num = calc_permission_num(user_p, group_p, other_p)
        print(f"\n生成的权限设置命令：chmod {perm_num} {file_name}")
    elif choice == "2":
        target = input("请输入待压缩的文件 / 目录名：")
        pack_name = input("请输入压缩包名称：")
        print("\n生成的压缩命令：")
        print(f"  tar格式：tar -zcvf {pack_name}.tar.gz {target}")
        print(f" zip格式：zip -r {pack_name}.zip {target}")
    else:
        print("无效的功能选择")


if __name__ == "__main__":
    daily_practice()
