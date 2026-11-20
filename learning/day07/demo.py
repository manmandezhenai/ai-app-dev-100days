"""Day07 知识点示例代码"""

# ====================== 知识点演示区 ======================
# 1. 基础异常捕获
print("\n===== 1. 基础异常捕获 =====")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("捕获到除数为0异常，已处理")

# 2. 多类型异常捕获
print("\n===== 2. 多类型异常捕获 =====")
test_list = [1, 2, 3]
try:
    num = int("abc")
    print(test_list[5])
except ValueError:
    print("捕获到值转换异常")
except IndexError:
    print("捕获到索引越界异常")

# 3. else与finally分支
print("\n===== 3. else与finally分支 =====")
try:
    num = int("123")
except ValueError:
    print("转换失败")
else:
    print(f"转换成功，结果：{num}")
finally:
    print("finally收尾逻辑执行完毕")

# 4. 统一捕获多个异常
print("\n===== 4. 统一捕获多个异常 =====")
try:
    print(1 + "字符串")
except (TypeError, KeyError) as e:
    print(f"捕获到类型 / 键异常：{e}")


# ====================== 综合练习区 ======================
def safe_divide_calculator():
    """安全除法计算器，处理输入异常、除数异常，统计计算结果"""
    print("\n===== 综合练习：安全除法计算器 =====")
    success_count = 0
    fail_count = 0

    for i in range(3):
        print(f"\n第{i + 1}次计算")
        input_a = input("请输入被除数：")
        input_b = input("请输入除数：")

        try:
            num_a = float(input_a)
            num_b = float(input_b)
            result = num_a / num_b
        except ValueError:
            print("输入无效，请输入数字")
            fail_count += 1
        except ZeroDivisionError:
            print("除数不能为0，请重新输入")
            fail_count += 1
        else:
            print(f"计算结果：{result}")
            success_count += 1
        finally:
            print("本次计算流程结束")

    print(f"\n计算统计：成功{success_count}次，失败{fail_count}次")


def daily_practice():
    """串联当日知识点的综合实操练习"""
    safe_divide_calculator()


if __name__ == "__main__":
    daily_practice()
