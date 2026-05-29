import streamlit as st

# 设置页面的配置项
st.set_page_config(
    page_title="Streamlit入门",
    page_icon="❤",

    # 布局
    layout="wide",

    # 控制的是侧边栏的状态
    initial_sidebar_state="expanded",

    menu_items={
        'Get Help':"https://.....",
        '.....':"....",
        "About":"# 这是一个Streamlit的入门页面~"
    }
)