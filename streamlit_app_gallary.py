import streamlit as st
import pandas as pd

# Define function to load data from selected files
@st.cache(allow_output_mutation=True)
def load_data(files):
    data = []
    for file in files:
        df = pd.read_excel(file, engine='openpyxl')
        data.append(df)
    return data

# Define pages
def page_1():
    st.write("<h1 style='text-align: center'>Select Files</h1>", unsafe_allow_html=True)
    files = st.file_uploader('Select up to 6 Excel files', type='xlsx', accept_multiple_files=True)
    if files:
        data = load_data(files)
        st.success('Data loaded successfully!')
        st.write("<h2 style='text-align: center'>Navigation</h2>", unsafe_allow_html=True)
        if st.button('Page 2', key='2'):
            page_2()
        if st.button('Page 3', key='3'):
            page_3()
        if st.button('Page 4', key='4'):
            page_4()
        if st.button('Page 5', key='5'):
            page_5()
        if st.button('Page 6', key='6'):
            page_6()

def page_2():
    st.write("<h1 style='text-align: center'>Page 2</h1>", unsafe_allow_html=True)

def page_3():
    st.write("<h1 style='text-align: center'>Page 3</h1>", unsafe_allow_html=True)

def page_4():
    st.write("<h1 style='text-align: center'>Page 4</h1>", unsafe_allow_html=True)

def page_5():
    st.write("<h1 style='text-align: center'>Page 5</h1>", unsafe_allow_html=True)

def page_6():
    st.write("<h1 style='text-align: center'>Page 6</h1>", unsafe_allow_html=True)

# Define app
def app():
    if st.sidebar.button('Page 1'):
        page_1()
    if st.sidebar.button('Page 2'):
        page_2()
    if st.sidebar.button('Page 3'):
        page_3()
    if st.sidebar.button('Page 4'):
        page_4()
    if st.sidebar.button('Page 5'):
        page_5()
    if st.sidebar.button('Page 6'):
        page_6()

# Run app
if __name__ == '__main__':
    app()
