# 03 - 函数

# 基本函数定义
def greet(name):
    """简单的问候函数"""
    return f"你好, {name}!"

# 调用函数
print("=== 基本函数 ===")
message = greet("小明")
print(message)

# 带默认参数的函数
def introduce(name, age=18, city="北京"):
    """带默认参数的函数"""
    return f"我叫{name}，今年{age}岁，来自{city}。"

print("\n=== 默认参数 ===")
print(introduce("张三"))
print(introduce("李四", 25))
print(introduce("王五", 30, "上海"))

# 多个返回值
def calculate(a, b):
    """返回多个值的函数"""
    add = a + b
    subtract = a - b
    multiply = a * b
    divide = a / b if b != 0 else 0
    return add, subtract, multiply, divide

print("\n=== 多个返回值 ===")
result1, result2, result3, result4 = calculate(10, 3)
print(f"10 + 3 = {result1}")
print(f"10 - 3 = {result2}")
print(f"10 × 3 = {result3}")
print(f"10 ÷ 3 = {result4:.2f}")

# 可变参数 *args
def sum_all(*numbers):
    """计算所有数字的和"""
    total = 0
    for num in numbers:
        total += num
    return total

print("\n=== 可变参数 *args ===")
print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

# 关键字参数 **kwargs
def print_info(**info):
    """打印所有信息"""
    for key, value in info.items():
        print(f"{key}: {value}")

print("\n=== 关键字参数 **kwargs ===")
print_info(name="小红", age=22, hobby="读书", city="广州")

# 组合参数
def complex_function(required, default="默认值", *args, **kwargs):
    """组合使用各种参数类型"""
    print(f"必需参数: {required}")
    print(f"默认参数: {default}")
    print(f"可变参数: {args}")
    print(f"关键字参数: {kwargs}")

print("\n=== 组合参数 ===")
complex_function("必需的", "自定义默认值", 1, 2, 3, name="测试", value=100)

# Lambda 函数
print("\n=== Lambda 函数 ===")
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"原数组: {numbers}")
print(f"平方后: {squared_numbers}")

# 过滤偶数
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"偶数: {even_numbers}")

# 递归函数
def factorial(n):
    """计算阶乘的递归函数"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("\n=== 递归函数 ===")
print(f"5! = {factorial(5)}")
print(f"6! = {factorial(6)}")