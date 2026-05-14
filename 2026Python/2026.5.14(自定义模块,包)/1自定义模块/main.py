# __all__指定from ... import *导入的是哪些功能
__all__ = ["log_separator1","log_separator3"]
"""
# 导入自定义模块
import my_fun

# 使用模块中的功能
print(my_fun.PI)

# 导入自定义模块
from my_fun import log_separator1,log_separator3,PI,NAME

# 使用模块中的功能
print(PI)

log_separator1
"""

# __all__是一个模块级别的特殊变量,用于指定from 模块名 import * 时会导入哪些功能(*通配了哪些功能)
# 注意:__all__控制的是 from ... import *时要导入的功能,并不会影响直接导入具体的功能(如from ... import功能)

from my_fun import *
log_separator1()