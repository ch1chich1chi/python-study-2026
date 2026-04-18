# 类型           操作                     含义                           样例
# 添加  字典名称[key] = value  往指定字典中添加key-value键值配对   dict["涛哥"] = 688
# 删除  字典名称.pop(key)  删除字典中指定的key,并返回该key对应的value  score = dict1.pop("涛哥")
# 删除  del 字典名称[key]     删除字典中指定的键值对                del dict1["涛哥"]
# 修改  字典名称[key] = value  修改字典中指定的key对应的值          dict1["小智"] = 658
# 查询  字典名称[key]         根据key获取value                    dict1["涛哥"]
# 查询  字典名称.get(key)     根据key获取value                    dict1.get("涛哥")
# 查询  字典名称.keys()       获取所有的key                       dict1.keys()
# 查询  字典名称.values()     获取所有的value                     dict1.values()
# 查询  字典名称.items()      获取所有的key-value键值对           dict1.items()

dict1 = {"王林":670,"李慕婉":608,"许立国":580,"韩立":688}
print(dict1)

# 添加 - key不存在就是添加
dict1["涛哥"] = 550
print(dict1)

# 修改 - key存在就是修改
dict1["涛哥"] = 620
print(dict1)

# 查询
print(dict1["涛哥"]) # 根据key获取value
print(dict1.get("涛哥")) # 根据key获取value

print(dict1.keys()) # 获取所有的key
print(dict1.values()) # 获取所有的values
print(dict1.items()) # 获取所有的键值对key:value

# 删除
score = dict1.pop("许立国")
print(score)

del dict1["韩立"]
print(dict1)


# 遍历
for k in dict1.keys():
    print(f"{k} : {dict1[k]}")

for item in dict1.items():
    print(f"{item[0]} : {item[1]}")

for k,v in dict1.items():
    print(f"{k} : {v}")