import streamlit as st
from PIL import Image
from streamlit.components.v1 import html
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="2_Profile", layout="wide", page_icon="🌍")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("style.css")

image_col, text_col = st.columns([1.5, 4.5])
with image_col:
    #image = Image.open("Images/Badri_new1.png")
    #new_image = image.resize((300, 250))
    #st.image(new_image)
    pass

with text_col:
    st.title("Badrinath Deshpande")
    # st.subheader("Software Engineer")
    st.markdown(f'<div style="font-size: 27px">{"Software Engineer"}</div>', unsafe_allow_html=True)

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)

text_about, text_carrer = st.columns([2, 5])
with text_about:
    st.markdown("### ABOUT ME")
    st.write("Total 12 years of Professional experience in **Quality Assurance, Computer system Validation, Audits, Testing and Project management.**")
    st.write("\n\n")
    st.markdown("### CONTACT")
    #st.button('Open link', on_click=open_page(url))
    contactMe_click = st.button("Contact Me")
    if contactMe_click:switch_page("Contact_Me")
    st.write("\n\n")
    st.markdown("### SKILLS")
    texts = """<div class="skills">
		<div class="progress-bar-container">
			<h6>Programming Skills</h6>
			<div class="progress-bar">
				<span class="percentage c"></span>
			</div>
		</div>
				<div class="progress-bar-container">
			<h6>Organizational Skills</h6>
			<div class="progress-bar">
				<span class="percentage orgs"></span>
			</div>
		</div>
		<div class="progress-bar-container">
			<h6>Innovative Thinking</h6>
			<div class="progress-bar">
				<span class="percentage inno"></span>
			</div>
		</div>
		<div class="progress-bar-container">
			<h6>Logic</h6>
			<div class="progress-bar">
				<span class="percentage logi"></span>
			</div>
		</div>
		<div class="progress-bar-container">
			<h6>Active Learning</h6>
			<div class="progress-bar">
				<span class="percentage actLearn"></span>
			</div>
		</div>
	</div>"""
    st.markdown(texts, unsafe_allow_html=True)

with text_carrer:
    st.markdown("### CAREER OBJECTIVES")
    st.write("1. Total 12 years of Professional experience in **Quality Assurance, Computer system Validation, Audits, Testing and Project management.**")
    st.write("2. Currently working in **Value Labs Pvt Ltd** Organization as **Validation Lead Engineer.**")
    st.write("\n\n")
    st.markdown("### EDUCATION")
    ed_year, ed_descr = st.columns([0.7,4])
    with ed_year:
        st.markdown("#### 2012")
        st.markdown("#### 2008")
        st.markdown("#### 2006")
    with ed_descr:
        st.write("**Bachelor Of Engineering** "+str("\n")+"**Instrumentation Technology**")
        st.write("PDA Engineering College, **VTU Belgaum Karnataka**")
        st.write("**PUC II Karnataka** " + str("\n") + "**Pre-University**")
        st.write("Nutan Vidyalaya, **Gulbarga Karnataka**")
        st.write("**Secondary School Leaving Certificate(SSLC)** " + str("\n"))
        st.write("Chandrakant Patil School, **Gulbarga Karnataka**")
    #st.text("Please click to")
    st.write("\n\n")
    st.markdown("### EXPERIENCE")
    job_year, job_descr = st.columns([0.7, 4])
    with job_year:
        st.markdown("#### 2021-2023")
        st.markdown("#### 2018-2021")
        st.markdown("#### 2012-2018")
    with job_descr:
        st.write("**Value labs India pvt ltd Organization and Pune location** ")
        st.write("Working as a **Project Lead**")
        st.write("**Cognizant Technology Solutions and Pune Location**")
        st.write("Worked as a **Validation Lead**")
        st.write("**Cenduit India Pvt. ltd. and Bangalore Location**")
        st.write("Worked as a **Validation Engineer**")
    st.write("\n\n")
    st.markdown("### HOBBIES OR INTERESTS")
    sports_img, music_img, travel_img, photography_img = st.columns([0.5, 0.5, 0.5, 0.5])
    with sports_img:
        image = Image.open('.\Images\sports.JPG')
        new_image = image.resize((50, 50))
        st.image(new_image)
    with music_img:
        image = Image.open('.\Images\Music.JPG')
        new_image = image.resize((50, 50))
        st.image(new_image)
    with travel_img:
        image = Image.open('.\Images\\travels.JPG')
        new_image = image.resize((50, 50))
        st.image(new_image)
    with photography_img:
        image = Image.open('.\Images\photo.JPG')
        new_image = image.resize((50, 50))
        st.image(new_image)

