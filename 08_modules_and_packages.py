# 08 - 模块和包

print("=== 导入标准库模块 ===")

# 不同的导入方式
import math
from datetime import datetime, timedelta
from random import randint, choice
import os as operating_system

# 使用 math 模块
print(f"π 的值: {math.pi:.4f}")
print(f"10的平方根: {math.sqrt(10):.4f}")
print(f"sin(π/2): {math.sin(math.pi/2)}")

# 使用 datetime
now = datetime.now()
print(f"当前时间: {now}")
tomorrow = now + timedelta(days=1)
print(f"明天这时候: {tomorrow}")

# 使用 random
print(f"随机整数(1-100): {randint(1, 100)}")
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print(f"随机水果: {choice(fruits)}")

# 使用重命名的 os 模块
print(f"当前工作目录: {operating_system.getcwd()}")

print("\n=== 创建自定义模块 ===")

# 创建一个数学工具模块
math_utils_content = '''"""
数学工具模块
包含一些常用的数学函数
"""

def factorial(n):
    """计算阶乘"""
    if n < 0:
        raise ValueError("阶乘的参数必须是非负整数")
    if n <= 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    """判断是否为质数"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """生成斐波那契数列的前n项"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list

def gcd(a, b):
    """计算最大公约数（辗转相除法）"""
    while b:
        a, b = b, a % b
    return a

# 模块级变量
PI = 3.14159265359
E = 2.71828182846

# 模块初始化时执行的代码
print("数学工具模块已加载")

if __name__ == "__main__":
    # 当模块作为脚本直接运行时执行
    print("直接运行数学工具模块的测试:")
    print(f"5! = {factorial(5)}")
    print(f"17是质数吗? {is_prime(17)}")
    print(f"斐波那契数列前10项: {fibonacci(10)}")
    print(f"gcd(48, 18) = {gcd(48, 18)}")
'''

# 写入模块文件
with open("math_utils.py", "w", encoding="utf-8") as f:
    f.write(math_utils_content)
print("✓ 已创建 math_utils.py 模块")

# 导入并使用自定义模块
import math_utils

print(f"使用自定义模块:")
print(f"6! = {math_utils.factorial(6)}")
print(f"29是质数吗? {math_utils.is_prime(29)}")
print(f"斐波那契数列前8项: {math_utils.fibonacci(8)}")
print(f"PI常量: {math_utils.PI}")

print("\n=== 创建包 (Package) ===")

# 创建包目录结构
import os

package_name = "my_package"
if not os.path.exists(package_name):
    os.mkdir(package_name)
    print(f"✓ 已创建包目录: {package_name}")

# 创建 __init__.py 文件
init_content = '''"""
my_package - 演示Python包的使用
"""

__version__ = "1.0.0"
__author__ = "Python学习者"

# 包级别的导入
from .string_utils import reverse_string, count_words
from .data_utils import find_max, calculate_average

# 包初始化时执行
print(f"my_package v{__version__} 已加载")

# 定义包的公开接口
__all__ = [
    'reverse_string',
    'count_words', 
    'find_max',
    'calculate_average'
]
'''

with open(f"{package_name}/__init__.py", "w", encoding="utf-8") as f:
    f.write(init_content)

# 创建子模块1: string_utils.py
string_utils_content = '''"""
字符串工具模块
"""

def reverse_string(text):
    """反转字符串"""
    return text[::-1]

def count_words(text):
    """统计单词数量"""
    return len(text.split())

def capitalize_words(text):
    """将每个单词的首字母大写"""
    return ' '.join(word.capitalize() for word in text.split())

def remove_spaces(text):
    """移除所有空格"""
    return text.replace(' ', '')

if __name__ == "__main__":
    # 测试代码
    test_text = "hello world python"
    print(f"原文: {test_text}")
    print(f"反转: {reverse_string(test_text)}")
    print(f"单词数: {count_words(test_text)}")
    print(f"首字母大写: {capitalize_words(test_text)}")
'''

with open(f"{package_name}/string_utils.py", "w", encoding="utf-8") as f:
    f.write(string_utils_content)

