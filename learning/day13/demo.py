"""Day13 知识点示例代码"""
import csv
import os

# ====================== 知识点演示区 ======================
# 1. 列表模式写入CSV
print("\n===== 1. 列表模式写入CSV =====")
csv_file = "day13_list_demo.csv"
header = ["学号", "姓名", "成绩"]
data_rows = [
    ["001", "张三", 85],
    ["002", "李四", 92],
    ["003", "王五", 78]
]

with open(csv_file, 'w', encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data_rows)
print("列表模式CSV写入完成！")

# 2. 列表模式读取CSV
print("\n===== 2. 列表模式读取CSV =====")
with open(csv_file, 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    print("CSV内容：")
    for row in reader:
        print(row)

# 3. 字典模式写入CSV
print("\n===== 3. 字典模式写入CSV =====")
dict_file = "day13_dict_demo.csv"
fields = ["商品编号", "商品名称", "价格"]
goods_list = [
    {"商品编号": "G01", "商品名称": "笔记本", "价格": 3999},
    {"商品编号": "G02", "商品名称": "鼠标", "价格": 99},
    {"商品编号": "G03", "商品名称": "键盘", "价格": 199}
]

with open(dict_file, 'w', encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(goods_list)
print("字典模式CSV写入完成！")

# 4. 字典模式读取CSV
print("\n===== 4. 字典模式读取CSV =====")
with open(dict_file, 'r', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("商品清单：")
    for row in reader:
        print(f"编号：{row['商品编号']}，名称：{row['商品名称']}，价格：{row['价格']}元")


# ====================== 综合练习区 ======================
def score_csv_manager():
    """学生成绩CSV管理工具，录入数据写入文件，读取后统计平均分"""
    print("\n===== 综合练习：成绩CSV管理系统 =====")
    file_path = "day13_scores.csv"
    count = int(input("请输入学生人数："))
    fields = ["学号", "姓名", "成绩"]
    student_list = []
    for i in range(count):
        print(f"\n第{i + 1}名学生")
        stu_id = input("学号：")
        name = input("姓名：")
        score = input("成绩：")
        student_list.append({
            "学号": stu_id,
            "姓名": name,
            "成绩": score
        })

    # 写入CSV
    with open(file_path, 'w', encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(student_list)
    print(f"\n成绩数据已写入 {file_path}")

    # 读取并统计
    total_score = 0
    pass_count = 0
    print("\n===== 成绩统计 =====")
    with open(file_path, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            score = float(row['成绩'])
            total_score += score
            if score >= 60:
                pass_count += 1
            print(f"{row['学号']} - {row['姓名']} - {score}分")

    if count > 0:
        average = total_score / count
        print(f"\n平均分：{average:.2f}")
        print(f"及格人数：{pass_count}人")
        print(f"及格率：{pass_count / count * 100:.1f}%")
    else:
        print("无有效数据")

    # 清理测试文件
    os.remove(csv_file)
    os.remove(dict_file)
    os.remove(file_path)


def daily_practice():
    """串联当日知识点的综合实操练习"""
    score_csv_manager()


if __name__ == "__main__":
    daily_practice()
