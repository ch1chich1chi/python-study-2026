"""
Streamlit
Streamlit是一个开源的Python,专为数据工程师及机器学习工程师设计,原来快速基于Python代码构建交互的web网站(无需掌握前端技术)
官方网站:https://streamlit.io

Streamlit入门程序:
    1.安装streamlit:pip install streamlit
    2.在python文件中引入streamlit模块
    3.基于streamlit中提供的API来构建web应用
    4.运行程序:streamlit run xxxx.py
"""

import streamlit as st

# 大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

# 运行要去终端中输入 streamlit run xxxx.py,输入完run后,空一格,输入第一个字,之后按TAB
# 应用运行起来之后,默认占用一个端口8501