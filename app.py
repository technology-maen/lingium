import streamlit as st
from PIL import Image

# Set up the logo and favicon for the application
logo = st.logo("images/logo1.png", icon_image='images/logo3.png')
favicon = Image.open('images/logo4.png')

# Configure the Streamlit page settings
st.set_page_config(page_title="Lingium", page_icon=favicon)

# Define navigation for the application
pg = st.navigation([
    st.Page("home.py", title='Home'),  # Home page
    st.Page("project.py", title='Get Started'),  # Project page
], position='top')

# Run the navigation
pg.run()