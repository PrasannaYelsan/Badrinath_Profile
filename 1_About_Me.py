import datetime
import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Badrinath Deshpande",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded")

def add_logo(logo_path, width, height):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    modified_logo = logo.resize((width, height))
    return modified_logo

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("style.css")

# About me page with two columns
image_col, text_col = st.columns([3, 4])

with image_col:
    st.write("\n")
    st.write("\n")
    st.markdown('<p style="font-family:monospace; color:purple; font-size: 42px;">Welcome</p>',
                unsafe_allow_html=True)
    st.write("\n")
    st.write("\n")

    def time_in_range(start, end, current):
        """Returns whether current is in the range [start, end]"""
        return start <= current <= end
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    # st.write("\n")
    start = datetime.time(0, 0, 0)
    end = datetime.time(11, 59, 0)
    current = datetime.datetime.now().time().hour
    if 0 <= current < 12:
        st.markdown(f'<div style="font-size: 27px">{" Hello Good Morning..."}</div>', unsafe_allow_html=True)
    if 12 <= current < 16:
        st.markdown(f'<div style="font-size: 27px">{" Hello Good Afternoon..."}</div>', unsafe_allow_html=True)
    if 16 <= current < 24:
        st.markdown(f'<div style="font-size: 27px">{" Hello Good Evening..."}</div>', unsafe_allow_html=True)
    st.write("\n")
    st.markdown('<p style="font-family:monospace; color:purple; font-size: 32px;">My name is Badrinath Deshpande</p>',
                unsafe_allow_html=True)
    st.write("\n")
    st.write("\n")
    btn_profile, btn_contactMe = st.columns(2)
    with btn_profile:
        profile_click=st.button("Profile")
        if profile_click:
            switch_page("Profile")

    with btn_contactMe:
        contactMe_click = st.button("Contact Me")
        if contactMe_click:
            switch_page("Contact_Me")

with text_col:
    image = Image.open('.\blob\main\Images/Badri_new1.png')
    st.image(image, caption='Badrinath Deshpande')
