# 获取TIOBE编程语言排行榜单

# 步骤
# 1.查看TIOBE网站的robots.txt文件,明确资源获取的规则
# 2.安装requests库,用于发送网络请求(pip install requests)
# 3.编写python代码,访问TIOBE网站,获取数据

import requests

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送请求,获取数据
response = requests.get(target_url) # 在浏览器地址栏所发起的所有的请求,请求方式都是get

# 输出数据到控制台
print(response.text)