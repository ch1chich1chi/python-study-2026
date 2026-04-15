# 案例1:将用户输入的10个数字,存储到一个列表中,并将列表中的数字进行排序,输出其中的最小值 最大值和平均值

# 1.定义列表
num_list = []

# 2.将用户输入的10个数字存入列表
for i in range(10):
    num = int(input("请输入一个有效的数字:"))
    num_list.append(num)
print("数字列表:",num_list)

# 3.排序
num_list.sort()
print("排序后的数字:",num_list)

# 4.输出其中的最小值 最大值和平均值 ---> sum() 求和 ; len() 获取元素的个数(列表的长度) max() 获取最大值 min() 获取最小值
print("最小值:",num_list[1])
print("最大值:",num_list[-1])
print("平均值:",sum(num_list) / len(num_list))