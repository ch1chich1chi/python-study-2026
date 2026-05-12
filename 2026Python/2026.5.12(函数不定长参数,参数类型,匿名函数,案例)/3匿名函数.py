# 定义命名函数
# def 函数名(参数列表):
#   函数体...
# def out_line():
#   print('-----')
# def add(x,y):
#   return x+y
# out_line()
# print(add(10,20))

# 匿名函数指的是没有名称的函数,需要通过lambda表达式来声明函数,可以简化简单函数的编写(单行表达式)
# 定义匿名函数
# lambda 参数列表 : 函数体
# out_line = lambda : print('-----------')
# add = lambda : x,y : x + y
# out_line()
# print(add(100,200))
# 注意:函数逻辑比较简单(单行表达式)且只在一个地方使用,可以考虑使用匿名函数,简化书写(通常作为高阶函数的参数使用)
# 匿名函数中可以返回结果,也可以不返回结果.返回结果时,不要写return,表达式的运行结果就是要返回的结果

# 匿名函数
# 需求1:打印一个分割线
# def out_line():
    # print('-----')

out_line = lambda : print('-----')
out_line

# 需求2:计算两个数之和
# def add(x,y):
    # return x + y

add = lambda x,y : x + y
print(add(100,200))

# 需求3:完成如下列表的排序操作,按照每一个元素的字符个数,从小到大排序
data_list = ["C++","C","Python","Jack","PHP","Java","Go","JavaScript","Rust"]
data_list.sort(key = lambda item : len(item),reverse = False ) # key控制列表中的函数如何排序 reverse默认False 不反转 

# 建议使用匿名函数的情况:函数逻辑简单,只在一个地方调用(常作为高阶函数的参数)
# 建议使用命名函数的情况:函数逻辑复杂,需要多步操作,需要多个地方重复使用或需要加文档说明
# 代码的可读性和可维护性比简洁性更重要