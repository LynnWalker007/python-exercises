# 04 - 列表和字典

# 列表 (List)
print("=== 列表操作 ===")
fruits = ["苹果", "香蕉", "橙子"]
print(f"原始列表: {fruits}")

# 添加元素
fruits.append("葡萄")
print(f"添加葡萄后: {fruits}")

fruits.insert(1, "草莓")
print(f"在位置1插入草莓: {fruits}")

# 删除元素
removed = fruits.pop()
print(f"删除最后一个元素 '{removed}': {fruits}")

fruits.remove("香蕉")
print(f"删除香蕉: {fruits}")

# 列表切片
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"\n原数组: {numbers}")
print(f"前5个: {numbers[:5]}")
print(f"后5个: {numbers[5:]}")
print(f"中间部分: {numbers[2:7]}")
print(f"每隔2个: {numbers[::2]}")
print(f"倒序: {numbers[::-1]}")

# 列表推导式
print("\n=== 列表推导式 ===")
squares = [x**2 for x in range(1, 6)]
print(f"1-5的平方: {squares}")

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"1-10中偶数的平方: {even_squares}")

# 嵌套列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"\n矩阵: {matrix}")
print(f"第2行第3列: {matrix[1][2]}")

# 列表方法
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\n原列表: {numbers}")
print(f"长度: {len(numbers)}")
print(f"最大值: {max(numbers)}")
print(f"最小值: {min(numbers)}")
print(f"总和: {sum(numbers)}")
print(f"1出现次数: {numbers.count(1)}")

sorted_numbers = sorted(numbers)
print(f"排序后: {sorted_numbers}")

# 字典 (Dictionary)
print("\n=== 字典操作 ===")
person = {
    "name": "张三",
    "age": 25,
    "city": "北京",
    "hobbies": ["读书", "游泳", "编程"]
}

print(f"姓名: {person['name']}")
print(f"年龄: {person['age']}")
print(f"爱好: {person['hobbies']}")

# 添加/修改键值对
person["email"] = "zhangsan@example.com"
person["age"] = 26
print(f"\n更新后的信息: {person}")

# 字典方法
print(f"\n所有键: {list(person.keys())}")
print(f"所有值: {list(person.values())}")
print(f"所有键值对: {list(person.items())}")

# 安全访问字典值
email = person.get("email", "未提供")
phone = person.get("phone", "未提供")
print(f"邮箱: {email}")
print(f"电话: {phone}")

# 字典推导式
print("\n=== 字典推导式 ===")
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"数字及其平方: {squares_dict}")

# 嵌套字典
students = {
    "张三": {"数学": 85, "英语": 92, "物理": 78},
    "李四": {"数学": 90, "英语": 87, "物理": 95},
    "王五": {"数学": 78, "英语": 85, "物理": 82}
}

print(f"\n学生成绩:")
for name, scores in students.items():
    avg = sum(scores.values()) / len(scores)
    print(f"{name}: {scores}, 平均分: {avg:.1f}")

# 集合 (Set)
print("\n=== 集合操作 ===")
numbers_set = {1, 2, 3, 4, 5, 3, 2, 1}
print(f"集合(自动去重): {numbers_set}")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"集合1: {set1}")
print(f"集合2: {set2}")
print(f"交集: {set1 & set2}")
print(f"并集: {set1 | set2}")
print(f"差集: {set1 - set2}")

# 元组 (Tuple)
print("\n=== 元组操作 ===")
coordinates = (10, 20)
rgb_color = (255, 128, 0)
print(f"坐标: {coordinates}")
print(f"RGB颜色: {rgb_color}")

x, y = coordinates
r, g, b = rgb_color
print(f"x={x}, y={y}")
print(f"红={r}, 绿={g}, 蓝={b}")

# 元组是不可变的
print(f"元组长度: {len(coordinates)}")
print(f"第一个元素: {coordinates[0]}")
# coordinates[0] = 15  # 这会报错，因为元组不可变