# 默认参数也称为缺省参数,用于在定义函数时,为参数提供默认值,调用函数时,可以不传递有默认值的参数
# 注意:默认参数必须放在没有默认值的参数列表后面,一个函数定义时是可以设置多个默认参数的
# 函数调用时,如果默认参数传递了值,则会修改默认的参数值;如果没有传递该参数,则直接使用默认值

# 定义函数
def reg_stu(name,age,gender="男",city="北京"):
    print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

# 调用函数
stu = reg_stu("王林", 20)
print(stu)

stu = reg_stu("李慕婉", 18, "女")
print(stu)

stu = reg_stu("韩立",22,city="上海")
print(stu)