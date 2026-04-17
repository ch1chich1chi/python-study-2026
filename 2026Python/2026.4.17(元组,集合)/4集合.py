# 集合
# 集合(set)是一种无序的 不可重复 可修改的数据容器

# 定义集合
s1 = {7,23,5,3,2,0,5,4,12,43,64,22,0}

print(s1)
print(type(s1))

# 定义空集合
s2 = set()
print(s2)
print(type(s2))
# 注意:空集合的定义不可以使用{},{}表示的是字典;由于集合是无序的,因此是不支持下标索引访问的

#  操作                         含义                                          样例
# add(..)            添加元素到集合中                                        s1.add('t')
# remove(..)        移除集合中的指定元素(指定元素不存在将报错)                 s1.remove('t')
# pop()             随机删除集合中的元素并返回                                e = s.pop()
# clear()             清空集合                                              s1.clear()
# difference()  求取两个集合的差集(包含在第一个集合但不包含在第二个集合的元素)   s1.difference(s2)
# union()            求取两个集合的并集                                      s1.union(s2)
# intersection()     求取两个集合的交集                                      s1.intersection(s2)

# add():添加元素到集合
s1 = {100,200,300,400,500,600,700,800}
print(s1)

s1.add(1200)
print(s1)

# remove():移除集合中的指定元素(指定元素不存在将报错)
s1.remove(200)
print(s1)

# pop();随机删除集合中的元素并返回
e = s1.pop()
print(e)

# clear():清空集合
s1.clear()
print(s1)

s2 = {"A","B","C","D","E","X","Y"}
s3 = {"C","E","Y","Z"}
# difference():求取两个集合的差集(包含在第一个集合但不包含在第二个集合的元素)
print(s2.difference(s3))
print(s3.difference(s2))

# union():求两个集合的并集
print(s2.union(s3))
print(s3.union(s2))

# intersection():求两个集合的交集
print(s2.intersection(s3))
print(s3.intersection(s2))