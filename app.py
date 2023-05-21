import streamlit as st
import time

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

page_bg_img ="""
<style>
[ data-testid="stAppViewContainer"] {
    
background-image: url("https://images.unsplash.com/photo-1643424975787-f134e78ecbc8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=871&q=80");

opacity:0.5;

background-size: cover;
}

[data-testid="stToolbar] {
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("""
# The Pomodoro App: Your Productivity Buddy
""")

button_clicked = st.button("Start")

t1 = 1500
t2 = 300

if button_clicked:
    with st.empty():
        while t1:
            mins, secs = divmod(t1,60)
            timer = '{:02d}:{:02d}'.format(mins,secs)
            st.header(f"⏳{timer}")
            time.sleep(1)
            t1 -= 1
            st.success("🥳 25 minutes are up! Now take a well deserved break :) ")
            
    with st.empty():
        while t2:
            mins2, secs2 = divmod(t2,60)
            timer2 = '{:02d}:{:02d}'.format(mins2,secs2)
            st.header(f"😇{timer2}")
            time.sleep(1)
            t2 -= 1
            st.error("⏲ Chop Chop back to work time, 5 minutes are up ")
                        