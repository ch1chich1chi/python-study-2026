# 文件操作:
#     路径写法:
#         相对路径:相对于当前做目录的路径(从当前文件所在目录开始查找)
#               . :当前目录 ----> ./2026.6.6/望庐山瀑布.txt  ./可以省略
#              .. :上一级目录 可以叠加写

#         绝对路径:是从文件系统的目录开始,完整的描述文件位置的路径(注意:\在字符串中表示的是转义字符,可以用\\,也可以/)

# 写文件
with open("2望庐山瀑布.txt","w",encoding="utf-8") as f:
    f.write("静夜思(李白)\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")

# 读文件
with open("2望庐山瀑布.txt","r",encoding="utf-8") as f:
    content = f.read()
    print(content)

# a:追加模式,新内容会被追加在原有内容之后;文件不存在则创建新文件

# 写文件
# a:append 追加内容;w:write,覆盖内容 ----> 文件不存在,则创建文件
with open("2望庐山瀑布.txt","a",encoding="utf-8") as f:
    f.write("静夜思(李白)\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")