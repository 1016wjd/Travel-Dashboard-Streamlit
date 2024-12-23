import streamlit as st

st.title('Hello Streamlit')
st.header('this is header')
st.subheader('this is subheader')

# 2:3으로 컬럼분할 이름생성
col1, col2 = st.columns([2,3])


with col1:
    st.title('here is column1')
with col2:
    st.title('here is column2')
    st.checkbox('this is checkbox1 in col2')


col1.subheader('this is subheader1 in col1')
col2.checkbox('this is checkbox2 in col2')

tab1, tab2= st.tabs(['Tab A' , 'Tab B'])
with tab1:
  #tab A 를 누르면 표시될 내용
  st.write('hello')
    
with tab2:
  #tab B를 누르면 표시될 내용 
  st.write('hi')


st.sidebar.title('this is sidebar')
st.sidebar.checkbox('체크박스에 표시될 문구')