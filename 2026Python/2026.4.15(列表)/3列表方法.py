# 列表的常用方法就是指列表这种数据类型内置的常见功能(添加元素 删除元素 排序等)
#   方法            作用                   样例
# append()  在列表的尾部追加元素          s.append(10086)
# insert()  在指定索引之前,插入该元素        s.insert(0,92)
# remove()  移除列表中第一个匹配到的值       s.remove(75)
# pop()  删除表中指定索引位置的元素(如果未指定索引,默认删除最后一个) )  s.pop(2)/s.pop()
# sort()  对列表进行排序(列表元素的数据类型一致,才可以进行排序)  s.sort()
# reverse()  反转列表元素     s.reverse()

s = [56,90,88,65,90,100,209,72,145]
print(s)

# append():再列表尾部追加元素
s.append(188)
print(s)

# insert():在指定索引之前,插入元素
s.insert(2,80)
print(s)

# remove():移除列表中第一个匹配到的元素
s.remove(90)
print(s)

# pop():删除列表中指定索引位置的元素并返回(如果未指定,默认删除最后一个)
e = s.pop(1)
print(e)

e = s.pop()
print(e)

# sort():排序
s.sort()
print(s)

# reverse():反转元素
s.reverse()
print(s)
