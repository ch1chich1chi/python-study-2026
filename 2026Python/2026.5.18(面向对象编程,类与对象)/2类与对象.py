# 类的定义
# 定义类的语法如下:

# 定义类 -- 动态添加属性
# class 类名:
#   pass

# 创建对象
# 对象名 = 类名()
# 对象名.属性名1 = 属性值1
# 对象名.属性名2 = 属性值2

# 说明:类名的命名规范,遵循大驼峰命名法,每个单词的首字母大写,单词之间没有分隔符,比如:UserInfo,UserAccount
# 说明:__dict__ 是Python中用户自定义类实例的一个特殊属性,用于以字典形式存储对象的属性

# 定义类 ----> 不推荐 动态的为对象添加属性
class Car:
    pass

# 创建对象
c1 = Car()
# 动态的为对象添加属性
c1.color = "red"
c1.brand = "BMW"
c1.name = "X5"
c1.price = 500000

print(c1)
print(c1.brand)
print(c1.__dict__) # 会将对象中的所有属性以字典的形式输出出来

#  定义类 -- 定义类时指定实例属性
# class 类名:
#   def __init__(self,参数列表):
#       self.属性名 = 参数值
#       self.属性名 = 参数值

# 创建对象
# 对象名 = 类名(参数列表)

# __init__:初始化方法,对象创建后自动调用,主要用于设置对象的初始状态(设置对象属性)
# self:方法的第一个参数,表示当前创建的实例对象
# 说明:定义在类的外面的称之为函数,定义在类中的函数称之为方法

# 定义类
class Car:
    # __init__:初始化方法,会在对象创建时自动调用,可以在该方法中为对象设置对应的属性;
    # self:是第一个参数,表示当前所创建出来的实例对象
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕,对象属性已经添加完毕")

# 创建对象
c1 = Car("红色","BMW","X7",800000)
print(c1.__dict__)