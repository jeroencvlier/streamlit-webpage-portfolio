from PIL import Image
from pages.utils import (
    load_css,
    title_header,
    project_folder,
    project_buttons,
    im,
)
import streamlit as st


st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Jeroen | Projects!",
    page_icon=im,
)

load_css()
title_header("Digital Portfolio Streamlit", line=True)
this_project = project_folder / "StreamlitPortfolio"


# --------------------------------------------------------------
# Project Description
# --------------------------------------------------------------

with open(f"{this_project}/project_readme.md", "r") as f:
    project_readme = f.read()


with st.container():
    st.markdown(project_readme, unsafe_allow_html=True)

# --------------------------------------------------------------
# Project Image
# --------------------------------------------------------------
image = Image.open(f"{this_project}/streamlit-logo.png")
with st.container():
    st.image(image)


# --------------------------------------------------------------
# Buttons
# --------------------------------------------------------------
github_link = "https://www.github.com/jeroencvlier/DDPG-Continuous-Control"
project_buttons(github_link)
