# 类型注解是Python中的一种语法特性,用于明确标识变量 函数参数和返回值的数据类型,从而使代码更清晰 更安全 更易维护

# 定义变量 - 未指定类型注解 - 类型推断
# 类型推断是指Python解释器自动推断出变量 表达式或函数返回值的数据类型的能力,而无需开发者显式声明
# 注意:在对变量进行直接赋值,或者涉及到变量的运算 容器的推导等场景时,解释器会自动推导出变量的类型
a = 695
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A","C","E",100]
phones = {"121313","131414"}
options = {"count":0,"total":0}
goods = ("手机",5999,1)

names.append("x")
names.append(10010)
names.append(10010.0)

print(names)

# 定义变量 - 指定类型注解
a2: int = 695
score2: float = 98.5
hobby2: str = "Python"
flag2: bool = True
pic2: None = None

names2: list[str | int] = ["A","C","E"]
phones2: set[str] = {"121313","131414"}
options2: dict[str,int] = {"count":0,"total":0}
goods2: tuple[str,int,int] = ("手机",5999,1)

names2.append("x")

# 类型注解只是起到语法提示作用,并不会影响程序运行的结果
# Python是动态类型语言,添加的类型注解只是提示,并不是强制约束