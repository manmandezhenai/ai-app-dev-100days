"""Day11 知识点示例代码"""
import os

# ====================== 知识点演示区 ======================
# 1. 目录遍历方法演示
print("\n===== 1. 目录遍历方法演示 =====")
test_dir = "day11_test_dir"
os.makedirs(test_dir, exist_ok=True)
# 创建测试文件
for i in range(3):
    with open(os.path.join(test_dir, f"file{i + 1}.txt"), "w", encoding="utf-8") as f:
        f.write(f"测试文件{i + 1}内容\n第二行数据\n")

print("单层目录遍历结果：")
file_names = os.listdir(test_dir)
for name in file_names:
    print(f"- {name}")

print("\n递归目录遍历结果：")
for root, dirs, files in os.walk(test_dir):
    for file in files:
        full_path = os.path.join(root, file)
        print(f"- {full_path}")

# 2. 文件后缀过滤演示
print("\n===== 2. 文件后缀过滤演示 =====")
all_files = os.listdir(test_dir)
txt_files = [f for f in all_files if f.endswith(".txt")]
print(f"目录下所有文件：{all_files}")
print(f"筛选出的 .txt 文件：{txt_files}")

# 3. 文本基础清洗演示
print("\n===== 3. 文本基础清洗演示 =====")
raw_text = "  第一行 内容  \n\n  第二行数据  \n  \n第三行\t制表符\n"
print("原始文本：")
print(repr(raw_text))

clean_lines = []
for line in raw_text.splitlines():
    clean_line = line.strip()
    if clean_line:
        clean_line = clean_line.replace("\t", " ")
        clean_lines.append(clean_line)

clean_text = "\n".join(clean_lines)
print("\n清洗后文本：")
print(clean_text)

# 4. 单文件清洗流程演示
print("\n===== 4. 单文件清洗流程演示 =====")
file_path = os.path.join(test_dir, "file1.txt")
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

clean_count = 0
result_lines = []
for line in lines:
    line = line.strip()
    if line:
        result_lines.append(line)
        clean_count += 1

print(f"原始行数：{len(lines)}，清洗后有效行数：{clean_count}")
print(f"清洗后内容：{result_lines}")


# ====================== 综合练习区 ======================
def batch_clean_file(source_dir, target_dir):
    """
    批量清洗指定目录下的所有txt文件，输出到目标目录
    :param source_dir: 源文件目录
    :param target_dir: 清洗后文件输出目录
    :return: 返回处理统计信息字典
    """
    os.makedirs(target_dir, exist_ok=True)
    file_count = 0
    total_clean_lines = 0

    for root, dirs, files in os.walk(source_dir):
        for file_name in files:
            if not file_name.endswith(".txt"):
                continue
            src_path = os.path.join(root, file_name)
            dst_path = os.path.join(target_dir, file_name)

            # 读取并清洗
            with open(src_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            clean_lines = []
            for line in lines:
                line = line.strip()
                if line:
                    clean_lines.append(line)

            # 写入清洗结果
            with open(dst_path, "w", encoding="utf-8") as f:
                f.write("\n".join(clean_lines))

            file_count += 1
            total_clean_lines += len(clean_lines)

    return {
        "file_count": file_count,
        "total_lines": total_clean_lines
    }


def daily_practice():
    """批量文本清洗综合练习，创建测试文件并执行批量清洗"""
    print("\n===== 综合练习：批量文本清洗工具 =====")
    source_dir = "day11_source"
    target_dir = "day11_clean"
    os.makedirs(source_dir, exist_ok=True)

    # 创建测试文件
    test_contents = [
        "  用户1, 张三 , 20岁  \n\n  用户2, 李四 , 21岁\n",
        "  数据A: 100 \n  数据B: 200 \n\n  数据C: 300\n",
        "  日志1: 启动成功\n\n  日志2: 运行中  \n  日志3: 结束\n"
    ]
    for idx, content in enumerate(test_contents):
        with open(os.path.join(source_dir, f"data{idx + 1}.txt"), "w", encoding="utf-8") as f:
            f.write(content)

    # 执行批量清洗
    stats = batch_clean_file(source_dir, target_dir)

    print(f"处理完成：共清洗 {stats['file_count']} 个文件")
    print(f"累计有效行数：{stats['total_lines']} 行")
    print(f"清洗结果已输出到：{target_dir} 目录")

    # 清理测试文件
    import shutil
    for dir_path in [test_dir, source_dir, target_dir]:
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
    print("\n测试目录已清理")

if __name__ == "__main__":
    daily_practice()