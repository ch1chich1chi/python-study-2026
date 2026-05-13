# 模块导入方式
# 在使用模块中提供的功能之前,必须得先导入,再使用
# 模块导入的具体语法如下:
#   导入形式                             代码样例                            调用方式          调用方式
# import 模块名                      import random,os                    模块名.功能名  random.randint(10.100)
# import 模块名 as 别名              import random as rd                 别名.功能名  rd.randint(10,100)
# from 模块名 import 功能名          import random import randint,choice 功能名       randint(10,100)
# from 模块名 import 功能名 as 别名  from random import randint as rint  别名        rint(10,100)
# from 模块名 import *              from import random *                功能名      randint(10,100)

# 导入模块
import random as rd

for i in range(100):
    print(rd.randint(1,100)) # 包含1和100

# 导入模块中的功能
# from random import randint as rint
from random import * # *叫通配符

for i in range(100):
    print(randint(1,100))

# 导入语句,放入整个python文件的最上方