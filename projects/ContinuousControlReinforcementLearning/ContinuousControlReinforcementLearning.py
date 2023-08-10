from pages.utils import (
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
title_header("Dynamic Control RL", title_class="title3", line=True)
this_project = project_folder / "ContinuousControlReinforcementLearning"

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
st.write("##")

video_file_path = f"{this_project}/ContinuousControl.mp4"
st.markdown(load_mp4(video_file_path), unsafe_allow_html=True)


# --------------------------------------------------------------
# Github link
# --------------------------------------------------------------

github_link = "https://www.github.com/jeroencvlier/DDPG-Continuous-Control"
project_buttons(github_link)
