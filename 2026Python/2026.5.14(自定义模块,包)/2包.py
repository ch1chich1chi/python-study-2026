# 包:本质就是一个文件夹,该文件夹中可以包含若干个python模块(.py文件),文件下还包含了一个__init__.py
# 作用:模块文件较多时,用来管理多个模块(包的本质也是一个模块)

# 包的导入方式
# 导入形式                       代码样例                                 调用方式             调用方式
# import 包名.模块名              import utils.my_fun                     包名.模块名.功能名  utils.my_fun.log_separator1()
# from 包名 import 模块名         from utils import my_fun                模块名.功能名       my_fun.log_separator1()
# from 包名 import *             from utils import *                     模块名.功能名       my_fun.log_separator1()
# from 包名.模块名 import 功能名  from utils.my_fun import log_separator1 功能名             log_separator1()
# from 包名.模块名 import *      from utils.my_fun import *               功能名            log_separator1()

# 1.导入模块
"""
import utils.my_fun

utils.my_fun.log_separator1()
utils.my_fun.log_separator2()

from utils import my_fun

my_fun.log_separator1()
my_fun.log_separator2()
"""

# 注意:如果要通过 from utils import * 导入包下的所有模块,需要__init__.py文件中添加__all__=[]
"""
from utils import *

my_fun.log_separator1()
my_fun.log_separator4()

print(my_var.PI)
print(my_var.NAME)
"""
# 2.导入模块中的功能
# 相对路径:从当前文件所在目录开始查找
from utils.my_fun import log_separator1,log_separator3

# 绝对路径:从项目的根目录下开始查找

log_separator1()
log_separator3()