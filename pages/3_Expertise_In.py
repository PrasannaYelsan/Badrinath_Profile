import streamlit as st

st.set_page_config(
    page_title="Badrinath Deshpande :--> Expertise-In",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded")

# bootstrap 4 collapse example
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
texts = """<div class ="profile">Expertise-In</div>"""
st.header("🧪 SOFTWARE VALIDATION & PROJECTS.")

sw_validation, projects = st.columns([2.5,2.5])
with sw_validation:
    st.markdown(
        """
        ### SOFTWARE VALIDATION :
        - Qualification of the IT infrastructure 
            - Prospective validation
            - Retrospective validation
        - Fit-Gap or Inspection Readiness Analysis (internal Audits / Compliance Checks)
        - CSV Framework Check: Checking your validation framework and validation documentation for completeness and efficiency
        - 21 CFR Part 11 & EU GMP Annex11 Assessments
        - Data Integrity Assessment
        - Development of remediation plans, e.g. adapting your risk-based validation strategy to new regulatory requirements
        - Design of software validation strategy and framework including work instructions, templates and training materials
        - Software Validation / IT Compliance Workshops
        - Guidance on test strategies
        - Data migration and verification strategies and respective documention
        - Coaching of QA / validation managers""")

with projects:
    st.markdown(
        """
        ### PROJECTS DELIVERED :
        - ERP systems (SAP, Microsoft Dynamics, Oracle)
        - Cloud-based systems (SaaS, PaaS)
        - Document management systems (DMS)
        - laboratory information and management systems (LIMS)
        - IT systems in the clinical sector / clinical trial management systems
        - Pharmacovigilance systems
        - Customer developments """)