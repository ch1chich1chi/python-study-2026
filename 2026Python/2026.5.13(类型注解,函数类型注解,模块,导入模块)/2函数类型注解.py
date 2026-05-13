# 为函数添加类型注解,其实主要就是为函数的参数和返回值添加类型注解,具体语法如下:
def calc(scores: list[int]) -> float: # list[int]是参数的类型 float 是返回值的类型
  return sum(scores) / len(scores)

def calc_data(scores: list[int]) -> tuple[int,int,float]:
  max_v = max(scores)
  min_v = min(scores)
  avg_v = sum(scores) / len(scores)
  return max_v,min_v,avg_v

def circle_area_len(r:float) -> tuple[float,float]:
  return round(3.14 * r * r,1),round(2 * 3.14 * r,1)

al = circle_area_len(10)
print(al)

"""
案例2:电商订单计算器
定义一个函数,用于根据传入的一批商品信息(商品名 价格 数量) 优惠(优惠卷 积分抵扣) 运费信息计算订单的总金额
具体规则如下:
    1.优惠卷需要商品金额满5000才可以使用,且优惠卷金额不能超过商品总价
    2.积分抵扣需要商品总金额满5000才可以使用,100积分抵扣1元(且抵扣金额不能超过商品总价,积分只能整百抵扣``)
"""
def cacl_order_cost(*args: tuple[str,float,int],coupon = 0,score = 0,express = 0.0) -> float:
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