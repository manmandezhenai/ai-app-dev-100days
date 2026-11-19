"""Day01 知识点示例代码"""

# ====================== 知识点演示区 ======================
# 1. 变量定义与基础数据类型
print("\n===== 1. 变量定义与基础数据类型 =====")
user_name = "张三"
age = 20
height = 1.78
is_student = True
print(f"姓名：{user_name}，类型：{type(user_name)}")
print(f"年龄：{age}，类型：{type(age)}")
print(f"身高：{height}，类型：{type(height)}")
print(f"是否为学生：{is_student}，类型：{type(is_student)}")

# 2. print输出函数用法
print("\n===== 2. print输出函数用法 =====")
print("单条内容基础输出")
print("多内容拼接", "自动添加空格", "输出效果")
print("不换行输出测试", end=" ")
print("同一行后续内容")

# 3. 数据类型转换
print("\n===== 3. 数据类型转换 =====")
num_str = "123"
num_int = int(num_str)
print(f"字符串转整数结果：{num_int}，类型：{type(num_int)}")
price_str = "9.9"
price_float = float(price_str)
print(f"字符串转浮点数结果：{price_float}，类型：{type(price_float)}")


# ====================== 综合练习区 ======================
def daily_practice():
    """接收用户输入姓名与年龄，格式化输出个人信息汇总"""
    print("\n===== 综合练习：个人信息录入 =====")
    name = input("请输入您的姓名：")
    age = int(input("请输入您的年龄："))

    print("\n===== 信息汇总 =====")
    print(f"姓名：{name}")
    print(f"当前年龄：{age} 岁")
    print(f"明年年龄：{age + 1} 岁")


if __name__ == "__main__":
    daily_practice()
