import streamlit as st
import seaborn as sns

st.header('This is my second page')

image = st.file_uploader('Upload a file')
if image:
    st.image(image)

df = sns.load_dataset('tips')

st.line_chart(df.total_bill)
