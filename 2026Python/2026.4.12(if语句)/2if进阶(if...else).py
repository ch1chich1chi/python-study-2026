# if...else 结构
# if 要判断的条件:
#     条件成立时,执行对应的操作1
# else:
#    条件不成立时,执行对应的操作2

# 结合前面学习的输入输出及if条件判断的知识，完成B站登录功能的实现(正确账号和密码为18888888888/666888)
# 正确的账号和密码
ok_account = "18888888888"
ok_password = "666888"

# 1.接收用户输入账号和密码
account = input("请输入您的账号:")
password = input("请输入您的密码:")
# input返回的永远是字符串

if account == ok_account and password == ok_password:
    print("登陆成功~\n进入B站首页")
else:
    print("登陆失败~\n账号或密码错误")


# 案例:完成如下需求
# 1.需求:根据用户输入的年份，判断这一年是闰年还是平年，
#  非整百年份，且能被4整除的年份是闰年
#  整百年份(如1900年、2000年)必须能被400整除才是闰年
year = int(input("请输入需要判断年份:"))
if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
    print(f"{year}年是闰年")
else:
    print(f"{year}年是平年")

# 需求1：根据用户输入的数字，判断该数字是奇数还是偶数
num = int(input("请输入一个数字:"))
if num % 2 == 0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")

# 需求2：根据用户输入的年龄，判断该用户是否已经成年（>=18，成年；否则，未成年）
age = int(input("请输入您的年龄:"))
if age >= 18:
    print("您已成年")
else:
    print("您未成年")

# 需求3：根据用户输入的数字，判断该数字是正数还是负数（不考虑0）
num = int(input("请输入一个数字: "))
if num > 0:
    print(f"{num} 是正数")
else:
    print(f"{num} 是负数")

# 需求4：根据用户输入的考试分数，判断该分数是否及格了（大于等于60就是及格了）
grade = float(input("请输入您的成绩:"))
if grade >= 60:
    print("及格")
else:
    print("不及格")