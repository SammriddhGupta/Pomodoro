import streamlit as st
import time

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

page_bg_img ="""
<style>
[ data-testid="stAppViewContainer"] {
    
background-image: url("https://media.istockphoto.com/id/1161898151/photo/close-up-of-calendar-and-alarm-clock-on-the-green-background-planning-for-business-meeting-or.jpg?s=612x612&w=0&k=20&c=lfdqaJBf6g9RU3iGwUhSkN1UbAtDNurReQBmISSClpI=");

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
                        