# 异常
# 异常(也称为Bug)就是程序运行中出现的错误,它会中断程序的正常执行流程
# 作用:
# 保证数据 逻辑的正确性,避免程序执行混乱
# 在开发阶段,尽量发现更多的问题,尽早解决问题,保障程序正常执行

# 异常处理
# 程序运行过程中出现异常,有两种方案:
# 1.不做处理:整个程序因为一个Bug,中断执行
# 2.捕获异常:按照我们自己的处理方式,处理完异常,程序继续执行

# try:
#   可能出现异常的业务代码1
#   可能出现异常的业务代码2
#   ...
# expect[异常类型 as 变量名]:
#   出现异常时的预案
# [finally:
#   不管是否出现异常,都会执行的代码]

"""
try:
    print("= = = = = = = =")
    print(my_name)
    print("- - - - - - - -")
except NameError as e: # 捕获的是 NameError 类型的异常
    print("程序运行报错,错误信息:",e)
finally:
    print("释放资源 ~")
"""
    
try:
    print("= = = = = = = =")
    # print(my_name)
    print(1 / 0)
    print("- - - - - - - -")
except NameError as e: # 捕获的是 NameError 类型的异常
    print("名字不存在,请检查变量名或函数名字,异常信息:",e)
except ZeroDivisionError as e:
    print("0不能做被除数,异常信息:",e)
except Exception as e: # 捕获所有的异常
    print("程序运行出错了,请联系管理员,错误信息:",e)
# 这个Exception可以省略
# except: # 捕获所有的异常
#   print("程序运行出错了,请联系管理员,错误信息:")
finally: # 无论程序是否正常运行,finally代码块中的代码都会运行
    print("资源释放 ~")