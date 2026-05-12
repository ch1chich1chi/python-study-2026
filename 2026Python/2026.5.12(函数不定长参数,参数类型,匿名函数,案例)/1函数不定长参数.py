# 介绍:不定长参数也叫可变参数,用于函数定义及调用时参数个数不确定(0个或多个)的场景
# 类型:位置传递,关键字传递
# 需求:定义函数,根据传入的数据,计算这批数据中的最小值 最大值 平均值

# 不定长参数 - 位置传递(*args)

# 定义函数
def calc_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    return min_data,max_data,round(avg_data,1)

# 调用函数
data = calc_data(10,20,30,40,50,60,70,80,90)
print(data)
# 注意:传递的所有匹配的位置都会被args变量收集,这些参数会合并封装为一个元组,args是元组类型(注意并不会封装关键字参数)
# args只是约定俗成的变量名,并不是关键字,这里可以使用任何合法的变量名(如*data)

# 不定长参数 - 关键字传递(**kwargs)

# 定义函数
def calc_data(*args,**kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get('round') is not None:
        avg_data = round(avg_data,kwargs.get('round'))
    
    if kwargs.get(print):
        print(f"计算出来的最小值:{min_data},最大值:{max_data},平均值{avg_data}")
    
    return min_data,max_data,avg_data

data = calc_data(100,200,300,400,round = 2,print = True)
print(data)
# 注意:参数是以"键=值"形式传递的关键字参数,这些"键=值"参数都会被kwargs接受,并合并封装为一个字典类型
# kwargs只是约定俗成的变量名,并不是关键字,这里可以使用任何合法的变量名(如**options)

# *args适用于处理数量不确定的数据
# **kwargs适用于处理数量不确定的选项(函数的配置参数,用来制定函数的行为)
# 核心数据:你要什么
# 选项:你要什么样的