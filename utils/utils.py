import streamlit as st


def read_txt(file,add_number=False):
    with open(file,"r",encoding="utf-8") as txtfile:
        content=txtfile.readlines()
        if add_number:
            new_li=[]
            for ix,data in enumerate(content):
                new_li.append(f"{ix+1}.{data}")
            content=new_li
    return content



def create_input_window(param_li,api_string):
    for param_name in param_li:
        value = st.text_input(f"{param_name}:")
        api_string = api_string.replace("##PARAM",f"{value}",1)
    exec_result=st.text_input("result:")
    summarize_result=st.text_input("summarized:")
    return api_string,exec_result,summarize_result


