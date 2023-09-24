from pages.utils import (
    text_loader,
    v_space,
    load_css,
    title_header,
    project_folder,
    project_buttons,
    load_mp4,
    im,
)
import streamlit as st


st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Jeroen | RL - Continuous Control!",
    page_icon=im,
)

load_css()
title_header("Dynamic Control RL", title_class="title3", line=False)
this_project = project_folder / "ContinuousControlReinforcementLearning"

# --------------------------------------------------------------
# Project Introduction
# --------------------------------------------------------------

# with open(f"{this_project}/introduction.md", "r") as f:
#     project_readme = f.read()

introduction_text = text_loader(this_project, "introduction")
with st.container():
    st.markdown(introduction_text, unsafe_allow_html=True)

# --------------------------------------------------------------
# Project Image
# --------------------------------------------------------------
v_space(1)
video_file_path = f"{this_project}/ContinuousControl.mp4"
st.markdown(load_mp4(video_file_path), unsafe_allow_html=True)


# --------------------------------------------------------------
# Project Description
# --------------------------------------------------------------
v_space(1)
# with open(f"{this_project}/description.md", "r") as f:
#     project_readme = f.read()

description_text = text_loader(this_project, "description")

with st.container():
    st.markdown(description_text, unsafe_allow_html=True)


# --------------------------------------------------------------
# Github link
# --------------------------------------------------------------

github_link = "https://www.github.com/jeroencvlier/DDPG-Continuous-Control"
project_buttons(github_link)
