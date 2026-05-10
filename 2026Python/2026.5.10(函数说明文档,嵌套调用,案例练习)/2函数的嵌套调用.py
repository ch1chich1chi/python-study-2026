#  嵌套调用指的是在一个函数中,又调用了另外一个函数
# 函数调用遵循栈结构,最后被调用的函数最先返回LIFO(Last In First Out,后进先出,先进后出)
def function_a():                   # function_a() 开始
    print("a ... before")           #   打印 "a ... before"
    function_b()                    #   调用 function_b()
    print("a ... after")            #       打印 "b ... before"
                                    #       调用 function_c()
def function_b():                   #       打印"c ... "
    print("b ... before")           #   打印 "b ... after"
    function_c()                    #   function_b() 返回
    print("b ... after")            # 打印 "a ... after"
                                    # function_a() 返回
def function_c():
    print("c ...")

function_a()

print("函数调用完毕 ~")