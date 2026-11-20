"""Day12 知识点示例代码"""
import json
import os

# ====================== 知识点演示区 ======================
# 1. 基础序列化dumps用法
print("\n===== 1. 基础序列化dumps用法 =====")
user_dict = {"name": "张三", "age": 20, "is_student": True, "hobbies": ["编程", "阅读"]}
json_str = json.dumps(user_dict, ensure_ascii=False)
print(f"序列化后JSON字符串：{json_str}")
print(f"类型：{type(json_str)}")

# 2. 格式化序列化输出
print("\n===== 2. 格式化序列化输出 =====")
format_json = json.dumps(user_dict, ensure_ascii=False, indent=4)
print("格式化后的JSON：")
print(format_json)

# 3. 反序列化loads用法
print("\n===== 3. 反序列化loads用法 =====")
data = json.loads(json_str)
print(f"反序列化后数据：{data}")
print(f"类型：{type(data)}")
print(f"提取姓名字段：{data['name']}")

# 4. JSON文件读写dump/load
print("\n===== 4. JSON文件读写 =====")
file_path = "day12_user.json"
# 写入文件
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(user_dict, f, ensure_ascii=False, indent=2)
print("JSON文件写入完成！")

# 读取文件
with open(file_path, "r", encoding="utf-8") as f:
    load_data = json.load(f)
print(f"从文件读取的数据：{load_data}")


# ====================== 综合练习区 ======================
def student_score_manager():
    """学生成绩JSON管理工具，录入成绩、保存文件、读取统计"""
    print("\n===== 综合练习：学生成绩JSON管理系统 =====")
    student_list = []
    count = int(input("请输入学生人数："))

    for i in range(count):
        print(f"\n第{i + 1}名学生")
        stu_id = input("学号：")
        name = input("姓名：")
        score = float(input("成绩："))
        student_list.append({
            "stu_id": stu_id,
            "name": name,
            "score": score
        })

    # 保存到JSON文件
    save_path = "day12_scores.json"
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(student_list, f, ensure_ascii=False, indent=2)
    print(f"\n成绩数据已保存到 {save_path}")

    # 读取并统计
    with open(save_path, "r", encoding="utf-8") as f:
        load_scores = json.load(f)

    total = 0
    pass_count = 0
    print("\n===== 成绩统计 =====")
    for stu in load_scores:
        print(f"学号：{stu['stu_id']}，姓名：{stu['name']}，成绩：{stu['score']}")
        total += stu['score']
        if stu['score'] >= 60:
            pass_count += 1

    average = total / len(load_scores) if load_scores else 0
    if load_scores:
        print(f"\n平均分：{average:.2f}")
        print(f"及格人数：{pass_count} 人")
        print(f"及格率：{pass_count / len(load_scores) * 100:.1f}%")
    else:
        print("无有效数据")

    # 清理测试文件
    os.remove(file_path)
    os.remove(save_path)


def daily_practice():
    """串联当日知识点的综合实操练习"""
    student_score_manager()


if __name__ == "__main__":
    daily_practice()
