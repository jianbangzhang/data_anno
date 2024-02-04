import streamlit as st
from .systemplate_win import FixedTextWindow
from .doc_introduce import data_description_doc

def data_description():

    st.write("在做数据标注之前，请标注人员务必参考说明。"
             "在这里，我们提供了关于数据结构的说明信息，"
             "以帮助标注人员理解我们的数据集。")

    st.write("数据结构如下：")
    st.write("""[
                    {"id":"SPART_AGENT_TRAIN_1","conversations":[
                    {"from":"system","value:"<system><tool_list>"},
                    {"from":"user","value":"<task>"},
                    {"from":"assistant","value":"<plan><think><exec><result>"}
                ]""")
    win = FixedTextWindow()
    win.render()
    data_description_doc()









