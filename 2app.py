import streamlit as st

st.title("student registration")

name= st.text_input('enter a name')
age=st.number_input('enter your age', min_value=18)

course=st.selectbox(
    'select your course',
    ['python','data science','genrative ai']
)

skill= st.multiselect(
    'select your skill',
    ['python','sql','langchian','machin learning']
)

experiance = st.slider('years of experiance',1,10)

if st.button('submit'):
    st.success('registratino successfull')
    st.write('name',name)
    st.write('age',age)
    st.write('course',course)
    st.write('skills',skill)
    st.write('experiance',experiance)
    