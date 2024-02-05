import streamlit as st

class RealTimeResultWindow:
    def __init__(self):
        self.title = "2.查看运行结果："
        self.result = ""
        self.result_window = st.empty()

    def render(self,user_input,assistant_answer,one_data):
        st.subheader(self.title)
        option = st.radio('显示/不显示system prompt', ('不显示', '显示'))
        if option == "不显示":
            one_data = one_data[1:]
        self.result=f"USER:{user_input}"+"\n"+f"AGENT:{assistant_answer}\n\n"+f"FINAL DATA:{one_data}"
        st.text_area("Real-time Results", self.result, height=800)







