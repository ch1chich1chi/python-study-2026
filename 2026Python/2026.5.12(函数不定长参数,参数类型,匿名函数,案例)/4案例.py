# 案例1:N的阶乘
# 定义一个函数,根据传入的数字,计算数字阶乘的结果
# 分析 n的阶乘公式:f(n) = n * f(n-1)
# 递归调用(先层层递进,在逐层回归):指的是在函数中自己调用自己的情况 ----> 一定得有终结点
def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n-1)
    
"""
案例2:电商订单计算器
定义一个函数,用于根据传入的一批商品信息(商品名 价格 数量) 优惠(优惠卷 积分抵扣) 运费信息计算订单的总金额
具体规则如下:
    1.优惠卷需要商品金额满5000才可以使用,且优惠卷金额不能超过商品总价
    2.积分抵扣需要商品总金额满5000才可以使用,100积分抵扣1元(且抵扣金额不能超过商品总价,积分只能整百抵扣``)
"""
def cacl_order_cost(*args,coupon = 0,score = 0,express = 0.0):
    """
    传入的一批商品信息(商品名 价格 数量) 优惠(优惠卷 积分抵扣) 运费信息计算订单的总金额
    :param args:商品信息(商品名 价格 数量) ---> 如:("鼠标",188,2)("键盘",388,1)
    :param coupon:优惠卷
    :param ascore:积分
    :param express:运费
    :return:订单的总金额
    """
    # 订单总金额 = 商品总金额 - 优惠卷 - 积分抵扣 + 运费
    # 1.计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)

    # 2.扣减优惠卷
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost = total_cost - coupon # total_cost -= coupon

    # 3.扣减积分抵扣
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100

    # 4.添加运费
    total_cost += express

    return total_cost

# 测试
total = cacl_order_cost(("鼠标",188,2),("键盘",388,1),("手机",3999,1),coupon = 10,score = 4000,express = 9.9)
print(total)

total = cacl_order_cost(("鼠标",188,2),("键盘",388,1),("手机",6999,1),coupon = 10,score = 4000,express = 9.9)
print(total)

total = cacl_order_cost(("鼠标",188,2),("键盘",388,1),("手机",6999,1),express = 9.9)
print(total)