# 日常我们操作文件时,基本分为三部操作:打开 读/写 关闭

# 读文件
# 1.打开文件
f = open("F:/python的学习/2026/2026.6.2(文件操作入门,资源释放)/2.文件操作.txt","r",encoding="utf-8") # r:只读模式

# 2.读取文件
# content = f.read() # 读取所有内容
# print(content)

content_list = f.readlines()
for line in content_list:
    print(line.strip()) # strip方法可以去掉字符串两端的空白字符

# 3.关闭文件
f.close()

# 写文件
# 1.打开文件
f = open("F:/python的学习/2026/2026.6.2(文件操作入门,资源释放)/3.文件写入.txt","w",encoding="utf-8") # w:写入模式,如果文件不存在会自动创建,如果文件存在会覆盖原有内容

# 2.写入文件内容
f.write("静夜思(李白)\n")
f.write("床前明月光，\n")
f.write("疑是地上霜。\n")
f.write("举头望明月，\n")
f.write("低头思故乡。\n")

# 3.关闭文件
f.close()

# 编码:是将字符(文字,数字,符号)转换为计算机能够存储和处理的数字代码的规则系统,如:ASCII BGK UTF-8等
# 注意:如果操作完文件,并未调用close方法关闭文件,同时程序没有停止运行,那么这个文件将一直被Python程序占用,无法操作
