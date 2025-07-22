import streamlit as st
from PIL import Image
from streamlit_extras.switch_page_button import switch_page
favicon = Image.open('images/logo4.png')
st.set_page_config(page_title="Lingium", page_icon=favicon)
logo = st.logo("images/logo1.png",icon_image='images/logo3.png')
pg = st.navigation([
    st.Page("home.py",title='Home'),
    st.Page("project.py",title='Get Started'),
    ],position='top')
pg.run()