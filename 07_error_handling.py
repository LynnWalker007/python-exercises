# 07 - 错误处理和异常

print("=== 基本异常处理 ===")

# 基本 try-except 结构
def divide_numbers(a, b):
    """除法运算示例"""
    try:
        result = a / b
        print(f"{a} ÷ {b} = {result}")
        return result
    except ZeroDivisionError:
        print("错误: 不能除以零!")
        return None

# 测试除法函数
divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers(15, 3)

print("\n=== 处理多种异常类型 ===")

def process_list_item(my_list, index):
    """处理列表元素，演示多种异常"""
    try:
        # 可能的异常: IndexError, TypeError
        item = my_list[index]
        result = item * 2
        print(f"列表[{index}] = {item}, 结果 = {result}")
        return result
    except IndexError:
        print(f"错误: 索引 {index} 超出列表范围")
        return None
    except TypeError:
        print(f"错误: 无法对类型 {type(my_list[index])} 进行运算")
        return None
    except Exception as e:
        print(f"未知错误: {e}")
        return None

# 测试列表处理函数
test_list = [1, 2, "hello", 4, 5]
process_list_item(test_list, 1)   # 正常情况
process_list_item(test_list, 10)  # IndexError
process_list_item(test_list, 2)   # TypeError

print("\n=== 使用 else 和 finally ===")

def read_file_safely(filename):
    """安全读取文件，演示完整的异常处理结构"""
    file_handle = None
    try:
        print(f"尝试打开文件: {filename}")
        file_handle = open(filename, 'r', encoding='utf-8')
        content = file_handle.read()
        print(f"文件读取成功，长度: {len(content)} 字符")
        return content
    except FileNotFoundError:
        print(f"错误: 文件 {filename} 不存在")
        return None
    except PermissionError:
        print(f"错误: 没有权限读取文件 {filename}")
        return None
    except Exception as e:
        print(f"读取文件时发生未知错误: {e}")
        return None
    else:
        print("文件读取操作成功完成")  # 只在没有异常时执行
    finally:
        print("清理资源...")  # 无论是否有异常都会执行
        if file_handle and not file_handle.closed:
            file_handle.close()
            print("文件已关闭")

# 先创建一个测试文件
with open("test_file.txt", "w", encoding="utf-8") as f:
    f.write("这是测试文件内容\n第二行内容")

# 测试文件读取
read_file_safely("test_file.txt")    # 成功情况
read_file_safely("nonexistent.txt") # 文件不存在

print("\n=== 抛出自定义异常 ===")

class InvalidAgeError(Exception):
    """自定义异常 - 年龄无效"""
    def __init__(self, age, message="年龄必须在0-150之间"):
        self.age = age
        self.message = message
        super().__init__(self.message)

class InsufficientFundsError(Exception):
    """自定义异常 - 余额不足"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"余额不足: 当前余额 {balance}, 尝试取款 {amount}"
        super().__init__(message)

def validate_age(age):
    """验证年龄"""
    if not isinstance(age, int):
        raise TypeError("年龄必须是整数")
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    print(f"年龄 {age} 验证通过")

def withdraw_money(balance, amount):
    """取款操作"""
    if amount <= 0:
        raise ValueError("取款金额必须大于0")
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    
    new_balance = balance - amount
    print(f"取款成功: 取款 {amount}, 余额 {new_balance}")
    return new_balance

# 测试自定义异常
try:
    validate_age(25)    # 正常
    validate_age(200)   # 年龄无效
except InvalidAgeError as e:
    print(f"年龄验证失败: {e}")

try:
    validate_age("abc") # 类型错误
except (InvalidAgeError, TypeError) as e:
    print(f"验证失败: {e}")

try:
    withdraw_money(1000, 500)   # 正常
    withdraw_money(1000, 1500)  # 余额不足
except InsufficientFundsError as e:
    print(f"取款失败: {e}")
except ValueError as e:
    print(f"输入错误: {e}")

print("\n=== 异常链和调试信息 ===")

def level1_function():
    """第一层函数"""
    print("进入 level1_function")
    level2_function()

def level2_function():
    """第二层函数"""
    print("进入 level2_function")
    level3_function()

def level3_function():
    """第三层函数 - 会抛出异常"""
    print("进入 level3_function")
    result = 1 / 0  # 故意制造异常

def demonstrate_traceback():
    """演示异常追踪"""
    try:
        level1_function()
    except Exception as e:
        print(f"捕获异常: {e}")
        print("异常类型:", type(e).__name__)
        
        import traceback
        print("\n详细异常信息:")
        traceback.print_exc()

demonstrate_traceback()

print("\n=== 上下文管理器和 with 语句 ===")

class DatabaseConnection:
    """模拟数据库连接的上下文管理器"""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False
    
    def __enter__(self):
        """进入上下文时调用"""
        print(f"连接到数据库: {self.db_name}")
        self.connected = True
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """退出上下文时调用"""
        print(f"关闭数据库连接: {self.db_name}")
        self.connected = False
        if exc_type:
            print(f"处理异常: {exc_type.__name__}: {exc_value}")
        return False  # 不抑制异常
    
    def execute_query(self, query):
        """执行查询"""
        if not self.connected:
            raise RuntimeError("数据库未连接")
        print(f"执行查询: {query}")
        if "error" in query.lower():
            raise ValueError("查询包含错误")
        return f"查询 '{query}' 执行成功"

# 使用上下文管理器
print("正常情况:")
with DatabaseConnection("testdb") as db:
    result = db.execute_query("SELECT * FROM users")
    print(result)

print("\n异常情况:")
try:
    with DatabaseConnection("testdb") as db:
        db.execute_query("SELECT error FROM table")
except ValueError as e:
    print(f"查询失败: {e}")

print("\n=== 最佳实践示例 ===")

import logging

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def safe_calculator(operation, a, b):
    """安全的计算器函数"""
    
    # 输入验证
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("参数必须是数字")
    
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y
    }
    
    if operation not in operations:
        raise ValueError(f"不支持的操作: {operation}")
    
    try:
        result = operations[operation](a, b)
        logging.info(f"计算成功: {a} {operation} {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error(f"除零错误: {a} / {b}")
        raise
    except Exception as e:
        logging.error(f"计算出错: {e}")
        raise

# 测试安全计算器
test_cases = [
    ('add', 5, 3),
    ('divide', 10, 2),
    ('divide', 10, 0),    # 异常情况
    ('power', 2, 3),      # 不支持的操作
]

for operation, a, b in test_cases:
    try:
        result = safe_calculator(operation, a, b)
        print(f"✓ {operation}({a}, {b}) = {result}")
    except (TypeError, ValueError, ZeroDivisionError) as e:
        print(f"✗ {operation}({a}, {b}) 失败: {e}")

# 清理测试文件
import os
if os.path.exists("test_file.txt"):
    os.remove("test_file.txt")
    print("\n已清理测试文件")