"""Day20 Shell与远程连接工具脚本"""
# ====================== 知识点演示区 ======================
# 1. Shell基础常用命令
print("\n===== 1. Shell基础常用命令 =====")
shell_commands = [
    ("变量定义", "name=test"),
    ("引用变量", "echo $name"),
    ("导出环境变量", "export PATH=$PATH:/usr/local/bin"),
    ("管道筛选", "ls | grep .py"),
    ("输出重定向", "echo 内容 > test.txt"),
    ("追加重定向", "echo 内容 >> test.txt")
]

for name, cmd in shell_commands:
    print(f"  {name}：{cmd}")

# 2. SSH连接命令生成
print("\n===== 2. SSH连接命令生成 =====")


def generate_ssh_cmd(user, host, port=22):
    """
    生成SSH连接命令
    :param user: 服务器用户名
    :param host: 服务器地址
    :param port: 端口号，默认22
    :return: 连接命令字符串
    """
    if port == 22:
        return f"ssh {user}@{host}"
    return f"ssh -p {port} {user}@{host}"


demo_ssh = generate_ssh_cmd("root", "192.168.1.100", 2222)
print(f"示例连接命令：{demo_ssh}")

# 3. SCP传输命令生成
print("\n===== 3. SCP传输命令生成 =====")


def generate_scp_cmd(source, target, is_dir=False, port=22):
    """
    生成SCP传输命令
    :param source: 源文件路径
    :param target: 目标路径
    :param is_dir: 是否为目录，默认False
    :param port: 端口号，默认22
    :return: 传输命令字符串
    """
    dir_flag = "-r " if is_dir else ""
    port_flag = f"-p {port} " if port != 22 else ""
    return f"scp {port_flag}{dir_flag}{source} {target}"


upload_cmd = generate_scp_cmd(
    "./local_file.txt", "root@10.0.0.1:/opt/", is_dir=False)
print(f"本地上传命令：{upload_cmd}")
download_cmd = generate_scp_cmd(
    "root@10.0.0.1:/opt/remote_file.txt", "./download/")
print(f"远程下载命令：{download_cmd}")

# 4. 远程执行命令生成
print("\n===== 4. 远程执行命令生成 =====")


def generate_remote_exec(user, host, exec_cmd):
    """
    生成远程单条命令执行模板
    :param user: 用户名
    :param host: 服务器地址
    :param exec_cmd: 待执行的命令
    :return: 完整字符串
    """
    return f"ssh {user}@{host} \"{exec_cmd}\""


remote_cmd = generate_remote_exec("admin", "192.168.100.10", "ls /opt")
print(f"远程执行命令：{remote_cmd}")


# ====================== 综合练习区 ======================


def daily_practice():
    """接收服务器信息，生成SSH连接与文件传输命令模板"""
    print("\n===== 综合练习：远程操作命令生成器 =====")
    user = input("请输入服务器用户名：").strip()
    host = input("请输入服务器IP地址：").strip()
    port_input = input("请输入端口号（默认22）：").strip()
    port = int(port_input) if port_input.isdigit() else 22

    if not user or not host:
        print("用户名和服务器地址不能为空")
        return

    ssh_cmd = generate_ssh_cmd(user, host, port)
    print(f"\nSHH连接命令：{ssh_cmd}")

    print("\n--- SCP传输示例 ---")
    local_file = input("请输入本地文件路径：").strip()
    remote_path = input("请输入远程目标路径：").strip()
    is_dir = input("是否为目录？（y/n，默认n）：").strip().lower == "y"

    upload = generate_scp_cmd(
        local_file, f"{user}@{host}:{remote_path}", is_dir, port)
    print(f"\n上传命令：{upload}")

    remote_file = input("\n请输入远程文件路径：").strip()
    local_path = input("请输入本地保存路径：").strip()
    download = generate_scp_cmd(
        f"{user}@{host}:{remote_file}", local_path, is_dir, port)
    print(f"下载命令：{download}")


if __name__ == "__main__":
    daily_practice()
