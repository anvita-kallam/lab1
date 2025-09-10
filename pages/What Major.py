import streamlit as st
import random

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #2d1b2d 0%, #3d1a3d 50%, #8A0B3A 100%);
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
st.title("🐝🎓 What Georgia Tech Major Should You Study?")
st.header("Georgia Tech offers 35 undergraduate majors across its six colleges: Business, Computing, Design, Engineering, Liberal Arts, and Sciences. With this much choice, it's extremely difficult for students to narrow down what major is best for them.")
st.write("But don't worry! This simple quiz will help you (yes you) finally decide what you want to study!")

# Question 1
#NEW
q1 = st.radio(
    "1. What's your favorite type of problem to solve?",
    ["Coding puzzles 💻", "Designing things that fly ✈️", "Understanding the human body 🧬", "Building bridges & skyscrapers 🏗️"]
)

# Question 2
#NEW
q2 = st.multiselect(
    "2. Which of these subjects do you enjoy the most? (Pick all that apply)",
    ["Math ➗", "Physics ⚛️", "Biology 🧪", "Art/Design 🎨", "Economics 💰"]
)

# Question 3
#NEW
q3 = st.number_input(
    "3. How many hours per week would you ideally spend coding?",
    min_value=0, max_value=60, value=10
)

# Question 4
#NEW
q4 = st.slider(
    "4. How much do you enjoy teamwork vs. solo work? (0 = solo, 10 = teamwork)",
    min_value=0, max_value=10, value=5
)

# Question 5
st.write("5. Which campus spot would you hang out at the most?")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("Images/coc.jpeg", width=150)
    spot1 = "College of Computing"
with col2:
    st.image("Images/aerospace.jpg", width=150)
    spot2 = "Aerospace Engineering Building"
with col3:
    st.image("Images/bme.jpg", width=150)
    spot3 = "Biomedical Engineering"

q5 = st.radio("Pick your favorite spot:", [spot1, spot2, spot3])

#Result
st.write("---")
if st.button("See My GT Major 🐝"):  # NEW
    if "Coding puzzles 💻" in q1 or "Math ➗" in q2 or q3 > 20:
        major = "Computer Science (CS) 💻"
        desc = "You're logical, analytical, and love solving problems with code, which makes you a great fit for CS! Just please shower..."
    elif "Designing things that fly ✈️" in q1 or spot2 == q5:
        major = "Aerospace Engineering (AE) ✈️"
        desc = "You might just send the next rocket into space!"
    elif "Understanding the human body 🧬" in q1 or "Biology 🧪" in q2:
        major = "Biomedical Engineering (BME) 🧬"
        desc = "You want to improve healthcare and create technologies that help people. So amazing!"
    elif "Building bridges & skyscrapers 🏗️" in q1 or "Physics ⚛️" in q2:
        major = "Civil Engineering (CE) 🏗️"
        desc = "You think practically, love building things, and want to leave a lasting impact on society with advanced infrastructure."
    else:
        major = "Industrial Engineering (IE) 📊"
        desc = "You’re versatile, people-focused, and always finding better, more optimized ways to do things. Way to go!"

    st.subheader(f"Your GT Major is: {major} 🎓")
    st.success(desc)

    # Balloons
    #NEW
    st.balloons()
