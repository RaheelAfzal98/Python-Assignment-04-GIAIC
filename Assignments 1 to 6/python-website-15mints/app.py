# ---------------- PYTHON SPACE ----------------
import streamlit as st
from datetime import datetime

# App title
st.title("🌟 Welcome to Python Space")

# Sidebar navigation
st.sidebar.title("Menu")
selection = st.sidebar.radio("Navigate to", ["Dashboard", "Who We Are", "Reach Out"])

# Dashboard page
if selection == "Dashboard":
    st.header("📊 Dashboard")
    st.markdown("### Welcome to My Simple Website!")
    st.markdown("Explore this mini web app powered by **Streamlit + Python**.")

    # Input field
    user_name = st.text_input("What's your name?")
    if user_name:
        st.success(f"Hi {user_name}, glad you're here!")

    # Time button
    if st.button("Show Current Time"):
        current_time = datetime.now().strftime('%A, %d %B %Y — %I:%M:%S %p')
        st.info(f"🕒 Current Time: {current_time}")

# About page
elif selection == "Who We Are":
    st.header("👥 About This App")
    st.markdown("Learn what powers this project and what makes it awesome.")

    colA, colB = st.columns(2)
    with colA:
        st.subheader("Highlights")
        st.markdown("""
        - 🔧 Lightweight Design  
        - ⏱ Rapid Prototyping  
        - 🌐 Web-ready in minutes
        """)
    with colB:
        st.subheader("Stack Used")
        st.markdown("""
        - 🐍 Python  
        - 📈 Streamlit  
        - 🖌 HTML & Markdown
        """)

# Contact page
else:
    st.header("📬 Contact Form")

    with st.form("form_contact"):
        user_email = st.text_input("Email Address")
        user_query = st.text_area("Your Query")
        send = st.form_submit_button("Submit")

    if send:
        st.success("✅ Your message has been received. We'll respond shortly!")
