# 多态
# 多态是指同一个方法,具有不同的形态 行为 表现

class Car: # 父类,所有类都有一个父类就是object
    def __init__(self,brand,model,color,owner):
        self.brand = brand     # 品牌(公有属性)
        self.model = model     # 型号
        self.color = color     # 颜色
        self.__owner = owner   # 拥有者(私有属性)

    def start(self): # 启动
        print(f"{self.brand} {self.model} 正在启动...")

    def run(self): # 行驶
        print(f"{self.__owner} {self.brand} {self.model} 正在行驶...")
        self.__control_fuel() # 调用私有方法

    def stop(self): # 停止
        print(f"{self.brand} {self.model} 停止行驶...")

    def get_owner(self):
        return self.__owner[0:1] + "**"

    def charge(self):
        print(f"{self.brand} {self.model} 正在补充燃料...")

# 燃油车
class FuelCar(Car): # 子类
    def charge(self):
        print(f"{self.brand} {self.model} 正在加油...")

# 电车
class ElectricCar(Car): # 子类
    def charge(self):
        print(f"{self.brand} {self.model} 正在充电...")

# 补充燃料函数
def handle_charge(car:Car): # 函数参数类型声明 - 参数类型为父类,支持传入子类
    car.charge()

# 测试代码
if __name__ == "__main__":
    handle_charge(FuelCar("BMW","X5","黑色","张三"))
    handle_charge(ElectricCar("特斯拉","Model S","红色","李四"))
# 同一调用语句,传入对象不同,触发不同行为