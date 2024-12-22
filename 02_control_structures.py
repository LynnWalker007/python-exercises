# 02 - 控制结构 (条件语句和循环)

# 条件语句 - if/elif/else
print("=== 条件语句 ===")
score = 85

if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 70:
    grade = "中等"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"分数: {score}, 等级: {grade}")

# 比较运算符
print("\n--- 比较运算符 ---")
x = 10
y = 20
print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x != y: {x != y}")
print(f"x < y: {x < y}")
print(f"x > y: {x > y}")
print(f"x <= y: {x <= y}")
print(f"x >= y: {x >= y}")

# 逻辑运算符
print("\n--- 逻辑运算符 ---")
a = True
b = False
print(f"a = {a}, b = {b}")
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")

# for 循环
print("\n=== for 循环 ===")
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print("水果列表:")
for fruit in fruits:
    print(f"- {fruit}")

print("\n数字循环:")
for i in range(5):
    print(f"数字: {i}")

print("\n带范围的循环:")
for i in range(2, 8, 2):
    print(f"偶数: {i}")

# while 循环
print("\n=== while 循环 ===")
count = 0
while count < 5:
    print(f"计数: {count}")
    count += 1

# 循环控制 - break 和 continue
print("\n=== 循环控制 ===")
print("使用 break:")
for i in range(10):
    if i == 5:
        break
    print(f"i = {i}")

print("\n使用 continue:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"奇数: {i}")