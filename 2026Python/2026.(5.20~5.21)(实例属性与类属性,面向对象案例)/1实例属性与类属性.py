# 属性分为:
# 实例属性:实例属性 属于每个具体对象的属性,每个对象都是独立的(各个对象特有的数据)
# 类属性:类属性是属于类本身的属性,所有实例共享的(所有对象共享的数据或配置)
# 说明:通过实例查找属性时,会先查找实例属性,实例属性不存在时,在查找类属性

class Car:
    # 类属性(所有实例对象共享的)
    wheel = 4 # 轮胎数量
    tax_rate = 0.1 # 购置税的税率

    def __init__(self,c_color,c_brand,c_name,c_price):
        # 实例属性
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        self.wheel = 2

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

# 测试
c1 = Car("白色","BYD","汉",180000)
print(c1.brand)
print(c1.wheel)
# 通过实例查找属性时,会先查找实例属性,实例属性不存在时,在查找类属性

# 通过类名访问类属性
print(Car.wheel)