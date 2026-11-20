"""Day06 知识点示例代码"""
import sys
import os
import random

# ====================== 知识点演示区 ======================
# 1. 标准库模块基础调用
print("\n===== 1. 标准库模块基础调用 =====")
print(f"Python版本信息：{sys.version}")
print(f"当前工作目录：{os.getcwd()}")
print(f"生成0-10随机整数：{random.randint(0, 10)}")

# 2. os模块路径与文件操作
print("\n===== 2. os模块路径操作 =====")
demo_path = os.path.join("test_dir", "demo.txt")
print(f"拼接后的路径：{demo_path}")
print(f"当前脚本是否为文件：{os.path.isfile(__file__)}")

# 3. random模块常用方法
print("\n===== 3. random模块常用方法 =====")
fruit_list = ["苹果", "香蕉", "橙子", "葡萄"]
print(f"列表随机选择一个：{random.choice(fruit_list)}")
print(f"0-1随机浮点数：{random.random():.3f}")
random.shuffle(fruit_list)
print(f"打乱后的列表：{fruit_list}")


# ====================== 综合练习区 ======================
def env_info_check():
    """输出当前Python环境基础信息，生成随机测试数据集"""
    print("\n===== 综合练习：环境信息检测工具 =====")
    print("【环境基础信息】")
    print(f"Python主版本：{sys.version_info.major}.{sys.version_info.minor}")
    print(f"平台系统：{sys.platform}")
    print(f"当前脚本绝对路径：{os.path.abspath(__file__)}")

    print("\n【随机测试数据生成】")
    test_nums = []
    for _ in range(5):
        test_nums.append(random.randint(1, 100))
    print(f"生成5个1-100的随机整数：{test_nums}")
    print(f"其中最大值：{max(test_nums)}，最小值：{min(test_nums)}")
    sample = random.sample(test_nums, 2)
    print(f"随机抽取2个样本：{sample}")


def daily_practice():
    """串联当日知识点的综合实操练习"""
    env_info_check()


if __name__ == '__main__':
    daily_practice()
