import streamlit as st

# Inject CSS styles and fade-up animation
st.markdown("""
    <style>
    @keyframes fadeUp {
        0% {
            opacity: 0;
            transform: translateY(40px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .fade-up {
        animation: fadeUp 2s ease-out forwards;
    }

    .logo-bottom-left {
        position: fixed;
        bottom: 10px;
        left: 10px;
        z-index: 999;
    }

    .aqua-text {
        font-size: 70px;
        font-weight: bold;
        text-align: center;
        margin-top: 60px;
    }

    .subtitle {
        font-size: 22px;
        text-align: center;
        color: white;
        margin-top: 10px;
    }

    .green {
        color: #00A600; /* green */
    }

    .blue {
        color: #1e90ff; /* blue */
    }

    .intro {
        text-align: center;
        color: white;
        font-size: 18px;
        margin-top: 20px;
        padding: 0 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Title with green "Ling" and blue "ium"
st.markdown("<div class='aqua-text fade-up'><span class='green'>Ling</span><span class='blue'>ium</span></div>", unsafe_allow_html=True)

# Subtitle
st.markdown("<div class='subtitle'>Connect with native speakers.</div>", unsafe_allow_html=True)

# Logo
st.markdown(
    "<div class='logo-bottom-left'><img src='images/logo1.png' width='100'></div>",
    unsafe_allow_html=True
)

# Short welcome paragraph
st.markdown("""
<div class='intro'>
Welcome to <span style='color:"#55b1d4";'>Ling</span><span style='color:"#42b47a";'>ium</span> — your smart language learning companion! 
Answer a few quick questions, and we’ll connect you with the best Discord servers and resources to match your goals.
</div>
""", unsafe_allow_html=True)
