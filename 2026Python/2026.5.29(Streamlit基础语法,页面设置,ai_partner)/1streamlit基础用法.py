# 去streamlit官方文档

import streamlit as st

# 段落文字
st.write("我")
st.write("爱")
st.write("你")

# 图片
# st.image("./xxx/xxx.图片后缀",width=图片宽度) # . 代表当前目录 ./xxx/xxx.图片后缀
# st.image("xxx/xxx.图片后缀") # 如果从当前目录引入, ./ 可以省略

# 音频
# st.audio("")同上

# 视频
# st.video("")同上

# Logo
# st.logo("")同上

# 表格
student_data = {
    "姓名":["王林","李慕婉","贝罗","111","222"],
    "学号":[1,2,3,4,5],
    "语文":[99,98,96,87,89]
}
st.table(student_data)

# 输入框
# 普通输入框
name = st.text_input("请输入姓名:")
st.write(f"您输入的姓名为:{name}")

# 密码输入框
password = st.text_input("请输入密码:",type="password")
st.write(f"您输入的密码为:{password}")

# 单选按钮
gender = st.radio("请输入您的性别",["男","女","未知"],index=2)
st.write(f"您的性别为:{gender}")