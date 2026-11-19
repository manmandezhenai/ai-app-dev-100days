"""Day03 知识点示例代码"""

# ====================== 知识点演示区 ======================
# 1. 函数基础定义与调用
print("\n===== 1. 函数基础定义与调用 =====")


def greet_user(name):
    """向指定用户输出问候语"""
    print(f"你好，{name}！欢迎学习Python函数")


greet_user("张三")

# 2. 三类参数用法演示
print("\n===== 2. 函数参数分类演示 =====")


def calculate_area(length, width=1):
    """
    计算矩形面积
    :param length: 长度，位置参数
    :param width: 宽度，默认参数
    :return: 矩形面积
    """
    return length * width


# 位置参数调用
area1 = calculate_area(5, 3)
print(f"位置参数调用，面积：{area1}")
# 省略默认参数
area2 = calculate_area(4)
print(f"省略默认参数，面积：{area2}")
# 关键字参数调用
area3 = calculate_area(width=4, length=6)
print(f"关键字参数调用：{area3}")

# 3. return返回值用法
print("\n===== 3. return返回值演示 =====")


def divide_num(a, b):
    """计算两数的商和余数，返回多个结果"""
    quotient = a // b
    remainder = a % b
    return quotient, remainder


q, r = divide_num(10, 3)
print(f"10除以3，商：{q}，余数：{r}")


def no_return_func():
    """无return的函数"""
    print("该函数没有显式返回值")


result = no_return_func()
print(f"无return函数的返回值：{result}")

# 4. 变量作用域演示
print("\n===== 4. 变量作用域演示 =====")
global_num = 100


def scope_test():
    local_num = 50
    print(f"函数内部读取全局变量：{global_num}")
    print(f"函数内部局部变量：{local_num}")


scope_test()
print(f"函数外部全局变量：{global_num}")


# ====================== 综合练习区 ======================
def calculate_sum_average(start, end=10):
    """
    计算指定范围内整数的累加和与平均值
    :param start: 起始整数，位置参数
    :param end: 结束整数，默认参数
    :return: 累加和、平均值
    """
    total = 0
    for num in range(start, end + 1):
        total += num
    count = end - start + 1
    average = total / count
    return total, average


def daily_practice():
    """接收用户输入起止数字，调用函数计算并输出结果"""
    print("\n===== 综合练习：范围累加与平均值计算 =====")
    start_input = input("请输入起始整数：")
    end_input = input("请输入结束整数（直接回车使用默认值10）：")

    start = int(start_input)
    if end_input.strip() == "":
        total, avg = calculate_sum_average(start)
    else:
        end = int(end_input)
        total, avg = calculate_sum_average(start, end)

    print(f"累加和：{total}")
    print(f"平均值：{avg:.2f}")


if __name__ == "__main__":
    daily_practice()
