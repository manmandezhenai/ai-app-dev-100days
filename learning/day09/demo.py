"""Day09 知识点示例代码"""

# ====================== 知识点演示区 ======================
# 1. 类的基础定义与实例化
print("\n===== 1. 类的基础定义与实例化 =====")


class Student:
    """学生基础定义"""

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu1 = Student("张三", 20)
stu2 = Student("李四", 21)
print(f"学生1 - 姓名：{stu1.name}，年龄：{stu1.age}")
print(f"学生2 - 姓名：{stu2.name}，年龄：{stu2.age}")

# 2. 实例方法定义与调用
print("\n===== 2. 实例方法定义与调用 =====")


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):
        """输出学生自我介绍"""
        print(f"我叫{self.name}，当前成绩：{self.score}分")

    def update_score(self, new_score):
        """更新学生成绩"""
        self.score = new_score


stu = Student("王五", 85)
stu.introduce()
stu.update_score(92)
print("更新成绩后：")
stu.introduce()

# 3. 多实例属性独立性
print("\n===== 3. 多实例属性独立性 =====")
stu_a = Student("小明", 78)
stu_b = Student("小红", 95)
stu_a.update_score(80)
print(f"小明成绩：{stu_a.score}")
print(f"小红成绩：{stu_b.score}")
print("修改小明成绩不影响小红的成绩")

# 4. 属性修改与动态添加
print("\n===== 4. 属性修改与动态添加 =====")
book = type("Book", (), {})()
book.title = "Python入门"
book.price = 59.9
print(f"图书：{book.title}，价格：{book.price}元")


# ====================== 综合练习区 ======================
class Book:
    """图书类，存储图书信息并提供打折计算方法"""

    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def get_discount_price(self, discount):
        """
        计算打折后的价格
        :param discount: 折扣比例，0-1之间
        """
        return discount * self.price

    def show_info(self):
        """输出图片完整信息"""
        print(f"编号：{self.book_id}，书名：{self.title}")
        print(f"作者：{self.author}，原价：{self.price}元")


def daily_practice():
    """图书管理小工具，创建多本图书并批量计算打折总价"""
    print("\n===== 综合练习：图书打折管理系统 =====")
    book_list = []
    book_count = 2
    for i in range(book_count):
        print(f"\n请输入{i + 1}本图书信息")
        book_id = input("图书编号：")
        title = input("书名：")
        author = input("作者：")
        price = float(input("原价："))
        book = Book(book_id, title, author, price)
        book_list.append(book)

    discount = float(input("\n请输入统一折扣比例（如0.8表示8折）："))
    total_original = 0
    total_discount = 0

    print("\n===== 图书清单与打折结果 =====")
    for idx, book in enumerate(book_list, 1):
        print(f"\n第{idx}本：")

        book.show_info()
        dis_price = book.get_discount_price(discount)
        print(f"打折后价格：{dis_price}")
        total_original += book.price
        total_discount += dis_price

    print(f"\n原价总价：{total_original:.2f}元")
    print(f"打折总价：{total_discount:.2f}元")
    print(f"共节省：{total_original - total_discount:.2f}元")


if __name__ == "__main__":
    daily_practice()
