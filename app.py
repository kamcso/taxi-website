import streamlit as st

st.secrets['apikey']

st.markdown('# Hello this is my first website')

st.header('This is a header')

st.write('This is text')

columns = st.columns(2)

with columns[0]:
    if st.checkbox('This is a checkbox'):
        st.write('The checkbox is ticked')

    if st.button('This is a button'):
        st.write('The button is clicked')

    st.image('peru.jpg', width=200)

with columns[1]:
    value = st.slider('This is a slider')

    if value:
        st.write(value * 1000)

    st.date_input('date', value='today')
