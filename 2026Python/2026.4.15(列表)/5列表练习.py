# 1.创建一个列表，里面包含数字：10, 20, 30, 40, 50
# (1).打印第 1 个元素
# (2).打印最后 1 个元素
# (3).把第 3 个元素改成 99
# (4).打印整个列表
list = [10,20,30,40,50]
# (1).
print(list[0])
# (2).
print(list[-1])
# (3).
list[2] = 99
# (4).
print(list)

# 2.列表 names = ['Tom', 'Jerry', 'Alice', 'Bob']
# (1).在末尾添加一个名字 'David'
# (2).在第 2 个位置插入 'Lily'
# (3).删除名字 'Alice'
# (4).遍历列表，打印每个名字
names = ['Tom', 'Jerry', 'Alice', 'Bob']
# (1).
names.append("David")
# (2).
names.insert(1,"Lily")
# (3).
names.remove("Alice")
# (4).
for i in names:
    print(i)

# 3.给定列表 nums = [2, 5, 8, 1, 9, 3, 7]
# (1).计算列表所有数字的总和
# (2).找出列表里最大的数
# (3).找出列表里最小的数
nums = [2,5,8,1,9,3,7]
# (1).
print(sum(nums))
# (2).
print(max(nums))
# (3).
print(min(nums))

# 4.列表 scores = [85, 92, 76, 58, 99, 66, 45]遍历列表，只打印大于等于 60 分的成绩。
scores = [85,92,76,58,99,66,45]
new_scores = [i for i in scores if i >= 60]
print(new_scores)

# 5.创建一个空列表，循环输入 3 个数字，把它们加入列表，最后输出列表和总和。
list = []
for i in range(3):
    num = int(input('请输入数字：'))
    list.append(num)
print(list)
print("总和：", sum(list))

# 6.现有列表 nums = [12,35,99,18,76,23,50]遍历列表，只打印偶数
nums = [12,35,99,18,76,23,50]
n = [i for i in nums if i % 2 == 0]
print(n)

# 7.列表 words = ['hello', 'world', 'python', 'list', 'loop']
# (1).统计列表里一共有多少个元素
# (2).打印所有长度大于4的单词
words = ['hello', 'world', 'python', 'list', 'loop']
# (1).
print("元素个数:",len(words))
# (2).
w = [i for i in words if len(i) > 4]
print(w)

# 8.给定列表 a = [1, 2, 3, 4, 5]创建一个新列表，里面每个数是原列表的平方结果应为：[1, 4, 9, 16, 25]
a = [1,2,3,4,5]
b = [i ** 2 for i in a]
print(b)

# 9.列表 scores = [90, 55, 78, 62, 49, 88, 73]统计里面：
# (1).及格（≥60）的人数
# (2).不及格（＜60）的人数
scores = [90, 55, 78, 62, 49, 88, 73]
pass_num = 0
fail_num = 0

for s in scores:
    if s >= 60:
        pass_num += 1
    else:
        fail_num += 1

print('及格人数：', pass_num)
print('不及格人数：', fail_num)

# 10.从列表 [11, 22, 33, 44, 55, 66] 中，把所有大于 30的数字，放进一个新列表，最后打印新列表。
nums = [11,22,33,44,55,66]
new_nums = [i for i in nums if i > 30]
print(new_nums)