# Python中的字典(dict),里面存储的是键值对(key:value)类型的数据,可以根据键(key)找到对应的值(value)
# 特点:键值对(key:value)存储 键(key)不能重复 可修改

# 定义字典
# 字典名称 = {key:value,key:value,key:value...}

# 定义空字典:
# 字典名称 = {}
# 字典名称 = dict()

# 根据key获取value
# 值 = 字典名称[key]

# 注意:字典(dict)中的value可以是任何类型的数据,而key不能为可变类型(如:不能为列表list 集合set 字典dict)

# 定义字典 -- key不能重复(如果重复,后面的值会覆盖前面的值)
dict1 = {"王林":670,"李慕婉":608,"许立国":580,"韩立":688}

print(dict1)
print(type(dict1))

# key必须得是不可变类型 str int float tuple,不能是 list set dict
dict2 = {0:32,(1,2):567}

# 访问
print(dict1["李慕婉"]) # 获取
dict1["李慕婉"] = 688 # 修改
print(dict1["李慕婉"])
