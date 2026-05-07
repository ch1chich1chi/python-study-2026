# 1.创建一个字典 user,内容是:姓名:小明,年龄:18,性别:男
# 把年龄改成 20
# 新增一个键值对:邮箱:xiaoming@qq.com
# 删除 性别 这个键
# 打印最终的字典
# 1. 创建字典
user = {"姓名": "小明", "年龄": 18, "性别": "男"}
# 2. 改年龄
user["年龄"] = 20
# 3. 新增邮箱
user["邮箱"] = "xiaoming@qq.com"
# 4. 删除性别
del user["性别"]
# 5. 打印
print(user)

# 给定字典 goods = {"name": "手机","price": 2999}
# 用 get 方法取出 name 的值,打印
# 用 get 方法取出 weight 的值,如果不存在就返回默认值 0,打印
goods = {"name": "手机", "price": 2999}
# 取name
print(goods.get("name"))
# 取weight，不存在就返回0,不会报错
print(goods.get("weight", 0))

# 3.给定字典 score = {"语文": 85,"数学": 92,"英语": 78}
# 遍历所有的键,打印出来
# 遍历所有的值,打印出来
# 遍历所有的键值对,打印成:语文: 85分 这样的格式
score = {"语文": 85, "数学": 92, "英语": 78}
# 1. 遍历所有键
print("所有科目:")
for k in score.keys():
    print(k)
# 2. 遍历所有值
print("\n所有成绩:")
for v in score.values():
    print(v)
# 3. 遍历键值对
print("\n成绩详情:")
for k, v in score.items():
    print(f"{k}:{v}分")

# 4.我们有一个学生列表,里面每个学生是一个字典: (字典嵌套)
"""
students = [
    {"name": "小明", "age": 18, "score": 85},
    {"name": "小红", "age": 19, "score": 92},
    {"name": "小刚", "age": 18, "score": 58}
]
完成以下操作:
遍历这个列表,打印所有学生的姓名和成绩
找出成绩大于 60 分的学生,把他们的姓名存到一个新列表里
计算这三个学生的平均成绩
"""
students = [
    {"name": "小明", "age": 18, "score": 85},
    {"name": "小红", "age": 19, "score": 92},
    {"name": "小刚", "age": 18, "score": 58}
]
# 1. 遍历打印所有学生信息
print("所有学生：")
for s in students:
    print(f"姓名：{s['name']}，成绩：{s['score']}")
# 2. 找出及格的学生姓名
pass_name = [s["score"] for s in students if s["score"] > 60]
print("\n及格的学生:",pass_name)
# 3. 计算平均成绩
total_score = 0
avg = sum(s["score"] for s in students) / len(students)
print("平均成绩：",avg)

# 5.给定字典 scores = {"小明": 85, "小红": 92, "小刚": 78, "小丽": 90}
# 把这些学生按成绩从高到低排序,输出排序后的结果
scores = {"小明": 85, "小红": 92, "小刚": 78, "小丽": 90}
# 按成绩从高到低排序：items()把字典转成(键,值)的列表，然后按值排序
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print("按成绩排序：", sorted_scores)

"""
6.实现一个简易学生成绩管理小工具，功能如下：
程序启动后，显示菜单：
plaintext
===== 成绩管理工具 =====
1. 添加学生成绩
2. 查询学生成绩
3. 显示所有学生
4. 统计及格人数
5. 退出
选择 1:输入学生姓名和成绩,把信息存到字典里
选择 2:输出他的成绩,如果不存在就提示 "学生不存在"
选择 3:打印所有学生的姓名和成绩
选择 4:统计成绩≥60的学生人数,输出结果
选择 5:退出程序
"""
menu = """
===== 成绩管理工具 =====
1. 添加学生成绩 
2. 查询学生成绩
3. 显示所有学生
4. 统计及格人数
5. 退出
"""
students_scores = {}

while True:
    print(menu)

    choice = input("请选择功能(1-5):")

    match choice:
        case "1": # 添加学生信息
            student_name = input("请输入学生姓名:")
            student_score = input("请输入学生成绩:")

            if student_name in students_scores:
                print("该学生成绩已存在,请重新录入 ~")
            else:
                students_scores[student_name] = {"score":student_score}
        case "2":
            if student_name not in students_scores:
                print("该学生不存在,请重新输入")
            else:
                student_info = students_scores[student_name]
                print(f"{student_name}的成绩是：{student_info["score"]}")
        case "3":
            for student_name in students_scores.keys():
                student_info = students_scores[student_name]
                print(f"学生姓名:{student_name},学生成绩:{student_info["score"]}")
        case "4":
            pass_count = sum(1 for s in students_scores.values() if s["score"] >= 60)
            print(f"及格人数：{pass_count}")
        case "5":
            print("退出程序")
            break
        case _:
            print("无效的选择，请重新输入")