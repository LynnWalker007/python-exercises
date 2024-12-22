# 05 - 文件读写操作

import os

print("=== 文件写入 ===")

# 写入文本文件
content = """这是第一行
这是第二行
这是第三行"""

with open("example.txt", "w", encoding="utf-8") as file:
    file.write(content)
print("已创建 example.txt 文件")

# 追加内容到文件
with open("example.txt", "a", encoding="utf-8") as file:
    file.write("\n这是追加的内容")
print("已追加内容到 example.txt")

print("\n=== 文件读取 ===")

# 读取整个文件
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("完整文件内容:")
    print(content)

# 按行读取文件
print("\n按行读取:")
with open("example.txt", "r", encoding="utf-8") as file:
    for line_num, line in enumerate(file, 1):
        print(f"第{line_num}行: {line.strip()}")

# 读取所有行到列表
with open("example.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(f"\n共读取{len(lines)}行:")
    for line in lines:
        print(f"- {line.strip()}")

print("\n=== JSON 文件操作 ===")
import json

# 创建字典数据
student_data = {
    "name": "李小明",
    "age": 20,
    "major": "计算机科学",
    "grades": {
        "数学": 95,
        "英语": 88,
        "编程": 92
    },
    "hobbies": ["阅读", "游泳", "编程"]
}

# 写入JSON文件
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student_data, file, ensure_ascii=False, indent=2)
print("已创建 student.json 文件")

# 读取JSON文件
with open("student.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)
    print(f"从JSON读取的数据:")
    print(f"姓名: {loaded_data['name']}")
    print(f"专业: {loaded_data['major']}")
    print(f"成绩: {loaded_data['grades']}")

print("\n=== CSV 文件操作 ===")
import csv

# 创建CSV数据
students = [
    ["姓名", "年龄", "专业", "成绩"],
    ["张三", "20", "计算机", "85"],
    ["李四", "21", "数学", "92"],
    ["王五", "19", "物理", "78"],
    ["赵六", "22", "化学", "90"]
]

# 写入CSV文件
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(students)
print("已创建 students.csv 文件")

# 读取CSV文件
print("CSV文件内容:")
with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 使用字典读取CSV
print("\n使用字典读取CSV:")
with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['姓名']} - {row['专业']} - {row['成绩']}分")

print("\n=== 文件和目录操作 ===")

# 检查文件是否存在
files_to_check = ["example.txt", "student.json", "nonexistent.txt"]
for filename in files_to_check:
    if os.path.exists(filename):
        print(f"✓ {filename} 存在")
        print(f"  文件大小: {os.path.getsize(filename)} 字节")
    else:
        print(f"✗ {filename} 不存在")

# 列出当前目录的文件
print(f"\n当前目录: {os.getcwd()}")
print("目录内容:")
for item in os.listdir("."):
    if os.path.isfile(item):
        print(f"📄 {item}")
    elif os.path.isdir(item):
        print(f"📁 {item}")

# 创建目录
if not os.path.exists("temp_folder"):
    os.mkdir("temp_folder")
    print("✓ 已创建 temp_folder 目录")

# 在目录中创建文件
temp_file_path = os.path.join("temp_folder", "temp_file.txt")
with open(temp_file_path, "w", encoding="utf-8") as file:
    file.write("这是临时文件的内容")
print(f"✓ 已创建 {temp_file_path}")

print("\n=== 文件操作最佳实践 ===")

def safe_read_file(filename):
    """安全读取文件的函数"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"错误: 文件 {filename} 不存在")
        return None
    except PermissionError:
        print(f"错误: 没有权限读取文件 {filename}")
        return None
    except Exception as e:
        print(f"读取文件时发生未知错误: {e}")
        return None

# 测试安全读取函数
content = safe_read_file("example.txt")
if content:
    print("成功读取文件内容")
    
content = safe_read_file("nonexistent.txt")
if not content:
    print("文件读取失败，已处理错误")

# 清理创建的文件（可选）
print("\n=== 清理文件 ===")
files_to_remove = ["example.txt", "student.json", "students.csv"]
for filename in files_to_remove:
    if os.path.exists(filename):
        # os.remove(filename)  # 取消注释以实际删除文件
        print(f"可以删除: {filename}")

# 删除临时目录和文件
if os.path.exists(temp_file_path):
    # os.remove(temp_file_path)  # 取消注释以实际删除文件
    print(f"可以删除: {temp_file_path}")

if os.path.exists("temp_folder"):
    # os.rmdir("temp_folder")  # 取消注释以实际删除目录
    print("可以删除: temp_folder 目录")