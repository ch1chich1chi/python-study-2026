# 练习 1：计算器升级版（算术运算符）
# 要求:
# 1.让用户输入两个数字 a 和 b
# 2.计算并输出：和、差、积、商、整除、取余、幂运算的结果
a = float(input("请输入第一个数字:"))
b = float(input("请输入第二个数字:"))
print(f"和：{a} + {b} = {a + b}")
print(f"差: {a} - {b} = {a - b}")
print(f"积：{a} * {b} = {a * b}")
print(f"商：{a} / {b} = {a / b}")
print(f"整除：{a} // {b} = {a // b}")
print(f"取余：{a} % {b} = {a % b}")
print(f"幂运算：{a} ** {b} = {a ** b}")

# 练习 2：成绩等级判断（比较 + 逻辑运算符）
# 要求:
# 1.输入学生成绩（0-100 分）
# 2.判断：
#    90 分及以上：优秀
#    80-89 分：良好
#    60-79 分：及格
#    60 分以下：不及格
# 3.用比较运算符 + 逻辑运算符实现
grade = float(input("请输入学生成绩:"))
print("成绩是否优秀(90~100):", grade >= 90 and grade <= 100)
print("成绩是否良好(80~89):", grade >= 80 and grade < 90)
print("成绩是否及格(60~79):", grade >= 60 and grade < 80)
print("成绩是否不及格：", grade >= 0 and grade < 60)
print("输入是否有效：", grade >= 0 and grade <= 100)