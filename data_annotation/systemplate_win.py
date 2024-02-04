import streamlit as st
from utils.utils import read_txt


class FixedTextWindow:
    def __init__(self):
        self.fixed_text = "大模型的system设定"
        self.systemplate="data/systemplate.txt"
        self.tool_template="data/tool_template.txt"
        self.inner_sep="\n"
        self.outer_sep="\n\n"

    def get_systemplate(self):
        template_text=read_txt(self.systemplate)
        system_template=self.inner_sep.join(template_text)
        return system_template

    def get_toolfunction_api(self):
        api_text=read_txt(self.tool_template)
        toolfunction_text=self.inner_sep.join(api_text)
        return toolfunction_text

    def render(self):
        systemplate = self.get_systemplate()
        tool_api = self.get_toolfunction_api()
        prompt_string = systemplate + self.outer_sep + tool_api
        st.subheader(self.fixed_text)
        st.write(prompt_string)

