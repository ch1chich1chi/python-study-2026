# 案例2:合并两个列表中的元素,并对合并的结果进行去重处理(去除列表中的重复元素)
num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]
"""
# 1.合并列表
for num in num_list2:
    num_list1.append(num)

print("合并之后的列表:",num_list1)

# 2.去重重复记录
new_list = [] # 去除重复记录后的列表
for num in num_list1:
    # 判断new_list中是否存在num元素,如果不存在,再添加
    if num not in new_list: # 判断元素是否存在于列表中,如果存在,则返回True;不存在,返回False
        new_list.append(num)

print("去除重复记录后的列表:",new_list)
"""
# 案例2简化(1):
# 1.合并列表
# 解包:将列表这一类容器解开成一个一个独立的元素
# 组包:将多个值合并到一个容器
num_list = [*num_list1,*num_list2]

print("合并之后的列表:",num_list)

# 案例2简化(2):
num_list = num_list1 + num_list2

print("合并之后的列表:",num_list)