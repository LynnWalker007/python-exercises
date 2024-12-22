# 01 - 变量和数据类型

# 基本变量赋值
name = "张三"
age = 25
height = 1.75
is_student = True

print(f"姓名: {name}")
print(f"年龄: {age}")
print(f"身高: {height}米")
print(f"是否是学生: {is_student}")

# 数据类型
print("\n--- 数据类型 ---")
print(f"name 的类型: {type(name)}")
print(f"age 的类型: {type(age)}")
print(f"height 的类型: {type(height)}")
print(f"is_student 的类型: {type(is_student)}")

# 字符串操作
print("\n--- 字符串操作 ---")
greeting = "你好，世界！"
print(f"原字符串: {greeting}")
print(f"字符串长度: {len(greeting)}")
print(f"转换为大写: {greeting.upper()}")
print(f"字符串切片: {greeting[0:2]}")

# 数值运算
print("\n--- 数值运算 ---")
a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")  # 整除
print(f"{a} % {b} = {a % b}")   # 取余
print(f"{a} ** {b} = {a ** b}") # 幂运算