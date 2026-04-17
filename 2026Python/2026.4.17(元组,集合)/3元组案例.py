# 案例:基于已学习的数据容器完成如下需求
# 根据提供的学生成绩单,完成如下需求
# 1.计算每个学生的总分、各科平均分,然后一并输出出来
# 2.统计各科成绩的最低分、最高分、平均分,并输出
# 3.查找成绩优秀(平均分大于90)的学生,并输出
# 学号    姓名    语文    数学    英语
# S001   王林     85      92      78
# S002   李慕婉   92      88      95
# S003   十三     78      85      82
# S004   曾牛     88      79      91
# S005   周轶     95      96      89
# S006   王卓     76      82      77
# S007   红蝶     89      91      94
# S008   徐立国   75      69      82
# S009   许木     86      89      98
# S010   遁天     66      59      72

students = (
    ("S001","王林",85,92,78),
    ("S002","李慕婉",92,88,95),
    ("S003","十三",78,85,82),
    ("S004","曾牛",88,79,91),
    ("S005","周轶",95,96,89),
    ("S006","王卓",76,82,77),
    ("S007","红蝶",89,91,94),
    ("S008","徐立国",75,69,82),
    ("S009","许木",86,89,98),
    ("S010","遁天",66,59,72),
)


# 1.计算每个学生的总分、各科平均分,然后一并输出出来 ---> {avg:.1f} ---> 保留一位小数
print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")
# 方式一:
"""
for s in students: # ("S001","王林",85,92,78)
    total = s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[0]} \t{s[1]} \t{s[2]} \t{s[3]} \t{s[4]} \t{total} \t{avg:.1f}")
"""

# 方式二:元组解包
for id,name,chinese,math,english in students: # ("S001","王林",85,92,78)
    total = chinese + math + english
    avg = total / 3
    print(f"{id} \t{name} \t{chinese} \t{math} \t{english} \t{total} \t{avg:.1f}")




print()

# 2.统计各科成绩的最低分、最高分、平均分,并输出
# 2.1 获取到各科的成绩列表
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]

# 2.2统计各科成绩的最低分、最高分、平均分,并输出
print(f"语文最低分: {min(chinese_scores)},最高分: {max(chinese_scores)},平均分: {sum(chinese_scores) / len(chinese_scores)}")
print(f"数学最低分: {min(math_scores)},最高分: {max(math_scores)},平均分: {sum(math_scores) / len(math_scores)}")
print(f"英语最低分: {min(english_scores)},最高分: {max(english_scores)},平均分: {sum(english_scores) / len(english_scores)}")

print()

# 3.查找成绩优秀(平均分大于90)的学生,并输出
print("优秀学生(平均分大于90)名单如下:")
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg > 90: # 优秀学生
        print(f"学号: {s[0]},姓名: {s[1]},平均分: {avg:.1f}")