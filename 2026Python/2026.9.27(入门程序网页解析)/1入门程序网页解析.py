# 获取TIOBE编程语言排行榜单

# 步骤
# 1.查看TIOBE网站的robots.txt文件,明确资源获取的规则
# 2.安装requests库,用于发送网络请求(pip install requests)
# 3.编写python代码,访问TIOBE网站,获取数据

import requests
from lxml import html

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送请求,获取数据
response = requests.get(target_url) # 在浏览器地址栏所发起的所有的请求,请求方式都是get

# 输出数据到控制台
# print(response.text)
document = html.fromstring(response.text)

# 解析数据
# 解析表头
# th_list = document.xpath("//table[@id='top20']/thead/tr/th/text()")
th_list = document.xpath("//table[@id='top20']/thead/tr/th/text()") 
# 打开浏览器,按f12,选Elements,点击最左边的小箭头,再点击网页上的数据,可以定位到元素,右键定位,选择copy,可以copy xpath
# 还有个copy full xpath,可以copy完整的xpath路径,但是不建议使用,因为网页结构一旦发生变化,就会失效
print(th_list)

# 解析表格中的数据
tr_list = document.xpath("//table[@id='top20']/tbody/tr")
for tr in tr_list:
    td_list = tr.xpath("./td/text()")
    print(td_list)