# 创建子模块2: data_utils.py
data_utils_content = '''"""
数据处理工具模块
"""

def find_max(numbers):
    """找到列表中的最大值"""
    if not numbers:
        return None
    return max(numbers)

def find_min(numbers):
    """找到列表中的最小值"""
    if not numbers:
        return None
    return min(numbers)

def calculate_average(numbers):
    """计算平均值"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def remove_duplicates(items):
    """移除重复项，保持顺序"""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def sort_by_length(strings):
    """按字符串长度排序"""
    return sorted(strings, key=len)

if __name__ == "__main__":
    # 测试代码
    test_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(f"数组: {test_numbers}")
    print(f"最大值: {find_max(test_numbers)}")
    print(f"最小值: {find_min(test_numbers)}")
    print(f"平均值: {calculate_average(test_numbers):.2f}")
    print(f"去重: {remove_duplicates(test_numbers)}")
'''

with open(f"{package_name}/data_utils.py", "w", encoding="utf-8") as f:
    f.write(data_utils_content)

print("✓ 已创建包结构和子模块")

# 导入和使用包
print("\n=== 使用自定义包 ===")

# 方法1: 导入整个包
import my_package
print(f"包版本: {my_package.__version__}")

# 使用包中的函数
text = "Python编程很有趣"
numbers = [1, 5, 3, 9, 2, 8, 4]

print(f"原文: {text}")
print(f"反转: {my_package.reverse_string(text)}")
print(f"单词数: {my_package.count_words(text)}")

print(f"数组: {numbers}")
print(f"最大值: {my_package.find_max(numbers)}")
print(f"平均值: {my_package.calculate_average(numbers):.2f}")

# 方法2: 从包中导入特定函数
from my_package import reverse_string, find_max
print(f"直接使用函数: {reverse_string('hello')}, max = {find_max([1,2,3])}")

# 方法3: 导入子模块
from my_package import string_utils, data_utils
print(f"子模块使用: {string_utils.capitalize_words('hello world')}")
print(f"去重: {data_utils.remove_duplicates([1,2,2,3,3,4])}")

print("\n=== 模块搜索路径 ===")

import sys
print("Python模块搜索路径:")
for i, path in enumerate(sys.path[:5], 1):  # 只显示前5个路径
    print(f"{i}. {path}")

print(f"当前脚本: {__file__ if '__file__' in globals() else '交互模式'}")
print(f"模块名: {__name__}")

print("\n=== 常用标准库模块示例 ===")

# collections - 特殊容器
from collections import Counter, defaultdict, deque

# Counter 计数器
text = "hello world"
char_count = Counter(text)
print(f"字符计数: {char_count}")
print(f"最常见的3个字符: {char_count.most_common(3)}")

# defaultdict 默认字典
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
dd['colors'].append('red')
print(f"defaultdict: {dict(dd)}")

# deque 双端队列
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(f"deque: {dq}")

# itertools - 迭代器工具
from itertools import combinations, permutations

items = ['A', 'B', 'C']
print(f"排列: {list(permutations(items, 2))}")
print(f"组合: {list(combinations(items, 2))}")

# json - JSON处理
import json

data = {
    "name": "张三",
    "age": 25,
    "skills": ["Python", "JavaScript", "SQL"]
}

json_string = json.dumps(data, ensure_ascii=False, indent=2)
print(f"JSON字符串:\n{json_string}")

parsed_data = json.loads(json_string)
print(f"解析后: {parsed_data['name']} 会 {len(parsed_data['skills'])} 种技能")

print("\n=== 清理创建的文件 ===")

# 清理函数
def cleanup_files():
    """清理演示创建的文件和目录"""
    import shutil
    
    files_to_remove = ["math_utils.py"]
    dirs_to_remove = ["my_package", "__pycache__"]
    
    for file in files_to_remove:
        if os.path.exists(file):
            os.remove(file)
            print(f"✓ 已删除文件: {file}")
    
    for dir in dirs_to_remove:
        if os.path.exists(dir):
            shutil.rmtree(dir)
            print(f"✓ 已删除目录: {dir}")

# 取消注释下面这行来清理文件
# cleanup_files()
print("注意: 演示文件未被删除，你可以查看创建的 math_utils.py 和 my_package/ 目录")