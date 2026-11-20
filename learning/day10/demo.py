"""Day10 知识点示例代码"""

# ====================== 知识点演示区 ======================
# 1. 规范命名与代码格式演示
print("\n===== 1. 规范命名与代码格式演示 =====")
MAX_STUDENT_COUNT = 50
DEFAULT_SCORE = 0
student_name = "张三"
total_score = 0


def calculate_average(total, count):
    """
    计算平均分
    :param total: 总分
    :param count: 统计人数
    """

    if count == 0:
        return DEFAULT_SCORE
    return total / count


print(f"常量示例：最大学生数：{MAX_STUDENT_COUNT}")
print(f"变量示例：学生姓名：{student_name}")
print(f"函数示例：平均分计算结果：{calculate_average(270, 3)}")

# 2. 单一职责函数拆分示例
print("\n===== 2. 单一职责函数拆分示例 =====")


def get_total_score(score_list):
    """计算成绩列表总分"""
    return sum(score_list)


def get_pass_count(score_list, pass_line=60):
    """统计及格人数"""
    count = 0
    for score in score_list:
        if score >= pass_line:
            count += 1
    return count


def print_score_result(total, pass_num, average):
    """格式化输出成绩统计结果"""
    print(f"总分：{total}")
    print(f"及格人数：{pass_num}")
    print(f"平均分：{average:.2f}")


scores = [85, 92, 76, 58, 90]
total = get_total_score(scores)
pass_num = get_pass_count(scores)
avg = calculate_average(total, len(scores))
print_score_result(total, pass_num, avg)

# 3. 类与函数分层结构
print("\n===== 3. 类与函数分层结构 =====")


class Student:
    """学生信息类"""

    def __init__(self, stu_id, name, score):
        self.stu_id = stu_id
        self.name = name
        self.score = score

    def get_grade(self):
        """获取成绩等级"""
        if self.score >= 90:
            return "优秀"
        elif self.score >= 60:
            return "及格"
        else:
            return "不及格"


def batch_get_grades(student_list):
    """批量获取学生等级列表"""
    grade_list = []
    for stu in student_list:
        grade_list.append((stu.name, stu.get_grade()))

    return grade_list


stu_list = [
    Student("001", "小明", 95),
    Student("002", "小红", 78),
    Student("003", "小刚", 55)
]
grades = batch_get_grades(stu_list)
for name, grade in grades:
    print(f"{name}：{grade}")

# 4. 主入口规范演示
print("\n===== 4. 主入口规范演示 =====")
print(f"当前模块名：{__name__}")
print("if __name__ == '__main__' 可确保模块被导入时不执行主逻辑")

# ====================== 综合练习区 ======================
DEFAULT_PASS_LINE = 60


def input_student_info():
    """接收用户输入，返回学生对象列表"""
    student_list = []
    count = int(input("请输入学生人数："))
    for i in range(count):
        print(f"\n第{i + 1}名学生")
        stu_id = input("学号：")
        name = input("姓名：")
        score = float(input("分数："))
        student = Student(stu_id, name, score)
        student_list.append(student)

    return student_list


def calculat_statistics(student_list, pass_line=DEFAULT_PASS_LINE):
    """计算成绩统计数据，返回统计字典"""
    total_score = 0
    pass_count = 0
    for stu in student_list:
        total_score += stu.score
        if stu.score >= pass_line:
            pass_count += 1
    average = total_score / len(student_list) if student_list else 0
    pass_rate = pass_count / len(student_list) if student_list else 0
    return {
        "total_student": len(student_list),
        "total_score": total_score,
        "pass_count": pass_count,
        "average": average,
        "pass_rate": pass_rate
    }


def print_statistics_report(stats):
    """格式化输出成绩统计报告"""
    print("\n===== 成绩统计报告 =====")
    print(f"学生总数：{stats['total_student']} 人")
    print(f"总分合计：{stats['total_score']:.2f} 分")
    print(f"及格人数：{stats['pass_count']} 人")
    print(f"平均分：{stats['average']:.2f} 分")
    print(f"及格率：{stats['pass_rate'] * 100:.1f}%")


def daily_practice():
    """符合工程规范的成绩统计工具，串联当日知识点"""
    print("\n===== 综合练习：工程化成绩统计系统 =====")
    student_list = input_student_info()
    stats = calculat_statistics(student_list)
    print_statistics_report(stats)
    print("\n代码遵循PEP8规范，函数单一职责，命名统一")


if __name__ == "__main__":
    daily_practice()
