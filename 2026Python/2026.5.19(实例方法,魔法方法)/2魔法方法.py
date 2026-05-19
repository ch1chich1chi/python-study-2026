# 魔法方法
# 魔法方法是指Python中提供的以双下划线开头和结尾的特殊方法,用于定义类的特殊性为,比如:__init__
# 魔法方法是不需要我们手动调用的,Python会在合适的时机自动调用

# 魔法方法    描述
# __init__  初始化方法
# __str__  字符串表示的方法
# __eq__  比较两个对象是否相等(equal)
# __lt__,__le__,__gt__,__ge__  支持比较两个对象的大小(小于(less than),小于等于(less than or equal),大于(greater than),大于等于(greater than or equal))

class Car:
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕,对象属性已添加完毕")

    # 定义实例方法
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶中")

    def total_cost(self,discount,rate = 0.1):
        """
        计算提车总费用 , 包含两个部分: 车的价格,税费 
        :param discount:折扣
        :param rate:税率
        :return:提车总费用
        """
        total_cost = self.price * discount + self.price * rate
        return total_cost
        print(total_cost)

    # 魔法方法
    def __str__(self):
        return f"{self.color} {self.brand} {self.name} {self.price}"
    
    def __eq__(self,other):
        return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price
    
    def __lt__(self,other):
        return self.price < other.price

# 测试
c1 = Car("白色","BYD","汉",180000)
print(c1)

c2 = Car("白色","BYD","汉",180000)
print(c2)

print(c1 == c2)

print(c1 < c2)