# 字符串定义方式
# 双引号定义
s1 = "Hello"

# 单引号定义
s2 = 'Python'

# 三引号定义(多行字符串)
s3 = """
  尊敬的客户:
      感谢您...
      我们会...
      祝好~
"""

# 把字符串当中的每一个字,都称之为一个字符
# 字符:是文本世界的基本单位,一个字母 一个数字 一个标点符号 一个汉字等都是一个字符

print(s1)
print(s2,s3)

print(isinstance(s1,str))
print(type(s2))
print(type(s3))

# 定义字符串--->It's very good
# 转义字符  名称  作用
# \'      单引号 表示单引号'
# \"      双引号 表示双引号"
# \n      换行符 开始新的一行(换行)
# \t      制表符 增加缩进,缩进一个制表符(tab)的大小
msg = 'It\'s very good'
print(msg)

msg2 = "It's very good"
print(msg2)

msg3 = "Hello 的意思就是\"您好\""
print(msg3)

msg4 = 'Hello 的意思就是\"您好\"'
print(msg4)

print("\t欢迎大家!\n\t记得学习哦 ~") # \n 换行   \t 按了Tab缩进