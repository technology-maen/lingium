import streamlit as st

# Apply custom styling for the page
st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the logo
st.image('images/logo1.png', width=300)

# Display the main heading
st.markdown("<div style='font-size: 28pt;'>Connect with native speakers.<br/></div>", unsafe_allow_html=True)

# Provide an introduction to the application
st.markdown(
    """Welcome to Lingium, your personalized language learning assistant! This project leverages machine learning to recommend the best Discord servers and resources tailored to your language learning goals. Whether you're preparing for certifications like IELTS or TOEFL, or simply looking to connect with native speakers, Lingium is here to guide you. Answer a few questions, and let our intelligent recommender system find the perfect match for your needs. Start your journey to mastering a new language today!"""
)