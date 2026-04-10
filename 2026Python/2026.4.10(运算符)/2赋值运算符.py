# 赋值运算符
# 运算符     描述         实例
#   =    赋值运算符     把 = 右边的结果赋值给左边的变量,如: num = 1+2,结果为num的值为3
#  +=   加法赋值运算符   num += 2 等效于 num = num + 2
#  -=   减法赋值运算符   num -= 2 等效于 num = num - 2
#  *=   乘法赋值运算符   num *= 2 等效于 num = num * 2
#  /=   除法赋值运算符   num /= 2 等效于 num = num / 2
#  %=   取模赋值运算符   num %= 2 等效于 num = num % 2
#  //=  取整除赋值运算符 num //= 2 等效于 num = num // 2
#  **=  幂赋值运算符     num **= 2 等效于 num = num ** 2

num = 85

num += 10 # num = num + 10
print("num += 10 后,num =",num)

num -= 10 # num = num - 10
print("num -= 10 后,num =",num)

num *= 10 # num = num * 10
print("num *= 10 后,num =",num)

num /= 10 # num= num / 10
print("num /= 10 后,num =",num)

num //= 10 #num = num // 10
print("num //= 10 后,num =",num)

num %=3 # num = num % 3
print("num %= 3 后,num =",num)

num **= 3 # num = num ** 3
print("num ** = 3 后,num =",num)