"""Day14 知识点示例代码"""
import re

# ====================== 知识点演示区 ======================
# 1. 基础匹配函数用法
print("\n===== 1. 基础匹配函数用法 =====")
test_text = "Python 123 正则测试 456"
# match匹配开头
match_result = re.match(r"Python", test_text)
print(f"match开头匹配结果：{match_result.group() if match_result else '无匹配'}")

# search全文匹配
search_result = re.search(r"\d+", test_text)
print(f"search首个数字匹配：{search_result.group()}")

# findall全量匹配
all_nums = re.findall(r"\d+", test_text)
print(f"findall所有数字匹配：{all_nums}")

# 2. 常用元字符匹配演示
print("\n===== 2. 常用元字符匹配演示 =====")
demo_text = "用户：张三 手机号：13812345678 邮箱：zhangsan@qq.com"
# 匹配中文
name = re.search(r"用户：([\u4e00-\u9fa5]+)", demo_text)
print(f"提取姓名：{name.group(1)}")

# 匹配手机号
phone = re.search(r"手机号：(\d{11})", demo_text)
print(f"提取手机号：{phone.group(1)}")

# 匹配邮箱
email = re.search(r"邮箱：([\w@.]+)", demo_text)
print(f"提取邮箱：{email.group(1)}")

# 3. 多分组提取
print("\n===== 3. 多分组提取 =====")
info_text = "商品A-价格99元-库存50件"
result = re.search(r"(商品\w)-价格(\d+)元-库存(\d+)件", info_text)
if result:
    print(f"完整匹配：{result.group(0)}")
    print(f"商品名：{result.group(1)}")
    print(f"价格：{result.group(2)}")
    print(f"库存：{result.group(3)}")
    print(f"所有分组：{result.groups()}")

# 4. 替换与分割操作
print("\n===== 4. 替换与分割操作 =====")
raw_text = "abc123def456ghi789"
# 替换所有数字为星号
replace_text = re.sub(r"\d+", "***", raw_text)
print(f"数字替换后：{replace_text}")

# 按数字分割字符串
split_list = re.split(r"\d+", raw_text)
print(f"按数字分割：{split_list}")


# ====================== 综合练习区 ======================
def text_info_extractor():
    """从用户输入的文本中提取手机号、邮箱、数字并统计"""
    print("\n===== 综合练习：文本信息提取工具 =====")
    text = input("请输入包含手机号、邮箱、数字的混合文本：\n")

    # 提取手机号
    phone_pattern = r"1[3-9]\d{9}"
    phones = re.findall(phone_pattern, text)

    # 提取邮箱
    email_pattern = r"[0-9a-zA-Z_-]+@[0-9a-zA-Z_-]+\.[0-9a-zA-Z.]+"
    emails = re.findall(email_pattern, text)

    # 提取所有纯数字，然后过滤掉已经抓到的手机号，防止重复
    all_num_str = re.findall(r"\d+", text)
    nums = [n for n in all_num_str if n not in phones]

    print("\n===== 提取结果 =====")
    if phones:
        print(f"提取到手机号 {len(phones)} 个：{phones}")
    else:
        print("未提取到有效手机号")

    if emails:
        print(f"提取到邮箱 {len(emails)} 个：{emails}")
    else:
        print("未提取到有效邮箱")

    if nums:
        num_sum = sum(int(n) for n in nums)
        print(f"提取到数字 {len(nums)} 个：{nums}")
        print(f"数字累加和：{num_sum}")
    else:
        print("未提取到数字")


def daily_practice():
    """串联当日知识点的综合实操练习"""
    text_info_extractor()


if __name__ == "__main__":
    daily_practice()
