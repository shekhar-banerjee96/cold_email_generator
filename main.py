import streamlit as st
st.title("Cold Mail Generation")

url_input = st.text_input("Enter a URL :",value = 'https://jobs.nike.com/job/R-42328?from=job%20search%20funnel')

submit_button = st.button("Submit")

if submit_button:
    st.code("Hello Hiring Manager , I am from Atliq",language='unknown')