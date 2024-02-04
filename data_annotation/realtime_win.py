import streamlit as st

class RealTimeResultWindow:
    def __init__(self):
        self.title = "2.查看运行结果："
        self.result = ""

    def render(self):
        st.subheader(self.title)
        st.write(f"{self.result}")