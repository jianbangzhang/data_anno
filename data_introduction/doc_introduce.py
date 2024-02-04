import streamlit as st
from docx import Document
import pandas as pd

def read_docx_table(file_path):
    doc = Document(file_path)
    tables = []

    for table in doc.tables:
        data = []
        for row in table.rows:
            row_data = [cell.text for cell in row.cells]
            data.append(row_data)
        tables.append(pd.DataFrame(data))

    return tables

def data_description_doc():
    st.subheader('4.数据结构')
    local_file ="data/data_struct.docx"

    if local_file is not None:
        tables = read_docx_table(local_file)

        for idx, table in enumerate(tables):
            st.table(table)


