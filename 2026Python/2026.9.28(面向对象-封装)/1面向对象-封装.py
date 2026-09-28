# 封装
# 封装就是把数据(属性)和操作数据的函数(方法)捆绑在一起,形成一个独立的单元(类),并隐藏内部的实现细节->私有属性,只对外暴露必要的功能(方法)->公共属性
# 在前面加两个下划线,表示私有
# 私有:私有的属性和方法只能在类的内部使用
# 注意事项:Python中并没有真正的私有机制,约定在私有属性名和方法名前加__(两个下划线)

class Car:
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

if __name__ == "__main__":
    car = Car("宝马", "X5", "黑色","张三")
    print(car.brand)
    print(car.model)
    print(car.color)
    # print(car.__owner)
    print(car._Car__owner) # 通过类名访问私有属性

    car.start()
    car.run()
    car.stop()
    # car.__control_fuel()
    car.get_owner()
    car._Car__control_fuel() # 通过类名访问私有方法