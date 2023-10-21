from PIL import Image
from pages.utils import (
    text_loader,
    v_space,
    load_css,
    title_header,
    project_folder,
    project_buttons,
    im,
    load_png,
)
import streamlit as st


st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Jeroen | Projects!",
    page_icon=im,
)

load_css()
title_header("Digital Portfolio Streamlit", line=False)
this_project = project_folder / "StreamlitPortfolio"


# --------------------------------------------------------------
# Project Description
# --------------------------------------------------------------

project_readme = text_loader(this_project, "project_readme")
with st.container():
    st.markdown(project_readme, unsafe_allow_html=True)

# --------------------------------------------------------------
# Project Image
# --------------------------------------------------------------
v_space(1)

image_file_path = f"{this_project}/streamlit-logo.png"
st.markdown(load_png(image_file_path), unsafe_allow_html=True)

# --------------------------------------------------------------
# Credits
# --------------------------------------------------------------
v_space(1)

credit_readme = text_loader(this_project, "credit")

with st.container():
    st.markdown(credit_readme, unsafe_allow_html=True)


# --------------------------------------------------------------
# Buttons
# --------------------------------------------------------------
github_link = "https://www.github.com/jeroencvlier/streamlit-webpage-portfolio"
project_buttons(github_link)
