# if...elif...else结构
# if 要判断的条件1:
#     条件成立时,执行对应的操作1
# elif 要判断的条件2:
#     条件成立时,执行对应的操作2
# else:
#     条件不成立时,执行对应的操作3
# 注意: 满足第1个条件时,就不会判断第2个部分和第3个部分;条件1不成立,才会判断第2个部分;1和2都不成立,才会进入else

# 案例：根据用户输入的数字，判断该数字是正数还是负数
num = float(input("请输入数字:"))
if num > 0:
    print(f"{num}是正数")
elif num < 0:
    print(f"{num}是负数")
else:
    print(f"{num}是0")

# 案例:根据输入用户名、密码进行登录系统，
#   用户名、密码为 admin/666888或root/547527 或 zhangsan/123456，则输出登录成功
#   否则就提示用户名或密码错误
usersname = input("请输入用户名:")
password = input("请输入密码:")
if usersname == "admin" and password == 666888:
    print("登陆成功")
elif usersname == "root" and password == 547527:
    print("登陆成功")
elif usersname == "zhangsan" and password == 123456:
    print("登陆成功")
else:
    print("登陆失败.用户名或密码错误")