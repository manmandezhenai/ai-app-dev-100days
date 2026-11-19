"""Day05 知识点示例代码"""
# ====================== 知识点演示区 ======================
# 1. 字符串基础操作
print("\n===== 1. 字符串基础操作 =====")
text = "Hello Python"
print(f"原字符串：{text}")
print(f"索引访问第2个字符：{text[1]}")
print(f"切片获取前5个字符：{text[:5]}")
print(f"步长为2切片：{text[::2]}")
print(f"字符串拼接：{text + ' 学习'}")
print(f"字符串重复3次：{'abc' * 3}")

# 2. 常用字符串方法
print("\n===== 2. 常用字符串方法 =====")
raw_text = "  测试字符串,处理,示例  "
print(f"原始字符串：{repr(raw_text)}")
strip_text = raw_text.strip()
print(f"strip去除首尾空白：{repr(strip_text)}")
split_list = strip_text.split(',')
print(f"按逗号拆分：{split_list}")
join_text = "-".join(split_list)
print(f"用横杠拼接：{join_text}")
replace_text = strip_text.replace("测试", "演示")
print(f"替换内容：{replace_text}")
print(f"转大写：{'Hello'.upper()}")
print(f"是否以'.py'结尾：{'demo.py'.endswith('.py')}")

# 3. 字符串格式化
print("\n===== 3. 字符串格式化 =====")
name = "李四"
age = 22
score = 95.5
# f-string格式化
print(f"f-string格式化 - 姓名：{name}，年龄：{age}，成绩：{score:.1f}分")
# format方法格式化
print("format格式化 - 姓名：{}，年龄：{}，成绩：{:.1f}分".format(name, age, score))

# 4. 通用内置函数与关键字
print("\n===== 4. 通用内置函数与关键字 =====")
demo_str = "python"
print(f"字符串长度：{len(demo_str)}")
print(f"数字转字符串：{repr(str(123))}，类型：{type(str(123))}")
print(f"最大字符：{max(demo_str)}")
print(f"最小字符：{min(demo_str)}")
print(f"'th'是否在字符串中：{'th' in demo_str}")


# ====================== 综合练习区 ======================
def daily_practice():
    """用户输入信息清洗与格式化输出，串联当日字符串知识点"""
    print("\n===== 综合练习：用户信息格式化工具 =====")
    # 接收原始输入
    raw_name = input("请输入您的姓名（可能前后空格）：")
    raw_email = input("请输入您的邮箱：")
    raw_phone = input("请输入您的手机号：")

    # 字符串处理
    name = raw_name.strip()
    email = raw_email.strip().lower()
    phone = raw_phone.strip().replace(' ', '')

    # 基础格式校验
    is_email_valid = email.endswith('.com') and "@" in email
    is_phone_valid = len(phone) == 11 and phone.isdigit()

    # 格式化输出结果
    print("\n===== 信息处理结果 =====")
    print(f"姓名：{name}")
    print(f"邮箱：{email}，格式有效性：{'通过' if is_email_valid else '不通过'}")
    print(f"手机号：{phone}，格式有效性：{'通过' if is_phone_valid else '不通过'}")

    # 手机号脱敏展示
    if is_phone_valid:
        hide_phone = phone[:3] + "****" + phone[-4:]
        print(f"手机号脱敏展示：{hide_phone}")


if __name__ == '__main__':
    daily_practice()
