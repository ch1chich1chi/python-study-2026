# 1.定义函数 add(a,b),接收两个数字，返回两数之和
# 定义函数 max_num(a,b),返回两个数里较大的那个
# 调用上面两个函数,打印结果
def add(a, b):
    return a + b

def max_num(a, b):
    return a if a > b else b

print(add(3,5))
print(max_num(9,2))

# 2.给上面 add(a,b) 加上三引号多行说明文档写明:函数作用 参数含义 返回值含义
def add(a, b):
    """
    两数相加函数
    :param a: 第一个数字
    :param b: 第二个数字
    :return: 两数相加的结果
    """
    return a + b

# 3.写函数,设置默认参数：info(name,,age=18)
# 不传年龄时,默认就是 18
# 调用：info("张三") info("李四",20) 看效果
def info(name, age=18):
    print(f"姓名：{name}，年龄：{age}")

info("张三")
info("李四",20)

# 4.写函数 func1()
# 写函数 func2(),在 func2 里面调用 func1
# 最终只调用 func2(),让程序正常运行
def func1():
    print("第一层函数执行")

def func2():
    print("第二层函数执行")
    func1()

func2()

# 5.定义函数 calc_score(语文,数学,英语)
# 计算三科总分 平均分
# 总分 平均分都用 return 返回
# 外面调用函数,接收两个返回值并打印
def calc_score(chinese, math, english):
    total = chinese + math + english
    avg = total / 3
    return total, avg

sum_s, avg_s = calc_score(80,90,70)
print(f"总分：{sum_s}，平均分：{avg_s}")