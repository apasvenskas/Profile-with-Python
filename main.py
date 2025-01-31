import streamlit as st
import pandas

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

content2 = """
    Here is a library of apps that I have built using Python.
    """
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep = ";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code({row["url"]})]") #a link to a projects site (current a place holder)

with col4:
    for index, row in df[:10].iterrows(): # [:10] upt ot ten
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code({row["url"]})]")