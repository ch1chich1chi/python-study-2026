import streamlit as st

# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",

    # 布局
    layout="wide",

    # 控制的是侧边栏的状态
    initial_sidebar_state="expanded",

    menu_items={}
)

# 大标题
st.title("AI智能伴侣")

if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("请输入一句话")

if prompt:
    st.session_state.messages.append(prompt)

for message in st.session_state.messages:
    st.write(message)
# 为啥for放在if外面

# 更直接的办法——在页面上加一个按钮：

# if prompt:
#     st.session_state.messages.append(prompt)
#     for message in st.session_state.messages:
#         st.write(message)

# # 加一个按钮
# st.button("点我刷新")
# 输入消息后，点一下那个按钮，消息立刻就没了。因为点按钮触发重跑，此时 prompt = None，for 循环不执行。

# 本质原因就是：数据存在 st.session_state 里不会丢，但 st.write 只在代码跑到那一行时才生效。
# 你把 for 锁在 if 里面，就等于告诉程序"只有新消息来的时候才画"，其他时候不画。