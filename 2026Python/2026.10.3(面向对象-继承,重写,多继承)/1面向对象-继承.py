# 继承
# 继承描述的是两个类之间的关系,子类继承父类,就可以获取到父类的属性和方法(非私有)

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

    def __control_fuel(self): # 私有方法
        print(f"{self.brand} {self.model} 正在控制油门...")

    def get_owner(self):
        return self.__owner[0:1] + "**"

class FuelCar(Car): # 子类
    pass

class ElectricCar(Car): # 子类
    pass

if __name__ == "__main__":
    c1 = FuelCar("BMW","X5","黑色","张三")
    c1.start()
    c1.run()
    c1.stop()
    print(c1.brand)
    print(c1.get_owner())
    print(c1.model)
    print(c1.color)