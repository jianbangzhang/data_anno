import streamlit as st

from data_annotation.conversations_win import UserInputWindow
from data_annotation.realtime_win import RealTimeResultWindow
from data_introduction.introduct_prompt import data_description
from data_introduction.introduct_prompt import FixedTextWindow



def main():
    st.write("""
            <style>
                p {
                    text-indent: 2em;  /* 设置首行缩进为两个字符宽度 */
                }
                h1 {
                    text-align: center;  /* 设置标题居中 */
                }
            </style>
                """, unsafe_allow_html=True)
    selected_app = st.sidebar.selectbox("选择界面", ["数据说明", "数据标注"],
                                        placeholder="请选择数据窗口...")
    win = FixedTextWindow()

    if selected_app == "数据说明":
        st.title("SPARK AGENT数据说明")
        data_description(win)
    elif selected_app == "数据标注":
        prompt_string=win.get_prompt()
        st.title("SPARK AGENT数据标注平台")
        user_input_window = UserInputWindow(prompt_string)
        real_time_result_window = RealTimeResultWindow()

        user_input,assistant_answer,one_data=user_input_window.render()
        real_time_result_window.render(user_input,assistant_answer,one_data)
    else:
        raise ValueError("您选择的窗口不存在...")




if __name__ == "__main__":
    main()
