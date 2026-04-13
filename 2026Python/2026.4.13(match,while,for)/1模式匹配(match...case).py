# 模式匹配
# 结构模式匹配就是用一个清晰的 模板 去精准的匹配数据结构和内容,匹配成功则执行对应的操作
# 例:
"""day = input("请输入星期几(1~7):")
if day == "1":
    print("周一:工作会议日")
elif day == "2":
    print("周二:学习培训日")
elif day == "3":
    print("周三;项目开发日")
elif day == "4":
    print("周四:代码审查日")
elif day == "5":
    print("周五:总结规划日")
elif day == "6" or day == "7":
    print("周末:休息放松")
else:
    print("输入错误")
"""

day = input("请输入星期几(1~7):") # 执行流程:
match day:                       # 1.首先计算match指定的表达式的值
    case "1":                    # 2.从上到下依次和case后面的值进行匹配,匹配正确,就执行对应语句
        print("周一:工作会议日")  # 3.如果前面所有的cse都没对上,就会执行默认的case _
    case "2":
        print("周二:学习培训日")
    case "3":
        print("周三;项目开发日")
    case "4":
        print("周四:代码审查日")
    case "5":
        print("周五:总结规划日")
    case "6"|"7": # 其中的 | 表示或的关系,匹配多个模式中的任意一个
        print("周末:休息放松")
    case _ : # _ 匹配其他所有情况
        print("输入错误")

# 案例:简易计算器
# 实现一个计算器，可以实现 + - * / 算，用户输入需要运算的两个数以及运算符之后，就可以进行计算
num1 = float(input("请输入第一个数:"))
num2 = float(input("请输入第二个数:"))
oper = input("请输入运算符(+ - * /):")

match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0: # if条件成立,才匹配这个case
        print(f"{num1} / {num2} = {num1 / num2}")
    case _ :
        print("操作不支持")
# match:基于某个变量的多个固定值进行分支判断时,可以使用match模式匹配
# if:条件判断涉及复杂的逻辑判定 范围比较及组合条件时