import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Audrius Pasvenskas")
    content = """
        Hello, my name is Audrius, and I am a programmer who primarily works with JavaScript, Python, and C++. My journey into programming has been unconventional. I started with self-learning, attended a coding bootcamp, and am currently advancing my programming knowledge through various projects and college studies. I plan to further solidify my programming skills by earning a degree from a university. Unfortunately, the current job market has not been favorable to me, and my professional experience is somewhat limited to personal and voluntary projects.
     """
    st.info(content)
