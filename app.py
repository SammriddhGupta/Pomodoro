import streamlit as st
import time

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

st.write("""
# The Pomodoro App By Yours Truly Sammriddh aka Sam
""")

button_clicked = st.button("Start")

