# 练习 1：简单打招呼程序
# 要求
# 1.让用户输入姓名
# 2.输出：你好，XXX！欢迎学习 Python！
name = input("请输入您的姓名:")
print(f"你好,{name}!\n欢迎学习Python!")

# 练习 2：年龄计算小程序
# 要求
# 1.输入现在年龄
# 2.计算 10 年后的年龄
# 3.输出：10 年后你 XX 岁
age = int(input("请输入您的年龄:"))
future_age = 10
print(f"您10年后的年龄为:{age + future_age}")

# 练习 3：输出多种数据类型
# 要求
# 定义一个整数 a = 18
# 定义一个浮点数 b = 99.9
# 定义一个字符串 c = "AI Agent"
# 分别打印它们的值和类型 type ()
a = 18
b = 99.9
c = "AI Agent"
print(type(a))
print(type(b))
print(type(c))