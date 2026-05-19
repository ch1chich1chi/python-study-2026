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

# 测试
c1 = Car("红色","BMW","X7",800000)

# 调用对象中的方法,不用传递self
c1.running()

total = c1.total_cost(0.9,0.1)
print("提车的总费用为:",total)