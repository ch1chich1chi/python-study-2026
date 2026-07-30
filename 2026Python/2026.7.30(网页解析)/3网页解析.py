from lxml import html

# 读取html文件
with open('2index.html', 'r', encoding='utf-8') as f:
    html_text = f.read()

    # 解析html的文本,将其转换为一个文档对象
    doc = html.fromstring(html_text)

    # 解析表头 - xpath语法(这个不是2index.html的表头,只是一个例子)
    th_list = doc.xpath('//table/thead/tr/th/text()')
    print(th_list)

    # 解析表格和中的数据 - xpath语法(例子)
    # 获取第一行数据
    td_list = doc.xpath("//table/tbody/tr[1]/td/text()") # 从1开始,获取第一个tr
    print(td_list)

    # 获取所有行数据
    tr_list = doc.xpath("//table/tbody/tr")
    for tr in tr_list:
        td_list = tr.xpath("td/text()")
        print(td_list)