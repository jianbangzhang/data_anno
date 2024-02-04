import streamlit as st
from utils.utils import read_txt


class FixedTextWindow:
    def __init__(self):
        self.fixed_text = "1.大模型的system_prompt结构"
        self.user_text="2.用户输入任务/问题/闲聊"
        self.assistant_text="3.Agent回答"
        self.systemplate="data/systemplate.txt"
        self.tool_template="data/tool_template.txt"
        self.inner_sep="\n"
        self.outer_sep="\n\n"

    def get_systemplate(self):
        template_text=read_txt(self.systemplate)
        system_template=self.inner_sep.join(template_text)
        return system_template

    def get_toolfunction_api(self):
        api_text=read_txt(self.tool_template,add_number=True)
        toolfunction_text=self.inner_sep.join(api_text)
        return toolfunction_text


    def render(self):
        systemplate = self.get_systemplate()
        tool_api = self.get_toolfunction_api()
        prompt_string = systemplate + self.outer_sep + tool_api
        st.subheader(self.fixed_text)
        st.markdown("**<system><tool_list>**")
        st.write(prompt_string)

        st.subheader(self.user_text)
        st.markdown('**<task>**')
        st.write("用户输入任务:")
        st.write("比如：'查看讯飞总部位置。'")
        st.write("outcome:{'from':'user','value':'查看讯飞位置。'}")

        st.subheader(self.assistant_text)
        st.markdown("**<plan><think><exec>**")
        st.write("agent思考问题->执行子任务->输出结果")
        st.write("<plan>:好的，正在为您查找科大讯飞的总部位置.")
        st.write("<think>:调用地理位置查询工具JSON{'api_name':'location_tool',parameters:{'org':'科大讯飞总部'}}")
        st.write("<exec>:{'result':'安徽省合肥市蜀山区望江西路1037号'}")
        st.write("自然语言输出：您好，科大讯飞总部位于安徽省合肥市蜀山区望江西路1037号，还有什么需要帮助的吗？")

