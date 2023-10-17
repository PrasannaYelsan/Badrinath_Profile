import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Badrinath Deshpande :--> Contact Me",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded")


# bootstrap 4 collapse example
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("style.css")

sub_details, social_icons = st.columns([2, 2])
with sub_details:
    st.subheader("Contact Me")

with social_icons:
    st.markdown("**:black[Facebook]**")

contact_details, contact_form = st.columns([2, 2])
with contact_details:
    st.markdown("**:black[DON'T BE SHY]**")
    motivational_text = "Feel free to get in touch with me. I am always open to discussing new projects, creative ideas or opportunities to be part of your visions."
    st.markdown(motivational_text)
    image = Image.open('Images\Mail-icon.png')
    st.image(image)
    st.markdown("Badrinath.deshpande@gmail.com")
    image_call = Image.open('Images\Call.png')
    st.image(image_call)
    st.markdown("**:black[+91 99999 99999]**")
    image_loc = Image.open('Images\Location-icon.png')
    st.image(image_loc)
    st.markdown("**:black[Bangalore]**")

with contact_form:
    st.header("📧: Get in Touch with Me.")
    contact_form = """
    <form action = "https://formsubmit.co/prasannayelsangikar32@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="your name" required>
        <input type="email" name="email" placeholder="your email" required>
        <textarea name="message" placeholder="your message" required></textarea>  
        <button type="Submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
