"""Day02 知识点示例代码"""

# ====================== 知识点演示区 ======================
# 1. if双分支判断
print("\n===== 1. if双分支判断 =====")
score = 75
if score >= 60:
    print("成绩合格")
else:
    print("成绩不合格")

# 2. 多分支等级判定
print("\n===== 2. 多分支等级判定 =====")
if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"
print(f"成绩等级：{grade}")

# 3. for循环基础遍历
print("\n===== 3. for循环基础遍历 =====")
print("遍历字符串：")
for char in "Python":
    print(char, end=" ")

print("\nrange序列遍历：")
for i in range(1, 6):
    print(i, end=" ")

# 4. while循环计数
print("\n\n===== 4. while循环计数 =====")
count = 1
while count <= 5:
    print(f"第{count}次循环")
    count += 1

# 5. 循环控制语句
print("\n===== 5. 循环控制语句 =====")
print("continue跳过偶数：")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")

print("\nbreak遇到5终止：")
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=" ")


# ====================== 综合练习区 ======================
def daily_practice():
    """接收用户输入正整数，判定范围并计算累加和与奇数数量"""
    print("\n\n===== 综合练习：数字判断与累加 =====")
    num = int(input("请输入一个正整数："))

    # 分支校验输入有效性
    if num <= 0:
        print("输入无效，请输入正整数！")
        return

    # while循环计算累加和
    total = 0
    current = 1
    while current <= num:
        total += current
        current += 1
    print(f"1到{num}的累加和为：{total}")

    # for循环统计奇数个数
    odd_count = 0
    for i in range(1, num + 1):
        if i % 2 == 0:
            continue
        odd_count += 1
    print(f"1到{num}中共有{odd_count}个奇数")


if __name__ == "__main__":
    daily_practice()
