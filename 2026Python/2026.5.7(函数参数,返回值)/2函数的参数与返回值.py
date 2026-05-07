# 在定义函数时,根据业务需要,可以指定参数与返回值,具体格式如下:
# 定义函数
# def函数名(参数列表):
#    函数体
#    return返回值
# 调用函数
# 函数名(参数)

# 计算圆的面积
def circle_area(r):
    area = 3.14 * r * r
    return area

# 调用函数
c_area = circle_area(10)
print(c_area)

# 计算长方形的面积
def rectangle_area(l,w):
    area = l*w
    return area

# 调用函数
r_area = rectangle_area(20,10)
print(r_area)

# 注意:函数定义时如果有多个参数,多个参数之间使用逗号(,)分隔
# return语句只有返回功能,而没有输出打印的功能,如果要输出,需要结合print()函数来实现
# r l,w叫做形参(形式参数):函数定义时括号里的参数,只能在函数内使用(局部变量)
# 10 20,10叫做实参(实际参数):函数在实际调用时传入的参数,和形参一一对应

# 计算圆的面积,周长 -- 半径 ---> 如果返回值有多个,多个返回值之间逗号隔开 ---> 多个返回值会封装到元组之中
def circle_area_len(r):
    return 3.14 * r * r,round(2 * 3.14 * r, 1) # 四舍五入保留一位小数

al = circle_area_len(10)
print(al)
print(type(al))

area,len = circle_area_len(10) # 解包
print(area)
print(len)