import streamlit as st


class UserInputWindow:
    def __init__(self):
        self.title = "1.对话数据构造"
        self.placeholder = "输入对话数据："
        self.input_text = ""

    def create_conversations(self):
        conversation_mode = st.radio("选择对话模式:", ["单轮对话", "多轮对话"])
        tool_calls = st.radio("工具库调用次数:", ["0次", "1次", "多次"])
        if conversation_mode=="单轮对话":
            if tool_calls=="0次":
                st.write("用户输入一般是大模型直接回答的通知化问题：")
                user_input=st.sidebar.text_input("用户问题/闲聊：")
                assistant_answer=st.sidebar.text_input("agent直接回答：")
            elif tool_calls=="1次":
                st.write("用户输入一般是大模型需要调用工具的任务：")
                user_input = st.sidebar.text_input("用户问题/任务：")
                assistant_answer = st.sidebar.text_input("agent不能直接回答：")
            elif tool_calls=="多次":
                pass
            else:
                raise ValueError("不存在这种对话模式.")


    def render(self):
        st.subheader(self.title)
        self.create_conversations()
        self.input_text = st.sidebar.text_input(self.placeholder, self.input_text)