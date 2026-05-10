# 函数的说明文档是写在函数开头,用三个引号包裹的字符串,用于解释函数的功能、参数和返回值等信息,方便调用者清楚函数的具体作用及xijie
# 定义一个函数,根据半径,计算圆的周长,面积
# def circle_area_len(r):
#     """
#     该函数用于根据圆的半径,计算圆的周长和面积
#     :param r: 圆的半径  param:描述函数的参数
#     :return: 圆的周长和面积  return:描述函数的返回值
#     """
#     return 2 * 3.14 * r, 3.14 * r ** 2
# al = circle_area_len(10)
# print(al)

# 查看函数说明文档:
# 使用help函数,比如help(circle_area_len)
# 鼠标悬浮在函数上,自动显示

def circle_area_len(r):
    """
    该函数用于根据圆的半径,计算圆的周长和面积
    :param r: 圆的半径
    :return: 圆的周长和面积
    """
    return 2 * 3.14 * r, 3.14 * r ** 2
al = circle_area_len(10)
print(al)

help(circle_area_len)