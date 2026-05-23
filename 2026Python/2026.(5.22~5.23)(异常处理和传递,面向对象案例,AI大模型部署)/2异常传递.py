# 异常的传递
# 异常传递就是异常在函数调用中层层上报的过程,知道有人处理它,或者程序崩溃
def fun1():                         # if __name__ == "__main__"
    print("fun1 ... running ...")
    fun2()                          #   fun1()

def fun2():                         #   fun2()
    print("fun2 ... running ...")
    fun3()                          #   fun3()

def fun3():                         #   print(my_color)
    print("fun3 ... running ...")
    print(my_color)

if __name__ == "__main__":
    try:
        fun1()
    except Exception as e:
        print("程序运行出错了,请联系管理员,错误信息:",e)