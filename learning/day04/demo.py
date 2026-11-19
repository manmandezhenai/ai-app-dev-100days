"""Day04 知识点示例代码"""

# ====================== 知识点演示区 ======================
# 1. 列表常用方法演示
print("\n===== 1. 列表常用方法演示 =====")
num_list = [1, 2, 3]
print(f"原始列表：{num_list}")
num_list.append(4)
print(f"append添加元素后：{num_list}")
num_list.insert(1, 10)
print(f"insert插入元素后：{num_list}")
pop_item = num_list.pop()
print(f"pop弹出末尾元素：{pop_item}，剩余列表：{num_list}")
print(f"切片获取前3个元素：{num_list[:3]}")

# 2. 字典常用操作演示
print("\n===== 2. 字典常用操作演示 =====")
student = {"name": "张三", "age": 20}
print(f"原始字典：{student}")
student["grade"] = "大三"
print(f"新增键值对后：{student}")
print(f"get获取存在的键：{student.get('name')}")
print(f"get获取不存在的键：{student.get('gender', '未知')}")
print(f"所有键：{list(student.keys())}")
print(f"所有值：{list(student.values())}")

# 3. 元组特性演示
print("\n===== 3. 元组特性演示 =====")
fixed_tuple = ("Python", "Java", "C++")
print(f"元组内容：{fixed_tuple}")
print(f"索引访问第一个元素：{fixed_tuple[0]}")
print(f"切片获取前两个元素：{fixed_tuple[:2]}")

# 4. 集合去重与操作演示
print("\n===== 4. 集合去重与操作演示 =====")
repeat_list = [1, 2, 2, 3, 3, 3]
unique_set = set(repeat_list)
print(f"列表去重后集合：{unique_set}")
unique_set.add(4)
print(f"add添加元素后：{unique_set}")
unique_set.remove(1)
print(f"remove删除元素后：{unique_set}")


# ====================== 综合练习区 ======================
def daily_practice():
    """学生成绩管理小工具，串联四类数据结构操作"""
    print("\n===== 综合练习：学生成绩管理 =====")
    # 元组存储固定科目
    subjects = ("语文", "数学", "英语")

    # 列表存储学生字典
    student_list = []

    # 添加3名学生
    for i in range(3):
        print(f"\n请输入第{i + 1}名学生信息")
        name = input("姓名：")
        score_list = []
        for sub in subjects:
            score = int(input(f"{sub}成绩："))
            score_list.append(score)
        student_dict = {
            "name": name,
            "score": dict(zip(subjects, score_list))
        }
        student_list.append(student_dict)

    # 遍历输出所有学生成绩
    print("\n===== 全部学生成绩汇总 =====")
    name_set = set()
    for stu in student_list:
        name = stu["name"]
        name_set.add(name)
        scores = stu["score"]
        total = sum(scores.values())
        print(f"姓名：{name}，各科成绩：{scores}，总分：{total}")

    print(f"\n去重后学生姓名集合：{name_set}")
    print(f"固定科目元组：{subjects}")


if __name__ == "__main__":
    daily_practice()
