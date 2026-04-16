# 方法                       作用                                        样例
# find()  在字符串中查找子串,返回第一次出现索引的位置,找不到返回-1    s.find('Python')
# count()  统计子串在字符串中出现的次数                     s.count('H')
# upper()  将字符串中所有字母转换为大写字母                 s.upper()
# lower()  将字符串中所有字母转换为小写字母                 s.lower()
# split()  将字符串按指定分隔符分割成列表                 s.split(' ')
# strip()  去除字符串两端的空白字符或指定字符                 s.strip()/s.strip('*')
# replace()  将字符串中的指定子串替换为新的子串                 s.replace('H', 'C')
# startswith()  检查字符串是否以指定子串开头,返回布尔值            s.startswith('P')

s = "Hello-Python-Hello-World "

# find() 查找指定字符串第一次出现的索引位置
index = s.find("-")
print(index)

# count() 统计指定字符串在字符串中出现的次数
c = s.count("o")
print(c)

# upper() 转为大写
su = s.upper()
print(su)

# lower() 转为小写
sl = s.lower()
print(sl)

# split() 按指定分隔符分割成列表
slist = s.split("-")
print(slist)

# strip() 去除字符串两端的空白字符或指定字符
ss = s.strip()
print(ss)

# replace() 替换字符串中的指定子串
sr = s.replace("-", "_")
print(sr)

# startswith()/endwith() 判断字符是否是以指定的字符串开头/结尾,返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Python"))