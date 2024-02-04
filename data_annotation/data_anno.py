import streamlit as st
import pandas as pd

def data_annotation_app():
    st.title('数据标注界面')

    # 读取示例数据，你可以根据你的数据格式进行修改
    data = pd.DataFrame({
        'ID': [1, 2, 3],
        'Text': ['Example 1', 'Example 2', 'Example 3'],
        'Label': ['', '', ''],
    })

    st.write("这是一个简单的数据标注界面。请在 'Label' 列中输入相应的标注。")

    # 显示数据表格
    annotated_data = st.table(data)

    # 添加标注
    with st.form(key='label_form'):
        st.write("输入标注:")
        labels = st.text_area("Label", value='', key='label_input')
        submit_button = st.form_submit_button(label='提交标注')

        if submit_button:
            # 处理标注数据，你可以在这里保存标注数据到数据库或文件
            st.success("标注已提交!")