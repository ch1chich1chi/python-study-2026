# 继承-重写
# 重写是指子类继承父类后,如果父类折中的方法不满足需求,可以在子类中重新定义父类已有的方法(方法名相同),从而用子类的实现替换父类的实现
# 注意:如果子类在重写父类的方法时,需要调用父类的方法,可以通过父类名.方法名(self) / super().方法名来调用

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

class FuelCar(Car): # 子类
    def charge(self):
        print(f"{self.brand} {self.model} 正在加油...")

class ElectricCar(Car): # 子类
    def charge(self):
        # 方式一:super().方法名()
        super().charge()
        # 方式二:父类名.方法名(self)
        # Car.charge(self)
        print(f"{self.brand} {self.model} 正在充电...")

if __name__ == "__main__":
    c1 = FuelCar("BMW","X5","黑色","张三")
    c1.charge()
    c2 = ElectricCar("特斯拉","Model X","白色","李四")
    c2.charge()