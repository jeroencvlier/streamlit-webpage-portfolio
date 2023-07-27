from pathlib import Path
import streamlit as st
from st_pages import Page, add_page_title, show_pages

st.set_page_config(layout="centered",initial_sidebar_state="expanded")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
parent_dir = current_dir.parent
css_file = parent_dir / "styles" / "main.css"

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


gif_url = "https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif"
st.title("Thank you for your reaching out!")
st.image(gif_url)
st.write("I will get back to you as soon as possible.")
