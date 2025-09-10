import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #2d1b2d 0%, #3d1a3d 50%, #78294F 100%);
        color: #ffe6f0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    h1, h2, h3, h4 {
        color: #ff99cc;
        font-weight: 600;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }

    h1 {
        color: #ff66b2;
        border-bottom: 3px solid #ff66b2;
        padding-bottom: 10px;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2d1b2d 0%, #3d1a3d 100%);
        color: #ffe6f0;
        border-right: 2px solid #ff66b2;
    }

    section[data-testid="stSidebar"] a {
        color: #ff66b2 !important;
        font-weight: 500;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    section[data-testid="stSidebar"] a:hover {
        color: #ff99cc !important;
    }


    div[data-baseweb="tab"] {
        background: rgba(45, 27, 45, 0.6);
        color: #ffe6f0;
        font-weight: 500;
        border: 1px solid rgba(255, 153, 204, 0.3);
        border-radius: 8px 8px 0 0;
        transition: all 0.3s ease;
    }
    div[data-baseweb="tab"]:hover {
        background: rgba(255, 102, 178, 0.1);
        color: #ff66b2;
        border-color: #ff66b2;
    }
    div[data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(90deg, #ff66b2, #ff99cc);
        color: white;
        border-color: #ff66b2;
    }

    .stProgress > div > div {
        background: linear-gradient(90deg, #ff66b2, #ff99cc);
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(255, 102, 178, 0.3);
    }


    .stMarkdown {
        color: #ffe6f0;
    }

    .stImage > img {
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        border: 2px solid rgba(255, 153, 204, 0.3);
    }

    .stSidebar .stText {
        color: #ffe6f0;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Title of App
st.title("🚀 Web Development Lab01")

# Assignment Data 
# TODO: Fill out your team number, section, and team members

st.header("📚 CS 1301")
st.subheader("Web Development - Section C")
st.subheader("Anvita Kallam")

# Add a fun divider
st.markdown("---")

# Introduction
# TODO: Write a quick description for all of your pages in this lab below, in the form:
#       1. **Page Name**: Description
#       2. **Page Name**: Description
#       3. **Page Name**: Description
#       4. **Page Name**: Description

st.markdown("""
### 🌟 Welcome to my Streamlit Web Development Lab01 app! 

Navigate between the pages using the sidebar to the left. Here's what you'll find:

1. **Portfolio**: Covers all things about me! Tap around to see what projects and experiences I've been up to.
2. **What Major**: Deciding you major at a school with 35+ offerings across 6 colleges may seem impossible, but this quiz condenses down all the hard decision-making for you!

""")

