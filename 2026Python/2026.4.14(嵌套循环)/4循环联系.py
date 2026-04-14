# 需求1：将1-1000之间（含1000）所有的5的倍数的数字累加起来
total = 0
for i in range(1,1001):
    if i % 5 == 0:
        total += i
print(f"1-1000 5的倍数数字之和:{total}")

# 需求2：统计字符串 "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd" 字符串中有多少个a和k。
total = 0
for i in "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd":
    if i == "a" or i == "k":
        total += 1
print("字符串中a和k出现的次数: ", total)

# 3.用嵌套循环打印下面的图案：
# *****
# *****
# *****
# *****
for i in range(4):
    for j in range(5):
        print("*",end="")
    print()

# 4.打印直角三角形：
# *
# **
# ***
# ****
# *****
for i in range(5):
    for j in range(i + 1):
        print("*",end="")
    print()

# 5.打印九九乘法表:
for i in range(1,10):
    for j in range(1,i + 1):
        print(f"{i} x {j} = {i * j}",end="\t")
    print()    

# 6.用 while 循环嵌套，打印 1～10 的数字，每行 5 个，分两行:
i = 1
while i <= 10:
    count = 0
    while count < 5 and i <= 10:
        print(i, end=' ')
        i += 1
        count += 1
    print()

# 7.输出 1～50 之间的所有质数
for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")