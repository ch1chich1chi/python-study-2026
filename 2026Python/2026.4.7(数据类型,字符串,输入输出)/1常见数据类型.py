# 常见的数据类型:int float str bool NoneType
# 1.通过 tyep() 语句来得到数据的类型,具体语法为: tyep(要查看类型的数据)
# type(..)
print(type("Hello")) # str
print(type(10)) # int
print(type(3.14)) # float
print(type(True)) # bool
print(type(False)) # bool
print(type(None)) # NoneType

# type(..) 变量本身无类型,tyep(变量)输出的类型是变量中存储的数据的类型
num = 5.0
print(num)
print(type(num)) # float


# 2.通过isinstance()检查数据类型是否属于指定的值,返回的是一个bool值,具体语法为: isinstance(数据,类型)
# type(..)
num = 5
print(isinstance(num,int)) # True
print(isinstance(num,float)) # False