"""
北京市居民年度用电电费计算：根据输入的用电度数，计算电费
北京市居民电费采用阶梯电价计价方式，所谓阶梯电价是指按照用户消费的电量分段定价，用电价格随用电量增加呈阶梯状逐级递增的一种电价定价机制。
- 阶梯电价规则：
  1. 第一档:2880度以下,电费单价0.4883元/度
  2. 第二档:2880-4800度,电费单价0.5383元/度
  3. 第三档:4800度以上,电费单价0.7883元/度
"""

usage_elec = int(input("请输入用电度数: "))

first_max = 2880  
second_max = 4800  

first_price = 0.4883  
second_price = 0.5383  
third_price = 0.7883  

if usage_elec <= 4800:
    if first_max <= usage_elec <= second_max:
        total_cost = first_price * first_max + (usage_elec - first_max) * second_price
    else:
        total_cost = usage_elec * first_price
else:
    total_cost = first_price * first_max + (second_max - first_max) * second_price + (usage_elec - second_max) * third_price
print(f"{usage_elec} 度的电费是: {total_cost} 元")