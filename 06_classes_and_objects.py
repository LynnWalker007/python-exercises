# 06 - 类和对象 (面向对象编程)

print("=== 基础类定义 ===")

class Person:
    """人员类 - 基础示例"""
    
    def __init__(self, name, age):
        """构造函数"""
        self.name = name
        self.age = age
    
    def introduce(self):
        """自我介绍方法"""
        return f"我叫{self.name}，今年{self.age}岁"
    
    def have_birthday(self):
        """过生日方法"""
        self.age += 1
        print(f"{self.name}过生日了！现在{self.age}岁")

# 创建对象实例
person1 = Person("张三", 25)
person2 = Person("李四", 30)

print(person1.introduce())
print(person2.introduce())

person1.have_birthday()
print(person1.introduce())

print("\n=== 类属性和实例属性 ===")

class Student:
    """学生类 - 演示类属性和实例属性"""
    
    # 类属性 - 所有实例共享
    school_name = "清华大学"
    student_count = 0
    
    def __init__(self, name, student_id, major):
        """构造函数"""
        # 实例属性 - 每个实例独有
        self.name = name
        self.student_id = student_id
        self.major = major
        self.grades = {}
        
        # 更新学生计数
        Student.student_count += 1
    
    def add_grade(self, subject, grade):
        """添加成绩"""
        self.grades[subject] = grade
    
    def get_average(self):
        """计算平均分"""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)
    
    def get_info(self):
        """获取学生信息"""
        avg = self.get_average()
        return f"学号: {self.student_id}, 姓名: {self.name}, 专业: {self.major}, 平均分: {avg:.1f}"
    
    @classmethod
    def get_student_count(cls):
        """类方法 - 获取学生总数"""
        return cls.student_count
    
    @staticmethod
    def is_passing_grade(grade):
        """静态方法 - 判断是否及格"""
        return grade >= 60

# 创建学生对象
student1 = Student("王小明", "2021001", "计算机科学")
student2 = Student("李小红", "2021002", "数学")

print(f"学校: {Student.school_name}")
print(f"学生总数: {Student.get_student_count()}")

student1.add_grade("数学", 85)
student1.add_grade("英语", 92)
student1.add_grade("编程", 88)

student2.add_grade("数学", 95)
student2.add_grade("英语", 78)

print(student1.get_info())
print(student2.get_info())

print(f"85分是否及格: {Student.is_passing_grade(85)}")
print(f"55分是否及格: {Student.is_passing_grade(55)}")

print("\n=== 继承 ===")

class Animal:
    """动物基类"""
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        """发出声音 - 基类方法"""
        return f"{self.name}发出了声音"
    
    def introduce(self):
        """自我介绍"""
        return f"我是{self.name}，是一只{self.species}"

class Dog(Animal):
    """狗类 - 继承自Animal"""
    
    def __init__(self, name, breed):
        super().__init__(name, "狗")  # 调用父类构造函数
        self.breed = breed
    
    def make_sound(self):
        """重写父类方法"""
        return f"{self.name}汪汪叫"
    
    def fetch(self):
        """狗特有的方法"""
        return f"{self.name}去捡球了"

class Cat(Animal):
    """猫类 - 继承自Animal"""
    
    def __init__(self, name, color):
        super().__init__(name, "猫")
        self.color = color
    
    def make_sound(self):
        """重写父类方法"""
        return f"{self.name}喵喵叫"
    
    def climb(self):
        """猫特有的方法"""
        return f"{self.color}色的{self.name}爬上了树"

# 创建动物对象
dog = Dog("小白", "金毛")
cat = Cat("小花", "橙")

print(dog.introduce())
print(dog.make_sound())
print(dog.fetch())

print(cat.introduce())
print(cat.make_sound())
print(cat.climb())

print("\n=== 多态 ===")

animals = [dog, cat]
print("所有动物的声音:")
for animal in animals:
    print(f"- {animal.make_sound()}")

print("\n=== 封装和私有属性 ===")

class BankAccount:
    """银行账户类 - 演示封装"""
    
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.__balance = initial_balance  # 私有属性
        self.__transaction_history = []   # 私有属性
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"存款: +{amount}")
            return f"存款成功，当前余额: {self.__balance}"
        return "存款金额必须大于0"
    
    def withdraw(self, amount):
        """取款"""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"取款: -{amount}")
            return f"取款成功，当前余额: {self.__balance}"
        return "余额不足或取款金额无效"
    
    def get_balance(self):
        """获取余额"""
        return self.__balance
    
    def get_transaction_history(self):
        """获取交易记录"""
        return self.__transaction_history.copy()
    
    def __str__(self):
        """字符串表示"""
        return f"账户: {self.account_number}, 余额: {self.__balance}"

# 创建银行账户
account = BankAccount("123456789", 1000)
print(account)

print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))  # 余额不足

print(f"当前余额: {account.get_balance()}")
print(f"交易记录: {account.get_transaction_history()}")

# 不能直接访问私有属性
# print(account.__balance)  # 这会报错

print("\n=== 特殊方法 (魔术方法) ===")

class Point:
    """点类 - 演示特殊方法"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """字符串表示"""
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        """开发者字符串表示"""
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):
        """加法运算"""
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        """相等比较"""
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        """长度 (距离原点的距离)"""
        return int((self.x**2 + self.y**2)**0.5)

# 创建点对象
p1 = Point(3, 4)
p2 = Point(1, 2)

print(f"点1: {p1}")
print(f"点2: {p2}")
print(f"点1 + 点2 = {p1 + p2}")
print(f"点1 == 点2: {p1 == p2}")
print(f"点1的长度: {len(p1)}")

print("\n=== 属性装饰器 ===")

class Circle:
    """圆类 - 演示属性装饰器"""
    
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """半径属性"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """设置半径"""
        if value > 0:
            self._radius = value
        else:
            raise ValueError("半径必须大于0")
    
    @property
    def area(self):
        """面积属性 (只读)"""
        return 3.14159 * self._radius ** 2
    
    @property
    def circumference(self):
        """周长属性 (只读)"""
        return 2 * 3.14159 * self._radius

# 创建圆对象
circle = Circle(5)
print(f"半径: {circle.radius}")
print(f"面积: {circle.area:.2f}")
print(f"周长: {circle.circumference:.2f}")

circle.radius = 3
print(f"修改后半径: {circle.radius}")
print(f"修改后面积: {circle.area:.2f}")

try:
    circle.radius = -1  # 这会抛出异常
except ValueError as e:
    print(f"错误: {e}")