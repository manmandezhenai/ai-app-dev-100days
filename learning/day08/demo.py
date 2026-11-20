"""Day08 知识点示例代码"""
import os

# ====================== 知识点演示区 ======================
# 1. 文本文件基础写入与读取
print("\n===== 1. 文本文件基础写入与读取 =====")
file = open("day08_demo.txt", "w", encoding="utf-8")
file.write("第一行内容：Python文件读写\n")
file.write("第二行内容：基础操作演示\n")
file.close()
print("文件写入完成！")

file = open("day08_demo.txt", "r", encoding="utf-8")
content = file.read()
print("\n读取全部内容：")
print(content)
file.close()

# 2. 逐行读取与列表写入
print("\n===== 2. 逐行读取与列表写入 =====")
lines = ["第三行：列表写入测试\n", "第四行：多行内容批量写入\n"]
with open("day08_demo.txt", "a", encoding="utf-8") as f:
    f.writelines(lines)
print("列表内容追加完成！")

with open("day08_demo.txt", "r", encoding="utf-8") as f:
    print("\n逐行读取结果：")
    line_num = 1
    for line in f:
        print(f"第{line_num}行：{line.strip()}")
        line_num += 1

# 3. with上下文管理器读写
print("\n===== 3. with上下文管理器读写 =====")
with open("day08_tset.txt", "w", encoding="utf-8") as f:
    f.write("with语法自动管理文件\n")
    f.write("无需手动关闭文件")
print("with写入完成！")

with open("day08_tset.txt", "r", encoding="utf-8") as f:
    read_lines = f.readlines()
    print(f"readlines返回列表：共{len(read_lines)}行")

# 4. 二进制文件复制演示
print("\n===== 4. 二进制文件复制演示 =====")
with open("day08_bin_src.bin", "wb") as f:
    f.write(b"binary test data 123456")
print("源二进制文件创建完成！")

with open("day08_bin_src.bin", "rb") as src_f:
    bin_data = src_f.read()
    with open("day08_bin_copy.bin", "wb") as dst_f:
        dst_f.write(bin_data)
print("二进制文件复制完成！")

with open("day08_bin_copy.bin", "rb") as f:
    print(f"复制后文件内容：{f.read()}")


# ====================== 综合练习区 ======================
def student_score_record():
    """学生成绩录入工具，写入文件后读取统计平均分"""
    print("\n===== 综合练习：学生成绩录入系统 =====")
    score_file = "day08_score.txt"
    student_count = 3

    with open(score_file, "w", encoding="utf-8") as f:
        for i in range(student_count):
            name = input(f"请输入第{i + 1}名学生姓名：")
            score = input(f"请输入{name}的成绩：")
            f.write(f"{name},{score}\n")
    print("成绩写入完成！")

    total_score = 0
    valid_count = 0
    print("\n成绩清单：")
    with open(score_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, score_str = line.split(",")
            try:
                score = float(score_str)
                total_score += score
                valid_count += 1
                print(f"{name}：{score}分")
            except ValueError:
                print(f"{name}：成绩无效")

        if valid_count > 0:
            avg_score = total_score / valid_count
            print(f"\n有效人数：{valid_count}人，平均分：{avg_score:.2f}分")
        else:
            print("\n无有效成绩数据")


def daily_practice():
    """串联当日知识点的综合实操练习"""
    student_score_record()
    # 清理测试文件
    test_files = ["day08_tset.txt", "day08_demo.txt", "day08_bin_src.bin", "day08_bin_copy.bin", "day08_score.txt"]
    for file in test_files:
        if os.path.exists(file):
            os.remove(file)


if __name__ == "__main__":
    daily_practice()
