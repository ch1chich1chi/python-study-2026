# 1.成绩等级
# 90 以上：优秀
# 80–89：良好
# 60–79：及格
# 60 以下：不及格
score = int(input("请输入成绩:"))
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")