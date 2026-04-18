# 1.给定元组 user = ("小明", 20, 92.5)
# 分别取出姓名、年龄、成绩，打印成：姓名：小明，年龄：20，成绩：92.5
# 遍历这个元组，逐个输出元素
user = ("小明", 20, 92.5)
name,age,score = user
print(f"姓名: {name},年龄: {age},成绩: {score}")
for i in user:
    print(i)

# 2.把元组 (15, 25) 解包给变量 x 和 y，然后计算 x + y 并输出结果
x,y = (15,25)
print(f"x + y = {x + y}")

# 3.给定列表 nums = [5, 2, 2, 3, 3, 3, 1, 5, 5]，用集合给它去重，最后转成列表输出
nums = [5, 2, 2, 3, 3, 3, 1, 5, 5]
new_nums = list(set(nums))
print(new_nums)

# 4.有两个列表
# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [4, 5, 6, 7, 8, 9]
# 用集合找出两个列表的共同元素，输出结果
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
new_list = set(list1).intersection(set(list2))
print("共同元素:",new_list)

# 5.创建集合 s = {10, 20, 30, 40}
# 添加元素 50
# 删除元素 20
# 判断 30 是否在集合里，输出判断结果
s = {10,20,30,40}
s.add(50)
s.remove(20)
if 30 in s:
    print("30是在集合里")
# print("30是否在集合里",30 in s)
print("当前集合:", s)

# 6.输入一个字符串，统计里面有多少个不重复的字符
# 示例：
# 输入：aabbccddeeff
# 输出：6（因为只有 a/b/c/d/e/f 6 种）
s = input("请输入字符串:")
print("不重复字符的数量:",len(set(s)))