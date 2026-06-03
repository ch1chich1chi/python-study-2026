# JSON是软件开发中最常用的数据交换格式,而为了简化JSON数据的处理,在Python标准库中就是提供了处理JSON数据的核心模块json

import json

# 写入json数据
user = {
    "name":"小马",
    "age":"18",
    "gender":"男",
    "hobbies":["reading","swimming"]
}
with open("F:/python的学习/2026/2026.6.3(读写json格式文件,保存会话,新建会话)/2文件写入.json","w",encoding="utf-8") as f:
    # ensure_ascii:默认为True,确保所有的数据输出的都是ascii编码(非ASCII码会进行转义);False,非ASCII码保留原样输出
    # indent:会在输出的json数据中添加缩进(格式化)
    json.dump(user,f,ensure_ascii=False,indent=2) # 序列化

# 读取json文件
with open("F:/python的学习/2026/2026.6.3(读写json格式文件,保存会话,新建会话)/2文件写入.json","r",encoding="utf-8") as f:
    user = json.load(f) # 反序列化
    print(user)
    print(type(user))