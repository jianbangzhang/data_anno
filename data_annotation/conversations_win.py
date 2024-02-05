import streamlit as st
from utils.utils import create_input_window

class UserInputWindow:
    def __init__(self,prompt_string):
        self.title = "1.对话数据构造"
        self.input_text = ""
        self.user_input=st.sidebar.text_input
        self.assistant_answer=st.sidebar.text_input
        self.think=lambda x:f"<|startofthink|>\n```JSON{x}```\n<|endofthink|>"
        self.user_input_format={"from":"user","value":"##INPUT"}
        self.assistant_answer_format={"from":"assistant","value":"##ANSWER"}
        self.system={"from":"system","value":prompt_string}
        self.plan=""
        self.sep = "\n"
        self.exec_result_string="{\"result\":\"##RESULT\"}"
        self.exec_result_format=lambda x:f"<|startofexec|>```JSON{x}```<|endofexec|>"
        self.one_data=[self.system]
        

    def create_conversations(self):
        # Use unique keys for each st.selectbox widget
        user_input = "<task>"
        assistant_answer = "<think>"
        conversation_mode = st.selectbox("选择对话模式:", ["单轮对话", "多轮对话"], index=0)
        tool_calls = st.selectbox("工具库调用次数:", ["零次", "一次", "多次"], index=0)
        tool_api_param_dict=self.get_tool_api()
        tool_list = list(tool_api_param_dict.keys())

        if conversation_mode == "单轮对话":
            if tool_calls == "零次":
                st.write("用户输入一般是大模型直接回答的通识化问题：")
                user_input = self.user_input("用户问题/任务/闲聊：", key="user_input_0")
                assistant_answer = self.assistant_answer("agent回答：", key="assistant_answer_0")
            elif tool_calls == "一次":
                st.write("用户输入一般是大模型需要调用工具的简单任务：")
                user_input = self.user_input("用户问题/任务/闲聊：", key="user_input_1")
                assistant_answer = self.assistant_answer("agent思考：", key="assistant_answer_1")
                choose_api = st.selectbox("选择的工具:", tool_list,key="one_round_one_call")
                api_param_li=tool_api_param_dict[choose_api]
                api_string=api_param_li[0]
                api_string,exec_result,summarized=create_input_window(api_param_li[1:],api_string)
                api_string_filled=self.think(api_string)

                self.plan=assistant_answer
                exec=self.exec_result_format(self.exec_result_string.replace("##RESULT",exec_result))
                assistant_string=self.plan+self.sep+api_string_filled+self.sep+exec+self.sep+summarized
                self.user_input_format["value"]=user_input
                self.assistant_answer_format["value"]=assistant_string
                self.one_data.append(self.user_input_format)
                self.one_data.append(self.assistant_answer_format)
            elif tool_calls == "多次":
                st.write("用户输入一般是大模型需要多次调用工具的复杂任务：")
                user_input = self.user_input("用户问题/任务/闲聊：", key="user_input_m")
                assistant_answer = self.assistant_answer("agent回答：", key="assistant_answer_m")
            else:
                raise ValueError("不存在这种对话模式.")
        return user_input, assistant_answer,self.one_data


    def get_tool_api(self):
        tool_mapping = {
            "weather_info": ["{\"api_name\": \"weather_info\", \"parameters\": [{\"city\": \"##PARAM\"}, {\"date\": \"##PARAM\"}]}","city","date"],
            "calculator": ["{\"api_name\": \"calculator\", \"parameters\": [{\"expression\": \"##PARAM\"}]}","expression"],
            "lookupCharge": ["{\"api_name\": \"lookupCharge\", \"parameters\": [{\"month\": \"##PARAM\"}]}","month"],
            "calendar": ["{\"api_name\": \"calendar\", \"parameters\": [{\"date_string\": \"##PARAM\"}]}","date_string"],
            "knowledgeRetrieval": ["{\"api_name\": \"knowledgeRetrieval\",\"parameters\": [{\"query\": \"##PARAM\"}, {\"keyword\":\"##PARAM\"}]}","query","keyword"]
        }
        return tool_mapping


    def render(self):
        st.subheader(self.title)
        user_input, assistant_answer, one_data= self.create_conversations()
        return user_input, assistant_answer,one_data